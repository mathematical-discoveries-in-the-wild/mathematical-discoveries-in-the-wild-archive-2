# Namioka--Phelps spaces satisfy the nonlinear dual fixed-point theorem

Status: `candidate full solution likely valid; human review recommended`

Source: Andrzej Wiśnicki, *Around the nonlinear Ryll--Nardzewski theorem*,
arXiv:1903.12123v2, Question 1 on page 10 (Corollary 3.2 in the published
numbering).

## Result

Question 1 has an affirmative answer.  Let `V` be a Hausdorff locally convex
Namioka--Phelps space, let `V*` carry its weak-star topology and its standard
uniformity `xi*` of uniform convergence on bounded subsets of `V`, and let
`Q` be an equicontinuous weak-star compact convex subset of `V*`.  Every
weak-star continuous semigroup action on `Q` which is `xi*`-nonexpansive and
`xi*`-distal has a common fixed point.

This is the exact locally convex nonlinear analogue of the source's Asplund
Corollary 3.2 under the conventions for Namioka--Phelps spaces and the dual
system fixed-point property in Glasner--Megrelishvili.

## Proof mechanism

Namioka--Phelps fragmentation first lifts `xi*`-distality of a minimal compact
subsystem to weak-star distality, which supplies an invariant Radon probability
measure.  For each bounded set `B` in `V` and each scale, fragmentation gives
a positive-measure set of small `p_B`-diameter.  Nonexpansivity transports it
to equal-mass neighborhoods of every orbit point, so a packing argument makes
the orbit totally bounded for every seminorm `p_B`.  The weak-star compact,
equicontinuous set is complete for `xi*`; hence the minimal subsystem is
`xi*`-compact.  The locally convex DeMarr normal-structure argument then
shrinks the minimal invariant convex set unless the subsystem is a singleton.

## Scope

The packet answers Question 1 only.  It does not claim a resolution of the
broader Question 2 asking for nonlinear counterparts of both Theorems 1.5 and
1.6 of Glasner--Megrelishvili.  Equicontinuity of `Q` is part of the standard
locally convex dual formulation; it is automatic for weak-star compact sets
when `V` is barrelled.

## Files

- `main.tex` and `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: arXiv:1903.12123v2.
- `supporting_paper_1007.5303.pdf`: Glasner--Megrelishvili definitions and
  affine dual fixed-point theorem.
- `figures/open_problem_crop.png`: source Question 1 and Question 2.
- `VERIFICATION.md`: mathematical and rendering checks.

Human review should focus on the strong-dual completeness lemma and on the
entourage form of the packing argument.  Both are proved explicitly rather
than assumed.

