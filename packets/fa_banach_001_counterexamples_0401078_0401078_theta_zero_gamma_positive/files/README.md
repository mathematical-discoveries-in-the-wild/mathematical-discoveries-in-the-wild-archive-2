# Theta and Gamma polynomial capacities differ

This packet answers the open question in arXiv:math/0401078 by constructing a
one-dimensional vector subspace with

`Theta = 0 < Gamma`.

The smallest explicit example is

`Q=(-1,1), m=2, k=0, p=2, alpha=1, A=span{1+x/2}`.

The packet also proves a family of separations for every `0<=k<=m-2` and
shows that the positive Gamma capacity can be made arbitrarily small.

Status: `candidate_counterexample_likely_valid`, pending human review.

Files:

- `main.tex`: definitions, general theorem, proof, explicit example, and scope.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_question_crop.png`: exact source question on PDF page 6.
- `code/verify_explicit_example.py`: exact arithmetic check of the example.
- `VERIFICATION.md`: proof, build, visual-QA, novelty, and hash record.
