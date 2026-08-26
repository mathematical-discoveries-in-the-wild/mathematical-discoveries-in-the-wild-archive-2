# Greedy classes need not be linear: answered before arXiv:1303.4972

Status: **literature already answered (negative)**. No new theorem is claimed.

Page 5 of Wojtaszczyk's arXiv:1303.4972 asks, in the general setting of a
Banach space with a basis, whether the greedy class
`G_q^alpha` is a linear space. Garrigós--Hernández--de Natividade,
arXiv:0911.4900, Section 7.2, had already given a counterexample. Their
parameters may be chosen as `p=2` and `q=1`, so the example is a Banach
space with a normalized lattice-unconditional canonical basis, exactly
within the assumptions of the later paper.

For every `alpha>0`, the earlier construction gives
`x,y in G_infinity^alpha` but `x+y not in G_infinity^alpha`.
The packet checks the rate computation explicitly.

## Contents

- `main.tex` and `solution_packet.pdf`: source-to-literature crosswalk and
  verification of the counterexample.
- `source_paper.pdf`: arXiv:1303.4972, containing the question on PDF page 5.
- `supporting_paper_0911.4900.pdf`: the earlier counterexample paper.
- `figures/source_question_page_5.png`: the question page.
- `figures/supporting_setup_page_21.png` and
  `figures/supporting_conclusion_page_22.png`: the two-page construction.

Related audit:
`runs/fa_banach_001/attempts/1303.4972_greedy_class_nonlinearity_literature_audit.md`.
