# Full result packet: the pseudomode exponent `1/7` is not optimal

status: `candidate_full_solution_likely_valid`

source_arxiv: `2410.01377`

source_result: Theorem 1.5, Lemma 3.9, recursion (3.13), and the explicit
optimality question on source PDF page 4 in Krejčiřík--Nguyen Duc--Raymond,
*The Laplacian with Complex Magnetic Fields*.

scope: full negative answer to whether the displayed power `1/7` is optimal;
the packet proves the stronger universal power `1/4` under exactly the source
hypotheses.  It does not claim that `1/4` is sharp.

## Result

Under the assumptions of source Theorem 1.5, the same WKB phase and transport
amplitudes produce compactly supported pseudomodes satisfying

```
||(L_{h,A} - h B(x0)) u_h|| <= exp(-C/h^(1/4)) ||u_h||.
```

Thus the source's `exp(-C/h^(1/7))` estimate is not optimal.

## Mechanism

The source recursion differentiates the preceding analytic amplitude only in
the three multi-orders

```
(1,2), (2,2), (1,3),
```

whose total orders are `3,4,4`.  Its proof uses Cauchy contours centered at the
origin and then combines the largest separate denominator losses, producing a
factor `j^7` at every recursion step.  On the same nested polydiscs, take
Cauchy circles centered at each actual evaluation point.  Every point on the
two recursion paths stays in the next smaller polydisc, so it has coordinate
margins exactly comparable to `1/j`.  Local Cauchy therefore costs only
`j^(alpha+beta)`, at worst `j^4`.

The resulting transport estimate is

```
|a_j| + |grad a_j| + |Delta a_j| <= M^(j+1) j^(4j)
```

on a fixed real neighborhood.  Truncating at
`N(h)=floor((e M h)^(-1/4))` makes the final transport term at most `e^(-N)`;
the cutoff commutator remains `e^(-c/h)`.  Gaussian normalization costs only a
polynomial factor, absorbed into `exp(-C/h^(1/4))`.

## Evidence

- `source_paper.pdf`: exact current arXiv PDF, corresponding to the 2026 SIAM
  publication.
- `figures/open_question_crop.png`: source PDF page 4 with the exact question.
- `main.tex`: self-contained centered-Cauchy lemma, nested-polydisc induction,
  WKB truncation, and normalization proof.
- `code/verify_exponent_bookkeeping.py`: deterministic derivative-order and
  optimal-truncation bookkeeping checks.
- `VERIFICATION.md`: hypothesis, path-geometry, complex-analysis, WKB,
  literature, build, and visual audit.
- `solution_packet.pdf`: compiled review packet.

## Novelty audit

A bounded search on 11 August 2026 covered the run indexes and local
full-source corpus; the exact arXiv id/title and `h^(1/7)` wording; close
official arXiv searches for complex-magnetic pseudomodes, exponent `1/4`,
optimal WKB truncation, and local Cauchy estimates; the September 2025 arXiv
revision; and the January 2026 SIAM publication record (DOI
`10.1137/24M1703628`).  No prior improvement of this exponent or matching
centered-Cauchy argument was found.  Novelty confidence is medium and
mathematical-validity confidence is high pending expert review.

## Human review recommendation

Check that every interpolation/evaluation point in recursion (3.13) lies in
the next smaller polydisc, that the three displayed derivative multi-orders
are exhaustive, and that the source's analytic prefactors have one common
bounded neighborhood.  Then check the `j^4` induction and the final relative
`L2` normalization.

