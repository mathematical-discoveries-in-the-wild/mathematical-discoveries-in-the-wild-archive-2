# Verification notes

## Mathematical core

For an internal metric functional on a sup-norm coordinate space,

`h_w(a e_i) < -epsilon`

forces every coordinate of `w` except possibly `i` below `||w||_infinity - epsilon`. Two such inequalities on distinct coordinates cover every coordinate and contradict the definition of the supremum norm.

If a metric functional is a pointwise limit of a net of internals, convergence is simultaneous on any fixed finite set. Therefore the two-point exclusion passes to the pointwise closure.

For any metric functional `h` and epsilon > 0, at most one term of an arbitrary-amplitude distinct-coordinate spike sequence can satisfy `h(x_n) < -epsilon`. Hence `liminf h(x_n) >= 0 = h(0)`.

## Boundary checks

- No attainment of the supremum norm is assumed.
- The argument works for nets, not merely sequential limits of internals.
- The amplitudes can be positive, negative, zero, bounded, or unbounded.
- The sequence lives in and is tested by all metric functionals of the whole space `c0`, not a proper metric subspace.
- Choosing amplitudes `a_n=n` makes the sequence norm-unbounded.

## Source and novelty checks

- Definition 1.1 and Conjecture 1.5 were checked against the official arXiv PDF and TeX source.
- The source already has an unbounded example on a proper non-linear subset of `l1`; Theorem 1.4 excludes the whole space `l1`. The packet's whole-space `c0` example is therefore not the source's subset example in disguise.
- Run registry, solution index, attempt index, and proof-gap index showed no pre-existing result for arXiv:2506.04154.
- Bounded exact-title, exact-conjecture, `c0`, coordinate-spike, horofunction, and author-name searches found no later primary source resolving the conjecture.

## Visual QA

The packet was compiled with `latexmk`, rendered page by page, and each page inspected for clipping, overflow, missing figures, and illegible text.
