# The 2-by-2 upper-bild trichotomy fails in every dimension n >= 3

Status: candidate full answer, likely valid, awaiting specialist review.

Carvalho, Diogo, and Mendes ask after Corollary 3.11 of arXiv:2008.02850
whether any of its three sign-regime descriptions of the upper bild can be
generalized from 2-by-2 complex matrices to higher dimensions. Their next
example treats the indefinite and positive-definite regimes at size three.

This packet closes the remaining singular positive-semidefinite branch and
uniformizes all three failures to every dimension `n>=3`. The key new family is

`A_n^0 = diag(1+i,1+i,0,...,0)`.

It has singular positive-semidefinite imaginary part, complex numerical range
`[0,1+i]`, and exact upper bild

`B^+(A_n^0) = conv{0,1,1+i}`.

Thus the upper bild is strictly larger than the upper complex numerical range.
Two companion diagonal families show, uniformly in `n`, that the other two
formulas fail as well.

Contents:

- `main.tex` and `solution_packet.pdf`: expert-facing statement and proof.
- `source_paper.pdf`: arXiv:2008.02850, including the source question.
- `figures/open_problem_crop.png`: source PDF page 9, showing Corollary 3.11,
  the natural question, and the beginning of Example 3.12.
- `code/verify_counterexamples.py`: exact quaternionic identity checks and an
  independent randomized bound check.
- `VERIFICATION.md`: mathematical, source, novelty, and PDF QA record.

The claim is deliberately precise: it disproves universal extension of the
three displayed 2-by-2 formulas. It does not assert that no other useful
higher-dimensional simplification can exist.
