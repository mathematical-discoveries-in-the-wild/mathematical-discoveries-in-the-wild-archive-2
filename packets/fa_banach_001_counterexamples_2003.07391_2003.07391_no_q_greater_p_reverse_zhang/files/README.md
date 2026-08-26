# No `q>p` reverse affine Zhang improvement

**Status:** candidate counterexample, likely valid; complete negative answer to
Section 7, item (6) of arXiv:2003.07391.

**Source:** Julián Haddad, Carlos Hugo Jiménez, and Marcos Montenegro, *From
affine Poincaré inequalities to affine spectral inequalities*, arXiv:2003.07391,
Section 7, item (6), PDF page 27.

## Result

For every dimension `n>=2`, every `p>=1`, every `q>p`, and every nonempty
open set `Omega`, there is no positive constant `C` such that

`E_p(f) >= C ||f||_q^((n-1)/n) ||grad f||_p^(1/n)`

for all smooth functions supported in `Omega`.

Compressing one coordinate of a fixed smooth bump by `epsilon` gives the exact
scalings

- `E_p(f_epsilon) = epsilon^(1/p-1/n) E_p(g)`;
- `||f_epsilon||_q = epsilon^(1/q)||g||_q`;
- `||grad f_epsilon||_p >= epsilon^(1/p-1)||partial_1 g||_p`.

The proposed inequality ratio is therefore at most
`C_g epsilon^(((n-1)/n)(1/p-1/q))`, which tends to zero precisely when `q>p`.
Thus the source's `L^p` exponent is sharp against every larger Lebesgue
exponent, even with a domain-dependent constant.

## Files and verification

- `solution_packet.pdf`: full theorem, covariance calculation, and novelty
  audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real source-page crop of item (6).
- `code/render_open_problem.py`: reproducible crop renderer.
- `code/verify_scaling.py`: exact rational simplification and representative
  positivity checks for the decay exponent.
- `VERIFIER_REPORT.md`: proof and render audit.
- Attempt record:
  `runs/fa_banach_001/attempts/2003.07391_reverse_zhang_q_obstruction.md`.

The most important human check is the general-linear covariance exponent
`1/p-1/n`; the packet derives it directly from the directional-norm unit ball.

Final packet SHA-256:
`ece37f1645d6f86092dcb8ac10634ad3a27ccd2653ed2705568dc82690bfc192`.
