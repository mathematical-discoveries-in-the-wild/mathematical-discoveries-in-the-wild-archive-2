# Critical-order Schatten counterexamples from sparse phase space

Status: candidate counterexample, likely valid, awaiting specialist review.

This packet disproves Open Problem 1.4 of arXiv:2301.04044. On the torus,
non-elliptic operators can belong to the requested Schatten class at the
critical order `m=-n/r`, rather than only below it.

The construction covers every allowed nonclassical parameter pair:

- if `0<rho<1`, sparse frequency packets give an exact-order multiplier in
  `S_r` for every `r>0` and every `0<=delta<rho`;
- if `rho=1` and `0<delta<1`, additional spatial concentration gives an
  exact-order Hilbert--Schmidt example.

Thus only `(rho,delta)=(1,0)`, the classical endpoint isolated in the source's
Open Problem 1.5, is not covered.

Contents:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: locally compiled source paper.
- `figures/open_problems_crop.png`: source PDF crop showing both open problems.
- `VERIFICATION.md`: line-by-line mathematical and artifact checks.
- `source_tex/`: archived source used to compile the source PDF.
