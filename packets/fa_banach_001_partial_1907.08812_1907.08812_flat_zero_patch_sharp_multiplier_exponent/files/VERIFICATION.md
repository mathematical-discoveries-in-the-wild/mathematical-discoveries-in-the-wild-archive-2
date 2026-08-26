# Verification report

Status: candidate substantial partial result likely valid; human review
requested.

## Formal audit

- The source's multiplier testing identity was transcribed directly: if
  `1/w in M_2^q`, then `||hat g||_q <= C ||wg||_2`.
- For a normal interval of radius `tau`, at least order `1/tau` Fourier
  coefficients have magnitude bounded below by a constant times `tau`, giving
  the exact `tau^(1-1/q)` lower bound.
- The integrated one-dimensional sectional `H^s` seminorm is bounded by the
  isotropic `H^s(T^d)` norm through the Fourier weight
  `|k_1|^(2s) <= |k|^(2s)`.
- For `s>1/2`, point evaluation on each normal section is continuous and agrees
  almost everywhere with the hyperplane Sobolev trace.
- The anchored fractional Poincare inequality scales as `tau^(2s)`.
- The localized sectional energy tends to zero by absolute continuity of its
  integrable Gagliardo density. This is what proves the critical endpoint.
- An `SL(d,Z)` torus automorphism and a translation preserve Fourier sequence
  norms and multiplier boundedness, giving all rational affine hyperplanes.

## Scope audit

The theorem assumes a relatively open flat trace-zero patch. It does not prove
the source's question for an arbitrary zero set of positive
`(d-1)`-dimensional Hausdorff measure, for lower-dimensional fractal sets, or
at `s=1`.

## Novelty and artifact audit

- The four cheap run indexes had no exact or semantic duplicate.
- Bounded exact-title and close-phrase primary-source searches on 11 August
  2026 found no later resolution or flat-zero-patch theorem.
- The official arXiv PDF is stored locally; page 30 was rendered at 200 dpi and
  contains the complete sharp-exponent question.
- The final packet was compiled without LaTeX warnings, rendered page by page,
  and visually inspected.

## Reviewer focus

Verify the local anchored fractional Poincare lemma and the section/trace
identification. Both are standard consequences of one-dimensional
`H^s -> C^(s-1/2)` for `s>1/2`; the rest of the proof is explicit scaling.
