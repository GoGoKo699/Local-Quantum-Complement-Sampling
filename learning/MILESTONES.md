# Thirty milestones for Local Quantum Complement Sampling

This map follows the scientific question: how much of a positive-amplitude subset sample must remain available for quantum processing to find an element absent from its hidden set? It connects the input model, the exact optimum, its implementation, and the comparisons that give the result meaning.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), available through the [author's book page][watrous]. The [Watrous bridge](WATROUS_BRIDGE.md) translates its notation and decision-theoretic tools into this project. The canonical claims and proofs remain in [the scientific account](../science/README.md). Watrous already formulates measurement optimization for arbitrary Hermitian payoff operators in §3.1.2; the project supplies the particular payoff identity, access restriction, and matching measurements and converse certificates.

## Allocation and dependencies

| Phase | Milestones | Scientific purpose |
| --- | --- | --- |
| Background/preliminaries | M01–M14 | Build from an individual sample and qubit to the joint framework of hidden ensembles, channels, measurements, decision payoffs, and explicit resource access. |
| Narrative/innovation | M15–M30 | Build from the payoff identity and local optimization to the exact frontier, physical implementation, classical comparisons, robustness, and complete interpretation. |

The **14/16 allocation** reflects the meeting of two subjects: quantum measurement optimization and sample-based inference about a hidden set. The first phase develops both before assembling the operational model. The second phase follows the proof's small components into the full scientific claim, with room for the source and comparison boundaries that determine what the advantage means. The map selects the load-bearing ideas rather than enumerating every calculation in the proof.

Dependencies name earlier milestones. Textbook pointers identify the relevant section or printed pages in the author's manuscript; the linked chapter PDFs open at the corresponding location. A textbook pointer supplies foundations, while a canonical science pointer supplies the project's particular statement or derivation. Research-level attribution is retained in those scientific pages and the [related-work account](../references/related-work.md).

## Background/preliminaries — M01–M14

### M01 — Sampling an occupied element and seeking an absent one

- **Central question:** What does one learn from a sample drawn from a set when the requested output must lie outside it?
- **Understanding target:** Define a universe of size $N=2^n$, a balanced hidden subset of size $K=N/2$, an ordinary uniform sample, and the event $Y\notin S$. Distinguish finding one absent element from producing a conditionally uniform complement sample.
- **Dependencies and story role:** Starting point. Establishes the task and observable outcome before introducing quantum states.
- **Conceptual connection:** A sampling promise specifies information access; an output condition specifies the decision problem.
- **Sources:** Watrous [probabilities and expectations, p. 48][w-probability]; [model: universe, subsets, and samples](../science/model.md#universe-subsets-and-positive-amplitude-samples).

### M02 — Positive amplitudes carry more than sampling probabilities

- **Central question:** How can a quantum input and a classical sample have the same computational-basis probabilities but different usefulness?
- **Understanding target:** Interpret $\lvert S\rangle=K^{-1/2}\sum_{x\in S}\lvert x\rangle$ and its density operator. Identify the off-diagonal terms removed by dephasing and explain why the specified positive phases are part of the promise.
- **Dependencies and story role:** Uses M01. Introduces the local mathematical resource that later interference exploits.
- **Conceptual connection:** Probability amplitudes become observable through a choice of measurement; diagonal probabilities alone do not specify a quantum state.
- **Sources:** Watrous [§1.1.2, Hermitian, positive, and density operators, pp. 17–18][w-positive] and [§2.1.2, quantum states][w-states]; [model: positive-amplitude samples](../science/model.md#universe-subsets-and-positive-amplitude-samples).

### M03 — A preparation ensemble is not a revealed label

- **Central question:** What is the difference between knowing how a source chooses states and knowing which state it chose on a run?
- **Understanding target:** Separate the hidden set, classical preparation randomness, delivered density operator, and receiver's information. Explain how a source can select among $\lvert0\rangle$, $\lvert1\rangle$, and $\lvert+\rangle$ while keeping that selection private.
- **Dependencies and story role:** Uses M01–M02. Establishes the information boundary needed for the small quantum decision problem.
- **Conceptual connection:** A classical description available to a simulator can be absent from the physical receiver's input; averaging states does not reveal their labels.
- **Sources:** Watrous [§2.1.2][w-states] and [§3.1.2, ensembles][w-ensemble]; [source preparation and isolation](../science/source-and-implementation.md#2-exact-preparation-of-the-hybrid-source).

### M04 — Measuring a prefix produces a classical–quantum input

- **Central question:** What remains after some input qubits are measured and their outcomes are kept?
- **Understanding target:** Read the tensor decomposition $x=(z,a)$ and the fiber $S_z$. Explain why prefix $z$ occurs with probability $\lvert S_z\rvert/K$ and leaves the normalized subset state on that fiber. Distinguish retaining a classical measurement record from discarding a register.
- **Dependencies and story role:** Uses M02–M03. Assembles individual states into the hybrid input delivered to the receiver.
- **Conceptual connection:** Tensor products, conditional states, and classical records jointly determine what information survives a compulsory measurement.
- **Sources:** Watrous [§1.1.1, tensor products, pp. 6–7][w-tensor], [§2.1, registers and states][w-registers], and [§2.1.3, reductions and purifications][w-reductions]; [model: a fixed retained subsystem](../science/model.md#a-fixed-retained-subsystem).

### M05 — A channel fixes which coherence survives

- **Central question:** How should a compulsory measurement or dephasing operation be represented before optimizing a receiver?
- **Understanding target:** Regard the input interface as a quantum channel independent of the hidden set. Explain the qubit map that preserves diagonal entries and multiplies off-diagonal entries by a known $\eta\in[0,1]$, including its classical endpoint.
- **Dependencies and story role:** Uses M02 and M04. Separates a transformation of the supplied input from later choices of decoder.
- **Conceptual connection:** Optimizing a measurement after a fixed channel is a constrained information-access problem; changing the channel changes the available resource.
- **Sources:** Watrous [§2.2, quantum channels][w-channels]; [model: fixed interface](../science/model.md#a-fixed-retained-subsystem) and [robustness: model](../science/robustness.md#1-model).

### M06 — A measurement is a collection of output effects

- **Central question:** How can a qubit support a measurement with more than two classical outcomes?
- **Understanding target:** Interpret effects $E_j\succeq0$, completeness $\sum_jE_j=I$, and probabilities $\operatorname{Tr}(E_j\rho)$. Distinguish a general POVM from a projective measurement and from an operation that discards selected outcomes.
- **Dependencies and story role:** Uses M02 and M05. Introduces the mathematical object that describes every permitted final decision.
- **Conceptual connection:** The dimension of the quantum input does not fix the number of reported classical alternatives.
- **Sources:** Watrous [§2.3, measurements, especially Definition 2.34][w-measurement]; [model: general receivers](../science/model.md#general-receivers-and-their-measurement-description).

### M07 — Instruments and ancillas reduce to an effective POVM

- **Central question:** Why can a converse about POVMs cover an elaborate receiver with fresh ancillas and intermediate measurements?
- **Understanding target:** Explain how the final classical output absorbs intermediate outcomes and postprocessing into one effective POVM on the supplied input. Identify the requirement that ancillary states contain no additional hidden-set information. Relate a generalized measurement to a unitary implementation on a larger system.
- **Dependencies and story role:** Uses M04–M06. Connects the abstract measurement description to physical receivers and to the scope of an optimality proof.
- **Conceptual connection:** A realization can use more hardware than the input dimension while leaving the induced decision probabilities unchanged.
- **Sources:** Watrous [§2.3.2, basic notions concerning measurements][w-measurement-notions] and [Theorem 2.42 and Corollary 2.43, Naimark representations][w-naimark]; [model: receiver description](../science/model.md#general-receivers-and-their-measurement-description).

### M08 — Success becomes a linear operator payoff

- **Central question:** How does a binary success criterion become a quantum measurement optimization?
- **Understanding target:** Convert success probability $p$ to signed score $V=2p-1$. Interpret a payoff operator as a state weighted by its output-dependent reward and averaged over the hidden ensemble. Explain why that Hermitian operator need not be a density operator.
- **Dependencies and story role:** Uses M01, M03, and M06. Supplies the decision-theoretic language in which the whole frontier will be proved.
- **Conceptual connection:** Averaging Born-rule probabilities turns a hidden-input decision problem into a linear objective over POVMs.
- **Sources:** Watrous [§3.1.2, Hermitian payoffs and measurement optimization, pp. 133–135][w-payoff]; [model: average success and score](../science/model.md#average-success-and-score) and [payoff identity: definition](../science/payoff-identity.md#the-identity).

### M09 — Conditioning changes the ensemble seen by a receiver

- **Central question:** How does observing a sample or prefix change the relative weights of possible hidden sets?
- **Understanding target:** Distinguish an unconditioned uniform ensemble from its posterior after an observation. Explain the size bias toward occupied fibers and exchangeability among positions not distinguished by the observation. Keep an ensemble-average guarantee separate from a guarantee for each fixed set.
- **Dependencies and story role:** Uses M01, M03, M04, and M08. Prepares both the payoff calculation and the ordinary-sample lower bound.
- **Conceptual connection:** Classical conditional probability remains essential inside a quantum decision problem because the hidden variable is a classical set.
- **Sources:** Watrous [probabilities and expectations, p. 48][w-probability] and [§3.1.2, ensemble objectives][w-ensemble]; [conditional pair ensemble](../science/robustness.md#2-conditional-ensemble-and-finite-size-payoff-operators) and [ordinary classical comparison](../science/source-and-implementation.md#4-success-probability-and-the-ordinary-classical-comparison).

### M10 — Parity constraints have a short Fourier description

- **Central question:** Why can a set defined by one binary parity constraint have a simple coherent representation?
- **Understanding target:** Interpret the Bernstein–Vazirani subset $S_{u,b}=\{x:u\cdot x=b\pmod2\}$ for nonzero $u$. Explain how the tensor Hadamard basis represents its state as a superposition of the uniform vector and one orthogonal Fourier vector.
- **Dependencies and story role:** Uses M01–M04. Introduces the second ensemble and the basis identity needed to compare its one-copy payoff with the unstructured ensemble.
- **Conceptual connection:** A structured classical constraint can be simple in a transformed quantum basis without making its multiple-copy learning problem identical to another ensemble's.
- **Sources:** Watrous [§1.1.1, vectors and tensor products][w-tensor] and [§2.1.2][w-states] for the linear-algebra framework; [payoff identity: BV Fourier decomposition](../science/payoff-identity.md#proof-for-the-bernsteinvazirani-ensemble) for the project-specific derivation.

### M11 — A reflection can turn occupied amplitudes into absent ones

- **Central question:** Why does reflection about the uniform vector complement a balanced subset state?
- **Understanding target:** Interpret the unitary $2\lvert s_D\rangle\langle s_D\rvert-I_D$ as a reflection and relate its action to interference. Distinguish a half-filled domain, which is complemented perfectly, from an arbitrary occupied fiber of unknown size.
- **Dependencies and story role:** Uses M02, M04, and M10. Connects elementary linear algebra to the established global complement-sampling mechanism.
- **Conceptual connection:** A known reflection can exploit a phase promise without learning every occupied label; its success depends on the occupied fraction.
- **Sources:** Watrous [§1.1.2, linear operators][w-operators] and [§2.2, unitary channels within the channel framework][w-channels]; [model: inherited global construction](../science/model.md) and [interpretation: the small diffuser](../science/interpretation.md#why-a-small-diffuser-is-optimal-for-larger-retained-blocks).

### M12 — A feasible dual operator can certify optimality

- **Central question:** How can one prove that no allowed measurement improves on a proposed decoder?
- **Understanding target:** Distinguish a feasible measurement from a feasible dual bound. Explain weak duality through the nonnegative trace of a product of positive-semidefinite operators and why an attaining measurement with the same value closes the converse. Recognize that positive-semidefinite constraints, rather than scalar probabilities alone, govern the optimization.
- **Dependencies and story role:** Uses M06 and M08. Supplies the final proof tool needed before assembling the model and its optimization.
- **Conceptual connection:** Convex optimization turns a universal claim over receivers into a small, checkable operator certificate.
- **Sources:** Watrous [§1.2.3, semidefinite programming, pp. 53–55][w-sdp] and [§3.1.2, measurement primal–dual problems, pp. 134–136][w-measurement-sdp]; [frontier: converse certificate](../science/access-frontier.md#a-certificate-for-the-converse).

### M13 — Input access, source work, and apparatus are different resources

- **Central question:** Which operations and information are included in the receiver's resource count?
- **Understanding target:** Separate retained input qubits from measurement ancillas, classical records, and output length. Account for source sampling and private membership evaluation separately. Explain why a known state-preparation label, a membership oracle, or preprocessing of discarded qubits would change the problem.
- **Dependencies and story role:** Uses M03–M07 and M09. Connects the mathematical input to a complete causal and computational interface.
- **Conceptual connection:** A quantum channel describes what is delivered; it does not make the process that produces the input free or grant its private information to the receiver.
- **Sources:** Watrous [§2.1, registers][w-registers] and [§2.2, channels][w-channels]; [model: resource interpretation](../science/model.md#resource-interpretation) and [source: resource accounting and isolation](../science/source-and-implementation.md#resource-accounting-and-isolation).

### M14 — The complete fixed-access decision problem

- **Central question:** What precise optimization remains after the input promise, causal order, and output rule have all been fixed?
- **Understanding target:** Assemble the hidden ensemble, one-copy input, compulsory computational measurement, classical prefix, fixed retained subsystem, arbitrary subsequent instrument, and mandatory classical output. Identify ordinary samples as the fully dephased interface. Explain why unrestricted streaming access and optimized source encodings are separate models.
- **Dependencies and story role:** Integrates M01–M13. Closes the background phase with the full operational problem whose solution the next phase develops.
- **Conceptual connection:** States, channels, decision payoffs, and resource accounting together specify the feasible receiver class and the meaning of its optimum.
- **Sources:** Watrous [§§2.1–2.3][w-registers] and [§3.1.2][w-ensemble]; [complete model](../science/model.md), [Watrous bridge](WATROUS_BRIDGE.md), and [interpretation: resource scope](../science/interpretation.md#what-is-counted-as-a-quantum-resource).

## Narrative/innovation — M15–M30

### M15 — A random balanced set has a simple payoff operator

- **Central question:** Which information about the exponentially large subset ensemble is relevant to the score of a fixed output?
- **Understanding target:** Derive the structure of $B_y=\mathbb E_S[\sigma(S,y)\lvert S\rangle\langle S\rvert]$ from inclusion probabilities for up to three positions. Explain why the result contains only the uniform vector, the output vector, and the factor $1/(N-1)$, while treating $N=2$ directly.
- **Dependencies and story role:** Uses M08–M09, M12, and M14. Begins the narrative with the operator identity that compresses the ensemble calculation.
- **Conceptual connection:** Exchangeability reduces a large hidden-variable average to a few matrix-entry cases.
- **Sources:** Watrous [§3.1.2, payoff formalism][w-payoff]; [payoff identity, Theorem 1 and balanced-set proof](../science/payoff-identity.md#the-identity).

### M16 — Different ensembles can define the same one-copy game

- **Central question:** Why do random balanced sets and BV parity sets give every one-copy measurement the same average score?
- **Understanding target:** Follow the cancellation under the random parity bit and the Fourier sum over nonzero $u$ to obtain the same $B_y$. Explain why this equality survives an identical input channel or receiver restriction. Keep it separate from equality of hidden ensembles or multiple-copy inference problems.
- **Dependencies and story role:** Uses M05, M08, M10, and M15. Extends the local identity into an exact operational equivalence for the entire one-copy receiver class.
- **Conceptual connection:** Equality of all output payoff operators is sufficient for equality of decision values, even when the underlying ensembles differ.
- **Sources:** Watrous [§2.2][w-channels] and [§3.1.2][w-payoff]; [BV payoff proof and Corollary 1](../science/payoff-identity.md#proof-for-the-bernsteinvazirani-ensemble).

### M17 — Prefix measurement reduces the converse to a local problem

- **Central question:** How does the fixed input interface turn an $N$-dimensional measurement optimization into identical $D=2^m$ dimensional problems?
- **Understanding target:** Identify the same-prefix effects $F_a^{(z)}$, the cost matrices $C_a$, and the subnormalized constraint $\sum_aF_a^{(z)}\preceq I_D$. Explain why the leftover effect can return another prefix when $B=N/D\geq2$, and why $B=1$ instead requires a complete POVM.
- **Dependencies and story role:** Uses M04, M06–M08, M12, and M15. Produces the local optimization on which all frontier cases depend.
- **Conceptual connection:** Classical output freedom becomes a mathematical completeness constraint; an outside-prefix answer is an allowed action, not abstention.
- **Sources:** Watrous [§3.1.2, measurement optimization][w-measurement-sdp]; [frontier: local reduction](../science/access-frontier.md#reduction-to-a-local-measurement-problem).

### M18 — Three outcomes resolve the one-qubit tradeoff

- **Central question:** What must a one-qubit decoder balance when it cannot tell whether its pair is singly or doubly occupied?
- **Understanding target:** Interpret the three effects $F_0,F_1,F_*$ and their actions: propose one member of the observed pair or return a different prefix. Explain why the private preparation label matters and why every outcome contributes to the unconditional score.
- **Dependencies and story role:** Uses M03, M06–M07, and M17. Gives a concrete attainable mechanism before its universal optimality calculation.
- **Conceptual connection:** A generalized measurement trades the chance to exploit a singleton against the need to escape a full pair of occupied outputs.
- **Sources:** Watrous [§2.3][w-measurement] and [§3.1.2][w-payoff]; [frontier: one retained qubit](../science/access-frontier.md#one-retained-qubit) and [interpretation: the small interference problem](../science/interpretation.md#a-small-interference-problem-survives-the-prefix-measurement).

### M19 — A two-dimensional certificate proves the one-qubit optimum

- **Central question:** What excludes every possible improvement on the three-outcome decoder in the fixed hybrid interface?
- **Understanding target:** Check $Y=-\tfrac14\lvert-\rangle\langle-\rvert\preceq0$ and $C_a-Y\succeq0$, and connect their trace bound to the attaining effects. Recover $L_2=-1/4$ and the exact success $p^\star_{n,1}=9N/[16(N-1)]$ for $n\geq2$.
- **Dependencies and story role:** Uses M12 and M17–M18. Converts an explicit strategy into the exact optimum over arbitrary permitted receivers.
- **Conceptual connection:** Matching primal and dual values certify the entire instrument class through its effective POVM representation.
- **Sources:** Watrous [§1.2.3][w-sdp] and [§3.1.2, optimality conditions][w-measurement-sdp]; [frontier: converse and one-qubit certificates](../science/access-frontier.md#one-retained-qubit).

### M20 — A small diffuser is optimal for larger retained blocks

- **Central question:** Why does the familiar reflection become the optimal local decoder once $m\geq2$?
- **Understanding target:** Connect the complete measurement induced by $U_D=2\lvert s_D\rangle\langle s_D\rvert-I_D$ to local cost $2-D$. Understand the matching dual operator and its two-dimensional slack check. Relate fiber occupancy $t$ to conditional success $4t(D-t)/D^2$ without assuming every fiber is balanced.
- **Dependencies and story role:** Uses M11–M12 and M17. Extends the mechanism and converse from one qubit to the entire larger-block regime.
- **Conceptual connection:** An inherited algorithm applied to an unknown fiber becomes an exact resource theorem only after its ensemble optimality is proved.
- **Sources:** Watrous [§1.1.2][w-operators] and [§1.2.3][w-sdp]; [frontier: two or more retained qubits](../science/access-frontier.md#two-or-more-retained-qubits) and [fiber success](../science/interpretation.md#why-a-small-diffuser-is-optimal-for-larger-retained-blocks).

### M21 — Assemble the frontier and its endpoints

- **Central question:** How do the classical, one-qubit, larger-block, and full-access cases fit into one exact result?
- **Understanding target:** Explain the piecewise frontier, the perfect $n=1$ endpoint, and the complete-POVM correction when no changed prefix exists. For $2\leq m\leq n$, interpret failure $(N/2^m-1)/(N-1)$ and the resulting logarithmic retained-input requirement for prescribed average error. Keep the one-qubit limit $9/16$ distinct from a $2/3$ guarantee.
- **Dependencies and story role:** Uses M17–M20. Integrates the local optimizations into the principal theorem before turning to physical and comparative consequences.
- **Conceptual connection:** Boundary conditions determine which local optimization is physically feasible and prevent incorrect extrapolation of a formula.
- **Sources:** Watrous [§3.1.2, complete measurement constraints][w-measurement-sdp]; [frontier, Theorem 2](../science/access-frontier.md#the-frontier) and [complete access and small endpoints](../science/access-frontier.md#complete-access-and-small-endpoints).

### M22 — Prepare the same hybrid input with a classical source and one qubit

- **Central question:** Can the delivered one-qubit interface be realized without preparing an entangled $n$-qubit subset state?
- **Understanding target:** Follow the source that samples $X=Zb\in S$, checks its partner, and privately selects $\lvert b\rangle$ or $\lvert+\rangle$. Prove equality with the partially measured subset state by the fiber weights. Charge the sampler, membership computation, prefix, and qubit while keeping the preparation label unavailable to the receiver.
- **Dependencies and story role:** Uses M03–M04, M13, and M18. Connects the abstract input to a distinct physical source realization.
- **Conceptual connection:** Operationally identical delivered states can have different preparation architectures; their equality does not erase source costs.
- **Sources:** Watrous [§2.1.2][w-states] and [§2.2][w-channels]; [source implementation, Proposition 1](../science/source-and-implementation.md#2-exact-preparation-of-the-hybrid-source).

### M23 — Realize the decoder and count its apparatus

- **Central question:** How does the three-outcome POVM become a complete laboratory operation?
- **Understanding target:** Relate weak detection of $\lvert+\rangle$, its other Kraus operator, and the final computational measurement to the three effects. Interpret the explicit Naimark isometry and ancilla circuit. Account for one initialized measurement ancilla, two CNOTs, four one-qubit rotations, readout, and rotation precision in the stated gate model.
- **Dependencies and story role:** Uses M06–M07, M18, and M22. Completes the implementation route from source through an output on every run.
- **Conceptual connection:** One retained input qubit is a statement about the input interface; a physical generalized measurement has its own hardware and control resources.
- **Sources:** Watrous [§2.3.2][w-measurement-notions] and [Theorem 2.42 and Corollary 2.43][w-naimark]; [decoder realization](../science/source-and-implementation.md#3-the-decoder-and-a-complete-physical-realization).

### M24 — Ordinary classical samples require a macroscopic count

- **Central question:** Why does a constant success bias remain expensive for an ordinary-sample classical receiver?
- **Understanding target:** Derive the unseen-output posterior $N/[2(N-d)]$ after $d$ distinct observations from a uniform balanced set. Use $d\leq q$ to interpret the necessary sample count $q\geq\lceil(N+8)/9\rceil$ for matching the exact one-qubit success. Distinguish a necessary bound from attainment under sampling with replacement.
- **Dependencies and story role:** Uses M01, M09, M14, and M19. Places the quantum interface's constant advantage against a matched, unlimited-computation classical baseline.
- **Conceptual connection:** The classical limitation follows from residual uncertainty in the hidden set, so additional computation cannot replace missing samples.
- **Sources:** Watrous [probability expectations, p. 48][w-probability] and [§3.1.2, ensemble decisions][w-ensemble]; [ordinary classical comparison and its primary attribution](../science/source-and-implementation.md#4-success-probability-and-the-ordinary-classical-comparison).

### M25 — A different classical source message changes the comparison

- **Central question:** Does the one-qubit advantage extend to the best classical encoding of the source's private membership information?
- **Understanding target:** Analyze the source that sends a flag precisely for the singleton pair $\{z1\}$. Explain its allowed receiver actions and success $5N/[8(N-1)]$, which exceeds the fixed quantum-input optimum. Identify why this message carries information absent from the ordinary dephased sample.
- **Dependencies and story role:** Uses M03, M09, M13, M19, and M22–M24. Tests the operational scope at the source boundary before drawing broader resource conclusions.
- **Conceptual connection:** A comparison between fixed input states does not optimize all source encodings of the same dimension or communication length.
- **Sources:** Watrous [§2.1, classical and quantum registers][w-registers] and [§3.1.2][w-ensemble]; [changed-source flag counterexample](../science/interpretation.md#a-changed-classical-source-can-do-better).

### M26 — Residual coherence has an exact finite-size payoff

- **Central question:** Which parts of the one-qubit advantage remain after a specified dephasing channel?
- **Understanding target:** Derive the size-biased singleton and double-occupancy weights after observing a prefix. Interpret the common payoff shift $A_j^{(N,\eta)}=(NB_j^{(\eta)}+\rho_\eta)/(N-1)$, including the nonzero finite-size fallback contribution. Explain why optimizing the shifted score reduces to one qubit optimization independent of $N$.
- **Dependencies and story role:** Uses M05, M08–M09, M18, and M22. Extends the ideal mechanism into a precisely specified noisy-input problem.
- **Conceptual connection:** Conditional probability and linear payoff structure preserve finite-size terms that would be lost by taking an asymptotic limit too early.
- **Sources:** Watrous [§2.2][w-channels] and [§3.1.2][w-payoff]; [robustness: conditional ensemble and payoff operators](../science/robustness.md#2-conditional-ensemble-and-finite-size-payoff-operators).

### M27 — Retuning and leaving the circuit fixed give different answers

- **Central question:** Why can every fixed positive residual coherence help an optimized decoder even when the original circuit has a threshold?
- **Understanding target:** Explain the symmetric POVM optimization yielding $c_\eta=\eta^2/[4(1+\eta)]$ and $V^{\rm opt}_{N,\eta}=(1+Nc_\eta)/(N-1)$. Contrast this with the unchanged decoder's score $(1+N(3\eta-1)/16)/(N-1)$. Track the known-$\eta$ assumption, the classical endpoint, and the distinct limiting biases.
- **Dependencies and story role:** Uses M12, M19, M23, and M26. Turns the dephasing model into a complete optimum and separates robustness of a resource from robustness of a fixed implementation.
- **Conceptual connection:** Knowledge of a noise parameter can change the optimal measurement without changing the supplied input model.
- **Sources:** Watrous [§3.1.2, measurement optimization][w-measurement-sdp]; [optimal dephased POVM](../science/robustness.md#3-optimal-povm-for-the-hybrid-input) and [unchanged ideal measurement](../science/robustness.md#5-leaving-the-ideal-measurement-unchanged).

### M28 — An efficient keyed source gives a conditional computational statement

- **Central question:** How can an efficiently described source preserve this decoder's advantage without claiming efficient preparation of a generic random set?
- **Understanding target:** Interpret $S_k=P_k(\{0\}\times\{0,1\}^{n-1})$ under a classical strong-PRP assumption with forward and inverse access. Follow the classical ordinary-sample hardness reduction and the separate classical simulation of this fixed decoder's success using private source labels. Distinguish these conditional polynomial-time conclusions from the uniform ensemble's information-theoretic bound.
- **Dependencies and story role:** Uses M03, M13, M22–M25. Connects the abstract source to a computational instantiation while retaining both information and security boundaries.
- **Conceptual connection:** A reduction may access private information to simulate an experiment without granting that information to the player whose performance is being compared.
- **Sources:** Watrous [§2.1.2][w-states] and [§3.1.2][w-ensemble] for ensemble probabilities; [source: strong-PRP assumption and Propositions 2–3](../science/source-and-implementation.md#5-an-efficient-source-under-a-classical-strong-prp-assumption) for the additional cryptographic assumption and reductions.

### M29 — Check which conclusions transfer and which do not

- **Central question:** Which changes of ensemble, input access, or performance quantifier preserve the established result?
- **Understanding target:** Reconcile the shared one-copy frontier with ordinary-sample complexities $\Omega(N)$ for random balanced sets and $\Theta(n)$ for BV sets. Use explicit fixed-set failures to separate average from worst-case performance. Explain what finite enumeration and certificate checks corroborate, and why they do not replace the analytical proof or validate a cryptographic assumption.
- **Dependencies and story role:** Uses M09, M14, M16, M21, and M24–M28. Integrates the proof and implementations with their exact transfer limits.
- **Conceptual connection:** Equality of a specified decision functional is narrower than equality of learning problems, source families, or physical access models.
- **Sources:** Watrous [§3.1.2, ensemble objectives][w-ensemble]; [interpretation: average-case failures](../science/interpretation.md#average-case-performance-is-essential), [two ensembles](../science/interpretation.md#two-useful-ensembles-with-different-multi-copy-consequences), and [verification scope](../verification/README.md).

### M30 — The complete scientific meaning of the access frontier

- **Central question:** What is the strongest precise conclusion supported by the model, proofs, source constructions, and comparisons together?
- **Understanding target:** Explain how a small retained subsystem preserves useful interference after compulsory computational measurements, why the frontier is exact over all allowed instruments, and what its constant bias means against ordinary samples. Keep private preparation labels, charged source work, ancilla costs, ensemble averages, conditional PRP hardness, and the classical flag countermodel in the same account.
- **Dependencies and story role:** Integrates M15–M29 with the operational framework of M14. Closes the narrative phase by joining the mechanism, converse, and interpretation into one bounded scientific contribution.
- **Conceptual connection:** A quantum advantage has a precise operational meaning only when input state, source encoding, allowed processing, output task, and comparator are stated together.
- **Sources:** Watrous [§§2.1–2.3][w-registers] and [§3.1.2][w-payoff]; [science overview](../science/README.md), [exact frontier](../science/access-frontier.md), and [physical interpretation and boundaries](../science/interpretation.md).

---

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific account](../science/README.md) · [Repository overview](../README.md)

[watrous]: https://cs.uwaterloo.ca/~watrous/TQI/
[w-tensor]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=6
[w-operators]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=8
[w-positive]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=17
[w-probability]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=48
[w-sdp]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=53
[w-registers]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=1
[w-states]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4
[w-reductions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=10
[w-channels]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=15
[w-measurement]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=43
[w-measurement-notions]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=48
[w-naimark]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=52
[w-ensemble]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=9
[w-payoff]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=10
[w-measurement-sdp]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=11
