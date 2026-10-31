# Related work and attribution

The scientific claim concerns a receiver that first measures a specified
set of input qubits in the computational basis and retains the measurement
record. The restricted resource is coherent access to the remaining input
qubits.

## The contribution being compared

For a uniform random balanced subset of an $`N=2^n`$-element universe, let

```math
V_m=2\Pr[\text{output outside the subset}]-1
```

be the best one-copy average score after the stipulated measurement leaves
$`m`$ input qubits available for quantum processing. The contribution is the
exact frontier

| Retained input qubits | Optimal score | Optimal success probability |
| --- | --- | --- |
| $`m=0`$ | $`1/(N-1)`$ | $`N/[2(N-1)]`$ |
| $`m=1\lt n`$ | $`(1+N/8)/(N-1)`$ | $`9N/[16(N-1)]`$ |
| $`2\leq m\leq n`$, $`D=2^m`$ | $`(N-2N/D+1)/(N-1)`$ | $`1-(N/D-1)/(N-1)`$ |

The case $`m=n=1`$ has success probability one. A general local instrument,
fresh ancillas, and classical processing are allowed after the prescribed
measurement. The parameter counts retained *input* qubits, not total apparatus
qubits. In particular, the three-outcome qubit POVM has a constant-size physical
implementation, whose additional apparatus must be accounted for.

The unrestricted complement-sampling separation is prior work. Here the
physical conclusion is that one retained input qubit preserves a constant
advantage, and two suffice for success above $`2/3`$. The classical comparison
continues to use ordinary samples from the original subset. This distinction
between acquisition models is essential.

## Closest complement-sampling papers

### Benedetti, Buhrman, and Weggemans (2026)

