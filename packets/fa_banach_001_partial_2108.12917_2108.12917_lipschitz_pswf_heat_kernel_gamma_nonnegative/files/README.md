# Lipschitz regularity for ball-PSWF heat kernels when gamma is nonnegative

**Status:** substantial partial result, likely valid; pending human review.

**Source:** Aline Bonami, Gérard Kerkyacharian and Pencho Petrushev,
*Gaussian Bounds for the Heat Kernel Associated to Prolate Spheroidal Wave
Functions with Applications*, arXiv:2108.12917, equation (8.23) and the open
question on PDF page 40.

## Result

For every dimension `d>=2`, every `gamma>=0`, and every PSWF parameter
`c>=0`, the exponent in the source's intrinsic heat-kernel Hölder estimate
can be chosen to be

```text
alpha = 1.
```

Thus the dependence is completely determined, at its maximal possible value,
on the full nonnegative half of the source's parameter range.

The proof identifies the weighted ball with the upper hemisphere carrying
density `s^(2 gamma)`.  The unperturbed operator becomes the weighted
spherical Laplacian.  Its Bakry--Émery tensor is

```text
(d-1+2 gamma)g + 2 gamma ds tensor ds/s^2,
```

which is nonnegative for `gamma>=0`.  Reverse Poincaré plus the known Gaussian
bound yields a pointwise intrinsic gradient estimate for the heat kernel.
Integration along a spherical geodesic gives the Lipschitz Gaussian estimate,
and the source's bounded-potential theorem transfers it to the PSWF operator.

## Scope

The interval `-1/2<gamma<0` remains open here.  In precisely that range the
normal component of the Bakry--Émery tensor tends to minus infinity at the
equator, so this argument cannot be continued.  Eight focused upgrade
attempts are recorded in
`runs/fa_banach_001/attempts/2108.12917_holder_exponent_upgrade_attempts.md`.

## Files and verification

- `main.tex` and `solution_packet.pdf`: theorem, geometric identification,
  gradient argument, limitations, and novelty audit.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: actual full-width rendering of equation
  (8.23) and the open question on source PDF page 40.

The proof is analytic and has no computational dependency.  Recommended
review focus: the weighted-Neumann closure at the equator for `0<gamma<1/2`,
the reverse-Poincaré kernel substitution, and the volume-doubling conversion
from the asymmetric to the symmetric Gaussian factor.

## Novelty check

Bounded searches on 17 August 2026 covered the run indexes, exact title/id and
question wording, weighted-ball heat-kernel and gradient phrases, and the
published paper's OpenAlex citation list.  Its sole listed citing work is
unrelated to the exponent question.  No explicit later determination was
found.  Novelty confidence is moderate because the curvature mechanism is
standard once the hemisphere model is written down.
