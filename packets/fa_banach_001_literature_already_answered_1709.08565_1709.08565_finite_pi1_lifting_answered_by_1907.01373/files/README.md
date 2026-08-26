# Finite-fundamental-group lifting question answered by arXiv:1907.01373

Status: `literature_already_answered`

## Source question

Antonin Monteil and Jean Van Schaftingen, *Uniform boundedness principles for
Sobolev maps into manifolds*, arXiv:1709.08565; Ann. Inst. H. Poincare C Anal.
Non Lineaire 36 (2019), 417-449.

Section 1.3, arXiv PDF page 4, asks whether the known condition
`sp not in [1,m)` is necessary for the universal-cover lifting property when
`0 < s < 1` and the compact target has a nontrivial finite fundamental group.
The discussion assumes a simply-connected domain manifold.

## Separate later answer

Petru Mironescu and Jean Van Schaftingen, *Lifting in compact covering spaces
for fractional Sobolev mappings*, arXiv:1907.01373; Analysis & PDE 14 (2021),
1851-1871, DOI 10.2140/apde.2021.14.1851.

The abstract and Theorem 1 (arXiv PDF pages 1-2) state that for a nontrivial
Riemannian covering with compact connected covering space, and for an
`m`-dimensional compact simply-connected domain, every `W^{s,p}` map lifts if
and only if `sp` is not in `[1,2)`. In particular every map lifts throughout
`2 <= sp < m`, the range left uncertain by the source question.

For a compact connected target with finite fundamental group, the universal
cover is finite-sheeted and hence compact, so Theorem 1 applies directly. The
answer to the proposed necessity is therefore **no** when `m >= 3`: the correct
exceptional interval is `[1,2)`, not `[1,m)`. For `m = 2` the two intervals
coincide. This is a full characterization in the compact-cover setting, not a
new result of this run.

The later paper explicitly says that its result settles completely the Sobolev
lifting question over covering spaces. It also cites the source paper and has
Jean Van Schaftingen as a common author.

## Evidence and search status

- `source_paper.pdf`: arXiv:1709.08565.
- `supporting_paper_1907.01373.pdf`: the separate answering paper.
- `figures/open_problem_crop.png`: source Section 1.3, PDF page 4.
- `figures/supporting_answer_crop.png`: supporting Theorem 1, PDF page 2.
- `figures/supporting_theorem_crop.png`: tighter readable crop of the theorem and the
  sentence identifying the previously open range.
- `verification.md`: hypothesis matching and visual/source checks.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

A bounded search checked the run indexes, both local TeX sources, exact lifting
terminology, and later compact/noncompact covering-space papers through
2026-08-09. The decisive exact match is arXiv:1907.01373.
