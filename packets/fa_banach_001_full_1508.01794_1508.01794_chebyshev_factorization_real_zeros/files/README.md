# Full solution: zeros of the basic Jacobi-type-pencil polynomials

Status: candidate full solution, independently rechecked and likely valid,
pending expert review.

Source: S. M. Zagorodnyuk, “Orthogonal polynomials related to some
Jacobi-type pencils,” arXiv:1508.01794, formula (8) and the open problem on
source PDF page 6.

The source conjectures that every zero of its explicitly represented
polynomial `p_n` is real.  This packet proves more: after the affine change
`lambda = sqrt(2)t-1`, a period-eight Chebyshev factorization gives the full
zero multiset.  Every zero is real and simple.  For `n >= 4`, exactly one zero
lies below `-1-sqrt(2)` and the other `n-1` lie between
`-1-sqrt(2)` and `-1+sqrt(2)`; the first three degrees have all zeros in that
open interval.  Also, `lambda=-2` is a zero exactly when `n = 2 mod 4`.

Files:

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: local rendering of the ingested arXiv source.
- `figures/open_problem_crop.png`: readable crop of the source question.
- `code/verify_factorizations.py`: exact symbolic and numerical regression
  checks.
- `code/crop_open_problem.py`: reproducible source-page crop.
- `verification_report.md`: adversarial proof and artifact verification.

The most useful expert check is the residue-class factorization table in the
main theorem and the argument that the two factors share no zero except the
single removable overlap at `t=-1/sqrt(2)` when `n = 2 mod 4`.
