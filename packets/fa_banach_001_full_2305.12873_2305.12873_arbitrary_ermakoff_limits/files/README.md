# Arbitrary positive finite Ermakoff limits

This packet fully answers the example question in footnote 3 on source PDF
page 5 of arXiv:2305.12873.

For every prescribed `a>0`, it constructs a continuous strictly increasing
function `g:[1,infinity)->[1,infinity)` with `g(1)=1` such that

`t g(t) / g(exp(t)) = a`

for every sufficiently large `t`.  The key substitution
`h(x)=log(g(exp(x)))` turns the desired identity into
`h(exp(x))=h(x)+x-log(a)`, which is solved recursively across
iterated-exponential intervals.

Status: `candidate_full_proof_likely_valid`, pending human review.

Files:

- `main.tex`: source-grounded theorem and complete proof.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: primary arXiv source.
- `figures/source_question_crop.png`: readable source excerpt.
- `code/verify_construction.py`: independent numerical checks of the exact
  recurrence, monotonicity, junction continuity, and eventual ratios.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
