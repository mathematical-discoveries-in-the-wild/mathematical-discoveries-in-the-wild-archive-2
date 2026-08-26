# Countable mixed dual sums satisfy the desired weak* Sobolev differentiability conclusion

Status: `strong partial result - likely valid; human review recommended`

Source: Paul Creutz and Nikita Evseev, *Weak differentiability of metric space valued Sobolev maps*, arXiv:2303.17303v1, final paragraph of page 12.

Open question: Does the weak* Lebesgue density property of a dual Banach space imply that every higher-dimensional Sobolev map into that dual has a representative which is weak* differentiable almost everywhere?

Result: Let `X_k=V_k^*` be countably many dual Banach spaces. Assume, for each `k`, either that `V_k` is separable or that `X_k` has the Radon-Nikodym property. For every sum exponent `s in [1,infinity]`, the canonical dual sum

`X=(direct sum_k X_k)_{ell^s}`

has the weak* Lebesgue density property and satisfies the desired Sobolev-map conclusion for every bounded Euclidean domain and every finite Sobolev exponent.

This strictly enlarges the two sufficient classes stated in the source. For example, with `Gamma` of cardinality larger than the continuum,

`ell^infinity(N) direct-sum_2 ell^1(Gamma)`

has neither the Radon-Nikodym property nor any separable predual, but it has the weak* density property and every Sobolev map into it has an almost-everywhere weak* differentiable representative.

Proof mechanism: use one common ACL representative. In separable-predual coordinates, a countable dense family of scalar tests makes the good set measurable. In Radon-Nikodym coordinates, norm differentiability gives a measurable good set. A countable intersection gives simultaneous coordinate derivatives. Weak* lower semicontinuity on finite coordinate blocks assembles them into the full direct sum, and finite-support density in the canonical predual handles all three regimes `s=1`, `1<s<infinity`, and `s=infinity`.

Scope: The general implication remains open. The packet does not handle arbitrary weak* Lebesgue-density duals or uncountable direct sums.

Novelty check: Run indexes and bounded web/arXiv searches used the exact open sentence, source title/id, `weak* Lebesgue density property`, `direct sum`, and `Sobolev weak* differentiability`. The 2025 follow-up arXiv:2511.02520 was also inspected. No later resolution or countable mixed-sum theorem was found. This is not exhaustive bibliographic certification.

Human review focus: Check the measurability argument for Radon-Nikodym coordinates of the common ACL representative and the predual tail estimate at the endpoint sums `s=1,infinity`.
