# From Watrous to local quantum complement sampling

Suppose a source samples from a hidden set of allowed strings, while the receiver is asked to return a string outside that set. An ordinary sample identifies an element to avoid. A quantum sample can also preserve interference between possible elements. This project asks how much of that coherent input must remain after a specified computational-basis measurement.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Use the [official author page](https://cs.uwaterloo.ca/~watrous/TQI/) and its standard-layout chapter PDFs. The selected readings below supply the language of the proof; they do not require reading the whole book. This bridge adds the task-specific connections, while the [science pages](../science/README.md) remain the authoritative home of the results.

## 1. Selected reading scope

Page numbers below are the **printed page numbers** in the author's standard-layout manuscript. PDF page fragments refer to the individual chapter files, whose page counts restart. In particular, Chapter 2 starts on printed page 58 and Chapter 3 on printed page 124.

| Read when needed | Verified source location | Use in this project |
|---|---|---|
| States, mixtures, and classical records | [Chapter 2, §2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=1), “Registers and states,” starts p. 58; focus on §2.1.2, pp. 61–66 | Represent the supplied sample and the classical prefix without revealing the hidden preparation label. |
| Keeping a subsystem | [§2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10), “Reductions and purifications of quantum states,” starts p. 67; use the reduction discussion, pp. 67–68 | Distinguish discarding a register from measuring it and retaining its classical outcome. Purification results are not needed for the main proof. |
| Allowed physical transformations | [§2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15), “Quantum channels,” starts p. 72; Definition 2.13 is on p. 73 | Describe the compulsory input measurement and the residual-qubit dephasing model. |
| Outcomes and implementation | [§2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=43), “Measurements,” starts p. 100; Definition 2.34, p. 101; Theorem 2.42 and Corollary 2.43, p. 109; instruments, pp. 111–112 | Translate arbitrary decoders into POVMs and understand the role of a measurement ancilla. |
| Optimal decisions from quantum data | [Chapter 3, §3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=1), “Quantum state discrimination,” starts p. 124; focus on §3.1.2, pp. 132–136 | Use Hermitian payoff operators, the measurement SDP, and optimality certificates. |
| Why a converse certificate proves optimality | [Chapter 1, §1.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=53), “Semidefinite programming,” pp. 53–55 | Compare a feasible measurement with a feasible dual bound. The explicit matching certificates here can be checked directly by weak duality. |

For notation lookup only, Chapter 1 has vectors and tensor products in §1.1.1, pp. 1–7, and linear operators in §1.1.2, starting p. 8. Trace and the operator inner product appear on p. 15; Hermitian and positive-semidefinite operators on p. 17; density operators on p. 18. These are supporting pages within the same anchor, not additional prerequisites to finish before reading the project.

The most direct connection is **§3.1.2, equations (3.33)–(3.35), printed p. 133**. Watrous already allows arbitrary Hermitian payoff functions, rather than only a reward for correctly guessing a state label. The project uses that existing framework. Its additional work is to derive the appropriate payoffs from complement sampling and to solve the resulting restricted-access problem.

## 2. Notation and assumptions

| Watrous notation or concept | Project notation and interpretation |
|---|---|
| A finite-dimensional complex space $\mathcal X$ | The retained input register has dimension $D=2^m$. The measured prefix has $B=2^{n-m}$ possible classical values; $N=BD=2^n$. |
| A state $\rho\in\mathrm D(\mathcal X)$ | The original sample is $\lvert S\rangle\langle S\rvert$. The delivered state after the prefix measurement is $\rho_{ZA}^{S}$. |
| An ensemble written as a function $\eta(a)$ with positive operator values | A weighted state such as $p_t\rho_t$ records both the probability of a fiber type and its conditional state. The source's type label is not sent to the receiver. |
| A measurement $\mu(a)$ | An effect $E_{w,a}^{(z)}$ gives the probability of the final returned string $(w,a)$ conditional on observed prefix $z$. The one-qubit construction uses $E_0,E_1,E_*$. |
| The inner product $\langle A,B\rangle$ and adjoint $A^*$ | For Hermitian operators the payoff is $\operatorname{Tr}(AB)$. Project pages may write the adjoint as $A^\dagger$ and pure states in bra–ket notation. |
| A Hermitian payoff function $\varphi(a)$ | After the project-specific reduction, choose $\varphi(a)=-C_a$ for within-prefix outputs and $\varphi(*)=0$ for the fallback in the reduced optimization. |
| A dual variable that upper-bounds every $\varphi(a)$ | Its negative is the project's lower-bound certificate $Y$, satisfying $Y\preceq C_a$ and, when a fallback is available, $Y\preceq0$. |

The symbol $\eta$ has two different uses: Watrous uses it for an ensemble function, while the [robustness page](../science/robustness.md) uses a scalar $\eta\in[0,1]$ for remaining qubit coherence. They are unrelated.

### What the source promises

The hidden subset has size $K=N/2$, and the input is

$$
\lvert S\rangle=\frac1{\sqrt K}\sum_{x\in S}\lvert x\rangle.
$$

Its amplitudes are positive in the specified computational basis. This is more information than specifying only its measurement probabilities. Arbitrary phases with the same support would change the task.

Writing a string as $x=(z,a)$, prefix measurement produces

$$
\rho_{ZA}^{S}
=\frac1K\sum_z
\lvert z\rangle\langle z\rvert
\otimes
\lvert v_z\rangle\langle v_z\rvert,
\qquad
\lvert v_z\rangle=\sum_{a:(z,a)\in S}\lvert a\rangle.
$$

The classical record $z$ remains available. Taking only the partial trace over $Z$ would remove that record and define a different input. The model also forbids quantum preprocessing that transfers information out of the measured qubits before this interface is applied. These restrictions are specified in [the model](../science/model.md), not supplied by the textbook.

## 3. From a measurement problem to the exact frontier

The logical path has four steps.

**First, put the task into the payoff.** For each possible returned string $y$, the project averages the input state together with the signed score:

$$
B_y=\mathbb E_S\!\left[
\bigl(1-2\mathbf1_{\{y\in S\}}\bigr)
\lvert S\rangle\langle S\rvert
\right].
$$

The [payoff identity](../science/payoff-identity.md) derives this matrix using subset inclusion probabilities. It also proves that the random-balanced and Bernstein–Vazirani ensembles have the same $B_y$. Neither statement follows merely from the definition of a POVM.

**Second, impose the measured-prefix interface.** Only a block of the input remains quantum. The effective measurement is therefore block diagonal in the observed prefix. Within one block, let $F_a$ denote the effect that returns suffix $a$ with the same prefix. These effects need only satisfy

$$
F_a\succeq0,\qquad \sum_a F_a\preceq I_D.
$$

The remaining effect $F_*=I_D-\sum_aF_a$ returns a string with a different prefix. It is an ordinary output, rather than an aborted trial. This option exists when at least one prefix bit was measured.

**Third, apply the textbook's optimization framework to the actual costs.** With

$$
\lvert s_D\rangle=\frac1{\sqrt D}\sum_a\lvert a\rangle,
\qquad
C_a=\frac{\sqrt D}{2}
\left(
\lvert a\rangle\langle s_D\rvert+
\lvert s_D\rangle\langle a\rvert
\right),
$$

the local cost is

$$
L_D=
\min_{\{F_a\}}
\sum_a\operatorname{Tr}(C_aF_a).
$$

Adding the complete effect $F_*$ with zero reduced cost turns this into the measurement optimization of Watrous §3.1.2, with a sign change. The zero cost is a feature of the **reduced objective**: the full finite-size game still contains its common payoff term. It does not mean that fallback outputs are excluded from scoring.

**Fourth, exhibit both sides of the bound.** A matrix $Y$ with $Y\preceq0$ and $Y\preceq C_a$ obeys

$$
\sum_a\operatorname{Tr}(C_aF_a)-\operatorname{Tr}Y
=
\sum_a\operatorname{Tr}\!\left[(C_a-Y)F_a\right]
+\operatorname{Tr}\!\left[(-Y)F_*\right]
\geq0.
$$

Each term is nonnegative because it is the trace of a product of positive-semidefinite operators. A feasible measurement attaining $\operatorname{Tr}Y$ is optimal. The [access-frontier proof](../science/access-frontier.md) constructs these matching objects, including the exceptional one-qubit measurement. For full access, no changed prefix exists and completeness replaces the inequality constraint.

This argument explains what the certificate proves: an upper bound for **every receiver allowed by the input model**, including ancillary processing and intermediate measurements. It does not require solving an SDP numerically for every $n$.

## 4. A complete four-element example

Take $n=2$, $N=4$, and retain the last input qubit, so $m=1$. The universe is $\{00,01,10,11\}$, and $S$ is uniform over its six two-element subsets.

The source measures the first bit. A pair containing only $z0$ leaves $\lvert0\rangle$; one containing only $z1$ leaves $\lvert1\rangle$; a full pair leaves $\lvert+\rangle$. The receiver is told $z$ but not which of these three states was prepared.

Use the complete POVM

$$
E_0=\frac1{16}
\begin{pmatrix}1&-3\\-3&9\end{pmatrix},
\qquad
E_1=\frac1{16}
\begin{pmatrix}9&-3\\-3&1\end{pmatrix},
\qquad
E_*=\frac34\lvert+\rangle\langle+\rvert.
$$

These matrices are positive and sum to $I_2$. Its three possible input states give:

| Input state | Probability of $0$ | Probability of $1$ | Probability of $*$ |
|---|---:|---:|---:|
| $\lvert0\rangle$ | $1/16$ | $9/16$ | $3/8$ |
| $\lvert1\rangle$ | $9/16$ | $1/16$ | $3/8$ |
| $\lvert+\rangle$ | $1/8$ | $1/8$ | $3/4$ |

Outcomes $0$ and $1$ return $z0$ and $z1$. The fallback returns $(1-z)0$: it changes the observed first bit and appends zero. Every row sums to one, and every outcome returns an answer.

For example, if $S=\{00,01\}$, the prefix is certainly $0$ and the qubit is $\lvert+\rangle$. The three branches return $00$ with probability $1/8$, $01$ with probability $1/8$, and $10$ with probability $3/4$. The first two fail; the fallback succeeds. Thus $p_{\rm succ}=3/4$ and the signed score is $V=3/4-1/4=1/2$.

For completeness, the following table accounts for every final output for all six equally likely subsets. Its entries follow from the preceding three-state table and the probability of selecting each occupied pair.

| Hidden $S$ | $\Pr(00)$ | $\Pr(01)$ | $\Pr(10)$ | $\Pr(11)$ | Success $p$ | Score $V=2p-1$ |
|---|---:|---:|---:|---:|---:|---:|
| $\{00,01\}$ | $1/8$ | $1/8$ | $3/4$ | $0$ | $3/4$ | $1/2$ |
| $\{00,10\}$ | $7/32$ | $9/32$ | $7/32$ | $9/32$ | $9/16$ | $1/8$ |
| $\{00,11\}$ | $7/32$ | $9/32$ | $15/32$ | $1/32$ | $3/4$ | $1/2$ |
| $\{01,10\}$ | $15/32$ | $1/32$ | $7/32$ | $9/32$ | $3/4$ | $1/2$ |
| $\{01,11\}$ | $15/32$ | $1/32$ | $15/32$ | $1/32$ | $15/16$ | $7/8$ |
| $\{10,11\}$ | $3/4$ | $0$ | $1/8$ | $1/8$ | $3/4$ | $1/2$ |

Averaging the six success probabilities gives $3/4$, and averaging the scores gives $1/2$. This agrees with

$$
p^\star_{2,1}=\frac{9N}{16(N-1)}=\frac34.
$$

The value $3/4$ is specific to this small universe. With one retained input qubit and growing $N$, the success probability approaches $9/16$; the general one-qubit result does not promise success at least $2/3$.

For comparison, one ordinary classical sample identifies a member of $S$. Each of the other three strings is outside $S$ with posterior probability $2/3$, so the optimal classical one-sample success is $2/3$, with score $1/3$.

The example illustrates three distinctions. Success probability and signed score differ by the affine conversion $V=2p-1$. The result averages over hidden subsets, whose individual performances vary. Finally, the fallback is part of the algorithm's unconditional output distribution, so its success and failure must both be included.

## 5. What remains beyond the selected source

The anchor supplies the measurement and optimization framework. The following parts require the project's own arguments or its attributed primary research sources:

- **The task and ensemble calculation.** The positive-amplitude input promise, averaged payoff identity, and equality with the Bernstein–Vazirani one-copy game are derived in the model and payoff pages.
- **The exact access frontier.** The measured-prefix restriction, availability of changed-prefix outputs, matching local measurements and dual certificates, and small endpoints are proved in the access-frontier page.
- **The classical comparison.** The ordinary-sample posterior calculation is in the source page. Equal one-copy payoff operators do not equate the two ensembles' multi-copy classical sample complexities.
- **The source and circuit.** A private classical sample and partner-membership test prepare the same one-qubit hybrid input. In a continuous-rotation gate model, the explicit generalized measurement uses one initialized ancilla, two CNOTs, four one-qubit rotations, and at most two binary readouts; finite-alphabet compilation adds an accuracy-dependent cost. Watrous's dilation theorem explains why ancillary implementation is possible; these particular resources come from the project's construction.
- **Stability and efficient instantiation.** The dephasing calculation distinguishes a retuned measurement from the original fixed one. The efficient keyed source and its hardness claim require the stated classical strong-PRP assumption and the explicit reductions, rather than a textbook state-discrimination theorem.

The retained-qubit count is not a count of all hardware qubits, a lower bound on unrestricted streaming memory, or a guarantee for every fixed subset. Classical storage and source preparation remain charged. A source that sends a different classical flag can outperform the prescribed hybrid input; that [countermodel](../science/interpretation.md) bounds the claim to the stated input interface. The local game also supplies no general source-fidelity certificate.

## 6. Continue through the project

The [30-milestone map](MILESTONES.md) places these connections in dependency order. M01–M14 build the background and the fixed-access resource contract. M15–M30 develop the project-specific calculation, optimality, source, comparisons, stability, and final interpretation.

For a direct technical route, read [the model](../science/model.md), [the common payoff](../science/payoff-identity.md), and [the frontier](../science/access-frontier.md), followed by [source and implementation](../science/source-and-implementation.md) and [robustness](../science/robustness.md). The [verification page](../verification/README.md) explains what its finite checks establish; the general statements rest on the analytical proofs.

[Learning overview](README.md) · [Science overview](../science/README.md) · [Related work](../references/related-work.md)
