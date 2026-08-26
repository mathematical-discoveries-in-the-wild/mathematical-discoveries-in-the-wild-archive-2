# The `p=infinity` tree-extension endpoint follows from older literature

Status: `literature_implied_answer (endpoint subcase)`.

Fefferman--Klartag ask whether linear extension operators exist at the
extreme indices `p=1` and `p=infinity`.  The `p=infinity` half is a direct
instance of the older universal linear Lipschitz-extension theorem for metric
trees.

Give edge `e` length `a_e^{-1}` when the endpoint seminorm is

`max_e a_e |F(child(e))-F(parent(e))|`.

Then this is exactly the Lipschitz seminorm on the path-metric tree.  The
trace seminorm is the Lipschitz seminorm on its leaf set.  Theorem 2.4 of
Brudnyi--Brudnyi, arXiv:math/0404304, specialized to one tree, says that the
linear Lipschitz extension constant of every metric tree is bounded by a
universal constant.  Restricting their extension to the vertices gives the
requested Sobolev extension operator.

If `p=infinity` is interpreted as the literal limit of the source's weighted
`ell_p` formula, the edge weights disappear and the same deduction applies
with every edge length equal to one.

Files:

- `solution_packet.pdf`: concise deduction and scope.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:2301.13792 PDF.
- `supporting_metric_tree_extension.pdf`: official arXiv:math/0404304 PDF.
- `figures/open_problem_crop.png`: exact source question.
- `VERIFICATION.md`: source and artifact audit.

The supporting theorem predates the source question and does not identify
itself as answering that question.  This is therefore an agent-identified
implication, not an explicit literature answer.  It does not answer the
`p=1` endpoint, the inhomogeneous problem, or the central non-radial
conjecture for `1<p<infinity`, `p!=2`.
