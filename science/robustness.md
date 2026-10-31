# Residual coherence of the one-qubit decoder

This section evaluates a specified dephasing perturbation of the hybrid input. It also supplies the exact finite-size success calculation for the noiseless decoder. All results concern uniform random balanced subsets and the source obtained by measuring a fixed $`n-1`$-bit prefix. They do not describe an arbitrary noise channel, arbitrary source error, or optimal decoding of the original unrestricted $`n`$-qubit input.

## 1. Model

Let $`n\geq2`$, $`N=2^n`$, and $`K=N/2`$. Use the hybrid source $`\omega_S`$ and score convention in [source-and-implementation.md](source-and-implementation.md). After preparation, apply the qubit dephasing channel
```math
\mathcal D_\eta
\begin{pmatrix}a&b\\c&d\end{pmatrix}
=
\begin{pmatrix}a&\eta b\\\eta c&d\end{pmatrix},
\qquad 0\leq\eta\leq1.
\tag{1}
```
Thus basis states are unchanged and
```math
\rho_\eta=\mathcal D_\eta(|+\rangle\!\langle+|)
=\frac{I+\eta X}{2}.
\tag{2}
```
The optimization below assumes the parameter $`\eta`$ is known to the decoder. A separate calculation gives the performance when the ideal measurement is left unchanged.

The prefix is classical. Conditional on its value $`z`$, the decoder can use any qubit POVM, ancillary processing and classical postprocessing. Outputs inside $`B_z=\{z0,z1\}`$ are distinguished individually; all outputs outside $`B_z`$ have the same average payoff operator and can be merged into a fallback outcome.

## 2. Conditional ensemble and finite-size payoff operators

Every prefix is observed with probability $`2/N`$. Conditional on observing a particular prefix, its pair is occupied in one of three ways:

| Occupied pair elements | Qubit state | Conditional probability |
|---|---|---:|
| $`z0`$ only | $`\lvert0\rangle\langle0\rvert`$ | $`N/[4(N-1)]`$ |
| $`z1`$ only | $`\lvert1\rangle\langle1\rvert`$ | $`N/[4(N-1)]`$ |
| Both | $`\rho_\eta`$ | $`(N-2)/[2(N-1)]`$ |

For example, the unconditioned probability that a fixed pair has exactly its $`0`$-element occupied is $`K(N-K)/[N(N-1)]`$. Such a pair produces the observed prefix with probability $`1/K`$. Dividing by $`2/N`$ gives the first row. The double-occupancy row follows in the same way, with observation probability $`2/K`$.

For a singleton pair, any fixed output outside that pair has expected score zero: the remaining $`N-2`$ positions contain exactly $`K-1=(N-2)/2`$ members of $`S`$. For a doubly occupied pair, an outside output has expected score
```math
1-\frac{2(K-2)}{N-2}=\frac{2}{N-2}.
\tag{3}
```
The conditional ensemble is exchangeable on those outside positions, so this statement holds for every such output. It remains valid when an output is selected by an outcome of a qubit measurement: conditional on the pair occupancy, the qubit state has no further dependence on the outside membership pattern.

Let $`A_0^{(N,\eta)},A_1^{(N,\eta)},A_*^{(N,\eta)}`$ denote the average payoff operators for outputting $`z0,z1`$, or an outside string. Define
```math
B_0^{(\eta)}
=\begin{pmatrix}-1/2&-\eta/4\\-\eta/4&0\end{pmatrix},
\quad
B_1^{(\eta)}
=\begin{pmatrix}0&-\eta/4\\-\eta/4&-1/2\end{pmatrix},
\quad
B_*^{(\eta)}=0.
\tag{4}
```
The table and (3) give the exact identity
```math
A_j^{(N,\eta)}
=\frac{N B_j^{(\eta)}+\rho_\eta}{N-1},
\qquad j\in\{0,1,*\}.
\tag{5}
```
For instance,
```math
A_0^{(N,\eta)}
=\frac{N}{4(N-1)}
 (|1\rangle\!\langle1|-|0\rangle\!\langle0|)
-\frac{N-2}{2(N-1)}\rho_\eta.
```
The fallback contribution is $`\rho_\eta/(N-1)`$, rather than zero at finite $`N`$.

