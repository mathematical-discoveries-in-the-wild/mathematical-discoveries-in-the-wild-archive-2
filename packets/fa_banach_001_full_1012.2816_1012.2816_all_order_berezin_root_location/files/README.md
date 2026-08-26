# All-order zero exclusion for the polyanalytic Berezin multiplier

Status: **candidate full solution, likely valid; human review requested**.

This packet answers Question 1 of Čučković–Le, arXiv:1012.2816. For every polyanalytic order `n >= 2`, all roots of the source polynomial `Q_n` lie outside

`Omega_infinity = {lambda : 4 Re(lambda) + (Im(lambda))^2 <= 0}`.

The proof uses `lambda = 4s(s-1)`, which maps the closed strip `0 <= Re(s) <= 1` onto the parabolic region. An exact Jacobi/continuous-dual-Hahn identity gives

`Re(Q_n(4iy(iy-1))) = 1 + a sum of nonnegative absolute squares`.

Symmetry supplies the other strip boundary, and the harmonic minimum principle yields `Re(Q_n(4s(s-1))) >= 1` on the whole strip.

Files:

- `solution_packet.pdf`: review packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: page-13 question crop.
- `code/verify_identity.py`: exact-rational verification of the decisive polynomial identity for any requested finite range.

Primary review focus: Lemma 1 (the boundary-square identity), including its normalization and recurrence induction. The finite checker is supporting QA, not the proof of the all-order theorem.
