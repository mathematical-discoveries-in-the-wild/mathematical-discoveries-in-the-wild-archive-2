# A dimension-order rate for the Orlicz mean radius (arXiv:2011.07523)

**Status:** candidate full affirmative solution, subject to human review.

Alonso-Gutiérrez and Prochno ask whether the limiting Gibbs radius `L_Z`
approximates the root-mean-square radius of a uniform point in an Orlicz ball
fast enough to transfer their complete moderate-deviation thin-shell range.
They obtain such a transfer under the stronger growth assumption
`M(x) = Omega(x^4)`.

The packet proves the stronger general rate

```text
E ||X_n||_2^2 / n = L_Z^2 + O(1/n)
```

for every Orlicz function. Consequently, under the source hypothesis
`M(x) = Omega(x^2)`, the source Theorem B remains valid with `L_Z` replaced
by the exact root-mean-square radius for every
`n^(-1/2) << t_n << 1`, with the same exponent and prefactor.

The proof uses the exact Gibbs tilt of uniform measure on the ball. After
conditioning on the first energy coordinate, a third-order one-dimensional
Edgeworth expansion and a boundary-layer second-difference cancellation make
the centered numerator `O(n^(-3/2))`; the normalizing mass is of order
`n^(-1/2)`. Their ratio is `O(1/n)`.

## Files

- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of source page 13.
- `main.tex`: packet source; build and QA intermediates are in `tmp/`.

## Verification report

The proof was audited around the four sensitive points: the sign in the Gibbs
weight, the integration-by-parts formula for the boundary layer, the extra
factor supplied by the mixed second difference, and the event inclusion that
changes centers. No numerical computation is used.

The principal external dependency is the standard third-order Edgeworth
expansion under Cramér's condition, with a uniform `o(n^(-3/2))` remainder.
The packet verifies that `M(Z)-R` has all moments and an absolutely continuous
law, hence satisfies the required Cramér condition even when the convex
Orlicz function is nonsmooth.

## Novelty and human-review focus

The cheap run indexes and targeted web searches through 2026-08-09 found no
statement of the `O(1/n)` mean-radius rate. The closest later result is
arXiv:2407.15579, which develops a bivariate Edgeworth expansion and a
quantitative CLT under an additional `C^2`-off-a-discrete-set convention. It
does not state this rate or the exact centering transfer and explicitly notes
that its smoothness convention excludes some general convex Orlicz functions.
Novelty remains subject to expert review.

The main review target is the boundary-layer lemma: verify the order-three
Edgeworth remainder and the `O(n^(-3/2))` mixed second-difference estimate.

Ledger:
`runs/fa_banach_001/ledger/results/2011.07523_orlicz_mean_radius_rate.json`.
