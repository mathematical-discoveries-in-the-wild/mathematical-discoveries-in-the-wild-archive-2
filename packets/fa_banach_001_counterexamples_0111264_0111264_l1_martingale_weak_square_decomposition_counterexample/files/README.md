# Problem 6.6 fails for bounded L1 martingales

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source: Randrianantoanina, arXiv:math/0111264, Problem 6.6 on source PDF
page 29.

## Result

The literal statement of Problem 6.6 is false, already for an abelian finite
von Neumann algebra.  On a probability space split into blocks `A_k` of mass
`2^{-k}`, put a depth-`k` dyadic spike of total mass `a_k=1/k^2` in block
`A_k`.  The positive martingale of conditional expectations has constant
`L1` norm `sum_k a_k<infinity`.

At every one of the `k` local splitting levels in `A_k`, the last martingale
difference alone contributes at least `a_k/2` to the integral of the square
function.  Hence

```text
integral S(x) >= (1/2) sum_k k a_k
              = (1/2) sum_k 1/k
              = infinity.
```

In an abelian algebra, column and row square functions coincide with the
ordinary square function.  If a decomposition required by Problem 6.6
existed with `y in H1_C` and `z in H1_R`, pointwise Minkowski would give
`S(x)<=S(y)+S(z)` and therefore `x in H1`, contradicting the calculation.
The admissible set in the problem's infimum is empty, so no universal
constant can exist.

## Scope

Later weak-square-function results for `L2` martingales give important dense
subcases, but they do not repair the universal quantifier over all bounded
`L1` martingales together with the strong Hardy-membership conditions printed
in Problem 6.6.  The counterexample targets that literal formulation.

## Files

- `main.tex`: complete counterexample proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/problem_6_6_crop.png`: actual crop of Problem 6.6.
- `code/crop_problem.py`: reproducible crop script.
- `code/verify_lower_bound.py`: finite-truncation arithmetic check.
- `verification_report.md`: source, proof, computation, build, and visual QA.

