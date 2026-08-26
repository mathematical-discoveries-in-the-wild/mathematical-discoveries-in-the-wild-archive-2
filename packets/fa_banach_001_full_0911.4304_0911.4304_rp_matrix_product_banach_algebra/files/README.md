# Full solution packet: ordinary multiplication on `R_p^I`

This packet gives a candidate full affirmative answer to Remark 3.8 of
arXiv:0911.4304.  For every set `I` and every `1 <= p < infinity`, the
natural predual `R_p^I` of bounded Schatten `p`-Schur multipliers is a
contractive Banach algebra under ordinary matrix multiplication.

The new ingredient is an elementary rank-one decomposition of
`(A*B)(X*Y)`.  For `p >= 2`, its projective cost is controlled by the
contractive embedding `S_{p'} -> S_2`; the source's duality
`R_p^I = R_{p'}^I` handles `1 < p < 2`, and the known endpoint handles
`p=1`.

Files:

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_question.png`: exact crop of Remark 3.8, PDF page 18.
- `code/verify_factorization.py`: finite-dimensional regression checks.
- `verification_report.md`: verification and novelty notes.
