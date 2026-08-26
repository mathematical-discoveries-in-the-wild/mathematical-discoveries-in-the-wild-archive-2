# Full solution: the quartic tracial `Y^2=1` atom-size conjecture

status: `full_solution_likely_valid`

source: Abhishek Bhardwaj and Aljaž Zalar, *The tracial moment
problem on quadratic varieties*, arXiv:2001.11614; J. Math. Anal. Appl.
498 (2021), 124936.

target: Conjecture 1 on source PDF page 12 asks whether, for a bivariate
quartic tracial moment matrix satisfying `Y^2=1`, existence of an arbitrary
representing measure is equivalent to existence of a measure using only
scalar and `2x2` atoms, and indeed to one using a single `2x2` atom.

packet: `runs/fa_banach_001/solutions/full/2001.11614_tracial_y2_single_2x2_reduction/`

ledger: `runs/fa_banach_001/ledger/results/2001.11614_tracial_y2_single_2x2_reduction.json`

## Result

Conjecture 1 is true. More precisely, every normalized bivariate quartic
tracial sequence satisfying `Y^2=1` that has any representing measure has a
representing measure of type `(m,1)`. In the noncommutative case one can take
`m <= 4`.

## Main idea

Combine the original finite measure into one finite tracial direct sum and
split it by the spectral projections of the involution `Y`. Write

`X = [[A,B],[B*,C]]`.

A single `2x2` atom is chosen so that its off-diagonal entry absorbs all of
`tau(BB*)`; its two diagonal entries are the `BB*`- and `B*B`-weighted means
of `A` and `C`. After subtraction, the moments through degree three on the
`Y=+1` and `Y=-1` sides become two ordinary univariate moment sequences.

The only issue is their combined fourth-moment budget. Orthogonal projection
of `A^2` and `C^2` onto the affine-linear polynomials gives an exact scalar
Schur-complement formula. A Hilbert-space Cauchy--Schwarz estimate, followed
by

`4(u+v-sqrt(uv)) >= 2*sqrt(2)*sqrt(u^2+v^2)`,

shows that some density leaves a nonnegative fourth-moment surplus. Moving
the density continuously until that surplus is zero makes both scalar Hankel
extensions flat, producing at most two scalar atoms on each sign.

## Verification

- The proof separately checks the commuting case, normalization of the
  `2x2` atom, positivity of both residual order-one Hankel matrices, the
  fourth-order Schur complements, and all degenerate rank-one cases.
- `code/verify_random_reduction.py` tested the exact identities and lower
  bound on 5,000 seeded random finite tracial direct sums; the minimum
  certified margin was nonnegative up to numerical tolerance.
- The source conjecture and preceding size-three theorem were checked on PDF
  page 12. The included crop shows the complete conjecture.
- Exact local-corpus searches and bounded arXiv/web searches through
  2026-08-09 found the source paper and adjacent earlier work, but no later
  paper claiming this reduction or resolving Conjecture 1.

## Human-review focus

Check the quartic identity in Step 4, the Sherman--Morrison formula for the
minimum scalar fourth moments, and the convention at singular endpoints.
These are the only delicate algebraic points; the rest is finite-dimensional
moment theory and Cauchy--Schwarz.

