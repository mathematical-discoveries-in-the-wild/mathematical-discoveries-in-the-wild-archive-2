# Verification report

Candidate: arXiv:1909.12587 Hardy-deficit norm subquestion

## Claim checked

For every integer `n >= 3`, the source functional `H` is nonconvex on
`C_c^infinity(B^n)`, so `H^(1/n)` is not a norm.  The analogous sharp
distance-to-boundary Hardy deficit is also nonconvex on every bounded smooth
convex domain.

## Verdict

**Likely valid.**  The ball theorem is a complete analytic counterexample to
the explicit norm subquestion.  The smooth-domain corollary is also complete
subject only to standard Fermi-coordinate identities.  Neither claim settles
the parent extremal-existence problem.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Log-layer lemma | valid | The change `t=log(s/epsilon_L)` gives the displayed quotient exactly; the compact support of `chi` makes every fixed layer smooth away from both endpoints. |
| Threshold | valid | `kappa_n=((n-1)/n)^n` is increasing and `kappa_3=8/27>1/4`. |
| Radial Hessian | valid | Both scalar second derivatives contribute `n(n-1)`; substituting `U=1-r^2` produces the potential `(1-r^2)^(-2)`. |
| Boundary asymptotics | valid | The gradient coefficient tends to `2^(n-2)` and the singular coefficient tends to `c_n/4=2^(n-2)kappa_n`. |
| Compact localization | valid | For each fixed layer its support has positive distance from the boundary, so a smooth compactly supported base can equal `1-r^2` on a neighborhood of that support. |
| Nonconvexity to non-norm | valid | If `N=H^(1/n)` were a norm, convexity of `x -> x^n` would make `H=N^n` convex. |
| Domain extension | likely valid | In Fermi coordinates the normalized gradient Hessian is the normal energy plus `1/(n-1)` times tangential energy.  Jacobian errors are `O(delta)D_L`; tangential energy is `O(delta^2)D_L`. |

## Adversarial checks

- The nonsmooth formal profile `sqrt(s)` is never used directly: it is cut
  off smoothly on a finite logarithmic interval.
- The base `1-r^2` need not itself be compactly supported; only its values on
  the perturbation support enter the Hessian, and a compact localization is
  constructed there.
- Negative Hessian is used only at points where the base and its radial
  derivative are nonzero, avoiding differentiability issues for `|.|^n`.
- The result is not overclaimed as an answer to extremal existence or to the
  convex-domain exponential inequality.

## Literature / novelty check

Bounded exact-title, arXiv-id, quoted-phrase, extremal, norm, and Hardy-deficit
convexity searches on 2026-08-12 found no later paper answering the exact
higher-dimensional norm question.  This supports, but does not certify,
novelty.

## Recommended human review

Check the radial coefficient calculation in equation (4.2) of the packet and
the Fermi-coordinate error estimate in the domain corollary.  These are the
only mathematically substantive pressure points.

