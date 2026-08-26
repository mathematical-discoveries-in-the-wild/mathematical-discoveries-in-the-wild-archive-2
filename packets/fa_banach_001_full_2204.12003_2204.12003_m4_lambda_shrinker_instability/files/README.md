# The fourfold Chang cylinder is unstable

Status: `candidate full solution, likely valid pending expert review`

Source: Steven Heilman, *Convex Cylinders and the Symmetric Gaussian
Isoperimetric Problem*, arXiv:2204.12003.  On PDF page 4, the source says that
the noncircular convex lambda-shrinker curves are known to be unstable for
even `m >= 6`, but that instability is unclear for `m = 2` and `m = 4`.

## Claimed result

The `m = 4` case is unstable.  More generally, every noncircular Chang curve
with even rotational order `m >= 4`, and every Euclidean cylinder over it, is
unstable for symmetric Gaussian perimeter at fixed Gaussian volume.

The missing observation is a nodal count.  If `tau=<x,T>`, then the normal
component of infinitesimal rotation is `+/-tau`.  Chang's phase-plane system
has `k'=k tau`; on each nonconstant curvature period, `tau` has two simple
sign intervals.  The `m`-fold curve consists of `m` such periods, so the
rotation Jacobi field has `2m` nodal domains.  For `m=4` this is eight, which is
strictly more than four.  The nodal-domain instability criterion already
proved in arXiv:1705.06643 therefore applies verbatim.

This resolves the source's `m=4` uncertainty.  It deliberately does not claim
to settle `m=2`, where the same count is exactly four and the cited criterion
is sharp at the level of this argument.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2204.12003.
- `supporting_chang_1410.1782.pdf`: construction and phase-plane equations.
- `supporting_heilman_1705.06643.pdf`: rotation/nodal-domain instability
  criterion.
- `figures/open_problem_crop.png`: source statement from PDF page 4.
- `verification.md`: proof audit and bounded novelty check.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

Bounded searches on 9 August 2026 used the source title and arXiv id together
with `m=4`, `Gamma_4`, `lambda shrinker`, `Gaussian perimeter`, `four nodal
domains`, and `infinitesimal rotation`.  The cheap run indexes and arXiv search
found no later paper recording this correction.  Novelty confidence is
moderate pending specialist review.

## Human review focus

Check that Chang's label `m` counts the number of full nonconstant
phase-plane periods needed to close the embedded curve.  In Chang's
construction this follows from the turning-angle condition
`Delta theta=2 pi/m`; it is the key bookkeeping point behind the count `2m`.

