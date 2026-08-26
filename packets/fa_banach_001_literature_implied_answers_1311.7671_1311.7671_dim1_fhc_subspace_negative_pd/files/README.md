# One-dimensional frequently hypercyclic-subspace extension is false

Status: `literature_implied_answer (full negative answer)`

Source question:

- Santiago Muro, Damián Pinasco, and Martín Savransky, *Strongly mixing
  convolution operators on Fréchet spaces of holomorphic functions*,
  arXiv:1311.7671, Integral Equations and Operator Theory 80 (2014), 453–468.
- In Section 4.1, arXiv PDF page 13, after proving the result for
  `dim(E)>1`, the authors say that the corresponding problem for `dim(E)=1`
  is open.

Supporting theorem:

- Frédéric Bayart, Romuald Ernst, and Quentin Menet, *Non-existence of
  frequently hypercyclic subspaces for P(D)*, Israel Journal of Mathematics
  214 (2016), 149–166, DOI 10.1007/s11856-016-1352-3.
- Theorem 1.2, supporting PDF page 3: for every polynomial `P`, the operator
  `P(D)` on `H(C)` has no frequently hypercyclic subspace.

Identification:

Take `P(z)=z`. The differentiation operator `D` on `H(C)` is a nontrivial
convolution operator in the source paper’s one-dimensional class. Theorem 1.2
therefore supplies a counterexample to the proposed universal extension: not
every nontrivial convolution operator in dimension one has a frequently
hypercyclic subspace.

This is placed under `literature_implied_answers`, not
`literature_already_answered`, because Bayart–Ernst–Menet explicitly answer a
question of Bonilla–Grosse-Erdmann and do not cite or identify the question in
arXiv:1311.7671. The implication for this source was identified in this run.

Files:

- `solution_packet.pdf`: compact status note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1311.7671.
- `supporting_paper_bayart_ernst_menet_2016.pdf`: decisive later paper.

