# Verification record

Date: 2026-08-11  
Agent: `agent_lane_12`  
Model: `GPT5.6`

## Mathematical audit

| Check | Status | Detail |
|---|---|---|
| Trace identity | pass | `tr(A^*A)=sum_i ||Ae_i||^2 >= N theta^2`. |
| Spectral count | pass | With `a=theta^2/4`, `r` eigenvalues above `a` imply `tr B <= r+(N-r)a`, hence `r>=ceil(3N theta^2/(4-theta^2))`. |
| High spectral field | pass | Functional calculus with a cutoff supported strictly above `a` gives local continuous approximants to each vector, proving lower semicontinuity without a constant-rank assumption. |
| Frame selection | pass | Michael's finite-dimensional selection theorem selects a unit section from an l.s.c. field of dimension at least `d+1`; iterating in orthogonal complements gives `q-d` orthonormal sections. |
| Connectivity count | pass | The unit sphere of an `r`-dimensional real subspace is `(r-2)`-connected; at each induction step the remaining dimension is at least `d+1`. |
| Noncompact base | pass | Michael's theorem assumes a paracompact base, not a compact one; `R^d` is paracompact with covering dimension `d`. |
| Pseudoinverse | pass | `R^*A^*AR > theta^2 I/4`; the canonical left inverse has norm `<2/theta`, and `R` is isometric. |
| Small-range fallback | pass | A fixed column gives a continuous factorization of `I_1` with norm product at most `1/theta`. |

## Literature audit

- Cheap run indexes: no existing result or attempt for arXiv:1909.00807.
- arXiv:2201.04238 / Fan et al. (2022): Theorem 3.10 answers the source's first, one-dimensional `theta^2 N` question; Section 5 explicitly leaves multidimensional domains open.
- arXiv:2512.15467 / Müller--Tomilov (2026): sole indexed citation to Fan et al.; still works on an interval and does not give this finite-dimensional multidimensional theorem.
- Bounded arXiv searches on 2026-08-11 for exact-title/restricted-invertibility/continuous-family phrases returned only arXiv:2201.04238 as a directly overlapping work.
- The selection theorem was checked against E. Michael, *Continuous selections II*, Ann. of Math. 64 (1956), Theorem 1.2 and its global finite-dimensional corollary.

## Artifact checks

- `main.tex` compiled with `latexmk`.
- The final PDF was checked for LaTeX warnings and text extraction.
- The final packet has 4 pages and SHA-256 `acdcdfc3d839174b07a1c0d8048040db19ced02e6fbde030de668547abce4768`.
- Every rendered page was visually inspected after the final compile; the source excerpt is tightly cropped to Question 2 and no clipping or overflow remains.
