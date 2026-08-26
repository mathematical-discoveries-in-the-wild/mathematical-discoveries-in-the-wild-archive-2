# Verification record

Date: 2026-08-11  
Agent: `agent_lane_12`  
Model: `GPT5.6`

## Mathematical audit

| Check | Status | Detail |
|---|---|---|
| Exact target | pass | Source PDF page 16, Problem 4.5 asks whether every stabilizer of a smooth Banach--Lie action on a Banach manifold is a Lie subgroup. |
| Infinitesimal stabilizer | pass | `h=ker(alpha_p)` is closed; brackets of fundamental fields vanishing at `p` also vanish at `p`. |
| Parametric linearity | pass | The charted fundamental vector field `F(x,y)` is linear in the Lie-algebra parameter `x`. |
| Mixed derivative | pass | `C^2` regularity makes `(x,z) -> D_y F(x,y)z` a continuous bilinear map, uniformly bounded for `y` near `0`; hence the local Lipschitz constant is at most `C||x||`. |
| Orbit containment | pass | Compactness of `[0,1]` and continuity of `(t,x)->exp(tx).p` give one fixed chart neighborhood for all sufficiently small `x`. |
| Grönwall estimate | pass | `||y(t)|| <= t exp(C||x||t)||F(x,0)||`; returning at time 1 gives `||v|| <= C||x||exp(C||x||)||v||`. |
| Flow uniqueness | pass | Once `F(x,0)=0`, the constant curve and the orbit have the same autonomous ODE and initial value, so `exp(Rx)` fixes `p`. |
| Local subgroup criterion | pass | In a local exponential chart, `H cap exp(U)=exp(h cap U)`; since `h` is closed, translated logarithm charts give the Banach--Lie subgroup structure with the subspace topology. |
| Complements/closed range | pass | Neither a complement to `h` nor closed range of the orbit derivative is used. |
| Scope boundary | pass | The proof answers Problem 4.5 only; it does not construct quotient manifolds for arbitrary nonsplit Lie subgroups. |

## Counterexample audit

Weighted coordinate-rotation actions can produce nondiscrete weighted lattice
stabilizers at the level of continuous strong actions, but the unbounded
frequencies destroy joint `C^1` regularity on a Banach neighborhood.  The
proof isolates the exact obstruction: smoothness forces the local Lipschitz
norm of the `x`-fundamental field to be `O(||x||)`, excluding nonconstant
period-one returns for small `x`.

## Literature audit

- Cheap indexes: no existing result or attempt for arXiv:0703710.
- arXiv:0804.4858 / Jotz--Neeb: proper actions have closed orbit tangents,
  yielding the known proper-action subcase.
- arXiv:2010.10165 / Diez--Rudolph (published 2022): explicitly says the
  general stabilizer question is not known even for Banach--Lie actions.
- arXiv:2602.12362 / Glöckner--Neeb, version 2 January 2026: repeats the exact
  problem as an open Banach transformation-group question.
- Bounded searches on 2026-08-11 used the exact question and combinations of
  `stabilizer`, `Banach-Lie subgroup`, `smooth action`, `G/H`, and
  `Problem IX.3.b`; no unrestricted solution was found.

## Artifact checks

- `source_paper.pdf` is a valid 24-page PDF.
- `figures/open_problem_crop.png` was rendered from source PDF page 16 and
  contains the complete Problem 4.5 statement at readable width.
- `main.tex` compiled with all build artifacts under `tmp/`; the final
  4-page PDF has no LaTeX warnings or overfull boxes.
- Every rendered page passed visual inspection after the final compile.
- `solution_packet.pdf` SHA-256:
  `50377a512014554a6499bbea02ef43fab0e2115df3262e1791d01ad10021f868`.
