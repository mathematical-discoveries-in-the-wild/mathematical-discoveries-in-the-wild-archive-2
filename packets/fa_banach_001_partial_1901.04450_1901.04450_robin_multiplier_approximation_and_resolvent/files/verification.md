# Verification Report

Candidate: arXiv:1901.04450 Robin boundary-trace approximation and
reciprocal-resolvent questions.

## Verdict

`likely valid substantial partial`

Confidence: 93/100.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Robin multiplier transcription | valid | Substituting `n=k+1` and `r=e^t` in source equation (8) gives exactly `b_n(t)`. |
| Nonresonance range | valid | `alpha-beta*n != 0` is precisely the source's solvability condition; for `beta!=0`, this is `a=alpha/beta` not a positive integer. |
| Scalar error ratio | valid | Direct algebra gives `(1-b_n)/(1-e^-nt)=(n q_n-a)/(n-a)`. |
| Bound on `q_n` | valid | Increasing concave `1-e^-tx`, vanishing at zero, gives `1<q_n<(n+1)/n`. |
| Uniformity in all degrees | valid | Large `n` are bounded uniformly using the preceding interval; finitely many low degrees have nonzero zero-time limits `(n+1-a)/(n-a)`. |
| Orthogonal norm comparison | valid | Spherical harmonic subspaces are mutually orthogonal, so pointwise multiplier comparison squares and sums without cross terms. |
| Quadratic K-functional formula | valid | Coordinatewise minimization gives `t^2 n^2/(1+t^2 n^2)` exactly. |
| Ordinary K-functional equivalence | valid | Euclidean norm and sum norm in two coordinates differ by at most `sqrt(2)`. |
| Poisson/K comparison | valid | `1-e^-x` is uniformly comparable to `x/sqrt(1+x^2)`. |
| `O(t)` converse | valid | Divide the quadratic formula by `t^2` and apply Fatou to recover square summability of `n h_n`. |
| `o(t)` saturation | valid | Each fixed nonzero harmonic component gives a nonzero limiting contribution after division by `t`. |
| Replacement derivative | valid | The derivative multiplier is `-n+beta*n/(alpha-beta*n)`; its bounded correction and graph equivalence follow from nonresonance and convergence of the normalized multiplier to `-1`. |
| Strong derivative domain | valid | The scalar error bound dominates the difference quotient by `constant*n`, allowing dominated convergence for `h in D(N)`. |
| Injective resolvent identity | valid | The factorization `(lambda I-A^-1)A=lambda(A-lambda^-1 I)` handles the domains and gives a bounded inverse formula. |
| Generalized-Drazin formula | valid in stated bounded setting | On the spectral `P` block the Drazin inverse is zero; on the invertible `Q` block the injective formula applies. |

## Adversarial checks

- The proof does not divide by `beta` when `beta=0`; that case is handled
  separately and is exactly the Poisson family.
- `alpha=0` is allowed: then `a=0`, and the ratio is `q_n`, uniformly between
  `1` and `2`.
- A positive noninteger `a` can make one low-degree ratio change sign for
  larger `t`. The theorem only needs approximation as `t downarrow 0`, and
  explicitly chooses a uniform sufficiently small `t0` before any such zero.
- Nonresonance excludes derivative zeros too: a derivative zero at degree
  `n` would require `a=n+1`, which is itself a forbidden resonance at the next
  degree.
- The source calls `S` the unit ball while using spherical harmonics and
  surface variables. The packet writes `S^2`, the mathematical boundary
  space intended by the formulas.
- No use is made of a nonexistent semigroup law for `V_t`.
- The generalized-Drazin statement is deliberately restricted to bounded
  operators; no unproved unbounded block-domain assertion is smuggled in.

## Computation

`code/check_robin_multipliers.py` passed symbolic checks of the factorization,
the zero-time derivative, and the scalar resolvent identity. Finite grids over
six parameter regimes, including opposite-sign, Neumann, and positive
noninteger ratios near resonances, found the predicted nonzero bounds.
These checks are diagnostic only.

## Scope

The direct/inverse approximation component and literal resolvent question are
fully answered. The packet does not construct every inverse-ergodic object in
the source and does not extend its bounded Drazin formula to the authors'
unbounded `a`-Drazin framework. Hence the conservative `partial` classification.

## Human review recommendation

Send to an approximation theorist familiar with spherical harmonics and to an
operator theorist for the closed-operator resolvent-domain statement. Focus
especially on the intended homogeneous/full graph-norm convention for the
source's K-functional.
