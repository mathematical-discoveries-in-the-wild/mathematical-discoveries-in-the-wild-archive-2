# Full counterexample packet for arXiv:0901.4115

The packet answers negatively the displayed local-translations question on
PDF page 3 of the source paper.

For every ambient dimension `d >= 2`, let `mu` be normalized surface measure
on the unit sphere and take the trivial strongly continuous unitary group
`U(t)=I`.  A sphere and any nontrivial translate intersect in a set of surface
measure zero, so the stated indicator identity is vacuous for `t != 0` and
automatic for `t=0`.  Nevertheless, surface measure on a positive-curvature
convex boundary admits no Fourier frame, by arXiv:1905.07032, Theorem 1.1;
therefore it is not spectral.

Files:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:0901.4115.
- `supporting_paper_1905.07032.pdf`: the primary non-Fourier-frame theorem.
- `figures/local_translation_question_crop.png`: exact source question.
- `code/make_crop.py`: reproducible crop.
- `code/verify_geometry.py`: elementary algebra/dimension checks.
- `verification.md`: audit record.

