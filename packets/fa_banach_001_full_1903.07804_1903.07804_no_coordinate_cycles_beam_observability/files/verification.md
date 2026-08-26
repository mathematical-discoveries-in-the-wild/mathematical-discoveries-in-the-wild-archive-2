# Verification report

## Claim checked

For every two distinct `a,b` outside the integers, every `T>0`, and arbitrary
observation base points, the inverse inequality (4.8) for the periodic beam
equation holds. This answers Open Question (iv) of arXiv:1903.07804 and
strengthens its rational parameter range to all real non-integer parameters.

## Mathematical audit

1. A nonzero lattice point `(x,y)` on `S_a` uniquely determines
   `a=(x^2+y^2)/(x-y)`. Hence the lattice point sets for distinct parameters
   are disjoint.
2. For non-integral `a`, two distinct points of `S_a` cannot share their
   second coordinate, because their first coordinates would be the two roots
   of a monic quadratic with sum `a`. The first-coordinate version gives root
   sum `-a`. This proves the coordinate injectivity needed to alternate both
   labels and edge directions around a cycle.
3. A cycle can therefore be labeled cyclically by
   `A_i=(x_i,y_i) in S_a` and `B_i=(x_{i+1},y_i) in S_b`.
4. Subtracting the equations of `A_i` and `B_i` and summing telescopes the
   square terms. What remains is
   `(a-b)(sum x_i-sum y_i)=0`, hence the coordinate sums agree.
5. Summing the `S_a` equations now gives
   `sum (x_i^2+y_i^2)=a(sum x_i-sum y_i)=0`. All coordinates would be zero,
   contradicting that the origin is excluded. No cycle exists.
6. The phase-weighted collision terms in the two observation estimates cause
   no hidden issue. When the collision graph is a finite forest, each path
   endpoint is controlled by a non-collision square term; a zero quadratic
   form propagates zero along the path regardless of its unimodular edge
   phases. Finite-dimensional injectivity gives coercivity.
7. If either parameter is irrational, its lattice-point set is empty and the
   source's one-observation theorem already gives the inequality. Thus the
   strengthening from rational to real non-integer parameters is valid.

## Computational audit

`code/cycle_search.py` independently enumerates lattice circles and tests all
candidate parameter pairs for cycles. The command

`conda run --no-capture-output -n sandbox python code/cycle_search.py --box 150`

reported no cycle among 21,178 non-integral parameter classes and 3,044 pairs
with at least four coordinate-sharing edges. The test is complete for
`|a|,|b|<=120`, since every coordinate on `S_a` has absolute value at most
`(1/2+1/sqrt(2))|a|<1.21|a|`. This is a regression check, not part of the
proof.

## Source-text audit

The arXiv source prints “integers” in Lemma 4.7 and Theorem 4.8. That word is
inconsistent with the lemma's own proof (which derives integrality as a
contradiction), the non-integral rational example immediately following the
theorem, and Open Question (iv). The packet states and proves the intended
non-integer graph reduction self-containedly. Human review should confirm
this editorial interpretation against the journal version.

## Literature and novelty audit

Bounded searches on 13 August 2026 used the exact title, arXiv:1903.07804,
the exact text of Open Question (iv), `G(a_1,a_2)`, coordinate cycles, moving
beam observations, and inverse inequality (4.8). The current arXiv version
still contains the open question. No later explicit answer or matching
telescoping argument was found. Novelty confidence is moderate.

## PDF audit

The final four-page packet was compiled to convergence with `latexmk` and
contains no unresolved references, warnings, overfull or underfull boxes, or
reported errors. It was rendered at 144 dpi, and every page was visually
inspected after the final mathematical edit.

## Human-review focus

Check the alternating cycle labeling, the two telescoping sums, the
phase-weighted forest-to-coercivity reduction, and the source's apparent
integer/non-integer typographical error.
