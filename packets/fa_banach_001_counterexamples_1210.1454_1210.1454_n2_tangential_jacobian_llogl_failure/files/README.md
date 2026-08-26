# The printed tangential L-log-L estimate fails at n=2

This packet gives a counterexample to equation (4.1) as stated on page 12 of
arXiv:1210.1454 without excluding n=2.

At n=2, the tangential determinant is the scalar derivative
det-prime grad(u) = partial_1 u. A ramp with slope A_k = exp(k^2) across width
ell_k = 1/(k A_k) tends strongly to zero in W^{1,1}, has nonnegative
tangential determinant, and has exactly k units of s log-plus s mass on a
fixed compact set inside a smooth domain. Thus no uniform estimate depending
continuously on the Sobolev bound can hold.

Status: candidate_counterexample_likely_valid, pending human review. The packet
is explicit that the genuinely compensated n >= 3 case remains open. If the
authors silently intended that range, this is a scope correction rather than a
resolution of the intended higher-dimensional problem.

Files:

- main.tex: exact construction, proof, upgrade attempts, scope, and novelty.
- solution_packet.pdf: compiled review packet.
- source_paper.pdf: official source arXiv PDF.
- figures/open_problem_crop.png: source excerpt containing (4.1).
- code/verify_scaling.py: exact scaling verifier.
- VERIFICATION.md: proof, executable, build, visual-QA, and hash record.
