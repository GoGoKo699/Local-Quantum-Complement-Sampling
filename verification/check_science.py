"""Independent finite checks of the local complement-sampling account.

Run from any directory with Python 3.10+ and NumPy. Direct Born-rule sums over
every balanced subset are compared with the analytical formulas. These checks
are not proofs of the asymptotic theorem, novelty, or a cryptographic assumption.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

TOL = 2e-11


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def close(actual, expected, message: str, tolerance: float = TOL) -> float:
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    require(error < tolerance, f"{message}: error {error:.3g}")
    return error


def balanced_masks(n: int) -> np.ndarray:
    N = 2**n
    subsets = np.asarray(list(itertools.combinations(range(N), N // 2)))
    masks = np.zeros((len(subsets), N))
    masks[np.arange(len(subsets))[:, None], subsets] = 1
    return masks


def bv_masks(n: int) -> np.ndarray:
    return np.asarray([
        [int(((u & x).bit_count() % 2) == b) for x in range(2**n)]
        for u in range(1, 2**n) for b in (0, 1)
    ], dtype=float)


def qubit_effects(eta: float = 1.0) -> list[np.ndarray]:
    x = eta / (2 * (1 + eta))
    v0, v1 = np.array([x, -(1 - x)]), np.array([-(1 - x), x])
    return [np.outer(v0, v0), np.outer(v1, v1),
            2 * x * (1 - x) * np.ones((2, 2))]


def block_effects(D: int) -> list[np.ndarray]:
    U = 2 * np.ones((D, D)) / D - np.eye(D)
    return [np.outer(U[:, a], U[:, a]) for a in range(D)]


def expected_score(n: int, m: int) -> float:
    N, D = 2**n, 2**m
    if n == 1:
        return 1.0
    if m == 0:
        return 1 / (N - 1)
    if m == 1:
        return (1 + N / 8) / (N - 1)
    return (N - 2 * N / D + 1) / (N - 1)


def direct_scores(masks: np.ndarray, m: int, eta: float = 1.0,
                  tuned_eta: float | None = None) -> np.ndarray:
    """Born probabilities, including the prefix probability and every outcome."""
    N, D = masks.shape[1], 2**m
    B, K = N // D, N // 2
    if m == 0:
        effects = [np.ones((1, 1))]
    elif m == 1 and B > 1:
        effects = qubit_effects(eta if tuned_eta is None else tuned_eta)
    else:
        effects = block_effects(D)
    scores, total_probability = np.zeros(len(masks)), np.zeros(len(masks))
    for z in range(B):
        v = masks[:, z * D:(z + 1) * D] / math.sqrt(K)
        rho = np.einsum("si,sj->sij", v, v)
        if m == 1:
            rho[:, 0, 1] *= eta
            rho[:, 1, 0] *= eta
        if m == 0:
            outputs = [z ^ (B // 2)]
        elif m == 1 and B > 1:
            outputs = [2 * z, 2 * z + 1, 2 * (z ^ (B // 2))]
        else:
            outputs = list(range(z * D, (z + 1) * D))
        for E, y in zip(effects, outputs):
            probability = np.einsum("ij,sji->s", E, rho)
            require(float(probability.min()) >= -TOL, "negative probability")
            total_probability += probability
            scores += probability * (1 - 2 * masks[:, y])
    close(total_probability, np.ones(len(masks)), "normalization, all outcomes")
    require(float(np.max(np.abs(scores))) <= 1 + TOL, "invalid score range")
    return scores


def payoff_checks(n: int) -> dict:
    N = 2**n
    s, basis = np.ones(N) / math.sqrt(N), np.eye(N)
    theoretical = np.asarray([
        (np.outer(s, s) - math.sqrt(N) / 2 *
         (np.outer(basis[y], s) + np.outer(s, basis[y]))) / (N - 1)
        for y in range(N)
    ])
    errors = {}
    for name, masks in (("balanced", balanced_masks(n)), ("BV", bv_masks(n))):
        psi = masks / math.sqrt(N / 2)
        empirical = np.einsum("sy,si,sj->yij", 1 - 2 * masks, psi, psi) / len(masks)
        errors[name] = close(empirical, theoretical, f"{name} payoff n={n}")
    return {"n": n, "max_entry_errors": errors}


def certificate_check(D: int) -> dict:
    s, I = np.ones(D) / math.sqrt(D), np.eye(D)
    P = np.outer(s, s)
    if D == 1:
        Y, effects, expected_cost = np.zeros((1, 1)), [np.zeros((1, 1))], 0.0
    elif D == 2:
        Y, effects, expected_cost = -(I - P) / 4, qubit_effects()[:2], -0.25
    else:
        Y, effects, expected_cost = (3 - D) * P / 2 - (I - P) / 2, block_effects(D), 2 - D
    costs = [math.sqrt(D) / 2 * (np.outer(I[a], s) + np.outer(s, I[a]))
             for a in range(D)]
    minimum_slack = min(float(np.linalg.eigvalsh(-Y).min()),
                        *(float(np.linalg.eigvalsh(C - Y).min()) for C in costs))
    minimum_effect = min(float(np.linalg.eigvalsh(I - sum(effects)).min()),
                         *(float(np.linalg.eigvalsh(E).min()) for E in effects))
    value = sum(float(np.trace(C @ E)) for C, E in zip(costs, effects))
    require(minimum_slack > -TOL and minimum_effect > -TOL, f"certificate D={D}")
    close(value, np.trace(Y), f"primal-dual equality D={D}")
    close(value, expected_cost, f"analytical cost D={D}")
    return {"D": D, "cost": value, "minimum_dual_slack": minimum_slack,
            "minimum_primal_slack": minimum_effect}


def source_check(n: int) -> dict:
    """Build source mixtures from actual sampled strings and partner membership."""
    masks, N = balanced_masks(n), 2**n
    worst = 0.0
    plus = np.ones((2, 2)) / 2
    for mask in masks:
        mixture = np.zeros((N // 2, 2, 2))
        for x in np.flatnonzero(mask):
            z, b = divmod(int(x), 2)
            if mask[x ^ 1]:
                state = plus
            else:
                state = np.zeros((2, 2)); state[b, b] = 1
            mixture[z] += state / (N // 2)
        fibers = mask.reshape(-1, 2)
        target = np.einsum("zi,zj->zij", fibers, fibers) / (N // 2)
        worst = max(worst, close(mixture, target, f"source equality n={n}"))
        diagonal = np.diagonal(mixture, axis1=1, axis2=2).reshape(-1)
        close(diagonal, mask / (N // 2), "dephased source is an ordinary sample")
    return {"n": n, "subsets": len(masks), "max_entry_error": worst}


def ry(theta: float) -> np.ndarray:
    c, s = math.cos(theta / 2), math.sin(theta / 2)
    return np.array([[c, -s], [s, c]])


def hardware_checks() -> dict:
    I = np.eye(2)
    CNOT = np.array([[1., 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]])
    max_error = 0.0
    for eta in (0.0, 0.2, 0.5, 1.0):
        theta = 2 * math.acos(1 / (1 + eta))
        controlled = np.zeros((4, 4)); controlled[:2, :2] = I
        controlled[2:, 2:] = ry(theta)
        decomposed = CNOT @ np.kron(I, ry(-theta / 2)) @ CNOT @ np.kron(I, ry(theta / 2))
        max_error = max(max_error, close(decomposed, controlled, "controlled rotation decomposition"))
        U = np.kron(ry(-math.pi / 2), I) @ controlled @ np.kron(ry(math.pi / 2), I)
        close(U.T @ U, np.eye(4), "unitarity")
        # Basis order |input,ancilla>; the ancilla is initialized in |0>.
        K0, K1 = U[np.ix_([0, 2], [0, 2])], U[np.ix_([1, 3], [0, 2])]
        physical = [K0.T @ np.diag([0., 1.]) @ K0,
                    K0.T @ np.diag([1., 0.]) @ K0, K1.T @ K1]
        for a, b in zip(physical, qubit_effects(eta)):
            max_error = max(max_error, close(a, b, "physical POVM effects"))
    W = np.array([[1., -3.], [-3., 1.], [math.sqrt(6), math.sqrt(6)]]) / 4
    max_error = max(max_error, close(W.T @ W, I, "Naimark isometry"))
    for row, E in zip(W, qubit_effects()):
        max_error = max(max_error, close(np.outer(row, row), E, "Naimark outcomes"))
    probabilities = np.asarray([[float(v @ E @ v) for E in qubit_effects()]
                                for v in (I[0], I[1], np.ones(2) / math.sqrt(2))])
    close(probabilities, [[1/16, 9/16, 3/8], [9/16, 1/16, 3/8], [1/8, 1/8, 3/4]],
          "exact classical simulator probability table")
    return {"eta_values": [0, 0.2, 0.5, 1], "max_entry_error": max_error,
            "source_state_outcome_probabilities": probabilities.tolist()}


def classical_posterior_checks() -> dict:
    masks = balanced_masks(3)
    values = []
    for d in range(1, 5):
        compatible = masks[np.all(masks[:, :d] == 1, axis=1)]
        posterior_success = 1 - compatible[:, d:].mean(axis=0)
        close(posterior_success, np.full(8 - d, 4 / (8 - d)), "classical posterior")
        values.append({"distinct_samples": d, "compatible_subsets": len(compatible),
                       "success_on_each_unseen_string": float(posterior_success[0])})
    return {"N": 8, "cases": values}


def changed_source_checks() -> list[dict]:
    """The flag uses source-private membership, so is NOT an ordinary sample."""
    results = []
    for n in (2, 3):
        N, total = 2**n, 0.0
        masks = balanced_masks(n)
        for mask in masks:
            for x in np.flatnonzero(mask):
                z, b = divmod(int(x), 2)
                flag = b == 1 and mask[x ^ 1] == 0
                y = 2 * z if flag else 2 * (z ^ (N // 4))
                total += (1 - 2 * mask[y]) / (N // 2)
        actual = total / len(masks)
        close(actual, (N + 4) / (4 * (N - 1)), "changed classical source flag")
        results.append({"n": n, "subsets": len(masks), "average_score": actual,
                        "average_success": (1 + actual) / 2,
                        "expected_success": 5 * N / (8 * (N - 1))})
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON report path")
    args = parser.parse_args()
    frontier, dephasing = [], []
    for n in range(1, 5):
        masks = balanced_masks(n)
        for m in range(n + 1):
            scores = direct_scores(masks, m)
            expected = expected_score(n, m)
            error = close(scores.mean(), expected, f"frontier n={n},m={m}")
            frontier.append({"n": n, "m": m, "subsets": len(masks),
                             "average_score": float(scores.mean()), "expected_score": expected,
                             "average_success": float((1 + scores.mean()) / 2),
                             "absolute_error": error})
        if n in (2, 3):
            N = 2**n
            for eta in (0.0, 0.2, 0.5, 1.0):
                for tuned in (True, False):
                    actual = float(direct_scores(masks, 1, eta, None if tuned else 1.0).mean())
                    c = eta**2 / (4 * (1 + eta)) if tuned else (3 * eta - 1) / 16
                    expected = (1 + N * c) / (N - 1)
                    error = close(actual, expected, "dephasing Born-rule score")
                    dephasing.append({"n": n, "eta": eta, "retuned": tuned,
                                      "actual_score": actual, "expected_score": expected,
                                      "absolute_error": error})
    bad_set = np.array([[1., 1., 0., 0., 1., 1., 0., 0.]])
    close(direct_scores(bad_set, 1), [-1], "one-qubit worst-case counterexample")
    full_fiber = np.array([[1., 1., 1., 1., 0., 0., 0., 0.]])
    close(direct_scores(full_fiber, 2), [-1], "block worst-case counterexample")
    root = Path(__file__).resolve().parents[1]
    source_hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted((root / "science").glob("*.md"))}
    result = {
        "status": "pass", "numpy_version": np.__version__, "tolerance": TOL,
        "source_sha256": source_hashes,
        "frontier_exhaustive": frontier, "dephasing_exhaustive": dephasing,
        "payoff_identities": [payoff_checks(n) for n in (1, 2, 3)],
        "primal_dual_certificates": [certificate_check(D) for D in (1, 2, 4, 8, 16, 32)],
        "hybrid_source_identity": [source_check(n) for n in (1, 2, 3)],
        "measurement_implementation": hardware_checks(),
        "classical_posterior": classical_posterior_checks(),
        "changed_classical_source": changed_source_checks(),
        "worst_case_counterexamples": {"n": 3, "one_qubit_set": [0, 1, 4, 5],
                                       "block_set": [0, 1, 2, 3], "success": 0},
        "limits": "Finite checks do not prove the general theorem, novelty, or strong-PRP security."
    }
    report = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
