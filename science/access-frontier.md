# Exact optimality with a retained input subsystem

The receiver may measure most of its sample classically and still gain a constant advantage from a single retained input qubit. More generally, the exact failure probability decreases with the dimension of the retained subsystem. Both conclusions admit matching upper bounds over arbitrary receivers in the stated access model.

Use the definitions in [the model](model.md): $N=2^n$, a fixed retained subsystem of $m$ qubits, $D=2^m$, and $B=N/D$ possible computational-prefix outcomes. The source is either the uniform balanced-subset ensemble or the Bernstein–Vazirani ensemble. Their [one-copy payoff operators](payoff-identity.md) are identical.

## The frontier

**Theorem 2.** For $n\geq2$, the optimal average score is

$$
V^\star_{n,m}
=
\begin{cases}
\dfrac1{N-1},&m=0,\\[6pt]
\dfrac{1+N/8}{N-1},&m=1,\\[6pt]
\dfrac{N-2N/D+1}{N-1},&2\leq m\leq n.
\end{cases}
$$

Equivalently, the optimal average success probability is

$$
p^\star_{n,m}
=
\begin{cases}
\dfrac{N}{2(N-1)},&m=0,\\[6pt]
\dfrac{9N}{16(N-1)},&m=1,\\[6pt]
\dfrac{N-N/D}{N-1},&2\leq m\leq n.
\end{cases}
$$

For the remaining case $n=1$, both $m=0$ and $m=1$ have success probability one: the subset contains one bit, and returning its complement solves the task.

The optimum includes arbitrary prefix-dependent instruments, fresh ancillary systems, adaptive operations within the retained block, and classical processing of all outcomes. Every run returns an $n$-bit string. The theorem concerns a fixed retained input subsystem; it makes no claim about unrestricted streaming or quantum-memory models.

## Reduction to a local measurement problem

Conditional on observed prefix $z$, write the receiver's POVM on the retained block as $E_{w,a}^{(z)}$, where $(w,a)$ is the string it returns. The effective input POVM is

$$
M_{w,a}
=\sum_{z=0}^{B-1}
\lvert z\rangle\langle z\rvert\otimes E_{w,a}^{(z)}.
$$

Let

$$
F_a^{(z)}=E_{z,a}^{(z)}.
$$

These effects correspond to outputs whose prefix equals the observed prefix. They form a subnormalized POVM:

$$
F_a^{(z)}\succeq0,
\qquad
\sum_{a=0}^{D-1}F_a^{(z)}\preceq I_D.
$$

The leftover effect contains all outputs with a different prefix. Such outputs are allowed; they are essential to the optimal one-qubit construction.

Write $\lvert s_N\rangle=\lvert s_B\rangle\otimes\lvert s_D\rangle$. Only the block with $z=w$ contributes to the interference term in the payoff identity:

$$
\langle s_N\rvert M_{w,a}\lvert w,a\rangle
=\frac1{\sqrt B}
\langle s_D\rvert F_a^{(w)}\lvert a\rangle.
$$

Define the Hermitian cost matrices

$$
C_a
=\frac{\sqrt D}{2}
\left(
\lvert a\rangle\langle s_D\rvert
+\lvert s_D\rangle\langle a\rvert
\right).
$$

The total score becomes

$$
V
=\frac{
1-\sum_{z=0}^{B-1}\sum_{a=0}^{D-1}
\operatorname{Tr}(C_aF_a^{(z)})
}{N-1}.
$$

When $B\geq2$, every subnormalized POVM is physically admissible. Complete it with

$$
F_*=I_D-\sum_aF_a
$$

and, on that outcome, return any fixed string whose prefix differs from the observed one. For example, flip one specified prefix bit and use a fixed suffix. This completion uses no knowledge of $S$ and never discards an outcome.

Thus, for $B\geq2$, each prefix has the same local optimization

$$
L_D=
\min_{F_a\succeq0,\;\sum_aF_a\preceq I_D}
\sum_a\operatorname{Tr}(C_aF_a),
\qquad
V^\star_{n,m}=\frac{1-BL_D}{N-1}.
$$

For $B=1$, no different prefix exists, so the completeness constraint is instead $\sum_aF_a=I_D$. That distinction accounts for the exceptional full-access one-qubit endpoint.

## A certificate for the converse

