# Verification record

## Mathematical checks

1. Source Lemma 4.5 gives
   `V_alpha >= N^(2 alpha-4)|x|^2(c_1-c_2/N^alpha)`.  Hence the negative
   part vanishes outside a homogeneous ball and is at most
   `C N^(alpha-2)` inside it.
2. Homogeneous polar integration gives `N^(alpha-2) in L^p_loc` exactly when
   `p(2-alpha)<Q`.  The interval `Q/2<p<Q/(2-alpha)` is nonempty for every
   `alpha>0`.
3. The exact potential estimate
   `|V_alpha| <= C(N^(2alpha-2)+N^(alpha-2))` implies
   `V_alpha in L^2_loc`, including the critical homogeneous dimension `Q=4`,
   because `2(2-alpha)<Q`.
4. For `1/2=1/p+1/r`, heat-kernel scaling gives
   `||e^(-tL)||_(2->r)<=C t^(-Q/(2p))`.  Integrating the resolvent yields
   `||W(L+lambda)^(-1)||_(2->2)
   <=C||W||_p lambda^(-1+Q/(2p))`, with a strictly negative exponent.
5. The first-order Sobolev inequality at exponent `2Q/(Q-2)` and
   interpolation make `W` infinitesimally form-bounded, so the deficiency
   criterion for semibounded symmetric operators applies.
6. The source Kato inequality gives
   `(L+lambda)|f| <= W|f|`.  Exhausting cutoffs justify testing against the
   noncompact positive resolvent function; commutators vanish using
   `||grad chi_R||_infinity=O(R^-1)`, `||L chi_R||_infinity=O(R^-2)`, and
   `f,g,grad g in L^2`.
7. The unitary-domain bridge is checked separately:
   `sqrt(w) grad(phi/sqrt(w))` is locally square-integrable and the
   conjugated operator is in weighted `L^2`.  Source Theorem 2.3 therefore
   places `phi/sqrt(w)` in the weighted form-operator domain.

Run the arithmetic verifier with:

```sh
conda run --no-capture-output -n sandbox python code/verify_exponent_window.py
```

It checks the critical dimension `Q=4`, several higher dimensions, values of
`alpha` down to `0.01`, the positive radial exponent, negative resolvent
exponent, and local-`L^2` inequality.  Every assertion passes.

## Literature and novelty checks

- Source: Tommaso Bruno and Mattia Calzi, *Weighted sub-Laplacians on
  Métivier Groups: Essential Self-Adjointness and Spectrum*,
  arXiv:1610.09850, published in Proceedings of the AMS 145 (2017),
  3579–3594.
- The run registry and local sources were searched for the arXiv id, title,
  Métivier group, weighted sub-Laplacian, Schrödinger potential, and essential
  self-adjointness.
- A bounded web search through 2026-08-13 used the exact open phrase and close
  variants involving `V_alpha`.  It found the source paper and papers citing
  it, but no explicit resolution of Remark 4.8.  This is not an exhaustive
  priority determination.
- The Kato and heat-resolvent ingredients are standard.  The substantive new
  step is recognizing that the source potential's entire negative part lies
  in the strict `p>Q/2` subcritical range and closing the deficiency equation
  quantitatively.

## Artifact and PDF checks

- The official arXiv PDF is stored as `source_paper.pdf`.
- Source PDF page 12 was rendered at 180 dpi; the crop contains the complete
  Corollary 4.7 and Remark 4.8.
- The packet was compiled with build artifacts under `tmp/build/`.
- All final PDF pages were rendered and visually inspected.
- The final log was checked for undefined references, missing citations,
  overfull boxes, and fatal errors.

## Human review recommendation

Review the cutoff-resolvent test and the distributional conjugation at the
identity first.  Those are the only two places where domain bookkeeping is
not purely formal.  The exponent window itself is strict and independently
checked.
