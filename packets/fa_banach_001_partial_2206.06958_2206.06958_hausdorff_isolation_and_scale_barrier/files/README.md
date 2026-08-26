# Hausdorff isolation and the scale-synchronization barrier

**Status:** substantial partial result, likely valid; pending human review.

The cached arXiv v1 asks whether its isolation lemma can use Hausdorff rather
than Minkowski dimension.  The live arXiv v2 (9 August 2026) replaces that by
the stronger question whether the full `H^1 -> L^1` multiplier lower bound can
use Hausdorff dimension.

The packet proves two results:

1. The v1 isolation lemma extends completely to Hausdorff-beta-null carriers,
   with arbitrary fine dyadic content and simultaneous separation from a
   mutually singular remainder.
2. The high-turbulence estimate extends to variable-depth Hausdorff stopping
   covers under the same inequality `alpha*rho+beta<0` as the source.

The current v2 question remains open because good stopping vertices need not
synchronize at a single generation, while the source's convolution argument
uses one common-scale Hardy atom.  Eight focused upgrade attempts and two
counterexample mechanisms are recorded in
`runs/fa_banach_001/attempts/2206.06958_hausdorff_dimension_upgrade_attempts.md`.

Files:

- `main.tex` and `solution_packet.pdf`: partial-result proof packet.
- `source_paper.pdf`: live arXiv v2 source PDF.
- `figures/open_problem_crop.png`: rendered v2 Open Problem 4.
- `tmp/`: compilation and visual-QA intermediates.
