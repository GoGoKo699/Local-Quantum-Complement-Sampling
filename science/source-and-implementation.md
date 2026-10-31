# Source access and implementation of the local decoder

## 1. Task and access convention

Let $n\geq 2$, $N=2^n$, and $K=N/2$. A hidden set $S\subseteq\{0,1\}^n$ has cardinality $K$. The player must output $y\notin S$. We use the signed score
$$
\sigma_S(y)=1-2\,\mathbf 1_{\{y\in S\}},
\qquad
V=2p_{\rm succ}-1.
$$
Unless a different ensemble is expressly specified, $S$ is uniform among all $K$-element subsets, and performance is averaged over $S$, the source, and the player's outcomes.

An ordinary classical sample is a uniformly random element of $S$. A quantum sample is
$$
|S\rangle=K^{-1/2}\sum_{x\in S}|x\rangle.
$$
The local decoder first measures the first $n-1$ sample qubits in the computational basis. Equivalently, its source supplies a classical prefix $Z$ and one remaining input qubit $Q$. This equivalence concerns a specified source channel; it does not grant the player a description of $S$, a membership oracle, the source's private random choices, or a state-preparation label.

The familiar global quantum decoder and classical sample lower bounds originate in the complement-sampling literature [1]. The claims proved here concern the source and decoder resources for the local strategy.

## 2. Exact preparation of the hybrid source

For $z\in\{0,1\}^{n-1}$, write
$$
B_z=\{z0,z1\},\qquad
s_{z,b}=\mathbf 1_{\{zb\in S\}},\qquad
|v_z\rangle=s_{z,0}|0\rangle+s_{z,1}|1\rangle.
$$
Computational-basis measurement of the prefix of $|S\rangle$ produces the classical–quantum state
$$
\omega_S
=\frac1K\sum_z |z\rangle\!\langle z|_C
  \otimes |v_z\rangle\!\langle v_z|_Q.
\tag{1}
$$
This expression is normalized because $\sum_z\langle v_z|v_z\rangle=K$.

**Proposition 1 — classical preparation of the source label.**
Suppose the source can draw one uniform classical $X\in S$ and evaluate membership in $S$ on one chosen string. It can prepare (1) using only one quantum qubit:

1. Draw $X=ZB$ uniformly from $S$.
2. Form its partner $X'=Z(1-B)$ and evaluate $\mathbf 1_{\{X'\in S\}}$.
3. Send the classical prefix $Z$. If $X'\in S$, prepare and send $|+\rangle$; otherwise prepare and send $|B\rangle$.

**Proof.**
Let $t_z=|S\cap B_z|$. Prefix $z$ is drawn with probability $t_z/K$. If $t_z=1$, the only possible sample identifies the occupied basis state, and the algorithm sends the corresponding $|b\rangle$. If $t_z=2$, either classical sample leads to $|+\rangle$. The resulting contribution is
$$
\frac{t_z}{K}
\frac{|v_z\rangle\!\langle v_z|}{t_z}
=\frac{|v_z\rangle\!\langle v_z|}{K}.
$$
Empty pairs have zero probability. Summing proves (1). $\square$

The proposition holds for any nonempty $S$ with $K$ replaced by $|S|$; balance is needed for the performance formulas below. It requires no coherent membership evaluation and no entangled state preparation. The source prepares one of $|0\rangle,|1\rangle,|+\rangle$, using a classically selected $I$, $X$, or $H$ operation on a fresh $|0\rangle$.

### Resource accounting and isolation

The source uses one classical sample, one classical membership evaluation, storage and transmission of an $n-1$-bit prefix, and one prepared qubit. The costs of the classical sampler, membership implementation, and any database or key are part of source preparation. They are not constant in $n$ by assumption. For a generic uniformly random balanced set, this proposition does not provide a compact classical representation or an efficient source.

