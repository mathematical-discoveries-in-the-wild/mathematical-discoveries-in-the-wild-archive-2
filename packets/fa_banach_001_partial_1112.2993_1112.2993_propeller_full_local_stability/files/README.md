# Full local stability of the Gaussian propeller

Run: `fa_banach_001`

Source: arXiv:1112.2993, Steven Heilman, Aukosh Jagannath, and Assaf
Naor, *Solution of the propeller conjecture in R^3*.

Status: `candidate_partial_result_likely_valid_needs_human_review`

## Source question

The source proves the Propeller Conjecture in dimension three and, on page 7,
identifies a proof extending to all dimensions as the next natural step. In the
equivalent Gaussian-width formulation, the conjecture asks whether every
centered finite coefficient list satisfies

    (E max_i <G,v_i>)^2 / sum_i ||v_i||^2 <= 9/(8*pi).

## New partial result

For every fixed number of coefficients, the planar three-blade propeller is a
locally rigid global optimizer against **all** sufficiently small perturbations
in arbitrary ambient dimension. This includes simultaneous deformation of the
three active blades, arbitrary longitudinal/transverse mixtures, and any fixed
finite collection of new vertices. Equality nearby occurs only for an
equilateral active triangle with all extra centered vertices equal to zero.

The packet also gives an explicit sufficient inequality certifying a general
configuration consisting of any centered nondegenerate triangle plus a small
arbitrary residual cloud.

## Proof mechanism

Translate by the mean of the three active vertices. The list becomes a
centered triangle plus residual vertices, and the centered denominator is
exactly

    S + eta^2 - (1/k)||sum_j y_j||^2,

whose residual term is at least `(3/k) eta^2`. The triangle support function
dominates a fixed multiple of the planar Gaussian radius. A residual vertex
can therefore win only when that radius is small; the two-dimensional
small-ball probability makes its expected gain `O(eta^3)`. The quadratic
denominator cost beats this cubic gain.

For the active triangle itself, Cauchy's perimeter formula and
`(a+b+c)^2 <= 3(a^2+b^2+c^2)` give the sharp constant `9/(8*pi)`, with
equality only for an equilateral triangle.

## Scope

This is a strict upgrade over the earlier run packet
`0807.4626_propeller_transverse_local_stability`, which allowed only a fixed
purely orthogonal residual cloud and did not allow the active triangle to
vary. It does **not** prove the global higher-dimensional Propeller Conjecture;
configurations far from the three-blade optimizer remain uncontrolled.

Human review should focus on the exact centered-denominator identity and the
conditional two-dimensional small-ball estimate in the residual-gain lemma.
The proof has no computational dependency.

Ledger:
`runs/fa_banach_001/ledger/results/1112.2993_propeller_full_local_stability.json`

