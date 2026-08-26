# Full solution packet: the sharp negative-dimension Cheeger constant

Status: candidate full solution, likely valid, needs human review.

Source: Emanuel Milman, *Beyond traditional Curvature-Dimension I: new model
spaces for isoperimetric and concentration inequalities in negative
dimension*, arXiv:1409.4109.

Question: Remark 5.20 asks whether the sharp diameter bound
`D_Che,infinity >= 2/D`, known in the traditional nonnegative-dimension
range, also holds for `CDD(0,N,D)` spaces when `N<=0`. The paper proves only
`1/D` there and reduces the improvement to an explicit one-dimensional power
density calculation.

Result: yes, and the constant is sharp. For every `N<=0`, every
`CDD(0,N,D)` weighted manifold satisfies

`D_Che,infinity >= 2/D`.

After writing `beta=-N` and scaling `[xi,xi+D]` to `[a,1]`, the reciprocal
reverse hazard of the model density `x^(-beta-1)` is
`phi_beta(x)=x(1-x^beta)/beta`, with limit `x log(1/x)` at `beta=0`. The
half-line Cheeger constant is the reciprocal of the maximum of this function
on the interval from the median to 1. The exact median relation and one
convex-tangent estimate show that this maximum is at most `(1-a)/2`.

Files:

- `main.tex`: complete proof.
- `solution_packet.pdf`: compiled and visually checked packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source page with Theorem 5.19 and Remark
  5.20.
- `code/verify_scalar.py`: high-precision numerical sanity check.
- `VERIFICATION.md`: verifier report.

Sharpness is attained by the uniform probability measure on an interval of
length `D`, which satisfies `CDD(0,N,D)` for every `N<=0` and has linear
Cheeger constant exactly `2/D`.
