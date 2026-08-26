# Counterexample to the upper-Minkowski Wasserstein conjecture

This packet gives a candidate full negative answer to the strongest conjecture
in the final paragraph of arXiv:1304.5219.  For every finite `D > 0`, it
constructs a compact countable ultrametric space `X_D` with upper Minkowski
dimension `D`, while the power-exponential critical parameter of `W_p(X_D)` is
zero for every `p >= 1`.

The construction consists of huge finite equilateral blocks at radii separated
by super-exponential gaps.  The blocks create the upper-Minkowski limsup.  Deep
inside each gap, all later probability mass can be collapsed to the unique
accumulation point, and the remaining finite probability simplex has a net
whose logarithmic size is negligible compared with every power-exponential
Hausdorff gauge.

Files:

- `main.tex`: complete construction and proof.
- `solution_packet.pdf`: rendered candidate counterexample packet.
- `verification.md`: proof, source, novelty, and render audit.
- `source_paper.pdf`: original paper, compiled from the archived arXiv source.
- `figures/open_problem_crop.png`: source page 21 with the conjecture.

Status: candidate full counterexample, likely valid; independent expert review
is requested.  The example has lower Minkowski dimension zero, so the possible
lower-Minkowski lower bound remains open.
