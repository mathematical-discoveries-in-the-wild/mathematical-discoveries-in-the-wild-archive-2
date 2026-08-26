# Rank-one characterization of the multiplier-curve case

This packet gives a full proof of the conjectured converse immediately after
Corollary 4.11 of arXiv:2507.21537v3, *Multiplier varieties and multiplier
algebras of CNP Dirichlet series kernels*, by Hamidul Ahmed, B. Krishna Das,
and Chaman Kumar Sahu.

## Files

- `solution_packet.pdf`: review-ready statement and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv v3 source PDF (14 May 2026).
- `figures/source_corollary_crop.png`: source PDF page 22, showing Corollary
  4.11 and both alternatives.
- `figures/open_problem_crop.png`: source PDF page 24, showing the conjectured
  converse.
- `VERIFICATION.md`: source, proof, novelty, build, and visual-QA record.
- `code/crop_source.py`: reproducible source-crop helper.

## Result

For finite or countably infinite weight/frequency data, either of the exact
curve equalities in Corollary 4.11 holds **if and only if**

```text
ln(n_i) / ln(n_1) is rational for every i >= 2.
```

Equivalently, the rational span of all frequency logarithms has dimension
one.  Thus the conjectured converse is true in both branches of the
corollary.

The necessity is stronger than requested.  If one ratio is irrational, every
multiplier variety containing the Dirichlet curve and relatively norm closed
in the ball contains a nonzero point outside the curve.  The construction
fixes the first phase along a vertical orbit while forcing the irrational
coordinate toward a phase that no point of the curve with that first
coordinate can have.

## Review focus

The decisive checks are: relative norm-closedness of the multiplier variety;
the diagonal-subsequence plus square-summable-tail argument when `d=infinity`;
and the two-coordinate phase contradiction excluding the limit from the
entire Dirichlet curve.  No unproved analytic or number-theoretic lemma remains.
