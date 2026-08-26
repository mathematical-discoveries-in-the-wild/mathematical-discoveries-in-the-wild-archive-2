# Verification report

Verdict: `candidate_substantial_partial_likely_valid`

Checked on 2026-08-13 by `agent_lane_12` / GPT5.6.

## Mathematical audit

- Checked that coordinate extraction is contractive from the Hilbert-weighted
  space to every scalar weighted coordinate space.
- Checked the necessity of uniform weighted-coordinate tails: continuous
  Hilbert-valued ranges are compact, their coordinate projections converge
  uniformly, and coordinatewise multiplication satisfies
  `||xy||_2 <= ||x||_2 ||y||_2`.
- Checked sufficiency by truncating the uniformly small tail and approximating
  finitely many coordinates with scalar continuous functions.
- Checked that essential boundedness of the Hilbert-valued weight converts
  unweighted vector-polynomial approximation into weighted approximation.
- Checked the disjoint-bump counterexample for `w_j=2^(-j)`: it is strongly
  measurable, Hilbert-valued pointwise, has weighted norm one, and each
  coordinate is continuous. Weighted distance below `1/2` would force a
  continuous approximant to have unbounded norm.
- Checked the primitive lifting identity
  `f-[f(a)+Vq]=V(f'-q)` for Bochner absolutely continuous representatives.
- Checked the one-sided weight comparison using Minkowski's integral
  inequality, with primitive norm at most `C(b-a)`.
- Checked the constant-weight corollary: `D_alpha` has dense range when every
  `alpha_j>0`, and boundedness of `D_alpha` commutes with Bochner
  differentiation.
- Checked the degeneracy example `G=R^2`, `w=(1,0)`, which makes the source's
  displayed quantity a seminorm and destroys representative-independent
  derivative membership.

## Upgrade audit

- Eight distinct routes are recorded in the attempt file. They include the
  exact source localization, same-author foundation, well-posedness audit,
  corrected uniform-tail theorem, counterexample, primitive reduction,
  explicit weight condition, and the stopped arbitrary-weight program.

## Artifact audit

- LaTeX built successfully in two final passes. The final log has no warning,
  overfull-box, underfull-box, undefined-reference, or fatal-error message.
- All three A4 packet pages were rendered at 150 dpi and visually inspected.
  No clipping, collision, malformed formula, or stranded heading was found.
- Source-paper PDF page 14 (printed page 244) was rendered and inspected; it
  contains Definition 3.1 and both exact “Interesting problems.”
- Ghostscript text extraction contains the uniform-tail theorem, primitive
  criterion, constant-weight answer, conservative scope statement, and both
  references.

SHA256:

- `solution_packet.pdf`:
  `2680d21d92b11568d36867b0de75767ea99743447c191d6261e010b9b745f89e`
- `source_paper.pdf`:
  `f67ed3d4c0c80d97b4d4bb6f0f7cc426f8b0d78339b36c60046e32af5ffaca3b`
- `main.tex`:
  `e30c6ff2f7ba02efca227ba9e59cc91d39a19022dae47395028523b5b5fb026f`

## Recommended reviewer focus

Check the necessity and sufficiency of the uniform weighted-tail condition,
the representative conventions in the corrected Sobolev space, and whether
the companion paper's infinite-dimensional theorem has a later correction.
