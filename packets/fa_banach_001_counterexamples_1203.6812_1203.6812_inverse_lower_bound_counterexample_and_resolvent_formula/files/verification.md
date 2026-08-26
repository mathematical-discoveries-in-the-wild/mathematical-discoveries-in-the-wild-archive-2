# Verification report

status: counterexample and full formula likely valid

## Proof-critical checks

1. The source explicitly distinguishes Loewner order `\succeq` from its
   notation `>=` for entrywise nonnegativity.  The counterexample therefore
   addresses the printed hypothesis, not a notation accident.
2. `J=(3/2)I+(1/2)11^T` has positive entries, is symmetric diagonally
   dominant, and is entrywise at most `S=I+11^T`.
3. Direct rank-one inversion gives `||J^-1||_infinity=7/9<5/4=
   ||S^-1||_infinity`.
4. The epsilon family is entrywise admissible and diagonally dominant for all
   sufficiently small positive epsilon.  Its inverse norm tends to
   `1/(alpha+m)`, which is strictly below the conjectured value for every
   `n>=3` and `alpha,m>0`.
5. The repaired motivating hypotheses also require an upper bound on each
   diagonal dominance.  The epsilon family violates that extra bound, so the
   packet does not claim to settle the repaired conjecture.
6. The denominator formula is exactly ordinary Cauchy--Binet applied to
   `M=XX^T` with weighted vertex, all-ones, and unsigned-incidence columns.
7. The numerator formula is Cauchy--Binet on each complementary minor in the
   cofactor formula.  Defining `Delta_i=det[e_i,A_F]` incorporates the two
   cofactor signs, including for off-diagonal inverse entries.
8. Restricting either finite sum to subsets containing exactly `k` graph-edge
   columns gives the coefficient of `t^k`; no interpolation or recurrence is
   hidden.

## Mechanical check

Run from the packet directory:

```sh
conda run --no-capture-output -n sandbox python code/verify_resolvent_formula.py
```

The script checks the displayed `3 x 3` counterexample and exhausts every one
of the 74 labelled simple graphs on 2, 3, or 4 vertices, at three positive
values of `t` per graph.  All 222 determinant and inverse comparisons match
at relative and absolute tolerance `2e-10`.  This is a sign/index audit; the
proof is analytic and does not depend on floating-point computation.

## Literature and novelty check

A bounded check through 17 August 2026 searched the run indexes, arXiv/web
results, and citation trails for the source id/title and close variants of
`Conjecture 8.1`, `signless Laplacian inverse entries`, and `exact
combinatorial formula (S+tP)^-1`.  It found Minghua Lin's proof of Conjecture
8.3 (arXiv:1212.1934), known TU-subgraph characteristic-polynomial formulas,
and specialized inverse formulas for trees and odd-unicyclic graphs, but no
exact answer to Conjecture 8.1 or Problem 8.2.  Novelty is only “apparently
new within the bounded search”; the incidence-minor formula is elementary and
may be folklore.

## Recommended human focus

Confirm the literal entrywise reading of `J<=S`, then audit the cofactor row
order in the numerator identity.  These are the only convention-sensitive
points.  Reviewers should keep the printed conjecture separate from the
stronger repaired conjecture with the missing diagonal-dominance cap.

## Packet QA

- `latexmk` completed with no warnings, undefined references, overfull boxes,
  underfull boxes, or errors in the final log.
- All four pages of the final PDF were rendered at 150 dpi and visually
  inspected after the last edit.  The full-width source crop, theorem and
  proof layouts, incidence-minor sums, margins, page transitions, and
  bibliography are clean.
- The verifier returned `PASS` for all 74 graphs and 222 parameterized
  comparisons.
- Final packet SHA-256:
  `af2335a3bd9f5dd357236f919885b1dac658edb72c5b5843006622612d14c7c6`.
