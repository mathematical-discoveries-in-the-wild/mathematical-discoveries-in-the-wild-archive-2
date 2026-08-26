# Every smooth Banach--Lie action has Lie-subgroup stabilizers

Status: `candidate_full_solution_likely_valid`.

Source: Jinpeng An and Karl-Hermann Neeb, *An implicit function theorem for
Banach spaces and some applications*, arXiv:math/0703710v1 / Math. Z. 262
(2009), 627–643, Problem 4.5 on PDF page 16.

Result: the answer is affirmative.  In fact, `C^2` regularity suffices.  If a
Banach--Lie group `G` acts `C^2` on a Banach manifold `M`, then every point
stabilizer `G_p` is a Banach--Lie subgroup of `G` in the subspace topology.

The proof is a local no-small-period argument.  In a chart at `p`, the orbit
of `exp(tx)` solves an ODE whose vector field is linear in `x`; its Lipschitz
constant is therefore `O(||x||)`.  A sufficiently small such vector field
cannot take `p` around a nonconstant period-one orbit.  Hence any small
`x` for which `exp(x)` fixes `p` already has zero infinitesimal action at
`p`, and then `exp(Rx)` fixes `p`.  Thus local logarithms of the stabilizer
are exactly its closed infinitesimal stabilizer algebra, giving the required
Banach--Lie subgroup chart.

This removes the closed-range hypothesis of the source’s Theorem 4.2.  It
does not settle the separate quotient-manifold direction of Conjecture 4.1.

Novelty check: the exact question is repeated as open in Diez--Rudolph,
arXiv:2010.10165 / *Annals of Global Analysis and Geometry* 61 (2022), and in
Glöckner--Neeb, *Infinite-Dimensional Lie Groups*, arXiv:2602.12362, version
of 2 January 2026.  Bounded searches through 2026-08-11 found the known
proper-action result arXiv:0804.4858, but no unrestricted solution.

Artifacts:

- `solution_packet.pdf`: complete proof and novelty boundary.
- `source_paper.pdf`: the original 24-page paper.
- `figures/open_problem_crop.png`: exact Problem 4.5 statement.
- `verification.md`: mathematical and artifact audit.

