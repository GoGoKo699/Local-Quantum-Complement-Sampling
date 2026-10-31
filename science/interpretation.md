# Physical interpretation and boundaries

The access frontier shows that a large quantum sample can lose almost all of its coherent input access while preserving a constant advantage for complement sampling. Understanding this statement requires keeping the input interface, source, measurement apparatus, and success criterion distinct.

## A small interference problem survives the prefix measurement

After the computational prefix is measured, the receiver sees a fiber of the hidden subset. With one retained input bit, the nonempty fiber is either a singleton or the whole two-element pair. The corresponding input qubit is a basis state or $`\lvert+\rangle`$; the receiver is not told which case occurred.

For a singleton fiber, the optimal qubit measurement has probability $`9/16`$ of returning the known-to-be-absent partner, probability $`1/16`$ of returning the occupied bit, and probability $`3/8`$ of choosing an outside-prefix fallback. In the uniform balanced ensemble, the fallback succeeds with probability $`1/2`$ conditional on that singleton. The resulting conditional success is $`3/4`$.

For a fully occupied pair, both within-prefix answers are wrong. The same measurement sends probability $`3/4`$ to the fallback. Conditional on this case, an outside-pair string succeeds with probability $`N/[2(N-2)]`$. The measurement therefore balances two incompatible requirements: exploit singleton occupancy while escaping a full pair. The exact occupancy weights give the [one-qubit success formula](source-and-implementation.md#4-success-probability-and-the-ordinary-classical-comparison).

No preparation label is revealed and no measurement outcome is discarded. The three nonorthogonal preparation possibilities explain why the receiver's operation is a quantum decision problem even though only one input qubit remains.

## Why a small diffuser is optimal for larger retained blocks

For retained dimension $`D\geq4`$, the attaining receiver applies the familiar diffuser $`2\lvert s_D\rangle\langle s_D\rvert-I`$ only within the observed fiber and returns the observed prefix. If that fiber contains $`t`$ elements, its normalized input is the equal superposition of those elements. The conditional success is

```math
p(\text{outside }S\mid S_z)
=\frac{4t(D-t)}{D^2}.
```

This follows directly because each of the $`D-t`$ absent labels acquires amplitude $`2\sqrt t/D`$. A half-full fiber is complemented perfectly. A full fiber cannot yield an absent element while its prefix is preserved.

The fiber size is unknown, and need not equal $`D/2`$. Optimality is consequently an ensemble statement: the [matching dual certificate](access-frontier.md#two-or-more-retained-qubits) proves that no allowed measurement can improve the average by adapting within the retained block or by changing the output prefix. The complete frontier is stronger than the observation that the original diffuser can be applied to fewer qubits.

## Average-case performance is essential

Fix the fallback to flip the first observed prefix bit and append zero. For $`n=3`$, the balanced set

```math
S=\{000,001,100,101\}
```

makes the one-qubit protocol fail on every run: each observed pair is full, and its fallback remains in the set. For a two-qubit retained block, the set $`S=\{000,001,010,011\}`$ similarly fills one entire fiber, so the within-fiber diffuser always returns a member.

Both examples are included in the [finite checks](../verification/README.md). They prevent the averaged theorem from being read as a worst-case local sampler. The full $`n`$-qubit diffuser has a different guarantee: it complements every balanced subset exactly, as established in the original [complement-sampling paper](https://arxiv.org/html/2502.08721v3).

## What is counted as a quantum resource?

The theorem counts the fixed input qubits left available after the stipulated computational measurement. The decoder may use a fresh measurement ancilla; the explicit qubit realization uses one. Classical storage, the $`n`$-bit output, source sampling, membership computation, and rotation accuracy are separately charged.

This is not an unrestricted streaming-memory bound. Processing many input qubits sequentially in different bases is outside the specified interface, even if a receiver uses little coherent workspace at any instant. Likewise, the theorem does not optimize arbitrary encodings by the source into classical messages. Its classical comparison is an ordinary uniform sample, obtained by fully dephasing the stated input.

The distinction matters for the efficient source. The referee knows a private membership relation and sends one of three prescribed states. A classical simulator given that preparation label can reproduce the fixed decoder's probabilities. The actual receiver is not given that label. This observation enables the [classical strong-PRP reduction](source-and-implementation.md#5-an-efficient-source-under-a-classical-strong-prp-assumption); it does not simulate the receiver from an ordinary sample alone.

### A changed classical source can do better

The same source-side sample and partner-membership check also permit a different, entirely classical message. Send the observed prefix $`z`$ and one flag bit that is one exactly when the pair is the singleton $`\{z1\}`$. The receiver returns $`z0`$ on flag one and a fixed outside-pair string otherwise.

The first case succeeds certainly. Conditional on a singleton $`\{z0\}`$, the fallback's expected score is zero; conditional on a full pair, it is $`2/(N-2)`$. Using the [conditional occupancy probabilities](robustness.md#2-conditional-ensemble-and-finite-size-payoff-operators) gives

```math
V_{\mathrm{flag}}
=\frac{N}{4(N-1)}+\frac1{N-1},
\qquad
p_{\mathrm{flag}}
=\frac{5N}{8(N-1)}
\longrightarrow\frac58.
```

This exceeds the fixed hybrid-input quantum optimum. The flag reveals source membership information that is absent from an ordinary sample. It is therefore a counterexample to extending the quantum advantage to optimized classical encodings or to the best source–receiver scheme with the same private membership resources. The fixed-source/dephased-source comparison in the theorem remains unchanged. Both the formula and this interface distinction are included in the verification record.

## Two useful ensembles, with different multi-copy consequences

The uniform balanced ensemble and the Bernstein–Vazirani ensemble have the same payoff operator for every possible output. Thus every one-copy measurement has the same averaged score on both. This equality transfers any receiver restriction imposed identically on the ensembles, including the retained-input frontier and dephasing of the remaining qubit.

It does not equate their multiple-copy learning problems. Uniform balanced sets require $`\Omega(N)`$ ordinary samples for constant success bias. The BV parity constraint can be learned with $`\Theta(n)`$ samples, as shown in the [BV benchmark analysis](https://arxiv.org/pdf/2511.11008v2). A one-copy score ratio of order $`N`$ in the BV game therefore has a different operational meaning from the balanced-ensemble sample-complexity separation.

## Coherence, source costs, and certification

For known residual coherence $`\eta>0`$, the optimal measurement can be retuned to preserve a limiting success bias $`\eta^2/[8(1+\eta)]`$. This is an exact statement for the specified dephasing channel. It does not cover arbitrary noise, unmodeled preparation errors, or arbitrary correlations with a receiver's ancillas. The preparation label remains private throughout the protocol. The ideal fixed measurement has its own threshold, derived separately in [the robustness account](robustness.md).

A generic random subset remains expensive to describe and prepare. The direct source construction replaces a large coherent preparation with explicitly charged classical sampling and membership resources. The keyed construction is efficient under a classical strong-PRP assumption, and its lower bound concerns efficient classical players. Neither construction turns an input-access theorem into an unconditional end-to-end runtime advantage for a classically specified task.

The known global benchmark also has a source-fidelity rigidity statement under its own trusted global decoder. The local protocol uses a different measurement, so that certification theorem is not inherited. The claim established here is the exact success frontier for the stated input and task.

[Science reading route](README.md) · [Model](model.md) · [Related work](../references/related-work.md)
