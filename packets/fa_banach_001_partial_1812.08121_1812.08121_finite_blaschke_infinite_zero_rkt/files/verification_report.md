# Verification report

Status: substantial partial result; mathematical audit passed locally.

## Source evidence

- The official arXiv PDF is `source_paper.pdf`.
- Source PDF page 8 contains the weighted `A^2_alpha` question.
- Source PDF page 9 contains the infinite-zero question.
- Both passages were rendered at 220 dpi, cropped without alteration, and
  inspected for readability.

## Mathematical audit

1. Checked the pullback norm identity and the identification of the `A^p`
   test lower bound with the standard `A^2` Berezin transform.
2. Checked the area-formula density for a finite Blaschke product, including
   multiplicities away from the finite critical-value set.
3. Checked that local roots of nonvanishing inverse derivatives make the
   unweighted density a finite sum of subharmonic terms.
4. Checked that Carleson disk upper bounds plus the submean inequality give a
   uniform outer density bound.
5. Checked the weighted density formula and uniform upper/lower comparison of
   its derivative and boundary-distance factors.
6. Checked that a compactly supported finite measure has Berezin transform
   tending to zero at the boundary.
7. Checked the Fredholm argument: bounded-symbol invertibility, compact
   perturbation, injectivity from positive-area support, and self-adjoint
   Fredholm invertibility.
8. Checked the transfer to all `A^p` through Luecking's exponent-independent
   dominating-set condition used by the source.
9. Checked the zero monodromy condition and analytic extension of `h^(p/2)`.
10. Checked the even-integer case independently by applying the Hilbert lower
    bound to `F=f^(p/2)`, without an exponent-transfer theorem.
11. Rejected the invalid arbitrary-measure shortcut using the counterexamples
    in arXiv:2405.05412.

No numerical experiment or symbolic computation is used as proof.

## Priority human checks

- Verify the weighted dominating-set theorem in precisely the normalization
  used for `A^2_alpha`.
- Verify uniform inverse-chart constants for a finite Blaschke product in the
  weighted density proof.
- Verify the source's exponent-independence step for the common pullback
  measure in the compatible-multiplicity theorem.

## Build and visual audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully on 2026-08-13.
- The final log contains no warnings, undefined references, overfull boxes,
  or underfull boxes.
- The packet has six pages.  All six were rendered at 150 dpi with Poppler
  and inspected individually; no clipping, overlap, missing glyphs,
  malformed equations, or unreadable text was found.
- Both 220-dpi source-question crops were inspected after the final recrop and
  contain the complete decisive passages without unrelated text.

## Artifact hashes (SHA-256)

- `solution_packet.pdf`:
  `bd58d5417b429e1b2f15a1631746c1904ec5b3dbe42e7b3e8e2bef4d72c11145`
- `source_paper.pdf`:
  `715590957142f59105da04e020d9207c629309afd62d3887f25e552fe8149d69`
- `figures/weighted_question_crop.png`:
  `cb1e75d3e771ec7617c42b91c97ace35fd861a9c2c6f2e130d64241b1fba0a66`
- `figures/infinite_zero_question_crop.png`:
  `3d4e13172bc8b27fc87fa12e9fbcf527b0f540c67f055501588a2a7b47ddf298`
- `supporting_papers/2405.05412.pdf`:
  `a63b8dd489c3514072385405e91c6d2af1758955139502f3eac626c46ba545b9`