The player receives only the prefix and qubit. In particular, the source does **not** send whether it prepared a singleton state or $|+\rangle$. Giving the player membership access or this preparation label changes the problem. Membership queries can find a complement element with constant expected query count for a balanced set.

The comparison also fixes the source encoding. If the source is instead allowed to send a classical flag computed from its private pair-membership information, a one-bit classical encoding can outperform this quantum decoder. The [explicit counterexample](interpretation.md#a-changed-classical-source-can-do-better) shows why the result does not claim an advantage over optimized classical source–receiver schemes.

Fully dephasing the qubit in (1) gives
$$
\frac1K\sum_{x\in S}|x\rangle\!\langle x|.
\tag{2}
$$
Thus the ordinary classical input is exactly the dephased version of the hybrid input. The comparison is between these two source outputs, with the source's private membership access excluded from both players' allowed operations.

## 3. The decoder and a complete physical realization

After receiving prefix $z$, the decoder measures its input qubit with
$$
E_0=\frac1{16}
\begin{pmatrix}1&-3\\-3&9\end{pmatrix},\quad
E_1=\frac1{16}
\begin{pmatrix}9&-3\\-3&1\end{pmatrix},\quad
E_*=\frac34|+\rangle\!\langle+|.
\tag{3}
$$
Each effect is positive and their sum is $I$. Outcomes $0$ and $1$ produce $z0$ and $z1$. Outcome $*$ produces a fixed string $f(z)$ outside $B_z$. For example, flip the first bit of $z$ and append $0$. This is why the construction assumes $n\geq2$.

All outcomes produce a candidate. No trial is discarded and no success flag is used to condition the reported score.

### Sequential realization with one initialized ancilla

First perform a weak detection of $|+\rangle$, with Kraus operators
$$
K_*=\frac{\sqrt3}{2}|+\rangle\!\langle+|,
\qquad
F=\frac12|+\rangle\!\langle+|+|-\rangle\!\langle-|
 =\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix}.
\tag{4}
$$
The detection outcome produces the fallback $f(z)$. On the other outcome, measure $Q$ in the computational basis and output the opposite bit. Its effects are
$$
F|1\rangle\!\langle1|F=E_0,\qquad
F|0\rangle\!\langle0|F=E_1,\qquad
K_*^\dagger K_*=E_*,
$$
so this realizes (3) exactly.

For a unitary-plus-projective implementation, initialize one ancillary qubit $A$ in $|0\rangle$. Apply the following operations in chronological order:

1. $R_y(\pi/2)$ to $Q$, mapping $|+\rangle$ to $|1\rangle$ and $|-\rangle$ to $|0\rangle$.
2. A controlled $R_y(2\pi/3)$ on $A$, controlled by $Q=1$.
3. $R_y(-\pi/2)$ to $Q$.
4. Measure $A$ in the computational basis. Outcome $1$ is $*$; outcome $0$ is followed by the computational-basis measurement of $Q$ described above.

Here $R_y(\theta)=\exp(-i\theta Y/2)$. The ancilla-$1$ Kraus operator is $K_*$, and the ancilla-$0$ Kraus operator is $F$. A controlled $R_y(\theta)$ can be implemented by $R_y(\theta/2)$ on its target, CNOT, $R_y(-\theta/2)$ on its target, CNOT, in that order. Consequently the complete weak detection uses **two CNOTs and four single-qubit rotations**, one initialized ancilla, and at most two binary readouts.

This implementation uses one coherent **input** qubit and one local measurement ancilla. It does not require entangling operations between different qubits of an $n$-qubit sample. It may entangle the input with its measurement ancilla, so it is not a claim that the entire physical implementation uses one hardware qubit or no entangling gates.

These exact gate counts use a continuous-rotation gate model. Compilation into a finite gate alphabet introduces an accuracy-dependent constant overhead. A constant implementation error small enough to preserve a positive success bias suffices for the sample separation; no precision scaling with $N$ is required for that statement.

