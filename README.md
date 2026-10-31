# Local Quantum Complement Sampling

**How much of a quantum sample must remain available for quantum processing to find an element absent from the sampled set?** For a uniformly random balanced subset of an $`N=2^n`$-element universe, the answer can be as small as one input qubit. Measuring the other $`n-1`$ qubits computationally leaves an exactly solvable classical–quantum decision problem with a constant success advantage.

This repository gives the complete optimal tradeoff between retained input qubits and average complement-sampling success, including explicit measurements, converse certificates, source preparation, and a dephasing analysis. The task and the unrestricted quantum–classical sample separation originate in [Benedetti, Buhrman, and Weggemans](https://arxiv.org/html/2502.08721v3); the contribution here is their precise behavior under the specified partial-measurement interface.

## Principal result

The unknown set $`S`$ contains $`N/2`$ strings. One input is the positive-amplitude sample

```math
\lvert S\rangle=\sqrt{\frac2N}\sum_{x\in S}\lvert x\rangle.
```

A fixed $`n-m`$ input qubits are measured in the computational basis before the receiver acts. The receiver gets the classical outcome and the remaining $`m`$ input qubits, may process them with fresh ancillas, and must return one string outside $`S`$. There is no membership oracle, abstention, or postselection at the receiver.

For $`n\geq2`$, the exact optimal **average success probability** is:

| Retained input qubits | Exact success probability | Limit for fixed $`m`$ as $`n`$ grows |
| --- | --- | --- |
| $`m=0`$ | $`N/[2(N-1)]`$ | $`1/2`$ |
| $`m=1`$ | $`9N/[16(N-1)]`$ | $`9/16`$ |
| $`2\leq m\leq n`$ | $`(N-N/2^m)/(N-1)`$ | $`1-2^{-m}`$ |

For $`n=1`$, reading the sampled bit and returning its complement succeeds perfectly. Full access $`m=n`$ also gives perfect success. The [frontier proof](science/access-frontier.md) covers arbitrary receivers after the stipulated interface, not only the attaining constructions.

One retained input qubit therefore preserves a constant success advantage. Two give limiting success $`3/4`$, and $`O(\log(1/\epsilon))`$ retained input qubits suffice for average failure at most $`\epsilon`$. For the uniform balanced-set ensemble, matching a fixed advantage with ordinary classical samples still requires $`\Omega(N)`$ samples, by the established classical lower bound.

## What supplies the advantage?

With one retained input qubit, the source delivers a classical prefix and one of three states: $`\lvert0\rangle`$, $`\lvert1\rangle`$, or $`\lvert+\rangle`$. The preparation label is private. An optimal three-outcome measurement either proposes a bit in that prefix or returns a string with a different prefix. Every outcome is used.

A trusted source can prepare the same input directly using one classical sample, one partner-membership check, and one prepared qubit. An explicit receiver uses one initialized measurement ancilla, two CNOTs, and four one-qubit rotations in a continuous-rotation gate model. These are separate source and apparatus costs; the theorem counts retained **input** qubits.

If the remaining qubit is dephased by a known factor $`\eta\in[0,1]`$, an optimally retuned measurement has score

```math
V_{N,\eta}^{\star}
=\frac{1+N\eta^2/[4(1+\eta)]}{N-1},
\qquad V=2p-1.
```

Every fixed $`\eta>0`$ preserves a constant limiting success bias. The [robustness analysis](science/robustness.md) also computes the distinct performance of an unchanged ideal measurement.

## Read the science

| Question | Authoritative account |
| --- | --- |
| What is the problem, and what can each party access? | [Model and operational task](science/model.md) |
| Why can two different input ensembles have the same one-copy behavior? | [Common payoff operator](science/payoff-identity.md) |
| What is the optimum, and why can no allowed receiver do better? | [Exact access frontier](science/access-frontier.md) |
| How are the source and measurement physically implemented? | [Source access and implementation](science/source-and-implementation.md) |
| How much residual coherence is useful? | [Dephasing and optimal retuning](science/robustness.md) |
| What does the result say about quantum resources? | [Physical interpretation and boundaries](science/interpretation.md) |
| Which ingredients are established in earlier work? | [Related work](references/related-work.md) and [bibliography](references/references.bib) |

For a connected route, start with the [science overview](science/README.md). For machine-assisted reading, use [llms.txt](llms.txt).

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) selects the relevant parts of the author's available manuscript, translates its notation, and connects general measurement optimization to this particular sampling task. A complete four-element example accounts for every output and separates success probability from signed score.

The [30-milestone map](learning/MILESTONES.md) follows the project's scientific dependencies. Its **14 background/preliminaries milestones** build the states, measurements, optimization tools, and fixed-access model; its **16 narrative/innovation milestones** develop the payoff identity, exact frontier, implementation, classical comparisons, and limitations. Each milestone states a central question, understanding target, dependencies, conceptual connection, and source pointers.

Start with the [learning overview](learning/README.md) and use the bridge alongside the milestones. The scientific account above remains the authoritative proof route.

## Reproduce the finite checks

With Python 3.10 or newer, run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_science.py --output /tmp/local-complement-checks.json
```

The suite exhausts all balanced subsets through $`n=4`$, checks both ensemble payoff identities, verifies primal–dual certificates, reconstructs the hybrid source, and composes the measurement circuit. See the [verification guide](verification/README.md) for the exact scope and expected values. These finite checks support the analytical proofs; they do not replace them or validate a cryptographic assumption.

## Scope that matters

- Success is averaged over the stated ensemble. The local decoder can fail on a particular fixed set.
- The access interface fixes which input qubits are measured and their measurement basis before receiver processing. It does not model unrestricted streaming quantum memory.
- Classical competitors receive ordinary samples, equivalently the fully dephased source. Arbitrary classical encodings of the source's private membership information are a different interface.
- Uniform balanced subsets and Bernstein–Vazirani subsets share the one-copy frontier, but their classical multi-copy sample complexities differ: $`\Omega(N)`$ versus $`\Theta(n)`$.
- Generic state preparation is charged. A separate efficient keyed-source construction uses an explicit classical strong-PRP assumption and gives conditional computational hardness, not the uniform-ensemble information-theoretic bound.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository retains its [MIT license](LICENSE).
