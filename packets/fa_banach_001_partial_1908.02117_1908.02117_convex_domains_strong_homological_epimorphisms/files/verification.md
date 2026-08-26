# Verification report

Verdict: candidate_substantial_partial_likely_valid

Checked on 2026-08-13 by agent_lane_12 / GPT5.6.

## Mathematical audit

- Checked the source definition: a strong homological epimorphism is exactly
  admissibility of the augmented complex obtained by completed balanced base
  change of a projective bimodule resolution.
- Checked the finite free diagonal Koszul resolution of O(C^n) and its signs
  under the coordinates v=z-w.
- Checked the Cartan identity delta d_v+d_v delta=E+k on exterior degree k.
- Checked (E+k)R_k=I for k>=1, E R_0=I-P, and
  R_(k-1) delta=delta R_k, including the exceptional k=1 step.
- Checked the contracting identities delta h_k+h_(k-1)delta=I and
  delta h_0=I-P, together with the diagonal section and augmentation.
- Checked that convexity makes the full radial hull of every compact subset
  remain compact in the difference domain.
- Checked continuity of R_k for k>=1 directly and of R_0 through its
  derivative integral formula; holomorphic differentiation is continuous in
  the compact-open Frechet topology.
- Checked the nuclear kernel identifications and cancellation of both
  balanced A-actions, yielding the holomorphic diagonal Koszul complex on
  U x U.
- Checked that the argument uses only convexity, not boundedness or boundary
  regularity, and specializes to the source's C^2 unit ball.

## Upgrade audit

- Eight distinct routes are recorded in the attempt file. The finite
  resolution, radial homotopy, topological continuity, balanced base change,
  and extension to all convex domains succeeded. The route to all Stein
  domains stops at the nonautomatic continuous splitting of nuclear Frechet
  exact sequences.

## Artifact audit

- LaTeX built successfully in two final passes. The final log has no warning,
  overfull-box, underfull-box, undefined-reference, or fatal-error message.
- All three A4 packet pages were rendered at 150 dpi and visually inspected.
  No clipping, collision, malformed formula, or stranded heading was found.
- Source-paper PDF page 18 was rendered and inspected; it contains Question
  6.1 and the explicit statement that the C^2 unit-ball case was unknown.
- Ghostscript text extraction contains the main theorem, unit-ball
  corollary, all homotopy identities, continuity argument, and conservative
  scope statement.

SHA256:

- solution_packet.pdf:
  9fcc09eb8dfa789d55f49c200f538d8e061dccb5e98b574dda758e60d6e8b0b7
- source_paper.pdf:
  4a67946a343f524325fe300fcfd2e421a895c3b3b99317293eab9576f41117f5
- main.tex:
  304703e70241750927325369866f61773e34da5e68084304b13d611f12511820

## Recommended reviewer focus

Check the equivalence between the base-changed bimodule Koszul resolution and
the source definition of a strong homological epimorphism, and verify the
degree-dependent radial homotopy identities.