**Citation key:** `BenedettiBuhrmanWeggemans2026`.
[Published article](https://journals.aps.org/prl/abstract/10.1103/q55v-wm7y);
[full arXiv version 3](https://arxiv.org/html/2502.08721v3), dated 30 January 2026.

The theorem-specific dependencies are:

| Location in the source | Inherited result |
| --- | --- |
| Main Problem 1; Supplement I.2, Theorem 4 | Complement sampling and the global diffuser $`2\lvert+_N\rangle\langle+_N\rvert-I`$, which swaps every balanced subset state with its complement |
| Supplement II.1, Lemma 2 and Theorem 6 | After $`q`$ distinct ordinary samples, the posterior gives success at most $`(N-K)/(N-q)`$ |
| Supplement II.3, Corollary 1 | For uniform balanced subsets, success $`1/2+\delta`$ requires $`q\geq N[1-(1+2\delta)^{-1}]`$ even with index-query access |
| Supplement II.4, Definition 5 and Theorem 7 | Classical strong-PRP security and conditional polynomial-time classical hardness |

The lower-bound proof conditions on the observed elements and counts compatible
complements; the average-case extension uses permutation symmetry. Neither the
global swapper nor that counting argument resolves a partially measured quantum
input. The new work is the restricted quantum optimum and its resource
interpretation. General-cardinality zero-error swapping in Supplement I.4–I.5
is a different optimization problem.

### Benedetti, Marin-Sanchez, Weggemans, Rosenkranz, and Buhrman (2026)

**Citation key:** `BenedettiEtAl2026Classicality`.
[Published article](https://www.nature.com/articles/s41467-026-77413-3);
[arXiv version 2, including all supplementary notes](https://arxiv.org/pdf/2511.11008v2),
dated 8 October 2026.

Supplementary Note 1 defines the signed payoff and proves the BV one-copy
classical value $`1/(N-1)`$, Eq. (12), while the global diffuser gives value one.
Supplementary Note 2, Theorems 1–2, establishes $`\Theta(n)`$ ordinary-sample
complexity for BV subsets. These statements must not be conflated with the
$`\Omega(N)`$ bound for uniformly random balanced subsets.

Supplementary Note 3, Theorem 3, derives source-fidelity rigidity using the
*global* diffuser and an additional reference measurement. Its proof uses
$`\Pi_S-U\Pi_SU^\dagger=|S\rangle\langle S|-|\bar S\rangle\langle\bar S|`$.
That identity does not apply to our local decoder. Note 4 restates strong-PRP
hardness; Note 5 analyzes global-circuit implementation.

The payoff-operator identity proved here equates the uniform balanced and BV ensembles
for **every one-copy POVM**, including the restricted receiver. Their
multi-copy classical learning problems remain different. Its test is designed to detect superposition without certifying
entanglement.

## Decision theory: the optimization method is established

Bandyopadhyay, Jain, Oppenheim, and Perry, *Conclusive exclusion of quantum
states*, gives the state-exclusion primal and dual SDPs in Section II,
Eqs. (3)–(4), and optimality conditions in Theorem 1. These are the relevant
methodological antecedents, including the treatment of a complete measurement
with no discarded outcomes. See `BandyopadhyayEtAl2014`,
[arXiv version 3](https://arxiv.org/html/1306.4683v3) and
[published article](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.89.022336).

For this task, the positive failure operators

```math
A_y=\mathbb E_S[\mathbf1_{y\in S}|S\rangle\langle S|]
```

make average failure $`\sum_y\mathrm{Tr}(A_yM_y)`$, an ordinary
minimum-cost measurement problem. Reducing that problem after the prescribed
dephasing, exploiting permutation symmetry, and exhibiting matching analytic
certificates supplies the task-specific result within this established
SDP framework.

There is an even closer mathematical antecedent for the special qubit case.
Chou, *Minimum-error discrimination among mirror-symmetric mixed quantum
states*, treats three mixed qubit states with two equal priors and reflection
symmetry (`Chou2004`,
[publisher](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.70.062316)).
Our reduced qubit objective lies in that family. In the basis
$`\{|+\rangle,|-\rangle\}`$, write

```math
C_0=\begin{pmatrix}1&1/2\\1/2&0\end{pmatrix},\qquad
C_1=\begin{pmatrix}1&-1/2\\-1/2&0\end{pmatrix},\qquad C_*=0.
```

Add the fallback effect to make a complete three-outcome POVM, and set
$`A_j=2I-C_j`$. All three $`A_j`$ are positive. Their traces are $`3,3,4`$, so
$`A_j/10`$ are prior-weighted states with priors $`3/10,3/10,4/10`$. The first
two are exchanged by the mirror and the third is maximally mixed. For every
complete measurement,

```math
\frac1{10}\sum_j\mathrm{Tr}(A_jF_j)
=\frac{4-\sum_j\mathrm{Tr}(C_jF_j)}{10}.
```

Thus the qubit value $`L_2=-1/4`$ is equivalent to discrimination success
$`17/40`$ for a mirror-symmetric mixed-state ensemble. The task-specific
result is the reduction from complement sampling and its extension to the
complete retained-input frontier. The ternary measurement is consistent with
the established theory of qubit discrimination.

## Nearby quantum-sample and small-quantum-resource advantages

**Quantum coupon collection.** Arunachalam et al., `ArunachalamEtAl2020`,
[TQC 2020 article](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.TQC.2020.10),
studies identifying the *entire* hidden subset from copies of its uniform
superposition. Its Table 1, Theorem 2, and Theorem 6 give tight copy bounds.
At balanced cardinality, full identification needs $`\Theta(N\log N)`$ copies.
Our output is one outside element, and the main resource is retained input
access. Their sample-only bound is therefore compatible with one-copy
complement sampling. Their separate reflection-access results do not give the
receiver a free reflection oracle in the present problem.

**One controllable qubit in sensing.** Kannan et al.,
`KannanEtAl2026SingleQubit`, [arXiv:2608.13521v1](https://arxiv.org/html/2608.13521v1),
Theorem 1, gives an exponential signal-query advantage by coupling a qubit to a
sensor, with specified probe energy and control. It concerns learning Fourier
features from physical signal access, whereas the present theorem
quantifies coherent input access to a supplied complement-sampling specimen.

**One clean qubit.** Knill and Laflamme, `KnillLaflamme1998`,
[published article](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.81.5672),
introduced computation with one polarized qubit and a larger mixed register.
The clean-qubit count there is different from the number of input qubits left
available for coherent processing here. The original paper discusses tasks
without known efficient classical algorithms; the present separation is an
unconditional average-case statement about ordinary sample counts.

## Efficient source and pseudorandom instantiation

The [source and implementation analysis](../science/source-and-implementation.md)
proves that one ordinary subset sample plus one private classical membership
evaluation lets a trusted source prepare exactly the prefix-and-qubit input.
The source prepares only $`|0\rangle`$, $`|1\rangle`$, or $`|+\rangle`$.

The original complement paper's Supplement II.4, Definition 5 and Theorem 7,
already uses classical strong-PRP security to obtain computational hardness
for ordinary-sample players. The additional result here is that the same
assumption suffices for the explicit local decoder's performance: its three
possible input states and fixed POVM have exactly classically simulable
probabilities, so a classical forward-and-inverse oracle distinguisher can
reproduce a scored trial. The keyed family therefore inherits the achieved
success $`9N/[16(N-1)]`$ up to negligible error.

This instantiation gives conditional hardness against polynomial-time
classical players. The information-theoretic $`\Omega(N)`$ bound and the exact
optimum over all local quantum instruments concern the uniform balanced-set
ensemble. The source keeps its membership information private; its sampler,
inverse computation, and verification costs are part of the resource model.

## Scope of the resulting theorem

The uniform balanced and BV ensembles have identical one-copy payoff
operators. The resulting restricted-input optimum holds for both, although
their multi-copy classical sample complexities differ. Applying the known
diffuser on a small retained block attains the $`m\geq2`$ frontier; matching
positive-semidefinite certificates establish optimality over all allowed
local instruments. The one-qubit endpoint requires a complete three-outcome
measurement with a changed-prefix output branch.

The consequence is quantitative: measuring all but one input qubit still
allows constant average success advantage while ordinary samples from a
uniform random balanced set require $`\Omega(N)`$ samples for that advantage.
This is an average-case acquisition result. It does not assert a worst-case
local sampler, a general streaming-memory lower bound, uniform sampling
within the complement, or an end-to-end exponential runtime improvement for
classical input data.
