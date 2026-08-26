# Verification Report

Verdict: `likely valid`, candidate full answer.

## Exact checks

1. Bad approximability gives pair separation: for `1<=i<j<=N`, `dist(x_i,x_j) >= c_α(j-i)^(-1/d) >= c_α N^(-1/d)`.
2. With `h=N^(-1/d)` and `t=h^2`, the field `K_t=-integral_0^t grad p_s ds` has divergence `δ_0-p_t`.
3. The torus heat-gradient bound integrates to `|K_t(z)| <= C r^(1-d) exp(-r^2/(Ct))`.
4. Annular packing of `h`-separated points gives `|F_hi(x)| <= C(h+h^d r(x)^(1-d))`, where `r(x)` is distance to the point set.
5. For `q=d/(d-1)`, this pointwise bound yields `measure{|F_hi|>λ} <= C(h/λ)^q`; hence `||F_hi||_{L^{q,infinity}} <= Ch`.
6. The exact Fourier estimate in the source proof gives `||P_t μ_N-1||_{H^{-1}} <= C/(N t^((d-1)/2))=Ch`. The gradient solution of the divergence equation therefore has `L^2` norm `Ch`, hence weak-`L^q` norm `Ch` because `q<=2`.
7. The total field has divergence `μ_N-1` and weak-`L^q` norm `Ch`.
8. O'Neil Lorentz Hölder pairs weak `L^q` with `L^{d,1}`. Layer-cake interpolation gives `||grad f||_{L^{d,1}} <= C ||grad f||_infinity^((d-1)/d)||grad f||_1^(1/d)`.

All powers of `N`, `h`, and the Lorentz conjugate exponents have been checked symbolically. No numerical experiment is used as proof.

## Potential reviewer sensitivities

- Fix one Laplacian sign convention throughout the divergence identities; the final absolute-value estimate is sign-insensitive.
- Verify the standard torus heat-kernel gradient estimate uniformly for `0<t<=1`.
- In the annular packing step, isolate at most one point inside half the separation radius and bound all remaining shells by `O(m^{d-1})` points.
- Compare the low-frequency `H^{-1}` normalization with the `2π` Fourier convention in the source; this changes only constants.

## Evidence crop

The source PDF was rendered at 180 dpi and page 8 was cropped by `code/make_open_problem_crop.py`. It contains Theorem 7 and both exact questions without altering the source text.

## Novelty bounds

Searched on August 11, 2026:

- local run registry, solutions, attempts, and source indexes;
- arXiv:1909.09046 and its 2020 journal record;
- exact endpoint phrases and combinations of `Kronecker sequence`, `L1 gradient`, `Lorentz`, `numerical integration`, and `badly approximable`;
- later 2024--2026 papers on quasi-uniform Kronecker sequences and Wasserstein equidistribution.

No paper claiming the exact endpoint was found. This is a bounded search, not a novelty certification.
