# Diagonal counterexample to the all-parameter inequivalence conjecture

This packet gives a full counterexample to the literal conjecture in
arXiv:0904.1710v2.

## Result

For every `1 <= p <= 2`, every pair of matrix sizes, and every bipartite
matrix `Y`,

`||Y||_{CL:p,p} = ||Y||_{NC:p,p} = ||Y||_p`.

The source conjectures inequivalence for every `1 < p <= 2` and every
`q >= 1`; choosing `q=p` therefore refutes it.  The source already states the
NC equality.  The packet proves the CL equality by computing the Hermitian
positive-decomposition gauge exactly.

The same calculation shows that the source's CL nonmonotonicity lemma is false
at its stated endpoint `p=q`.

## Files

- `main.tex`: complete proof, checks, and scope boundary.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: exact page-6 conjecture context.
- `tmp/`: compilation and final page-render QA artifacts.

## Limitation and review recommendation

The result does not settle the likely intended off-diagonal conjecture
`q != p`.  Human review should confirm the source's quantifiers and check
whether a later publication or erratum silently excludes the diagonal.
