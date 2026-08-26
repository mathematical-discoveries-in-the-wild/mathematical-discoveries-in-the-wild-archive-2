# Dyadic sharp-weight stability with a p-concave endpoint

Status: `candidate_partial_likely_valid`.

Source: Alessio Figalli, Peter van Hintum, and Marius Tiba,
*Sharp Quantitative Stability for the Prékopa-Leindler and
Borell-Brascamp-Lieb Inequalities*, arXiv:2501.04656, Remark 1.8 on page 5.

## Result

For every `p > -1/n` and every dyadic `lambda = 2^(-m)`, the sharp conjectured
bound

```text
C_(n,p) sqrt(delta/lambda)
```

holds if the input carrying weight `1-lambda` is already `p`-concave.  The
constant is independent of `m`.  The proof is based on an exact semigroup
identity for `p`-sup convolutions and the source theorem only at the fixed
midpoint weight.

Uniform densities on nested homothetic cubes show that the
`lambda^(-1/2)` dependence is necessary.  The same examples prove the new
quantitative lower bound `C_(n,p) >= c_n (np+1)^(-1/2)` as
`p -> -1/n`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/source_question_crop.png`: exact source-page crop.
- `code/verify_cube_expansion.py`: symbolic verification of the sharpness
  expansion and exact-distance asymptotic.
- `verification.md`: reproducibility and QA record.

## Scope

The unrestricted conjecture remains open here.  Without endpoint
`p`-concavity, the semigroup comparison has the wrong direction for
propagating a small final deficit backward.  Six distinct upgrade routes are
recorded in the accompanying attempt.

