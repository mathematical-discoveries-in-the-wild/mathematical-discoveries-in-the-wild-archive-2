# arXiv:1604.01211 — continuous interval square-root counterexample

Status: `candidate_counterexample_likely_valid`

The source asks which intervals in `C(K)` have interval square roots and
proves that `g >= 0` and `|f| <= g` are necessary. This packet shows those
conditions are not sufficient even for continuous boundary functions.

If `K` contains a nontrivial convergent sequence, a continuous `f` can be
chosen to alternate between small positive and negative values along it, with
`g = 1`. Any factorization of the lower boundary through a hypothetical
interval root would force both factors to tend to zero on the positive
subsequence, while one factor has modulus one on the negative subsequence.
This contradicts continuity.

Consequently, among first-countable compact Hausdorff spaces, `K` is finite
exactly when every continuous interval satisfying the pointwise necessary
conditions has an interval square root.

Files:

- `main.tex`: theorem, proof intuition, proof, scope, and literature audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: locally compiled arXiv source paper.
- `figures/open_problem_crop.png`: printed page 14 with the source question.
- `verification.md`: proof and artifact audit.
