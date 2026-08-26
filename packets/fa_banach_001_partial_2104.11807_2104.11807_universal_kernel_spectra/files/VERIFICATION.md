# Verification record

## Mathematical checks

- Question 2.12 was checked on page 7 of arXiv:2104.11807v1.
- The RKHS of the displayed kernel is identified explicitly with `ell_2(N)`;
  every function in it vanishes at the extra point `0`.
- For arbitrary finite atomic weights, the source integral formula gives
  `(T_mu T_mu^* f)(n)=w_n f(n)` and value zero at the extra point.
- The closure and adjoint domains were tracked after the unitary normalization
  `f_n -> sqrt(w_n) f_n`, so unbounded weights are covered.
- The resolvent criterion for a diagonal self-adjoint operator proves that its
  spectrum is the closure of the diagonal values, with the zero coordinate
  included exactly when it has positive measure.
- Every nonempty closed subset of `[0,infinity)` has a countable dense subset
  of its positive part; the separate zero coordinate handles isolated zero.

## Computational check

`code/check_diagonal_model.py` uses rational arithmetic on 2,000 generated
weight/function instances and passed 40,179 coordinate-level checks of the
kernel-integral formula, the normalized diagonal product, and finite spectral
sets.

## Artifact checks

- `source_paper.pdf`: 37 pages.
- `source_question.pdf`: one extracted page, visually inspected.
- `solution_packet.pdf`: compiled twice through `latexmk` with no warnings.
- The final PDF was rendered to RGB PNG at 170 dpi and every page was visually
  inspected after the last compilation.
