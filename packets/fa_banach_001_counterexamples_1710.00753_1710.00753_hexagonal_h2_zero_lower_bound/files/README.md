# The density-two hexagonal `h_2` system has lower frame bound zero

**Status:** candidate full negative answer, likely valid; human review
requested.

The source asks whether the second Hermite function on the hexagonal lattice
of density `2` has a positive Gabor lower frame bound, and reports a numerical
value near `0.29`. This packet proves that the sharp lower bound is instead
exactly zero.

For a canonical normalized hexagonal lattice, the integer-density Janssen
symbol is evaluated at a 3-torsion point. The resulting sum is

`B(u)+4u B'(u)+2u^2 B''(u)` at `u=2 pi/sqrt(3)`,

where `B` is the Borwein cubic theta function
`eta(tau)^3/eta(3 tau)`. A level-3 modular-form identity forces this
differential expression to vanish exactly at `tau=i/sqrt(3)`.

Files:

- `solution_packet.pdf`: review-ready negative answer and proof.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_borwein_cubic_theta.pdf`: cubic-theta reference.
- `figures/open_problem_crop.png`: source question on PDF page 2.
- `code/crop_source.py`: reproducible source-page crop.
- `code/verify_theta_zero.py`: high-precision and symbolic transcription audit.
- `tmp/`: build and rendered-page QA artifacts.

Bounded exact/current searches found no later explicit answer to this
nonseparable hexagonal question. Novelty confidence is moderate-high, subject
to expert review.
