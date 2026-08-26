# Bidirectional separation for well-ordered step mappings

Status: `candidate full solution likely valid`.

This packet answers the first open problem on PDF page 44 of Seppo
Heikkila and Antonin Slavik, *On summability, multipliability, product
integrability, and parallel translation*, arXiv:1410.1845.

The source asks whether a step mapping with well-ordered steps can be
Kurzweil product integrable without being Henstock--Kurzweil integrable, or
vice versa.  The packet gives both separations by explicit real `3 x 3`
matrix-valued step mappings.  Five-factor nilpotent commutator blocks have
identity exponential product but harmonic additive drift; deleting the fifth
factor makes the additive blocks cancel while their exponential products
have harmonic nilpotent drift.  A further principal-log construction gives
the first separation already in `M_2(R)`, the algebra emphasized by the
source.

The proof also records a caveat in the source's asserted sequence-level
equivalence: `exp(x_j) -> I` does not by itself imply `x_j -> 0`.  The examples
in the packet do satisfy `x_j -> 0`, and product integrability is verified
directly through the source's continuous-fundamental-matrix criterion, so the
answer does not rely on that problematic logarithm step.

Files:

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: source question on PDF page 44.
- `code/verify_commutator_blocks.py`: exact symbolic verification.
- `verification.md`: verification and novelty-search record.

