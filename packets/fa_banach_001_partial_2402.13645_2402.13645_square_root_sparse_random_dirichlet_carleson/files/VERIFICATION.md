# Verification

## Claim audit

- The source conjecture is visible on PDF page 17 and at source line 725.
- Lemma 4.4 is visible on PDF page 16 and at source lines 657--696.
- The source's known `a>1/2` Hilbert--Schmidt argument and Corollary 4.5 are
  visible on PDF pages 16--17 and at source lines 697--724.
- The packet concerns exactly the missing range `0<a<=1/2`.

## Proof audit

1. Uniform random angles kill unequal Fourier frequencies in the squared
   normalized kernel inner product.
2. The coefficient asymptotics `c_l ~ (1+l)^(-a)` give the power singularity
   for `a<1/2` and logarithm for `a=1/2`.
3. If radii lie in cells `A_m,A_k`, then
   `1-r_n^i r_j^i ~ 2^{-min(m_i,k_i)}`.
4. Grouping ordered off-diagonal pairs by cells yields the two displayed
   double-sum upper bounds for `E||G-I||_HS^2`.
5. Finite expectation of the nonnegative Hilbert--Schmidt square implies
   almost-sure finiteness. Thus `G=I+(G-I)` is bounded, so the normalized
   kernels are Bessel and the associated measure is Carleson.
6. Under `N_m <= C2^{(1/2-epsilon)|m|}`, the identity
   `(1-a)-(1-2a)/2=1/2` cancels the overlap exponent. The remaining geometric
   double series converges. At the endpoint the extra factor is polynomial
   and is still summable.
7. The same occupancy bound implies the necessary finite-mass series because
   `N_m2^{-(1-a)|m|} <= C2^{-(1/2-a+epsilon)|m|}`.

## Boundary and scope audit

- The proof uses only off-diagonal pairs; diagonal Gram entries are exactly
  one and are removed in `G-I`.
- Cells with small indices are harmless because all asymptotic estimates can
  be enlarged to uniform upper bounds by changing constants.
- Constants may depend on fixed `a` and `d`; no uniformity as `a` tends to
  zero is claimed.
- Divergence of the Hilbert--Schmidt criterion is not claimed to imply
  failure of the Carleson property.
- The full finite-mass conjecture is explicitly left unresolved.

## Artifact audit

- LaTeX compiled with no errors, warnings, overfull boxes, or unresolved
  references.
- The final PDF has four pages and yielded 1,195 words of extracted text.
- All four final pages were rendered at 130 DPI and visually inspected.
- Packet SHA-256:
  `ef4f460c87cd1bedcb2064fdae347564a09bdb7a26aee8e8cd50340c682960f6`.
- Source SHA-256:
  `b8d61c4b8d1c6c34a32ba7bc2a8dcc2a9bbeeb3670611a4f5cb59bd26a39d6fc`.
- Human review remains unchecked.
