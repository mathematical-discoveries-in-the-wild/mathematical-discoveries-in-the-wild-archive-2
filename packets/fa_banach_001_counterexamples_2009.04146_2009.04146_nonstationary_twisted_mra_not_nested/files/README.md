# The proposed nonstationary twisted MRA is not nested

Status: **candidate full negative answer to the wavelet-existence question as
printed; likely valid; send to human review**.

Source: S. R. Das, P. Massopust, and R. Radha, *Twisted B-splines in the
complex plane*, arXiv:2009.04146; Applied and Computational Harmonic Analysis
56 (2022), 250--282.  The construction is Definition 5.6 and Example 5.7 on
source PDF pages 26--28; the open question is at the bottom of page 28.

## Result

The spaces in Example 5.7 do not form a nonstationary twisted
multiresolution analysis.  In fact, `V_j` is not contained in `V_{j+1}` for
any `j >= 0`.

The paper itself computes each level-`j` generator as a nonzero phase times
the indicator of

`[k,k+2^{-j}) x [l,l+2^{-j})`.

Consequently every function in `V_{j+1}` is supported on the union of the
smaller corner squares of side `2^{-(j+1)}`.  The level-`j` generator at
`k=l=0` is nonzero on the part of its larger square omitted by that union.
Thus it is not in `V_{j+1}`.

It follows already at `j=0` that no subspace `W_0` can satisfy
`V_0 direct-sum W_0 = V_1`.  Hence no family `Psi_j` satisfying the open
question can exist for the spaces as defined.  This does not resolve the
paper's separate all-orders Riesz-sequence conjecture, and a corrected scaling
construction could pose a different wavelet problem.

## Files

- `solution_packet.pdf`: exact statement and proof.
- `source_paper.pdf`: original paper.
- `figures/construction_crop.png`: Definition 5.6 and Example 5.7 formula.
- `figures/open_problem_crop.png`: exact open question on page 28.
- `verification_report.md`: independent algebra/support audit.
- `novelty_search.md`: bounded exact-question search.
- `../../../../attempts/2009.04146_twisted_bspline_questions_attempt.md`:
  attempts on both extracted questions.

No numerical computation is used in the counterexample proof.