### Explicit Naimark isometry

An alternative direct specification is
$$
W=\frac14
\begin{pmatrix}
1&-3\\
-3&1\\
\sqrt6&\sqrt6
\end{pmatrix},\qquad W^\dagger W=I.
\tag{5}
$$
Computational-basis measurement of the three-dimensional output realizes (3). Embedding the three output labels into $|00\rangle,|01\rangle,|10\rangle$ uses the same single ancillary qubit. If both qubits are measured in a complete four-outcome implementation, the unused ideal outcome has probability zero and can be assigned the fallback rather than discarded.

## 4. Success probability and the ordinary classical comparison

For uniform balanced $S$, the decoder has
$$
V_1=\frac{1+N/8}{N-1},
\qquad
p_1=\frac{1+V_1}{2}
=\frac{9N}{16(N-1)}.
\tag{6}
$$
The finite-$N$ calculation and optimality within the hybrid input model are proved in [robustness.md](robustness.md), including the noiseless endpoint. As $N\to\infty$, $p_1\to9/16$. This is a constant positive success bias; it is not a claim of $2/3$ success for the one-qubit decoder.

For completeness, the classical comparison can be obtained directly from the posterior distribution. Suppose a classical player has observed a transcript containing $d$ distinct sampled strings, whose set is $D$. Conditional on the transcript, $S$ is uniform over the $K$-element sets containing $D$: every consistent set gives the same likelihood to the sampled sequence. Outputting a seen string loses with certainty. For each unseen $y$,
$$
\Pr(y\notin S\mid D)=\frac{N-K}{N-d}
=\frac{N}{2(N-d)}.
\tag{7}
$$
No computation or output randomization can exceed this conditional probability.

In particular, a player using at most $q<K$ ordinary samples satisfies
$$
p_{\rm cl}\leq\frac{N}{2(N-q)}.
\tag{8}
$$
Repeated samples can only weaken this upper bound. Matching the quantum probability (6) therefore requires
$$
q\geq\left\lceil\frac{N+8}{9}\right\rceil.
\tag{9}
$$
If $q\geq K$, (9) is already automatic for $N\geq4$. A target probability merely $9/16$, without the finite-size improvement in (6), still requires $q\geq\lceil N/9\rceil$. These are necessary ordinary-sample counts, not assertions that sampling with replacement attains equality.

The bound permits unlimited classical computation. It is an average-case input-access theorem for uniform balanced $S$; it is not a worst-case guarantee for the local decoder, a streaming-memory lower bound, or a theorem about a classical player with membership queries.

## 5. An efficient source under a classical strong-PRP assumption

This section gives a separate, conditional computational instantiation. It does not replace the uniform-set ensemble in the information-theoretic theorem.

### Assumption and keyed sets

Assume an efficiently evaluable keyed permutation family
$$
P_k:\{0,1\}^n\longrightarrow\{0,1\}^n
$$
with an efficiently evaluable inverse and a uniformly chosen secret key $k$. Assume **classical strong pseudorandom-permutation security**: every probabilistic polynomial-time classical distinguisher with adaptive oracle access to both $P_k$ and $P_k^{-1}$ has negligible distinguishing advantage over access to a uniform random permutation $\pi$ and $\pi^{-1}$. The security parameter is $n$, with polynomial key length and evaluation time. Both forward and inverse access are part of the assumption.

Define
$$
S_k=P_k(\{0\}\times\{0,1\}^{n-1}).
\tag{10}
$$
These sets are balanced. The trusted source samples $r\in\{0,1\}^{n-1}$, sets $x=P_k(0r)$, and tests the partner $x'$ by evaluating the first bit of $P_k^{-1}(x')$. Proposition 1 then prepares the exact hybrid source for $S_k$.

The source uses one forward permutation evaluation and one inverse evaluation, ordinary polynomial-size classical computation, and one qubit. The referee verifies a candidate $y$ with one inverse evaluation. The player receives neither the key nor permutation-oracle access.

