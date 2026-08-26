# Attempt Log

Target: arXiv:2505.00155, optimality of the `(log log n)^(alpha/2)` loss.

## Route 1: deterministic full-block lower bound

Idea: force every target-size subset of Fourier frequencies to contain a consecutive block of length comparable to `log n / log log n`.

Result: fails. A deterministic subset can meet every such block sparsely. The source's full-block mechanism is probabilistic and does not directly obstruct the best label-dependent subset.

## Route 2: many reordered Fourier components

Idea: place many frequency orderings on disjoint probability components so every target-size subset contains a full bad block in one ordering.

Result: fails as a full route. The component weight decreases by the number of orderings, and the resulting Luxemburg lower bound loses the factor one is trying to prove. Covering all target-size subsets also requires too many orderings by a direct union bound.

## Route 3: optimize the source endpoint conversion

Idea: vary the auxiliary `L^(p_1)` exponent or the threshold in the source proof to remove `log log n`.

Result: no closure. The endpoint conversion still evaluates `log D` at a polynomial in `log n`, producing `log log n`; allowing exponents to vary introduces uncontrolled convexity constants. This did not yield a proof of a constant upper bound.

## Salvaged theorem: all exchangeable selectors

The source's consecutive-block obstruction extends beyond Bernoulli sampling. Under uniform sampling without replacement, disjoint full-block events are negatively correlated, their expected count tends to infinity on an explicit dimension subsequence, and a second-moment bound gives a full block with probability tending to one. Conditioning on cardinality extends this to every exchangeable selector with the target minimum size.

The unrestricted deterministic optimality question remains open.
