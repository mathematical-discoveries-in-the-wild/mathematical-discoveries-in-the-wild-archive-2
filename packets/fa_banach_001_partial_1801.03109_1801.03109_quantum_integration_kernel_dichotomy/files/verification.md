# Verification notes

Status: `candidate_partial_likely_valid`; human review recommended.

## Formal checks

1. For the kernel-projection argument, the spectral projection
   `P(x)=1_{0}(D(x))` is weakly measurable as the strong pointwise limit of
   `(I+nD(x))^{-1}`. On the positive-measure set where it is nonzero, it has
   essential norm one and `D^(1/2) P D^(1/2)=0`.
2. Under `D>=cI` on `E`, functional calculus gives
   `||D^(-1/2)||<=c^(-1/2)` there. Thus
   `F=gD^(-1/2)AD^(-1/2)` is essentially bounded and its integrand is exactly
   `gA`.
3. Nonatomicity passes from `nu` to the mutually absolutely continuous scalar
   measure `nu_rho`, so a nonzero mean-zero bounded `g` exists on every
   positive-measure `E`.
4. In the block Fourier example, each block has eigenvalues `1+-a_k`; hence
   the density lies between `(1-a_1)I` and `(1+a_1)I`. The decay `a_k->0`
   makes the infinite block field norm-continuous.
5. A diagonal full-rank density operator makes `Tr(rho D(z))=1`, so Haar
   measure is exactly `nu_rho` and `D=dnu/dnu_rho`.
6. The diagonal and two off-diagonal entries of the scalar integral recover
   the zeroth, positive, and negative Fourier coefficients of any
   `f in L^infinity(T)`. Fourier uniqueness in `L^1(T)` proves injectivity.
7. If the POVM range were convex, it would contain `I/2`; scalar injectivity
   would then force a characteristic function to equal `1/2` almost
   everywhere, an impossibility.

## Scope and upgrade audit

Six distinct upgrade attempts were recorded in the attempt README. The only
unresolved case is where the density is injective but has dense nonclosed
range almost everywhere. In that case the inverse-density and commutator
kernel formulas can be unbounded. The packet therefore remains partial.

## Artifact checks

- Source evidence was rendered from physical PDF page 7.
- LaTeX was compiled with `latexmk -halt-on-error` with build files confined
  to `tmp/`.
- The final PDF was checked for warnings and visually inspected page by page.