### Classical hardness

**Proposition 2.**
Under the stated strong-PRP assumption, every probabilistic polynomial-time classical player using a polynomial number of ordinary samples from $S_k$ has success probability at most $1/2+\operatorname{negl}(n)$, averaged over the secret key.

**Proof.**
Given forward and inverse permutation oracles $P,P^{-1}$, a distinguisher simulates each requested sample as $P(0r)$ for fresh uniform $r$. It runs the player and accepts exactly when the first bit of $P^{-1}(y)$ is $1$ for the player's output $y$.

For a random key, its acceptance probability is the player's success on $S_k$. For a uniform random permutation, the image of the fixed half-domain is a uniform balanced subset, and the simulated samples are independent uniform samples from that subset. By (8), with polynomial sample cap $q(n)$, acceptance is at most
$$
\frac12+\frac{q(n)}{2(N-q(n))}
=\frac12+\operatorname{negl}(n).
$$
Any nonnegligible excess in the keyed case distinguishes the two oracle distributions, contradicting the assumption. $\square$

### Transfer of this decoder's success

The local decoder's success can also be transferred using only a **classical** distinguisher. For the three possible source states, the probabilities of the outcomes $0,1,*$ in (3) are

| Source state | Outcome $0$ | Outcome $1$ | Outcome $*$ |
|---|---:|---:|---:|
| $\lvert0\rangle$ | $1/16$ | $9/16$ | $3/8$ |
| $\lvert1\rangle$ | $9/16$ | $1/16$ | $3/8$ |
| $\lvert+\rangle$ | $1/8$ | $1/8$ | $3/4$ |

All entries can be sampled exactly with a constant number of fair bits.

**Proposition 3.**
Under the same assumption, the fixed decoder has
$$
\Pr[y\notin S_k]
=\frac{9N}{16(N-1)}+\operatorname{negl}(n),
\tag{11}
$$
where the signed error has negligible absolute value.

**Proof.**
A classical oracle distinguisher draws $x=P(0r)$, uses $P^{-1}(x')$ to determine which of the three source states would be prepared, samples the corresponding row of the table, forms the decoder's output $y$, and accepts exactly when the first bit of $P^{-1}(y)$ is $1$. It uses one forward and at most two inverse oracle queries.

For a uniform random permutation, acceptance is exactly (6), because its half-domain image is uniform among balanced subsets. For $P_k$, it is exactly the physical decoder's average success on the hybrid source for $S_k$. A nonnegligible difference contradicts classical strong-PRP security. $\square$

The reduction exploits the explicit classical simulation of this fixed decoder when the source's private membership information is available to the simulator. It does not grant that information to the player. It also does not establish success or optimality of an arbitrary quantum decoder on a pseudorandom ensemble.

No security against quantum oracle queries is assumed or needed for Propositions 2–3. The computational adversary in Proposition 2 and both reduction algorithms are classical. Classical strong PRPs already appear in the original complement-sampling construction [1]; the additional point here is the exact one-qubit source and the fixed-decoder success transfer.

The information-theoretic $\Omega(N)$ bound must **not** be asserted for the keyed family on the basis of this reduction. Proposition 2 is a conditional statement against polynomial-time players with polynomially many samples. A succinct keyed ensemble is different from the ensemble of all balanced subsets.

## References

1. M. Benedetti, H. Buhrman, and J. Weggemans, “Provable and Verifiable Quantum Advantage in Sample Complexity,” *Physical Review Letters* **136**, 040601 (2026), [doi:10.1103/q55v-wm7y](https://doi.org/10.1103/q55v-wm7y). The full text and supplement are available as [arXiv:2502.08721v3](https://arxiv.org/html/2502.08721v3). In particular, see the classical average-case analysis and the strong-PRP definition and reduction in the supplement.

For the complete reading route, see the [science overview](README.md).
