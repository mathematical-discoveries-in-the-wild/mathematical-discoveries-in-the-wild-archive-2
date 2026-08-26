# Exact fractional range for monomial-curve commutators

Status: `candidate_full_solution_likely_valid_human_review_needed`

Source: Tuomas Oikari, *On the L^p-to-L^q boundedness and compactness of
commutators along monomial curves*, arXiv:2304.00621, Question 1.15 (PDF
page 5).

## Result

Let `B = beta_1 + ... + beta_n`. The maximal initial half-open interval of
exponents in Question 1.15 is exactly

`[p,Q_n(p))`,

where

```text
Q_n(p) = (n-1)p/(n-p),                         1 < p <= n(n+1)/(n^2-n+2),
         n(n+1)p/(n(n+1)-2p),     n(n+1)/(n^2-n+2) <= p <= (n+1)/2,
         np/(n-1),                                      p >= (n+1)/2.
```

This is the vertical lower boundary of the sharp single-scale improving
polytope `Omega(n)`. Thus the sufficient range proved in the source is sharp
in every dimension, for every monomial exponent tuple and every allowed sign
pattern.

The paper's literal definition by an unrestricted supremum has a separate
dichotomy:

- if `p >= B/beta_n`, then its literal `p_max` is `Q_n(p)`;
- if `p < B/beta_n`, then its literal `p_max` is infinity, but only because
  `BMO^{beta,alpha}` consists of constants for all sufficiently large `q`.
  The estimate fails on a nonempty interval between `Q_n(p)` and that trivial
  tail, so `[p,infinity)` is not an interval of validity.

No assertion is made at the non-diagonal boundary `q=Q_n(p)`; boundary
inclusion is irrelevant to the requested half-open interval and supremum.

## Proof mechanism

Cladek and Ou proved that the positive single-scale average along the curve is
unbounded for every exponent pair outside `Omega(n)`, using normalized inputs
supported arbitrarily near the origin and dual witnesses supported near a
fixed positive curve arc. Choose a smooth symbol `b(x)=eta(x_n)` which is zero
on the input neighborhood and one on the output neighborhood. On those
supports the commutator pairing is exactly the Hilbert-transform pairing.

When `alpha <= beta_n`, this separator belongs to
`BMO^{beta,alpha}`. Hence every single-scale counterexample becomes a
counterexample to the proposed universal commutator estimate. This supplies
all facets of `Omega(n)`, including the higher-dimensional middle facet that a
simple ball/tube test misses.

When `alpha > beta_n`, anisotropic Holder regularity has ordinary exponent
greater than one on every coordinate line. Segment subdivision forces every
symbol to be constant, producing the literal-supremum degeneracy.

## Files

- `solution_packet.pdf`: full statement, proof, definition audit, and novelty
  check.
- `source_paper.pdf`: arXiv:2304.00621.
- `supporting_1704.07810.pdf`: Cladek--Ou's sharp single-scale obstruction.
- `figures/open_problem_crop.png`: Question 1.15 rendered from source PDF page
  5.
- `verification.md`: adversarial proof audit.
- Attempt log:
  `runs/fa_banach_001/attempts/2304.00621_sharp_commutator_fractional_range.md`.

Human review should focus on the separated-support transfer from Section 4.2
of Cladek--Ou and on the distinction between the maximal initial interval and
the source paper's literal, potentially disconnected supremum.
