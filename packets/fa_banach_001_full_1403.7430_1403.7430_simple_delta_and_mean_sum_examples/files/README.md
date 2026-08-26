# Simple mean-class examples for arXiv:1403.7430

Status: **candidate full resolution, likely valid**, of Open Question 10 and
of the literal simple-existence clause of Open Question 3.

The packet gives two elementary constructions on `J=R`:

1. The cone of nonnegative bounded continuous real functions is invariant,
   uniformly closed, contained in `BC`, and stable under all forward means,
   but fails `(Delta)` with the witness `f(t)=tanh(t)`.  This does not supply
   the optional linear refinement requested in Question 3.
2. For `U=span{cos t}` and `V=span{sin t}`, one has
   `MU=MV=N` (the a.e.-null class), while the two-dimensional space `U+V` is
   mean-invariant.  Hence `MU+MV` is strictly contained in `M(U+V)`, fully
   answering Question 10.

The proof is exact and uses only the explicit averaging matrix for sine and
cosine plus one-sided Lebesgue differentiation.  The source question is on
PDF page 30 and is reproduced in `figures/questions_q3_q10.png`.

Human review should focus on the source's convention about null functions in
mean classes and on the deliberately scoped wording for Question 3.  The
Question 10 result is unaffected by passing to a.e. equivalence classes.

Files:

- `main.tex` / `solution_packet.pdf`: proof packet
- `source_paper.pdf`: arXiv source paper
- `figures/questions_q3_q10.png`: source-question crop
- `code/check_identities.py`: independent numerical sanity check
- `VERIFIER_REPORT.md`: verification record

Ledger: `runs/fa_banach_001/ledger/results/1403.7430_simple_delta_and_mean_sum_examples.json`
