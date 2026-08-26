# Low-dimensional second-order HyUP conjecture: later literature answer

Remark 2.4 of arXiv:2012.12667 conjectures that the sharp inequality

`Q_N[u] >= (N+1)^2/4`

continues from `N >= 5` to every `2 <= N <= 4`.

Chen--Tang, arXiv:2508.15221, Theorem 1.1, disprove it for `N=2,3` using
the first-spherical-harmonic test `u(x)=x_1 exp(-|x|)`.  The exact quotients
are `3/4` and `84/25`, below `9/4` and `4`.  Huang--Ye,
arXiv:2510.00453, Theorem 1.2, later prove the conjectured inequality in
the remaining dimension `N=4`.

Files:

- `solution_packet.pdf`: reviewed literature-answer packet.
- `source_paper.pdf`: official arXiv:2012.12667 PDF.
- `supporting_paper_2508.15221.pdf`: negative answer for `N=2,3`.
- `supporting_paper_2510.00453.pdf`: positive answer for `N=4`.
- `verify_quotients.py`: exact standard-library arithmetic check.
- `evidence/`: source and later-theorem page renders/crops.
- `VERIFICATION.md`: scope and artifact QA record.

This packet records a later-literature resolution and makes no novelty claim.
