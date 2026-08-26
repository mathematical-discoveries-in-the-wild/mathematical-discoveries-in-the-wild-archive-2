# Verification

Status: `candidate_partial_result_likely_valid`

## Mathematical checks

- The square-root bonus is uniformly bounded by Cauchy--Schwarz.
- The scalar multiplier equation has a unique solution above the affine
  maximum because the maximum is attained and every weight is positive.
- The proposed optimizer sums to one and the tangent inequality for the
  square root proves global optimality and uniqueness.
- The optimized value simplifies to the formula displayed in the theorem.
- On a neighborhood of each point, the multiplier gap bounds every
  denominator away from zero. Uniformly bounded slopes and `sum w_i^2 <
  infinity` dominate every differentiated series.
- The scalar derivative with respect to the multiplier is strictly negative,
  so the Banach-space implicit function theorem applies.
- Shifting the upper approximation down by `epsilon` gives the one-sided
  estimate required by the source paper.

No computational experiment is used as evidence for the proof.

## Scope check

The packet explicitly assumes an attained countable affine maximum with
uniformly bounded slopes. It does not claim that every convex function has
such a representation, and it does not claim a full answer to the source
question.

## Rendering check

`main.tex` compiled successfully with `latexmk` under TeX Live 2026. The
final `solution_packet.pdf` has 5 letter-size pages. The LaTeX log contains
no warnings, undefined references, overfull boxes, or underfull boxes.

Every page was rasterized at 144 dpi and inspected individually. The title
and status box, source-question crop and caption, theorem statement, all
displayed formulas, page breaks, proof-ending marks, limitations section,
and bibliography are fully visible. No clipping, overlap, missing glyph,
or unreadably small packet text was found. The embedded source crop is
legible and contains the exact open question.

SHA-256 of `solution_packet.pdf`:

`51981de991944c6ec52a1482c90c8d3496c13472674eb0de617d6dca40b34b09`