For any POVM $`E=(E_0,E_1,E_*)`$, write
```math
v_\eta(E)=\sum_j\mathrm{tr}(E_jB_j^{(\eta)}).
```
Because the common term in (5) sums to $`\mathrm{tr}\rho_\eta=1`$,
```math
V_{N,\eta}(E)
=\frac{1+N v_\eta(E)}{N-1}.
\tag{6}
```
This shift is independent of the decoder. Consequently optimizing the finite-$`N`$ score is exactly equivalent to optimizing $`v_\eta`$.

## 3. Optimal POVM for the hybrid input

**Theorem.**
For $`0\leq\eta\leq1`$, the largest average score achievable by a decoder receiving this hybrid source is
```math
V_{N,\eta}^{\rm opt}
=
\frac{1+N c_\eta}{N-1},
\qquad
c_\eta=\frac{\eta^2}{4(1+\eta)}.
\tag{7}
```
An optimal POVM is
```math
\begin{aligned}
E_0^{(\eta)}
&=\begin{pmatrix}
x^2&-x(1-x)\\
-x(1-x)&(1-x)^2
\end{pmatrix},\\
E_1^{(\eta)}
&=\begin{pmatrix}
(1-x)^2&-x(1-x)\\
-x(1-x)&x^2
\end{pmatrix},\\
E_*^{(\eta)}
&=4x(1-x)|+\rangle\!\langle+|,
\qquad
x=\frac{\eta}{2(1+\eta)}.
\end{aligned}
\tag{8}
```

**Proof.**
The payoff matrices are real and are interchanged by conjugation with $`X`$ and exchange of output labels $`0,1`$. Averaging any POVM with its complex conjugate and with this relabeled conjugate preserves the objective and feasibility. It therefore suffices to take
```math
E_0=\begin{pmatrix}a&c\\c&b\end{pmatrix},
\qquad
E_1=\begin{pmatrix}b&c\\c&a\end{pmatrix}.
```
Positivity and completeness are equivalent to
```math
a,b\geq0,\qquad c^2\leq ab,\qquad
a+b+2|c|\leq1.
\tag{9}
```
The objective is
```math
v_\eta=-a-\eta c.
\tag{10}
```
For $`\eta\geq0`$, replacing $`c`$ by $`-|c|`$ cannot reduce it. Put $`t=-c\geq0`$. If $`a=0`$, positivity forces $`t=0`$, giving objective zero. Otherwise $`b\geq t^2/a`$, and (9) implies
```math
a+\frac{t^2}{a}+2t\leq1,
\qquad
t\leq\sqrt a-a.
```
Writing $`u=\sqrt a`$, we obtain
```math
v_\eta\leq \eta u-(1+\eta)u^2
\leq\frac{\eta^2}{4(1+\eta)}.
\tag{11}
```
Equality is attained at $`u=x=\eta/[2(1+\eta)]`$, $`b=(1-x)^2`$, and $`t=x(1-x)`$, yielding (8). Inserting (11) into (6) proves (7).

Any additional outcomes outside the observed pair can be merged because their payoff operators coincide. The argument is conditional on an arbitrary prefix, and every prefix has the same conditional optimization problem. Thus prefix-dependent measurements and arbitrary ancillary implementations do not improve the optimum. $`\square`$

This is an optimum for the specified hybrid input channel. An unrestricted player receiving the original coherent $`n`$-qubit subset state has a different resource and can use the global complement swapper.

## 4. Implementation and endpoints

