# Verification report

Candidate: arXiv:2502.01336, Open Problem 5 (PDF page 6)

## Claim checked

Exact incompressible strong Sobolev smoothing holds for continuous
unitriangular deformations on rectangles and for finite-energy radial twists
of the ball. The radial approximants map the ball onto itself and preserve the
boundary trace.

## Verdict

**Likely valid; candidate partial result; send to human review.**

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Rectangle density in `W^{1,p}` and uniformly | valid | Reflection gives a continuous Sobolev extension; mollification gives both convergences. Translation continuity also holds for `p=1`. |
| Unitriangular determinant | valid | The weak derivative is upper triangular with every diagonal entry equal to one. |
| Unitriangular global injectivity | valid | Back-substitution recovers `x_n,x_{n-1},...,x_1` exactly; no smallness assumption is used. |
| Unitriangular strong convergence | valid | Fubini lifts each tail-space `W^{1,p}` norm to the full rectangle by a fixed product-of-lengths factor. |
| Laminate reduction | valid | The determinant in the final column is a nonzero linear functional `Delta`; `ker Delta = ran B`, so the non-affine curve component lies in `ran B`. |
| Radial weak derivative | valid | The formula holds away from zero. The inner boundary term in integration by parts is `O(epsilon^n)` because the map has norm `epsilon` on the inner sphere. |
| Radial determinant | valid | The matrix determinant lemma leaves `theta'(r) x^T(R^T dot R)x/r`, which vanishes because `R^T dot R` is skew-symmetric. |
| Radial homeomorphism and fixed image | valid | Radius is preserved and the inverse is the twist with angle `-theta(r)`. Continuity at zero follows from `|T(x)|=|x|`, even if the angle has no limit. |
| Freezing near zero | valid | Its cost is bounded by `C(delta^n + integral_0^delta r^(n-1+p)|theta'|^p)`, and uniform error is at most `2 delta`. |
| Smooth diagonal approximation | valid | After freezing, the angle is ordinary `W^{1,p}(0,1)` and constant near zero. Mollification plus a vanishing endpoint correction preserves both properties. |
| Boundary trace | valid | `theta_k(1)=theta(1)` makes the rotations agree pointwise on the unit sphere. |

## Symbolic sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2502.01336_incompressible_triangular_and_radial_twist_approximation/code/check_jacobians.py
```

The script checks representative unitriangular maps in dimensions three and
four, and radial twists with polynomial angle in dimensions two and three. It
returns determinant `1` in every case and checks the radial inverse on symbolic
coordinates. This is only a sanity check; the general proof is analytic and
does not depend on the computation.

## Edge cases and limitations

- The proof explicitly includes `p=1`.
- The radial angle need not converge at zero; `theta(r)=log r` is allowed.
- The triangular theorem gives diffeomorphisms onto their own images, not in
  general onto the unchanged original image.
- The radial theorem does keep both domain and target equal to the unit ball.
- No argument is given for general incompressible Sobolev homeomorphisms.

## Literature and novelty check

The run's cheap indexes and bounded arXiv/web searches were checked on
2026-08-09 using the source id and combinations of `incompressible`, `volume
preserving`, `Sobolev approximation`, `determinant one`, `triangular`,
`laminate`, `shear`, and `radial twist`. No exact match was found.

arXiv:0901.1002 gives a nearby uniform volume-preserving approximation result,
not the strong Sobolev statement here. arXiv:2507.02854 gives general
piecewise-affine Sobolev approximation in dimensions 3 and 4, but its stated
theorem does not preserve determinant one. The novelty check is bounded, and
the structured mechanisms may be folklore.

## Human reviewer focus

1. Check the removal of the puncture in the radial weak-derivative formula.
2. Check the two-stage freeze-and-smooth diagonal argument for `p=1`.
3. Confirm the precise convention on whether an Open Problem 5 approximant
   must have the same image; only the radial theorem supplies that stronger
   property.
4. Search specialist nonlinear-elasticity literature for prior explicit
   determinant-preserving smoothing of triangular maps and radial twists.
