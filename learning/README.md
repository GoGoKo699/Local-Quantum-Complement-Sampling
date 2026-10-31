# Learning route

The central question is how much of a supplied quantum sample must remain available for processing after the other input qubits have been measured in the computational basis. One retained input qubit already gives a constant advantage for complement sampling; the exact frontier also shows how success changes with the retained dimension.

This route connects that result to states, measurements, and semidefinite optimization. It uses **one educational anchor**: John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), available through the [author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/).

## Reading route

1. **[The project-defined map](MILESTONES.md)** identifies exactly 30 understanding targets. M01–M14 assemble the background and operational model; M15–M30 connect the payoff identity, optimal measurements, implementations, comparisons, and limitations into the complete result.
2. **[The Watrous bridge](WATROUS_BRIDGE.md)** selects short portions of the book, translates its notation, explains what remains to be derived for this project, and gives a complete four-element example. Reading the whole book is unnecessary.
3. **[The scientific account](../science/README.md)** supplies the authoritative definitions, theorems, proofs, and implementation details. Start with the model, then the payoff identity and access frontier.
4. **[Verification](../verification/README.md)** separates analytical proofs from finite numerical checks and provides the reproduction route.

The map is organized around the scientific dependencies, rather than the textbook's chapter order. The bridge and science pages can be read alongside a milestone whenever its concepts become useful.

## Keep the comparison explicit

The input is a positive-amplitude subset sample with a fixed measured-prefix interface. The retained-qubit count is an input-access restriction, not an unrestricted quantum-memory bound. All measurement outcomes return a candidate string. The principal performance guarantee is an ensemble average.

An ordinary classical sample, a private source-membership computation, and an alternative classical message are different resources. The [interpretation page](../science/interpretation.md) explains this distinction, including a classical flag encoding that beats the hybrid source when the source interface is changed. The [source construction](../science/source-and-implementation.md) separately accounts for preparation and gives a conditional efficient implementation.

The textbook is the educational foundation. The [related-work account](../references/related-work.md) retains the primary research attribution and proof dependencies without expanding the educational anchor into a second reading list.

[Repository overview](../README.md) · [Science overview](../science/README.md)
