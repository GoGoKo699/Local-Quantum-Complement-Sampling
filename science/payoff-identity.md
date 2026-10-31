# The common one-copy payoff operator

The exact access frontier follows from a simple operator identity. For each possible output $`y`$, combine the input state and its success score into one matrix. For a uniformly random balanced subset, this matrix depends only on $`y`$ and the uniform state. The same matrix is obtained from the Bernstein–Vazirani ensemble.

The ensembles and access conventions are defined in [the model](model.md). Throughout, $`N=2^n`$, $`K=N/2`$, and

```math
\lvert s_N\rangle
=\frac1{\sqrt N}\sum_{x=0}^{N-1}\lvert x\rangle.
```

## The identity

For a subset ensemble, define the payoff operator for output $`y`$ by

```math
B_y
=\mathbb E_S\left[
\sigma(S,y)\lvert S\rangle\langle S\rvert
\right],
\qquad
\sigma(S,y)=1-2\mathbf{1}_{\{y\in S\}}.
```

**Theorem 1.** For the uniform ensemble of $`N/2`$-element subsets,

```math
B_y
=\frac{
\lvert s_N\rangle\langle s_N\rvert
-\frac{\sqrt N}{2}
\left(
\lvert y\rangle\langle s_N\rvert
+\lvert s_N\rangle\langle y\rvert
\right)
}{N-1}.
```

The same identity holds when $`S=S_{u,b}`$, with $`u\ne0`$ and $`b\in\{0,1\}`$ uniformly distributed as in [the Bernstein–Vazirani complement-sampling game](https://arxiv.org/html/2511.11008v2).

The identity is a statement about this particular input–output score. It is not an assertion that the two ensembles have the same hidden labels, conditional states, or multiple-copy learning problem.

## Proof for uniformly random balanced subsets

Let $`I_x=\mathbf{1}_{\{x\in S\}}`$. In the computational basis,

```math
\langle i\rvert B_y\lvert j\rangle
=\frac1K\mathbb E\left[(1-2I_y)I_iI_j\right].
```

For a uniformly chosen $`K`$-element subset, the inclusion probabilities of one, two, or three distinct elements are

```math
\mathbb E I_i=\frac KN,
\qquad
\mathbb E I_iI_j=\frac{K(K-1)}{N(N-1)},
```

```math
\mathbb E I_iI_jI_y
=\frac{K(K-1)(K-2)}{N(N-1)(N-2)}.
```

For $`N\geq4`$, substitution of $`K=N/2`$ gives four cases:

| Indices | Matrix entry |
|---|---|
| $`i=j=y`$ | $`-1/N`$ |
| $`i=j\ne y`$ | $`1/[N(N-1)]`$ |
| Exactly one of $`i,j`$ equals $`y`$ | $`-(N-2)/[2N(N-1)]`$ |
| $`i,j,y`$ all distinct | $`1/[N(N-1)]`$ |

For example, the last case is

```math
\frac{K-1}{N(N-1)}
\left(1-\frac{2(K-2)}{N-2}\right)
=\frac1{N(N-1)}.
```

The displayed operator in Theorem 1 has exactly these entries: its uniform-state term contributes $`1/[N(N-1)]`$ everywhere, while the two remaining terms modify row $`y`$ and column $`y`$.

For $`N=2`$, the ensemble consists of the two singleton subsets. Directly averaging their two computational-basis states gives $`B_0=\mathrm{diag}(-1/2,1/2)`$ and the analogous reversed expression for $`B_1`$, which also agree with Theorem 1. This treats the endpoint without using a three-element inclusion formula with a vanishing denominator.

## Proof for the Bernstein–Vazirani ensemble

Let $`H`$ be the one-qubit Hadamard gate, and define

```math
\lvert f_u\rangle=H^{\otimes n}\lvert u\rangle.
```

For $`u\ne0`$, the balanced subset state has the decomposition

```math
\lvert S_{u,b}\rangle
=\frac{
\lvert s_N\rangle+(-1)^b\lvert f_u\rangle
}{\sqrt2}.
```

The two states on the right are orthogonal. This is the Fourier representation of the binary parity constraint defining $`S_{u,b}`$.

The score of output $`y`$ is

```math
\sigma(S_{u,b},y)=-(-1)^{b+u\cdot y}.
```

Averaging over $`b`$ cancels the two diagonal terms in the density operator and leaves

```math
\frac12\sum_{b=0}^1
\sigma(S_{u,b},y)
\lvert S_{u,b}\rangle\langle S_{u,b}\rvert
=-\frac{(-1)^{u\cdot y}}2
\left(
\lvert s_N\rangle\langle f_u\rvert
+\lvert f_u\rangle\langle s_N\rvert
\right).
```

Fourier orthogonality gives

```math
\sum_{u\ne0}(-1)^{u\cdot y}\lvert f_u\rangle
=\sqrt N\lvert y\rangle-\lvert s_N\rangle.
```

Averaging the preceding expression over the $`N-1`$ nonzero values of $`u`$ therefore yields exactly the operator in Theorem 1.

## Consequence for every one-copy measurement

Any one-copy receiver with a classical output is described by a POVM $`\{M_y\}_{y\in\Omega}`$ on the original input, with $`M_y\succeq0`$ and $`\sum_yM_y=I_N`$. Its average score is

```math
V=\sum_y\mathrm{Tr}(M_yB_y).
```

Using Theorem 1 and POVM completeness,

```math
V
=\frac{
1-\sqrt N\mathrm{Re}
\sum_y\langle s_N\rvert M_y\lvert y\rangle
}{N-1}.
```

The first term is fixed because

```math
\sum_y\langle s_N\rvert M_y\lvert s_N\rangle=1.
```

All optimization is consequently concentrated in the remaining interference term. This form also holds for restricted receivers: their allowed measurements form a subset of the full POVM class. Preprocessing, ancillary systems, intermediate measurements, and classical outcome maps can be absorbed into the effective $`M_y`$ whenever they obey the input model and have no extra information about $`S`$.

**Corollary 1.** Every allowed one-copy receiver has the same average score under the uniform balanced-subset and Bernstein–Vazirani ensembles. Any receiver restriction that is imposed identically on the two ensembles therefore has the same one-copy optimum.

This transfers the [retained-subsystem frontier](access-frontier.md) between the ensembles. It does not transfer a multi-copy classical lower bound: the first ensemble has the established $`\Omega(N)`$ ordinary-sample requirement for constant advantage, whereas the parity ensemble can be learned from $`O(n)`$ classical samples. Those distinct comparisons are discussed in [the model](model.md#two-ensembles-and-two-different-classical-comparisons).

## Relation to earlier complement sampling

The unrestricted diffuser and the quantum–classical sample separation are established results of [Benedetti, Buhrman, and Weggemans](https://arxiv.org/html/2502.08721v3). The Bernstein–Vazirani benchmark, its one-copy classical score, and its separate multi-copy analysis are established by [Benedetti and collaborators](https://arxiv.org/html/2511.11008v2). The common payoff operator identifies precisely which information about these ensembles is relevant to an arbitrary one-copy decoder and makes the restricted-access optimization explicit.

**Next:** [Exact optimality with a retained input subsystem](access-frontier.md).
