# Verification report

## Verdict

Likely valid candidate partial result. No computational dependency is used.
The proof should receive human review, with the coordinate estimate in Step 1
as the main focus.

## Proof audit

1. **Admissible tests.** The functions
   \(u_R(x)=\phi(x_1)\eta(R^{-w_2}x_2,\ldots,R^{-w_N}x_N)\) are smooth and
   compactly supported for each finite \(R\).
2. **Haar scaling.** In exponential coordinates on a simply connected
   nilpotent group, Haar measure is a constant multiple of Lebesgue measure.
   Removing one weight-one coordinate leaves transverse Jacobian
   \(R^{Q-1}\).
3. **Vector-field error.** A horizontal left-invariant field has polynomial
   coefficients of the required homogeneous degrees. On the partial-dilation
   support, every derivative of the transverse cutoff is \(O(R^{-1})\), even
   when its coefficient contains the undilated variable \(x_1\).
4. **Kernel cancellation.** After choosing the first horizontal basis vector
   in \(\ker T\), the only order-one main term is
   \(T(e_1)\phi'(x_1)\eta_R=0\).
5. **Exponent check.** With \(q=Q/(Q-1)\),
   \((Q-1)/q=(Q-1)^2/Q=Q-2+1/Q\), strictly larger than \(Q-2\).
6. **Maximal hypoellipticity.** Injectivity of a finite-dimensional map
   \(T\) gives \(|v|\leq C|Tv|\), hence the required \(L^2\) estimate
   pointwise and by integration.
7. **Compatibility block.** The source's Proposition 7.1 supplies a
   homogeneous compatible cocanceling operator for the horizontal gradient.
   Composing it with a left inverse of \(T\) treats \(\operatorname{ran}T\).
   The added pure-derivative block vanishes on \(\operatorname{ran}T\) and is
   cocanceling on a chosen complement. Both blocks have the same order.

## Bounded novelty check

The exact arXiv id, title, and the terms "maximally hypoelliptic",
"cocanceling", "necessity", and "stratified" were checked in the run's four
cheap indexes and the locally loaded arXiv corpus. The exact-title citation
graph was also checked through OpenAlex on 2026-08-11. It listed three citing
works (2023, 2024, and 2025). The locally available 2023/2024 endpoint
Sobolev notes discuss the Euclidean characterization and cite the source only
for stratified-group estimates; the 2025 Cartan-group paper studies particular
hypoelliptic Laplacians. No explicit general or scalar-first-order necessity
theorem was found.

This was a bounded search, not an exhaustive MathSciNet/Zentralblatt review.
Novelty confidence is therefore moderate. Mathematical-validity confidence is
higher than novelty confidence.

## Human-review focus

Verify the standard polynomial normal form of the left-invariant horizontal
fields in the chosen exponential coordinates and the uniform
\(O(R^{-1})\) estimate under the partial (all-but-one-coordinate) dilation.

