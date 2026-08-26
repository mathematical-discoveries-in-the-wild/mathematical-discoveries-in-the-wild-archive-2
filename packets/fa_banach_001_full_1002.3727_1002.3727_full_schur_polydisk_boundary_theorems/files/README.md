# Full-Schur boundary theorems on every finite polydisk

Result type: `full`

Status: candidate full function-theoretic answer, likely valid pending expert review.

Source paper:

- Jim Agler, John E. McCarthy, and Nicholas J. Young, “A Carathéodory theorem
  for the bidisk via Hilbert space methods,” arXiv:1002.3727; corrected arXiv
  version dated 16 June 2026.
- Open question: final paragraph of the conclusion, PDF page 43.
- Exact text: “Finally, we observe that we do not know whether our results
  extend to functions in the Schur class (rather than the Schur-Agler class)
  of the tridisk.”
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

The packet proves that the source's two principal function-theoretic boundary
theorems extend from the bidisk to the full Schur class on every finite
polydisk, including Schur functions outside the Schur--Agler class.

At every B-point on every boundary face, every inward directional derivative
exists.  Its normalized slope is holomorphic, degree-one homogeneous, and
maps the inward cone to the open left half-plane.  The slope ignores all
coordinates in which the boundary point lies in the open disk.  With one
active coordinate it is exactly linear; with two active coordinates it has
the source theorem's exact Pick-class parametrization.  This strengthens the
2026 higher-dimensional theorem arXiv:2508.13742v2, whose hypothesis remains
Schur--Agler and whose directional statement is restricted to the torus.

The packet also proves, for arbitrary holomorphic functions on every finite
polydisk, that an angular differential implies nontangential convergence of
the ordinary gradient and conversely when the function and gradient have
nontangential limits.  At a Schur B-point, the Julia theorem supplies the
required unimodular function limit.  The same Cauchy argument yields a
higher-order angular-jet theorem.

## Main mechanism

Abate's full-Schur Julia inequality makes the scaled difference quotients a
normal family on the inward cone.  One-variable Julia--Carathéodory theory
gives convergence on a mixed totally-real/complex uniqueness slice, so all
normal-family cluster functions coincide.  On lower-dimensional boundary
faces, Liouville's theorem forces independence of the inactive coordinates.

For angular differentials, scaled polydiscs around a nontangential region
remain nontangential.  Cauchy's estimate differentiates the little-o
remainder.  The converse follows by integrating the gradient along segments
to the boundary point.

## Scope caveat

The source's broad phrase “our results” also encompasses Hilbert-space models,
generalized models, realizations, and operator formulas.  Those cannot extend
verbatim to arbitrary full-Schur functions in dimension at least three:
having an Agler model is equivalent to belonging to the Schur--Agler class.
The packet therefore gives a full answer for the two principal
function-theoretic boundary theorems and an exact obstruction to extending
the model-theoretic statements.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on PDF page 43.
- `verification.md`: proof audit, source checks, and review priorities.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Literature and novelty check

A bounded local/arXiv/web search on 17 August 2026 checked the exact source
sentence, the source title and citations, combinations of “directional
derivative,” “carapoint,” “angular gradient,” “Schur class,” “polydisk,” and
“tridisk,” Abate's arXiv:math/9612202, McCarthy--Pascoe's arXiv:1606.09629,
and the current arXiv:2508.13742v2.  No explicit full-Schur theorem matching
the packet was found.  Because the directional proof synthesizes known Julia
and normal-family mechanisms, novelty confidence is moderate; mathematical
confidence is high pending specialist review.

## Human review focus

Please check:

- the normal-family uniqueness argument on the mixed real/complex slice;
- the Liouville reduction on lower-dimensional faces;
- the endpoint-angle argument yielding the two Pick conditions;
- whether the source's phrase “our results” should be catalogued as the two
  principal function-theoretic theorems plus a negative model obstruction, as
  done here, or under a narrower status label.

