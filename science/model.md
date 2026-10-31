# Model and operational task

Complement sampling asks for an element that is absent from an unknown set, using samples drawn from that set. A quantum sample can carry useful information about absence because its amplitudes can interfere. The question here is how much of a supplied sample must remain available for quantum processing.

We study the exact optimum when a fixed subset of the input qubits is retained and every other input qubit is measured in the computational basis. The retained subsystem can undergo arbitrary quantum processing, and all measurement outcomes can be processed classically. The result concerns the receiver's access to the input; source preparation and readout have their own costs.

The complement-sampling task and its unrestricted quantum advantage were introduced by [Benedetti, Buhrman, and Weggemans](https://arxiv.org/html/2502.08721v3). Their global diffusion operator converts a balanced subset state into its complement state. The present [access frontier](access-frontier.md) determines what remains possible after most of the input has already been measured classically.

## Universe, subsets, and positive-amplitude samples

Let $n\geq 1$, $N=2^n$, and

$$
\Omega=\{0,1\}^n,
\qquad K=N/2.
$$

The unknown subset $S\subset\Omega$ has exactly $K$ elements. Its quantum sample is

$$
\lvert S\rangle
=\frac{1}{\sqrt K}\sum_{x\in S}\lvert x\rangle.
$$

The amplitudes in this definition are positive in the specified computational basis. That phase convention is part of the input promise. An arbitrary state with the same computational-basis probabilities need not provide the same resource.

The main ensemble draws $S$ uniformly from all $K$-element subsets. A receiver knows $n$, the ensemble, and its access restriction, but does not know $S$. It receives one sample. It has no membership oracle for $S$, classical description of $S$, preparation circuit, inverse preparation oracle, or additional copy unless an alternative model explicitly supplies one.

The output is one classical string $Y\in\Omega$. Success means $Y\notin S$. Every run produces an output: there is no abstention, postselection, or uncharged restart. The task requires a successful complement element, without additionally requiring the conditional distribution of successful outputs to be uniform over the complement.

## A fixed retained subsystem

Choose $m\in\{0,\ldots,n\}$ input qubits independently of $S$ and retain them for quantum processing. Relabel the fixed positions for notation so that

$$
x=(z,a),
\qquad
z\in\{0,1\}^{n-m},
\qquad
a\in\{0,1\}^{m}.
$$

Write

$$
D=2^m,
\qquad B=2^{n-m}=N/D.
$$

The prefix register $Z$ is measured in the computational basis, and the outcome $z$ is supplied classically. The suffix register $A$ remains quantum. The choice of retained positions is fixed before the input is accessed. In particular, the model does not permit an adaptive choice of the next coherent input qubit after learning previous measurement outcomes.

This measurement is the specified input interface. No quantum preprocessing may first couple $Z$ to $A$ or to a receiver ancilla and transfer information out of the measured qubits. The receiver's subsequent quantum operations act on the delivered $A$ system and fresh ancillary systems, using $z$ as classical control.

For each prefix, define the fiber and its unnormalized state by

$$
S_z=\{a:(z,a)\in S\},
\qquad
\lvert v_z\rangle=\sum_{a\in S_z}\lvert a\rangle.
$$

The receiver's complete input is the classical–quantum state

$$
\rho_{ZA}^{S}
=\frac1K\sum_{z=0}^{B-1}
\lvert z\rangle\langle z\rvert
\otimes
\lvert v_z\rangle\langle v_z\rvert.
$$

Its trace is one because $\sum_z\lvert S_z\rvert=K$. A nonempty fiber occurs with probability $\lvert S_z\rvert/K$ and leaves the normalized quantum state

$$
\lvert S_z\rangle
=\frac{1}{\sqrt{\lvert S_z\rvert}}
\sum_{a\in S_z}\lvert a\rangle.
$$

Empty fibers have zero probability. The fiber size is not supplied to the receiver. For $m=0$, this access reduces exactly to one ordinary uniform sample from $S$. For $m=n$, the whole subset state remains available.

The mathematical input may be produced either by preparing $\lvert S\rangle$ and measuring its prefix, or by a source that directly prepares the same classical–quantum state. An implementation of the latter must account for the classical sampling, membership information, quantum preparation, and communication it uses. Equality of the delivered states does not make either source free.

## General receivers and their measurement description

Conditional on $z$, the receiver may use an arbitrary quantum instrument on $A$, fresh ancillary systems, intermediate measurements, classical control, and randomization. Ancillary states carry no information about $S$ beyond the supplied input and may depend on the observed $z$. The receiver may return any string $(w,a)$; its returned prefix $w$ need not equal the observed prefix $z$.

All such procedures, including any residual quantum systems that are discarded, reduce to a positive-operator-valued measure on $A$:

$$
E_{w,a}^{(z)}\succeq0,
\qquad
\sum_{w=0}^{B-1}\sum_{a=0}^{D-1} E_{w,a}^{(z)}=I_D.
$$

The index $(w,a)$ is the final classical output, after all classical processing. This representation includes generalized measurements with any intermediate number of outcomes: outcomes leading to the same returned string are combined. Public or private randomization is included by averaging its effects. The [converse proof](access-frontier.md#reduction-to-a-local-measurement-problem) therefore covers arbitrary decoders in the stated access model, not only the explicit constructions used to attain the bound.

Fresh ancillary dimension and gate count remain implementation resources. The optimization allows them arbitrarily, making its upper bound independent of a particular measurement implementation. In particular, one retained **input** qubit does not imply an ancillary-free realization of a three-outcome measurement.

## Average success and score

Define

$$
\sigma(S,y)=1-2\mathbf{1}_{\{y\in S\}},
$$

so that success scores $+1$ and failure scores $-1$. For receiver $\mathcal A$,

$$
p(\mathcal A)
=\mathbb E_S\Pr_{\mathcal A}(Y\notin S\mid S),
\qquad
V(\mathcal A)=2p(\mathcal A)-1.
$$

The expectation includes the stated subset ensemble and all randomness in the receiver. Let $p^\star_{n,m}$ and $V^\star_{n,m}$ be the corresponding optimal values for the fixed retained-subsystem model. A completely uneducated uniform output has $p=1/2$ and $V=0$.

The [exact frontier](access-frontier.md) includes

$$
p^\star_{n,1}
=\frac{9N}{16(N-1)}
\longrightarrow\frac9{16},
\qquad n\geq2,
$$

and, for $2\leq m\leq n$,

$$
1-p^\star_{n,m}
=\frac{N/2^m-1}{N-1}.
$$

The one-qubit limit is a constant advantage above $1/2$; it is not a $2/3$-success guarantee. Ordinary repeated trials do not by themselves identify which returned strings are correct, because the receiver has no membership oracle. Any proposed success amplification needs its own protocol and accounting.

These guarantees are averaged over the chosen ensemble. They are not worst-case guarantees for each balanced subset. A fixed local protocol can perform poorly on a particular set even while its ensemble average attains the optimum.

## Two ensembles and two different classical comparisons

An efficiently described comparison ensemble consists of the Bernstein–Vazirani subsets

$$
S_{u,b}
=\{x\in\{0,1\}^n:u\cdot x=b\pmod2\},
$$

where $u$ is uniform over the nonzero bit strings and $b$ is uniform over $\{0,1\}$. This complement-sampling benchmark was developed by [Benedetti and collaborators](https://arxiv.org/html/2511.11008v2).

The [payoff-operator identity](payoff-identity.md) proves that the random-balanced and Bernstein–Vazirani ensembles give the same average score to every one-copy receiver. Thus the access frontier applies to both. Their multi-copy classical problems remain different:

- For uniformly random balanced subsets, matching any fixed success advantage above $1/2$ requires $\Omega(N)$ ordinary classical samples. This is the established average-case complement-sampling lower bound of [Benedetti, Buhrman, and Weggemans](https://arxiv.org/html/2502.08721v3).
- For the Bernstein–Vazirani ensemble, a single classical sample has the same optimal score $1/(N-1)$, but $O(n)$ samples suffice to learn enough of the hidden linear constraint. The [benchmark paper's Supplementary Note 2](https://arxiv.org/pdf/2511.11008v2) gives the matching linear classical sample complexity.

An exponential ratio between quantum and classical **one-copy scores** in the second ensemble is therefore distinct from the exponential **sample-complexity separation** in the first.

## Resource interpretation

The quantity $m$ counts input qubits left available for processing beyond computational-basis measurement. It does not measure an unrestricted receiver's quantum memory. For example, a receiver might process many successive input qubits in different bases while using a small coherent workspace; that is a different access pattern.

The result locates a small quantum interface inside a potentially large data source. It leaves explicit the cost of producing the promised sample, the $n$-bit measurement record and output, classical storage and processing, ancillary implementation, and any source-specific membership or preparation operations. No QRAM or free data loading is assumed. A query or sample separation at this interface is not an end-to-end runtime separation for classically specified inputs.

**Next:** [The common one-copy payoff operator](payoff-identity.md), followed by [the optimal access frontier](access-frontier.md).