Suppose a Hermitian operator $Y$ satisfies

$$
Y\preceq0,
\qquad
Y\preceq C_a\quad\text{for every }a.
$$

Then every feasible local subnormalized POVM obeys

$$
\begin{aligned}
\sum_a\operatorname{Tr}(C_aF_a)
&\geq\operatorname{Tr}\left(Y\sum_aF_a\right)\\
&\geq\operatorname{Tr}Y.
\end{aligned}
$$

The second inequality follows because $-Y$ and $I_D-\sum_aF_a$ are positive semidefinite. These inequalities give an explicit lower bound on the local cost and hence an upper bound on achievable score. A measurement attaining the same value proves optimality.

For a complete POVM, the condition $Y\preceq0$ is unnecessary: the last trace equals $\operatorname{Tr}Y$ directly. This is the standard primal–dual method for quantum measurement optimization; related optimality certificates are developed, for example, in [Bandyopadhyay, Jain, Oppenheim, and Perry's work on quantum state exclusion](https://arxiv.org/abs/1306.4683). Here the certificates can be checked as two-dimensional matrices.

## No retained qubit

For $m=0$, $D=1$ and $C_0=1$. The minimum over $0\leq F_0\leq1$ is $L_1=0$. It is attained by always returning a different string from the observed classical sample. Therefore

$$
V^\star_{n,0}=\frac1{N-1},
\qquad
p^\star_{n,0}=\frac{N}{2(N-1)}.
$$

This reproduces the known optimal one-sample classical value in complement sampling. It also gives success one at $N=2$.

## One retained qubit

Assume $m=1$ and $n\geq2$, so that $D=2$ and a changed-prefix output is available. Use the basis $\{\lvert+\rangle,\lvert-\rangle\}$. The cost matrices are

$$
C_0=
\begin{pmatrix}
1&1/2\\
1/2&0
\end{pmatrix},
\qquad
C_1=
\begin{pmatrix}
1&-1/2\\
-1/2&0
\end{pmatrix}.
$$

Choose

$$
Y=-\frac14\lvert-\rangle\langle-\rvert.
$$

It is negative semidefinite. Its two slacks are

$$
C_0-Y=
\begin{pmatrix}
1&1/2\\
1/2&1/4
\end{pmatrix},
\qquad
C_1-Y=
\begin{pmatrix}
1&-1/2\\
-1/2&1/4
\end{pmatrix}.
$$

Each is positive semidefinite with determinant zero. Hence $L_2\geq\operatorname{Tr}Y=-1/4$.

The matching measurement is

$$
F_0=\frac18
\begin{pmatrix}
1&-2\\
-2&4
\end{pmatrix},
\qquad
F_1=\frac18
\begin{pmatrix}
1&2\\
2&4
\end{pmatrix},
\qquad
F_*=\frac34\lvert+\rangle\langle+\rvert.
$$

All three effects are positive and sum to $I_2$. For outcomes $0$ and $1$, return the corresponding bit together with the observed prefix. For outcome $*$, return a string with a different prefix. The label $*$ is an internal measurement outcome, not an abstention.

Direct evaluation gives

$$
\operatorname{Tr}(C_0F_0)
=\operatorname{Tr}(C_1F_1)=-\frac18.
$$

Consequently $L_2=-1/4$. Since $B=N/2$,

$$
V^\star_{n,1}
=\frac{1+N/8}{N-1},
\qquad
p^\star_{n,1}
=\frac{9N}{16(N-1)}.
$$

For implementation in the computational basis, the same effects are

$$
F_0=\frac1{16}
\begin{pmatrix}
1&-3\\
-3&9
\end{pmatrix},
\qquad
F_1=\frac1{16}
\begin{pmatrix}
9&-3\\
-3&1
\end{pmatrix}.
$$

The matrices are independent of $n$ and $S$. The retained input is one qubit; a physical implementation of its generalized measurement can use a fresh ancillary system whose preparation and control costs are counted separately.

## Two or more retained qubits

For $D\geq4$, let $P=\lvert s_D\rangle\langle s_D\rvert$ and choose

$$
Y=\frac{3-D}{2}P-\frac12(I_D-P).
$$

Both eigenvalues are nonpositive. To check the slack for any output $a$, define

$$
\lvert v_a\rangle
=\frac{\sqrt D\lvert a\rangle-\lvert s_D\rangle}
{\sqrt{D-1}}.
$$

The vectors $\lvert s_D\rangle$ and $\lvert v_a\rangle$ are orthonormal. On their span,

$$
C_a-Y
=
\begin{pmatrix}
(D-1)/2&\sqrt{D-1}/2\\
\sqrt{D-1}/2&1/2
\end{pmatrix}.
$$

This matrix is positive semidefinite with determinant zero. On the remaining orthogonal subspace, $C_a-Y=I/2$. Thus the certificate is feasible and

$$
L_D\geq\operatorname{Tr}Y=2-D.
$$

For achievability, use the diffuser only on the retained block:

$$
U_D=2P-I_D,
\qquad
F_a=U_D\lvert a\rangle\langle a\rvert U_D.
$$

These effects form a complete projective measurement, so no changed-prefix outcome is needed. The receiver applies $U_D$, measures the retained qubits computationally, and returns their outcome with the observed prefix.

Since $U_D\lvert s_D\rangle=\lvert s_D\rangle$ and every diagonal entry of $U_D$ is $2/D-1$,

$$
\sum_a\operatorname{Tr}(C_aF_a)
=\sum_a\left(\frac2D-1\right)=2-D.
$$

The lower bound is attained. Substituting $B=N/D$ yields

$$
V^\star_{n,m}
=\frac{N-2N/D+1}{N-1},
\qquad
1-p^\star_{n,m}
=\frac{N/D-1}{N-1}.
$$

The diffuser itself is the established complement-sampling construction of [Benedetti, Buhrman, and Weggemans](https://arxiv.org/html/2502.08721v3). Its use on an unknown conditional fiber does not generally complement that fiber perfectly: its size need not be $D/2$ and is not known to the receiver. The matching certificate proves its optimality for the stated ensemble and retained-subsystem restriction.

## Complete access and small endpoints

If $m=n\geq2$, then $B=1$ and the local measurement must be complete. The preceding lower bound remains valid, and its attaining diffuser measurement is complete. It gives $p^\star_{n,n}=1$, recovering exact complementing of every balanced subset.

If $n=m=1$, a changed-prefix output is impossible, so the incomplete-POVM value $L_2=-1/4$ must not be used. With the complete-POVM constraint, take instead

$$
Y=\frac12\lvert+\rangle\langle+\rvert
-\frac12\lvert-\rangle\langle-\rvert.
$$

Although this $Y$ is not negative semidefinite, completeness permits it. Both $C_a-Y$ are positive semidefinite, and $\operatorname{Tr}Y=0$. The measurement that reads the computational bit and returns its opposite attains local cost zero. The score is therefore one, as required by the singleton-subset problem.

These endpoints also explain the special one-qubit formula: when a measured prefix exists, the receiver can assign a measurement outcome to a different prefix and improve upon the best decoder forced to preserve the prefix. This is ordinary classical output processing within the task, with every outcome included.

## Consequences and scope

One retained qubit improves success over one ordinary classical sample by

$$
p^\star_{n,1}-p^\star_{n,0}
=\frac{N}{16(N-1)}
\longrightarrow\frac1{16}.
$$

For any fixed $m\geq2$, the optimal average failure approaches $2^{-m}$ as $n$ grows. More directly,

$$
\frac{N/2^m-1}{N-1}\leq2^{-m},
$$

so retaining at most $\max\{2,\lceil\log_2(1/\epsilon)\rceil\}$ input qubits suffices for average failure at most $\epsilon$ when that many qubits are available. Retaining the whole input gives zero failure when the requested bound exceeds its size.

For the uniform balanced-subset ensemble, these are constant-advantage one-copy protocols against the established $\Omega(N)$ ordinary-classical-sample lower bound. For the Bernstein–Vazirani ensemble, they retain an exponential one-copy score ratio but do not imply an exponential classical multi-copy requirement. The [model and resource discussion](model.md#resource-interpretation) keeps these comparisons separate and includes source preparation, ancillary implementation, and readout costs.

The theorem fixes both the computational measurement interface and the retained input subsystem. Its accuracy is an ensemble average; source construction and an unrestricted receiver's coherent workspace are separate resource questions.

**Reading route:** [Model](model.md) · [Payoff identity](payoff-identity.md).
