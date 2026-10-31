# Reproducing the scientific checks

The analytical proofs are in [science/](../science/README.md). The executable checks below independently construct small input instances and measurement probabilities to catch normalization, finite-size, endpoint, and implementation errors. They are deliberately separate from claims of general optimality or computational hardness.

## Run

Use Python 3.10 or newer. The checked NumPy version is pinned in [requirements.txt](requirements.txt).

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py --output /tmp/local-complement-checks.json
```

The script exits nonzero on a failed check and prints a JSON report. The optional output path stores the same report; omitting it does not write a file. Numerical tolerances are $2\times10^{-11}$, and validation remains active under Python optimization. The report includes SHA256 hashes of the scientific pages present at execution.

The committed [checked report](checked-results.json) records the finite run accompanying this account. Its source hashes identify the scientific pages checked; a new run reports the pages present in your checkout.

## Scope

| Check | Construction and coverage | What it establishes |
| --- | --- | --- |
| Exact frontier | Direct Born-rule sums for every balanced subset at $n=1,2,3,4$ and every $0\leq m\leq n$ | Formula agreement for all tested finite instances; all outcomes sum to probability one |
| Common payoff operator | Independent subset enumeration and explicit nonzero parity labels at $n=1,2,3$ | Both ensembles match the stated operator entry by entry |
| Optimality certificates | Primal and dual slack eigenvalues, objective equality at $D=1,2,4,8,16,32$ | Feasibility and equality of the displayed finite-dimensional certificates |
| Hybrid source | Mixtures constructed from every sampled string and its partner-membership bit at $n=1,2,3$ | Equality with the measured-prefix source for each set, and ordinary samples after dephasing |
| Residual coherence | All balanced subsets at $n=2,3$, with $\eta=0,0.2,0.5,1$, for retuned and fixed measurements | Agreement with both distinct finite-size formulas |
| Physical measurement | Explicit two-qubit gate composition, controlled-rotation decomposition, Kraus operators, and Naimark isometry | The stated physical realization gives the intended effects and outcome probabilities |
| Classical posterior | All compatible balanced subsets for one through four distinct observations at $N=8$ | Exact posterior probability on each unseen output |
| Worst-case boundary | Two explicit balanced sets at $n=3$ | The local constructions can have zero success on a fixed set |
| Changed classical source | All balanced subsets at $n=2,3$, with a private-membership flag encoded at the source | A different one-bit classical source can exceed the prescribed quantum input's optimum; the ordinary-sample comparator is essential |

The largest exhaustive ensemble has $\binom{16}{8}=12{,}870$ sets. Across the frontier checks, the ensemble sizes are 2, 6, 70, and 12,870. Typical execution takes a few seconds or less on an ordinary CPU; no quantum simulator package, SDP solver, network access, or random seed is required.

## Representative expected values

| $N$ | $m=0$ success | $m=1$ success | $m=2$ success |
| --- | --- | --- | --- |
| 4 | $2/3$ | $3/4$ | $1$ |
| 8 | $4/7$ | $9/14$ | $6/7$ |
| 16 | $8/15$ | $3/5$ | $4/5$ |

For $m=n$, success is one. For the one-qubit effects, the source-state outcome probabilities are $(1/16,9/16,3/8)$ on $\lvert0\rangle$, $(9/16,1/16,3/8)$ on $\lvert1\rangle$, and $(1/8,1/8,3/4)$ on $\lvert+\rangle$. These rational probabilities also support the exact classical simulation used in the conditional strong-PRP argument.

## Limits of verification

Finite enumeration does not prove the all-dimension upper bound; the matching analytical certificates do. Numerical checks do not establish novelty, the existence or security of a strong-PRP family, fault-tolerant compilation costs, or experimental performance. The script checks a specified dephasing channel, not arbitrary physical noise. Scientific proof and source attribution should be read alongside the report.

[Repository overview](../README.md) · [Science reading route](../science/README.md)
