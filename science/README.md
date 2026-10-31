# Scientific account

Complement sampling asks for one element outside an unknown set using samples drawn from that set. The established global quantum algorithm uses interference across a positive-amplitude subset state. Here the question is which part of that input must remain available to the receiver after compulsory computational-basis measurements.

The exact result is a resource frontier. One retained input qubit gives average success approaching $9/16$; two give success approaching $3/4$; and, for $m\geq2$, the exact failure probability is

$$
1-p^\star_{n,m}=\frac{2^{n-m}-1}{2^n-1}.
$$

The source, receiver interface, classical comparison, and ensemble average are all part of this claim.

## A connected reading route

1. **[Model and operational task](model.md).** Define the positive-amplitude sample, compulsory partial measurement, output rule, and allowed instruments. Distinguish a retained input subsystem from unrestricted coherent memory.
2. **[Common one-copy payoff operator](payoff-identity.md).** Average the input state together with its signed output score. Prove the operator identity for uniform balanced subsets and for Bernstein–Vazirani subsets.
3. **[Exact access frontier](access-frontier.md).** Reduce arbitrary receivers to a local measurement optimization. Exhibit matching measurements and positive-semidefinite converse certificates, including all small endpoints.
4. **[Source access and implementation](source-and-implementation.md).** Prepare the same hybrid input with classical sampling and a private membership check; realize the qubit POVM with an explicit ancilla circuit. Derive the inherited classical comparison and a separate conditional strong-PRP construction.
5. **[Residual coherence](robustness.md).** Derive the finite-size dephasing payoffs and exact optimal retuning. Separate that optimum from the behavior of the unchanged circuit.
6. **[Physical interpretation and boundaries](interpretation.md).** Explain the roles of fiber occupancy, interference, classical encoding, source costs, and average-case performance.

## Proof dependencies

| Claim | Required input | Where the proof closes |
| --- | --- | --- |
| Same score for every one-copy receiver in the balanced and BV ensembles | Ensemble definitions and linearity of measurement probabilities | Payoff identity, Theorem 1 and Corollary 1 |
| Exact retained-input optimum | Payoff identity and the fixed measurement interface | Access frontier, Theorem 2; matching primal and dual certificates |
| Direct one-qubit source | One uniform sample and one private partner-membership evaluation | Source implementation, Proposition 1 |
| Keyed-family computational separation | Classical strong-PRP security with forward and inverse access | Source implementation, Propositions 2–3 |
| Optimal residual-coherence score | Known qubit dephasing parameter and the same hybrid interface | Robustness theorem and its finite-size payoff shift |

The [related-work account](../references/related-work.md) identifies the inherited global diffuser, sample lower bounds, BV benchmark, and measurement-optimization methods. The [verification suite](../verification/README.md) provides finite, independently constructed numerical checks. The analytical arguments are the general proofs.

[Repository overview](../README.md)
