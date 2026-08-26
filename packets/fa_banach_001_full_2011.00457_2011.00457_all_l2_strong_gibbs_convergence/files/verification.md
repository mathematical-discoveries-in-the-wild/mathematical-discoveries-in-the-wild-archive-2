# Verification record

## Source identification

- Checked the official arXiv PDF, Remark (2) after the corollary (PDF pages 24–25).
- The source proves convergence for `ell^1` and explicitly asks whether it holds for every initial condition in `ell^2`.
- Checked the source's Main Theorem: the eigenvectors `(p_hat_k)` form a Schauder basis, the semigroup has the norm-convergent spectral expansion, and the negative eigenvalues are ordered `nu_2<nu_3<...<0` with `nu_k -> 0`.

## Proof checks

- Let `P_N` be the Schauder partial-sum projections and `K=sup_N ||P_N||`.
- Verified the Abel identity `M_a = L I + sum_n (a_n-a_{n+1})P_n` for every bounded-variation scalar sequence with limit `L`.
- For `a_1=0` and `a_k=exp(t nu_k)` for `k>=2`, the scalar sequence tends to one and has total variation exactly one. Therefore `||exp(tA)-Pi|| <= 1+K`, uniformly in `t`.
- On a finite head through `N`, adjoining a zero tail gives total variation `2 exp(t nu_N)`, which yields the stated head–tail bound.
- Strong convergence follows by first fixing `N`, sending `t` to infinity, and then sending `N` to infinity.
- The normalized eigenvector test gives `||exp(tA)-Pi|| >= sup_{k>=2} exp(t nu_k)=1`, so operator-norm convergence is impossible.

## Literature check

Bounded searches through 2026-08-12 found the 2022 Acta Applicandae Mathematicae publication and Bögli–Vuillermot's 2023 grand-canonical paper. The latter uses a different self-adjoint generator on a weighted sequence space and does not state the exact ordinary-`ell^2` conclusion here. No exact later resolution was found. Novelty remains subject to expert database review.

## Artifact checks

- Official source PDF retained as `source_paper.pdf`.
- LaTeX compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- PDF metadata and extracted text checked.
- Every rendered page inspected for clipping, overlap, formula overflow, and missing glyphs.
