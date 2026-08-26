# Verification record

Date: 2026-08-12

## Source evidence

- Official arXiv PDF: figures/source_2004.01660.pdf.
- Definition 3.8: PDF page 25, rendered as figures/source_page25-25.png.
- Exact question: PDF page 27, rendered as figures/source_page27-27.png.
- Remark 3.12(i) asks whether Lemma 3.11's Wasserstein/Hilbert
  C1,1 equivalence also holds for C1-alpha when 0 < alpha < 1.

## Proof audit

1. The lift is exactly the radial Hilbert functional
   ||X||^(1+alpha)/(1+alpha).
2. Its gradient is the duality map
   J_alpha(X)=||X||^(alpha-1)X.
3. The proof establishes the dimension-free global estimate
   ||J_alpha(X)-J_alpha(Y)|| <= 3||X-Y||^alpha.
4. Integrating that estimate along a segment gives the precise
   O(||X-Y||^(1+alpha)) Taylor remainder.
5. The derivative factors through the law with Wasserstein gradient
   m_2(mu)^((alpha-1)/2)q; this is a genuine tangent gradient.
6. Optimal lifts turn the Hilbert Taylor estimate into the source's
   Definition 3.8(2).
7. At the standard Gaussian the gradient is the identity on support R,
   which cannot be alpha-Hölder for alpha < 1.
8. The failure occurs at one fixed measure, so it also defeats a local
   equivalence on any neighborhood of that measure.

## Reproducible check

Run:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/2004.01660_c1alpha_wasserstein_lift_equivalence_counterexample/code/verify_radial_holder.py

The script samples five exponents, five dimensions, and twelve orders of
magnitude. It checks the analytic Hölder and Taylor constants and the
unbounded supportwise ratio.

## Highest-value review points

- Confirm that Definition 3.8(1) requires global alpha-Hölder continuity
  on each support, as its text states.
- Confirm the factorization of the Hilbert derivative into the
  Wasserstein gradient in (7).
- Confirm that localizing the function spaces cannot repair a failure
  already present on the support of the standard Gaussian.

## Mechanical and visual checks

- verify_radial_holder.py passed for five exponents, five dimensions, and
  sampled scales from 10^-6 to 10^6.
- latexmk completed with no warnings, overfull boxes, or underfull boxes.
- The final 5-page packet was rendered at 140 dpi and every page was
  visually inspected after the last edit; no clipping, overlap, illegible
  source evidence, or malformed mathematics was found.
- Packet SHA-256:
  a2ad9dc541f37b62ae4cfb9bd42a38b280d6af0d048390815913c5a590ae5065.
- Official source PDF SHA-256:
  384b8d585a6861d051265e5a643f7f6d425d10d05ba6b3bb44ae342631851a25.
