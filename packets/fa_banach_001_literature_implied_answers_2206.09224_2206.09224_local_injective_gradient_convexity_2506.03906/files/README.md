# Arbitrary-domain Monge--Ampere rigidity with locally injective gradient

Status: `literature_implied_answer (partial subcase)`

Source: Mohammad Reza Pakzad, *Convexity of weakly regular surfaces of
distributional nonnegative intrinsic curvature*, arXiv:2206.09224v2,
Remark 1.6 on PDF page 5.

Supporting theorem: Andre Guerra and Riccardo Tione, *Constancy of the index
for gradient mappings*, arXiv:2506.03906v2, Theorem 5.1 and Corollary 5.2
(Ball) on PDF page 13. The underlying strict-convexity theorem is due to
J. M. Ball (1980).

## Result

Let `Omega` be a connected planar domain, `2/3 < alpha < 1`, and
`v in C^{1,alpha}_loc(Omega)` satisfy

```text
Det D^2 v = f >= 0
```

in distributions. If `grad v` is locally injective at every point, then one
fixed choice of sign makes `v` locally strictly convex throughout `Omega`.
If `Omega` is convex, that signed function is globally strictly convex. Its
Alexandrov Monge--Ampere measure is exactly the Radon measure `mu_f`.

The implication is short but uses two pieces of literature that are not linked
in either paper:

1. Local injectivity makes every point of the graph regular. Pakzad's
   Proposition 3.1 and its degree argument show that every regular point is
   elliptic. By the cited Pogorelov definition, the tangent plane then meets a
   small graph neighborhood only at the base point, so the corresponding
   affine tilt has a strict local minimum or maximum.
2. Ball's theorem, in the precise form restated as Guerra--Tione Corollary
   5.2, says that a locally injective gradient plus one locally supporting
   hyperplane forces strict convexity on a convex domain. Apply it to `v` or
   `-v` on a small ball. Overlapping balls cannot carry opposite signs, so
   connectedness fixes the sign globally.
3. Convex mollification identifies the very weak determinant with the
   Alexandrov measure.

## Scope boundary

This does **not** solve the source problem as stated. The open step is to
derive local discreteness or local injectivity of `grad v` from
`Det D^2 v >= 0` alone. Eight focused attempts did not obtain such a fiber
theorem. The full arbitrary-domain question therefore remains open.

This packet is filed as literature-implied rather than as a new partial proof:
Pakzad's degree/ellipticity theorem and Ball's strict-convexity theorem are
known, while their direct combination for this subcase was identified in the
run. Guerra and Tione do not state that they answer Pakzad's question.

## Files

- `source_paper.pdf`: original/open-problem paper.
- `supporting_paper_2506.03906.pdf`: supporting Ball theorem and critical-group
  constancy theorem.
- `figures/open_problem_crop.png`: Remark 1.6.
- `figures/source_elliptic_point_crop.png`: Pakzad's regular-point conclusion.
- `figures/supporting_ball_corollary_crop.png`: Guerra--Tione Corollary 5.2.
- `main.tex`, `solution_packet.pdf`: formal implication and proof.
- `verification_report.md`: proof-obligation and artifact audit.

Attempt record:
`runs/fa_banach_001/attempts/2206.09224_arbitrary_domain_monge_ampere_upgrade_attempts.md`.

Ledger:
`runs/fa_banach_001/ledger/results/2206.09224_local_injective_gradient_convexity_2506.03906.json`.
