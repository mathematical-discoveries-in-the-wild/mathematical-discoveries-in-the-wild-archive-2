# Verification report

## Exact calculations checked

- The positive tail is
  `T_q(y) = [Z_q(q-1)]^{-1} log(2+y)^(1-q)`.
- For `W_beta = 1+x^2 log^beta(2+x)`, the reciprocal energy density is
  asymptotic to `Z_q log(2+x)^(q-beta)/x`.
- If `beta < q+1`, its integral is asymptotic to
  `Z_q log(2+y)^(q-beta+1)/(q-beta+1)`.
- The Hardy product therefore has exponent `(1-q)+(q-beta+1)=2-beta`.
- At `beta=2`, the Hardy product tends to `1/(q-1)^2`.

## Necessity check

For the truncated Hardy potential `h_y`, the weighted energy is exactly
`I_W(y)`, while its squared norm is at least `T_q(y) I_W(y)^2`. Since it is
supported on a half-line of mass `1/2`, its variance is at least half its
squared norm. Hence any full-line weighted Poincare constant is at least
`T_q(y) I_W(y)/2`.

## Sufficiency check

The one-sided Muckenhoupt theorem gives constant at most `4 B_W`. Applying it
on both half-lines after subtracting `f(0)` introduces no additional factor,
because the two half-line energy integrals sum to the full energy.

## Reviewer focus

1. Confirm the smooth-core approximation for the truncated Hardy potentials.
2. Confirm that the eventual little-o comparison forces the Hardy product to
   infinity even when the weight is not regularly varying.
3. Treat the conclusion as order-sharpness; arbitrary oscillatory weights are
   governed by the exact Hardy product rather than by a pointwise minimum.

## Interrupted-lane recovery audit (2026-08-21)

The proof was rederived independently from the one-dimensional Hardy
criterion: the exact tail integral, reciprocal-energy exponent, critical
limit `1/(q-1)^2`, and one-sided necessity tests all check. `main.tex` was
force-rebuilt to a four-page PDF. The log has no LaTeX errors, undefined
references, or overfull boxes. All four pages were rendered at 120 dpi and
visually inspected; no clipping, overlap, malformed formula, or unreadable
source evidence was found.

## Protocol structure QA (2026-08-21)

An explicit expert-facing `Proof intuition` section was inserted between the
source question and the criterion/theorem. The source-question evidence was
regenerated directly from page 12 of `source_paper.pdf` as the focused PNG
`figures/source_question_page12.png`. The packet was force-rebuilt to four
pages; the final log has no LaTeX errors, undefined references, or overfull
boxes. All four final pages were rendered with Poppler at 130 dpi and visually
inspected. The crop, intuition, theorem, proof, margins, and page breaks are
readable and unclipped. SHA-256 of the final `solution_packet.pdf`:
`94d80e8c74598b6c6a431ad2e2b285f5fa8e4bdafd0312d5c77a0cb5c494605e`.
