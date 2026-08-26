# 2210.08687 — an implied 2-jet that is not 1-implied

Status: candidate full counterexample, likely valid; human review requested.

Model: GPT5.6.

Source: Charles Fefferman and Ary Shaviv, *A property of ideals of jets of
functions vanishing on a set*, arXiv:2210.08687 (2022), Definition 2.10 and
Remark 2.11 on source PDF page 12.

## Result

In the truncated nonunital 2-jet ring `P^2_0(R^3)`, set

`I = span{xz, yz, x^2+y^2}` and `p = x^2+2y^2`.

The packet proves that `I` is an ideal, that `I` implies `p` using the two
generators `xz,yz`, and that `p` is not 1-implied by `I`. The allowed
directions of `I` are exactly the two poles. Near them,

`p = (x/z)(xz) + (2y/z)(yz)`.

For a hypothetical single generator
`Q = a xz + b yz + c(x^2+y^2)`, derivatives at a pole give a contradiction.
When `(a,b)` is nonzero, a first derivative in that direction forces the
tame coefficient's value to be arbitrarily small, while a perpendicular
second derivative must reproduce a uniformly nonzero Hessian of `p`. When
`a=b=0`, subtracting the `xx` and `yy` derivative identities cancels the
coefficient and contradicts the arbitrarily small second derivatives of the
error.

## Files

- `main.tex`: exact question, proof intuition, and full counterexample proof.
- `solution_packet.pdf`: rendered human-review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: readable source crop.
- `code/crop_source.py`: reproducible crop script.
- `verification_report.md`: adversarial definition and quantifier audit.

## Reviewer focus

Please check the smooth homogeneous cutoff construction, the claim that the
pole point is interior to the equality region, and the constants when
componentwise derivative bounds are converted to directional bounds. The
two derivative contradictions then exhaust every possible `Q in I`.

## Novelty bound

The four run indexes and targeted searches through 11 August 2026 for the
exact terminology, source title, and sequel found no resolution. This is a
bounded search, so novelty remains provisional pending expert review.
