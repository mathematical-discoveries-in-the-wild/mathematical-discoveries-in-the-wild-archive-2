# No overcomplete lattice Gabor frame is a bi-infinite operator orbit

This packet gives a full negative answer to the Gabor part of the open
question in arXiv:1804.03438.  It proves that no overcomplete one-window
lattice Gabor frame in `L^2(R)`, under any ordering by `Z`, can equal
`(T^n f_0)_{n in Z}` for one bounded operator.  The theorem covers all lattice
densities and all nonzero `L^2` windows, including the rational-density cases
explicitly left open by arXiv:2004.02152.

The proof canonically tightens a hypothetical orbit, reducing it to a unitary
orbit.  It then compares threshold-correlation graphs: finite-threshold
Cayley graphs on `Z` have linear growth, while nondegenerate Gabor graphs on
`Z^2` have quadratic growth.  The degenerate rank-zero/rank-one case is ruled
out by the number of connected components.

Files:

- `solution_packet.pdf` — standalone proof note.
- `source_paper.pdf` — locally compiled arXiv:1804.03438.
- `later_partial_result_2004.02152.pdf` — locally compiled later paper that
  records the remaining rational-density case.
- `main.tex` — packet source.
- `verification.md` — mathematical, novelty, build, source-page, and visual
  checks.

The eight-stage attempt record is
`runs/fa_banach_001/attempts/1804.03438_gabor_biinfinite_orbit_growth_attempts.md`.
