# Weighted two-atom Cauchy dual classification

Status: candidate full solution, likely valid, awaiting specialist review.

For distinct `zeta1,zeta2` on the unit circle and arbitrary `c1,c2>0`, this
packet proves that the Cauchy dual of multiplication by `z` on

`D(c1 delta_zeta1 + c2 delta_zeta2)`

is subnormal if and only if the two support points are antipodal. The
antipodal direction is Theorem 2.3 of Chavan--Ghara--Reza
(arXiv:2103.10059); the new result is non-subnormality for every pair of
positive weights at non-antipodal support.

The source paper arXiv:2510.14004v2 proves only the two unit masses and, on
PDF page 25, explicitly proposes the arbitrary-weight extension. The proof
here uses its rank-two de Branges--Rovnyak setup but replaces angle-by-angle
estimates with an exact resultant for unequal weights and high-order
positivity minors for the common-ray and repeated-pole cases.

Contents:

- `main.tex` and `solution_packet.pdf`: expert-facing proof.
- `source_paper.pdf`: arXiv:2510.14004v2.
- `supporting_paper_2103.10059.pdf`: the simple-pole criterion and antipodal
  theorem used in the proof.
- `figures/open_problem_crop.png`: real full-width source-PDF crop of the
  Epilogue on page 25.
- `code/verify_identities.py`: exact symbolic checks for the main factors.
- `code/equal_pair_algebra.py`: exact derivation of the equal-weight Gram
  coefficients.
- `code/numeric_general_weights.py`: independent numerical reconstruction and
  grid check.
- `VERIFICATION.md`: proof, computation, source, novelty, and PDF QA record.

The result does not address measures supported at three or more points.
Review should focus first on the unequal-weight resultant and the
double-root finite-difference minor.
