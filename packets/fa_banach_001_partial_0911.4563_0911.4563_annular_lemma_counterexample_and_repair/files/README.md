# Counterexample and repair for the annular lemma in arXiv:0911.4563

Status: `substantial partial result, likely valid, pending human review`

The printed Assertion B of Lemma 3.4 in Mouhot--Russ--Sire is false even
for the one-dimensional standard Gaussian measure and `p=2`.  A unit-scale
cube centered at `R=2^k`, together with a smooth function having a small hole
at the center, makes the left side stay bounded below while the claimed right
side is `O(2^{-k})`.

The main `L^2` theorem is nevertheless repairable.  The false denominator
`(2^k sqrt(t))^n` is replaced by `t^(n/2)`, which is the scale of the cube on
which the subtracted mean is actually taken.  The extra polynomial annular
loss is absorbed by the proof's existing `exp(-c 2^k)` off-diagonal factor.

The packet also proves scalar `L^p` off-diagonal resolvent bounds for all
`1<p<infinity` by interpolation.  These are meaningful progress toward the
paragraph's intended global `L^p` square-function comparison, but they do not
settle it: the missing step is vector-valued square-function/off-diagonal
control, not a scalar estimate.

Files:

- `source_paper.pdf`: arXiv:0911.4563.
- `figures/lemma_3_4_B_crop.png`: the printed annular assertion.
- `figures/proof_and_lp_question_crop.png`: the one-line proof and the exact
  `L^p` question.
- `main.tex`, `solution_packet.pdf`: counterexample, correction, repaired
  summation, and precise remaining obstruction.
- `verification.md`: mathematical and artifact checks.

