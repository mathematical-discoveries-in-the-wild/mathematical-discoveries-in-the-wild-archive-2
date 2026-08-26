# Verification record

## Source statement

- The cached arXiv source was extracted and compiled locally to a 32-page PDF.
- Compiled page 4 explicitly asks whether pseudoconvexity can be strengthened
  to convexity for `-2<p<-1` and states Theorem B.
- The complete page was rendered at 170 dpi and visually checked before
  inclusion.

## Proof checks

- The radial formula uses the source identity
  `rho_{I_{C,p}K}^{-p}=J_{C,p}(rho_K^{2n+p})/(2n+p)`.
- On `S^1`-invariant functions, the source reduces every admissible `C` to the
  disk up to a positive scalar; such a homothety cannot affect convexity.
- Division by `Gamma(p+2)` is the correct endpoint normalization. The source
  proves uniform convergence to a positive multiple of the complex spherical
  Radon transform at `p=-2`.
- Unitary equivariance gives `X(T_p f)=T_p(Xf)` for infinitesimal rotation
  fields. Applying the source's `C^0` convergence to a finite spanning family
  of first and second rotation derivatives gives `C^2` convergence.
- The input `rho_K^{2n+p}` depends continuously on `(p,rho_K)` in `C^2` near
  the constant function one. Positivity makes the power `1/p` harmless on the
  compact interval `[-2,-1]`.
- The spherical Hessian criterion is applied to the reciprocal radial
  function: `nabla_S^2 g+g I>0` implies that its one-homogeneous extension is a
  strictly convex gauge.
- Compactness in `p` is used before choosing the input neighborhood, so the
  same neighborhood works for the entire missing interval.
- `GL(n,C)` contravariance transfers the ball-neighborhood result to every
  Hermitian ellipsoid.

## Computational diagnostics

- The retained `CP^1` script uses Gauss--Jacobi quadrature with weight
  `t^{-q/2}` and therefore does not sample across the negative-moment
  singularity naively.
- Direct high-resolution chord checks rejected all apparent Hessian
  violations. These calculations are diagnostic only and are not used in the
  proof.

## Literature scope

- arXiv:2304.00794 was checked in full around the definition, endpoint limit,
  multiplier formulas, pseudoconvexity proof, and counterexample section.
- arXiv:1201.0437 was checked for the complex Busemann endpoint.
- Berck's 2009 convexity theorem was checked for the real `p>-1` range.
- Exact-phrase, title, citation, and arXiv searches through 11 August 2026 did
  not locate a later full resolution or this uniform local statement.
- The result is classified cautiously as a candidate partial theorem.

## Build and render checks

- `source_paper.pdf` compiles to 32 pages and has SHA-256
  `94c8c343136caf5870502dfb2f26bfebb8714f2999929bff4137f45559d3a6d2`.
- `solution_packet.pdf` compiles to five A4 pages and has SHA-256
  `73fdb5bda2f3f31980d74af90324e7e9dfd5b26b4092cb5a1e6c9535993b69f9`.
- The final packet log contains no warnings, overfull or underfull boxes,
  undefined references, or multiply defined labels.
- Every page was rendered at 150 dpi and visually checked for clipping,
  legibility, equation layout, and source-screenshot readability.
