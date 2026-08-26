# Separability Splits Length from Geodesic Structure

Status: `candidate_partial_likely_valid`

Source: Guillaume Sérieys, *Nonlinear Lebesgue spaces: Curves and geometry*,
arXiv:2603.09459 (2026), Remarks 4.5–4.6 on arXiv PDF page 31.

The source asks whether completeness and separability of the target metric
space can be relaxed in its theorem transferring length/geodesic structure to
nonlinear Lebesgue spaces.

This packet proves two complementary results:

1. If the target N is a complete length space, global separability is
   unnecessary: every two admissible maps, together with the base map, take
   values in a closed separable complete length subspace obtained by a
   countable approximate-midpoint construction.
2. For every p in (1,infinity], separability cannot generally be removed from
   the geodesic conclusion. An uncountable ladder has two separable rails and
   uncountably many isolated rung midpoints. Endpoint maps range in the rails,
   but strict convexity forces any function-space midpoint to range through all
   rung midpoints, contradicting the definition's separably-valued condition.

The completeness-relaxation question remains open. At p=1 the ladder example
does admit a geodesic by switching endpoint values on a growing measurable set.

Review recommendation: verify the closed separable length-hull lemma and the
completeness of the uncountable metric graph first; the Lp midpoint obstruction
is then short.

Files:

- `source_paper.pdf`: arXiv source.
- `figures/open_problem_crop.png`: Remarks 4.5–4.6.
- `main.tex`, `solution_packet.pdf`: proof packet.
- `verification_report.md`: proof and rendering checklist.
