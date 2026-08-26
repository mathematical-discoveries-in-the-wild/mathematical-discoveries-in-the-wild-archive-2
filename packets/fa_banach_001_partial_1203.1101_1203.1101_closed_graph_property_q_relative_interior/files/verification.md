# Verification report

Verdict: `candidate_substantial_partial_likely_valid`

Checked on 2026-08-13 by `agent_lane_12` / GPT5.6.

## Mathematical audit

- Checked the product-neighborhood proof for convex graphs without using
  reflexivity, metrizability, or sequential closure.
- Checked the annihilator saturation identity
  `A(x)+Y^perp=A(x)` directly from maximality.
- Checked maximality of the restriction operator on the closed subspace `Y`
  using Hahn--Banach extension.
- Checked weak-star continuity of restriction and the direction of the image
  inclusion for weak-star closed convex hulls.
- Checked separately that `hat(A)(x)` is empty outside the closed affine hull.
- No claim is made for the general empty-relative-interior, nonconvex-graph
  case.

## Upgrade audit

The attempt file records eight materially distinct routes: direct
maximality/Fitzpatrick covariance, convex graphs, relative-interior
compression, a supremum subdifferential, a polyhedral normal cone, a smooth
compact ellipsoid, asymptotic normal directions, and finite-dimensional
minimax compression. The three counterexample templates were rejected
because their graphs fail the hypothesis, not because of a computational
test.

## Artifact audit

- LaTeX built successfully in two passes. The final log has no warning,
  overfull-box, underfull-box, undefined-reference, or fatal-error message.
- All three A4 packet pages were rendered at 150 dpi and visually inspected.
  No clipping, collision, malformed formula, or stranded heading was found.
- Source-paper pages 20--22 were rendered and inspected; printed page 21
  contains the exact question immediately after Example 5.2.
- Ghostscript text extraction contains the title, both theorem statements,
  the conservative scope qualification, and the bibliography.

SHA256:

- `solution_packet.pdf`:
  `5d0c947773c1e9dea737b4c6086d97c67e8fd769e505ffccbc2583a2bc1ddd38`
- `source_paper.pdf`:
  `4a6608a3ccc514e675831e12024dd73c225479b596d400e1a238583eb6f53bab`
- `main.tex`:
  `e861cc8f7960e78baa9b25ac6a9b3ea27842e170dd46a44b9402fa428268bad0`

## Recommended reviewer focus

Verify the lifting step in Theorem 2: restriction maps a Cesari witness for
`A` to one for `B`, and annihilator saturation then lifts membership back to
`A(x)`. Also assess whether the relative-interior extension is already
implicit in a known restriction theorem; the bounded novelty search did not
locate this exact formulation.
