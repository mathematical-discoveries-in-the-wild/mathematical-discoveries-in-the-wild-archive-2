# Verification report

## Claims checked

1. For every `epsilon > 0` and `s` in `{1,2,infinity}`, a polynomial
   nonvanishing on the closed bidisk has a degree-one OPA with a zero of
   `l_s` norm below `epsilon`.
2. Consequently the universal degree-one zero-exclusion radius is exactly
   zero in all three norms, even over zero-free polynomials.
3. The limiting affine OPA has exact zero depths tending to zero at the
   stated rates.

Verdict: candidate full solution; likely valid.

## Normal-equation audit

- After dividing by the nonzero constant coefficient, the degree-one OPA
  coefficients satisfy a two-by-two moment system for the probability
  measure `|f|^2 dm / ||f||_2^2`.
- Positivity of the full Gram matrix and its Schur complement give a
  nonzero constant coefficient and uniqueness.
- Weak convergence of the measures gives coefficient convergence whenever
  the limiting two-by-two moment matrix is invertible.

## Concentration audit

- For `D=m^2`, the exponent matrix of
  `G_m=z_1^m+z_1^(m-1)z_2^m` has determinant `D`, so its maximum set on the
  torus consists of exactly `D` explicitly parametrized points.
- All maxima are nondegenerate with the same Hessian.
- A root-of-unity filter in the second coordinate assigns equal maximal
  weight to exactly two selected points and a factor `exp(-2M)` to every
  other maximum.
- First sending `t` to infinity and then `M` to infinity therefore yields
  equal point masses at `(1,1)` and `(a_m,b_m)`.

## Limiting-depth audit

- The feature rows `(1,1)` and `(a_m,b_m)` are independent because
  `a_m != b_m`, so the limiting normalized OPA vanishes at both points.
- Solving the interpolation equations gives
  `q_1=(b_m-1)/(a_m-b_m)` and `q_2=(1-a_m)/(a_m-b_m)`.
- Duality gives the exact `l_s` distance from the origin to the affine zero
  hyperplane as `1/||(q_1,q_2)||_(s*)`.
- The chord identities give decay asymptotic to `1/m`,
  `1/(sqrt(2)m)`, and `1/(2m)` for `s=1,2,infinity`, respectively.

## Polynomial-upgrade audit

- The exponential construction is entire and zero-free.
- Its Taylor polynomials converge uniformly on the closed bidisk. Since the
  entire function has positive minimum modulus there, sufficiently high
  truncations remain zero-free.
- Uniform convergence implies Hardy-norm convergence and hence convergence
  of the finite Gram matrices and degree-one OPA coefficients, preserving
  each strict zero-depth inequality.

## Upgrade-attempt log

- Attempt 1 reduced the source's symmetric two-parameter family to stable
  one-dimensional positive sums and reproduced its reported benchmark.
- Attempt 2 searched broader zero-free exponential families and found
  explicit finite examples with depth below `0.15`.
- Attempt 3 replaced numerical search with the two-point concentration
  codebook and proved that all three depth infima are zero.
- Attempt 4 upgraded the zero-free entire functions to zero-free
  polynomials by uniform Taylor approximation.

## Exact finite check

`code/verify_two_point_construction.py` checks the group relations, solves
the two-point interpolation equations, verifies the chord formulas, and
prints decreasing depths through `m=100`. It finishes with
`all_group_relations_and_depth_formulas_verified=true`.

## Novelty audit

Bounded primary-source searches through 2026-08-11 covered the exact
question, degree-one OPAs, zero-free polynomials on the bidisk, and zeros
arbitrarily close to the origin. They recovered the two source papers and
one-variable zero-exclusion results, but no primary source stating this
theorem. Novelty confidence is moderate because the search was bounded.

## Source and render audit

- `source_paper.pdf` is the official 9-page arXiv:2508.15938 PDF.
- `question_source_2405.16943.pdf` is the official 16-page arXiv:2405.16943
  PDF.
- Source pages 13, 14, and 8 were visually inspected and fully reproduced
  where relevant.
- The packet compiled without warnings, overfull boxes, undefined
  references, or multiply defined labels.
- The final packet has 8 pages; every page was visually inspected after the
  last edit.
- Final packet SHA-256:
  `fcc0b688400cdd03f0907af5afac9269b3ea95e8f85bc5945d689969913e002b`.
- arXiv:2508.15938 source SHA-256:
  `8eb51f3facbfa23f130a9aa64251ed482f213f2d13dbf629079b9e2817afbafa`.
- arXiv:2405.16943 source SHA-256:
  `2f3a3a619bc4ec7103a24fc76bef1b4f1b2f654ad65d096322b7e302e713c06a`.
- Source images `question-13.png`, `question-14.png`, and `target-8.png`
  have SHA-256 values
  `20ec6bf048d92ea898e46000b8fdc5300875a0732bdc88d91c0d6dce62bfe34f`,
  `6fe227c5305760aac87953322e9f88d7be8cf9a1c3b984255c92484ed7002692`,
  and `cdbb36c116002cfde0068f293ca503da2c4941781d89e0bbea13e721e88d096f`.
- Checker SHA-256:
  `28e3b16a28d6cc365935d110be276427eea80500d4e040822443f64dcdf98998`.

## Human verifier focus

Audit the two-stage Laplace limit, the moment-to-interpolation passage, and
the preservation of zero-freeness and OPA coefficients under Taylor
approximation.

