# Verification report

Status: substantial partial result; proof audit passed locally.

## Source evidence

- Official arXiv PDF copied as `source_paper.pdf`.
- The exact open question is in the concluding remarks on PDF page 12.
- `figures/open_problem_crop.png` is a readable 220-dpi full-width crop
  containing the complete question and graphon analogy.

## Mathematical audit

1. Checked that a consistent sample of all affine points on each degree-one
   coordinate is a uniform scalar affine map, and independent coordinates
   combine into a uniform affine map to the finite coordinate space.
2. Checked the inclusion--exclusion formula reconstructing every atom of the
   finite Boolean restriction law from densities of affine subsystems.
3. Checked that quotienting by the full translation-period subgroup produces
   an aperiodic core and preserves the uniform-affine restriction law.
4. Checked `ker(L) subset Per(h o A)`, with equality when `L` is surjective
   and `h` is aperiodic.
5. Checked the dimension comparison: lower-dimensional targets produce only
   periodic arrays on the larger full cube, while a square target produces an
   aperiodic array with positive probability.
6. Checked that the aperiodic stratum in equal dimension is exactly the
   affine orbit and is uniform on that orbit, even when the core has affine
   stabilizers.
7. Checked the converse by invariance of the uniform affine-map law under
   composition with a fixed affine bijection.

No numerical experiment or external theorem is used as proof.

## Remaining human checks

- Confirm the marginal interpretation of the source consistency measure for
  selected degree-(1,0) coordinates.
- Confirm that the source premise over every affine system indeed includes
  every subsystem used in inclusion--exclusion.
- Keep the fractional and infinite-coordinate upgrades outside the promoted
  theorem.

## Build and visual audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully on 2026-08-13.
- The final log has no warnings, undefined references, overfull boxes, or
  underfull boxes.
- `solution_packet.pdf` has five pages.  All five were rendered at 150 dpi
  with Poppler and inspected individually; no clipping, overlap, missing
  glyphs, unreadable text, or malformed equations were found.
- The 220-dpi source-question crop was also inspected and is readable.

## Artifact hashes (SHA-256)

- `solution_packet.pdf`:
  `d4f633199c4b325085c18a62bf2b7bebefa0dec35eb8253f5c16317c73dc47e2`
- `source_paper.pdf`:
  `97664cc3e0b039592ed33b45e947eccd98f34c4c1327450051f5e706b187bfc6`
- `figures/open_problem_crop.png`:
  `1fc10396ef356f0940998d5064f20dcac3b755c607fcb66e019b2ea767a39973`
