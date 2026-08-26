# Counterexamples to three extended convergence questions

Classification: candidate new full counterexample, likely valid, needs human
review.

For the one-dimensional Hilbert space, the identity maximally monotone operator,
and explicit admissible inexact solutions, this packet shows:

- Solodov--Svaiter Algorithm 9.1 need not converge when `sigma=1`, and can
  diverge for every `sigma>1`.
- Iusem--Pennanen--Svaiter Algorithm 10.1 need not converge when `nu=1`, even
  for parameters in formula (10.1) with `sigma>=1`, and can diverge for
  `nu>1`.
- Parente--Lotito--Solodov Algorithm 11.1 need not converge in the extended
  regime even when every local `sigma_n<1` but `sup sigma_n=1`; it can diverge
  for any global `sigma>1`.

At the boundary, all three constructions use
`a_n=1-1/(n+2)^2` and produce
`x_n=(n+2)/(2(n+1)) -> 1/2`, while the unique zero is 0.

Files:

- `main.tex` -- full proof and parameter audit.
- `solution_packet.pdf` -- compiled review packet.
- `source_paper.pdf` -- source paper.
- `figures/` -- exact source-question crops.
- `verify_counterexamples.py` -- exact rational-arithmetic verification.

Review should focus on matching the source's update conventions and on
literature novelty; the scalar algebra itself is exact.

