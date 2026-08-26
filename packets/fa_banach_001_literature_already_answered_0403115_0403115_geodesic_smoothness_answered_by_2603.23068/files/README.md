# Geodesic smoothness in `G^m(V)` — negative literature answer

Status:
`literature_answered_negative_in_general_by_2603.23068; low_steps_3_to_8_not_settled_here`

Remark 14 of arXiv:math/0403115 asks whether minimizing
Carnot--Caratheodory geodesics in the free nilpotent groups `G^m(V)` are
smooth for `m>=3`.

Rossi, Schiavoni Piazza, and Socionovo, arXiv:2603.23068v3, Theorem 1.3,
construct a rank-two Carnot group with a minimizing geodesic that is
non-smooth at an interior point.  Since every rank-two step-`s` Carnot group
is a metric quotient of the free group `G^s(R^2)`, lifting their geodesic gives
a non-smooth minimizing geodesic in the free group as well.

For their lowest parameter `b=5`, the constructed group has step 9.  Thus the
blanket smoothness extension beyond step two is false, and counterexamples
transfer to `G^m(R^d)` for every `m>=9`, `d>=2`.

## Files

- `solution_packet.pdf`: source-to-literature implication and scope.
- `source_paper.pdf`: arXiv:math/0403115.
- `supporting_paper_2603.23068.pdf`: resolving paper, v3.
- `figures/source_open_problem_crop.png`: source Remark 14.
- `figures/supporting_theorem_crop.png`: supporting Theorem 1.3.
- `VERIFICATION.md`: theorem, transfer, source, and render checks.

## Scope

The 2026 theorem answers the general all-geodesics-smooth question negatively.
This packet does not claim that steps 3 through 8 are resolved, nor that an
endpoint admitting a non-smooth minimizer admits no smooth minimizer.