The POVM (8) has the same sequential implementation as the ideal decoder. Define
```math
\lambda_\eta=4x(1-x)
=1-\frac{1}{(1+\eta)^2}.
```
Weakly detect $`|+\rangle`$ with effect $`\lambda_\eta|+\rangle\langle+|`$. The other Kraus operator is
```math
F_\eta
=\frac{1}{1+\eta}|+\rangle\!\langle+|
 +|-\rangle\!\langle-|
=(1-x)I-xX.
\tag{12}
```
On this outcome, measure in the computational basis and return the opposite bit. The detection outcome produces the fallback. All trials are retained.

The ancilla circuit changes only its controlled rotation angle, from $`2\pi/3`$ to
```math
\theta_\eta=2\arccos\!\left(\frac1{1+\eta}\right).
\tag{13}
```
It still needs one initialized ancilla, two CNOTs, four single-qubit rotations, and at most two binary readouts in the explicit decomposition. Degenerate angles can be simplified.

At $`\eta=1`$, $`x=1/4`$, and (8) is the ideal POVM. Equation (7) gives
```math
V_{N,1}^{\rm opt}=\frac{1+N/8}{N-1},
\qquad
p_{N,1}^{\rm opt}=\frac{9N}{16(N-1)}.
\tag{14}
```

At $`\eta=0`$, $`x=0`$, $`E_0=|1\rangle\langle1|`$, $`E_1=|0\rangle\langle0|`$, and $`E_*=0`$. The decoder simply measures the remaining classical bit and outputs its partner. It achieves
```math
V_{N,0}^{\rm opt}=\frac1{N-1},
\qquad
p_{N,0}^{\rm opt}=\frac{N}{2(N-1)},
\tag{15}
```
exactly the optimal success with one ordinary classical sample. The finite positive score in (15) is the exclusion of the already observed sample, not residual quantum coherence.

For each fixed $`\eta>0`$, the limiting success probability is
```math
\frac12+\frac{\eta^2}{8(1+\eta)}>\frac12.
\tag{16}
```
Thus a fixed positive amount of coherence on the sole retained input qubit preserves a constant success bias. This statement uses the measurement adapted to that $`\eta`$.

## 5. Leaving the ideal measurement unchanged

If the source is dephased but the decoder continues to use the ideal effects (3) of the implementation section, then $`a=1/16`$ and $`c=-3/16`$ in (10). Therefore
```math
V_{N,\eta}^{\rm fixed}
=\frac{1+N(3\eta-1)/16}{N-1},
\qquad
p_{N,\eta}^{\rm fixed}
=\frac{N(15+3\eta)}{32(N-1)}.
\tag{17}
```
The fixed ideal measurement has a positive limiting bias precisely when $`\eta>1/3`$. At $`\eta=1`$, (17) agrees with (14). At $`\eta=0`$, it is inferior to the classical partner rule, as expected for an untuned measurement.

Equations (7) and (17) must not be conflated: (7) allows the controlled rotation to be retuned, whereas (17) describes the original fixed circuit.

## 6. Classical sample consequence

For a fixed $`\eta`$, the optimal success in (7) is
```math
p_{N,\eta}^{\rm opt}
=\frac{N(1+c_\eta)}{2(N-1)}.
\tag{18}
```
Combining (18) with the ordinary-sample upper bound $`N/[2(N-q)]`$ gives the necessary count
```math
q\geq
\left\lceil\frac{Nc_\eta+1}{1+c_\eta}\right\rceil.
\tag{19}
```
For $`\eta=1`$, this is $`\lceil(N+8)/9\rceil`$. For $`\eta=0`$, it is one. Every fixed $`\eta>0`$ yields a linear-in-$`N`$ necessary classical sample count.

The comparison remains an input-access result. Neither the dephasing calculation nor its positive bias certifies fidelity of an arbitrary source, forces extensive quantum memory, or supplies a worst-case guarantee for an arbitrary fixed subset.

For the complete reading route, see the [science overview](README.md).
