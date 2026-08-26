# Full solution packet: nonseparable strong-random fixed points

## Source

- Plern Saipara, Poom Kumam, and Yeol Je Cho, *Random fixed point
  theorems for Hardy–Rogers self-random operators with applications to random
  integral equations*, arXiv:1706.01634v1 (2017), *Stochastics* 90 (2018),
  297–311.
- Open problem: printed page 12, after the application theorem: “Can Theorems
  1.3 and 3.2 be generalized to non-separable Banach spaces?”

## Classification

- Status: `candidate_full_solution_likely_valid`.
- Result: affirmative extension of both named theorems to every real Banach
  space under the canonical nonseparable strong-random formulation.
- Formulation: random variables and constant operator sections are strongly
  (Bochner) measurable. This agrees with the source's convention in separable
  Banach spaces.

## Result

Let `X` be an arbitrary real Banach space and let
`T: Ω × X → X` have strongly measurable constant sections and almost surely
continuous fibers. If either the source's Greguš–Ćirić inequality or its
five-term Hardy–Rogers inequality holds almost surely for every pair of strong
random variables (with the source coefficient restrictions), then `T` has a
unique strong random fixed point.

## Proof idea

Close the zero random variable under the random operator and rational linear
combinations. This gives countably many strong random variables `(d_k)`. For
each outcome their closed span is a separable invariant Banach subspace, and a
countable intersection synchronizes all null sets there. The applicable
deterministic theorem supplies a fiberwise fixed point.

To prove that fixed point is strongly measurable, select the first `d_k` whose
residual is below `1/n`. These are strong random variables. Explicit estimates
bound distance to the fixed point by a finite fiberwise constant times the
residual, so the selected sequence converges almost surely to the fixed point.
This avoids raw Picard iteration, which can fail for the Greguš–Ćirić class
(`T=-I` is the basic example).

## Exact scope

The packet does not claim that bare Borel-measurable sections are sufficient
in every nonseparable codomain. Strong measurability is the stable and standard
nonseparable replacement; it is no additional restriction in the separable
setting. The result therefore gives a full affirmative generalization in that
canonical formulation.

## Verification and novelty

- The formal proof separately checks strong composition, the random invariant
  hull, synchronization of null sets, deterministic fiberwise existence,
  measurable residual minimizers, two residual error bounds, and uniqueness.
- `code/verify_residual_bounds.py` ran 100,000 reproducible scalar stress tests
  for each residual estimate and returned `PASS`. This is only a sanity check;
  the packet proves the estimates symbolically.
- Bounded searches on 2026-08-11 used the exact source question/title and the
  combinations `Hardy-Rogers`, `nonseparable`, `strongly measurable`, `strong
  random operator`, `random fixed point`, and `countable invariant subspace`.
  Guo–Zhang–Wang–Yuan (2020, arXiv:1904.03607) gives a nonseparable strong
  random **nonexpansive** theorem on weakly compact convex sets with normal
  structure, but does not cover this whole-space result. No exact answer or
  this construction was located. Novelty confidence is bounded, not
  exhaustive.

## Human review

Prioritize the countable-invariant-hull argument, use of the deterministic
Greguš–Ćirić theorem on the random subspace, both residual bounds, and whether
the strong-random formulation is accepted as the intended nonseparable reading
of the source question.

## Files

- `main.tex`: self-contained expert-facing packet.
- `solution_packet.pdf`: compiled and visually inspected packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of the page-12 question.
- `code/verify_residual_bounds.py`: deterministic scalar sanity check.
- `verification_report.md`: commands, hashes, and review notes.

