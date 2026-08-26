# Linear imaginary biharmonic counterexample to upper-curve optimality

This packet gives a candidate full negative answer to the universal/full-line
interpretation of the curve-optimality question following Theorem 2.2 of
arXiv:2201.03305.

For the admissible purely imaginary potential `V(x)=i x`, Fourier transform
turns the full-line biharmonic operator into `-d/dxi + xi^4`.  The imaginary
part `beta` of the spectral parameter is removed exactly by a unit-modulus
Fourier phase.  Cutting off the exact homogeneous solution produces
pseudomodes for every `alpha -> infinity`, uniformly in `beta`, with residual
at most

`C_e alpha^(1/16) exp(-(8/5-e) alpha^(5/4))`.

Taking `alpha=beta^3` lies far beyond the source's proposed upper curve of
order `beta^(8/3-o(1))`, disproving its necessity for the original full-line
pseudospectrum.

Files:

- `main.tex`: complete proof and scope audit.
- `solution_packet.pdf`: rendered candidate counterexample packet.
- `verification.md`: source, proof, novelty, and render checks.
- `source_paper.pdf`: original paper compiled from the archived arXiv source.
- `figures/open_problem_crop.png`: source page 7 with Theorem 2.2 and the open
  optimality statement.

Status: candidate counterexample, likely valid.  A half-line realization or a
restriction to positive-half-line-supported pseudomodes remains open.
