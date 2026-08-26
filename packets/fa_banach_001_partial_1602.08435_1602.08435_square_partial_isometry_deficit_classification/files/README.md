# 1602.08435 — square partial isometry deficit classifications

Status: `candidate major partial result; likely valid; pending human review`

Source: John Jasper, Jireh Loreaux, and Gary Weiss, *Thompson's theorem for
compact operators and diagonals of unitary operators*, arXiv:1602.08435,
Question 6.2.

For a sequence `d=(d_j)`, define the modulus deficit

`Delta(d) = sum_j (1-|d_j|)`.

The packet proves:

- every square partial-isometry diagonal of defect `r` satisfies
  `|d_j|<=1` and `Delta(d)>=r`;
- the `r=infinity` case is completely characterized by `|d_j|<=1` and
  `Delta(d)=infinity`;
- if the deficit is infinite, the same diagonal can be realized with every
  prescribed square defect `r=0,1,2,...,infinity`;
- for finite `r`, the lower bound is sufficient on the exact boundary
  `Delta(d)=r`; for positive finite `r` it is also sufficient for every
  eventually unimodular sequence.

The proof combines a sharp pointwise inequality for the diagonals of the
kernel and cokernel projections, finite Thompson blocks, the source's unitary
diagonal theorem, and a finite-rank projection-diagonal construction.

The packet does **not** settle the remaining finite-intermediate regime
`r<Delta(d)<infinity` with infinitely many non-unimodular entries.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_question_crop.png`: Question 6.2 on source page 21.
- `code/check_deficit_bounds.py`: finite Thompson and random-matrix checks.
- `verification.md`: proof, build, visual, and novelty audit.
