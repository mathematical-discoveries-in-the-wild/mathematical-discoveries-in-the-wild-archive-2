# Counterexample packet: qG-star is not maximal

Status: `candidate_counterexample_likely_valid`

Source: Fernando García-Castaño and M. A. Melguizo Padial,
*On dentability and cones with a large dual*, RACSAM 113 (2019),
2679–2690; arXiv:2401.10102, Problem 1 on printed page 9.

## Result

The answer to the source maximality problem is **no**, even among closed
pointed cones in Banach spaces.

Let `X = c0 ⊕∞ R` and

```text
p(x) = sup_k 2^(-k) |x_k - x_(k+1)|,
C = {(x,t) : t >= p(x)}.
```

The epigraph `C` is a closed pointed cone. Every `(f,a)` in its dual cone
satisfies `sum_k f_k = 0`, so `C* - C*` lies in a proper closed hyperplane of
`X*`; hence `C` is outside `qG*`. On the other hand,
`(e_n,p(e_n))` is a weakly null sequence in `C` with norm one. Therefore zero
lies in the weak closure of every truncated cone `C \ epsilon B_X`, and `C`
cannot have a bounded base. Both sides of the source equivalence are false,
so the equivalence holds for `C`. Adjoining `C` strictly enlarges `qG*`.

## Files

- `main.tex`: self-contained statement, construction, proof, and scope audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: published source paper.
- `figures/source_problem_page9.png`: complete source page containing the
  corollary and maximality problem.
- `verification.md`: proof, source, literature, and visual QA record.

## Human verification focus

Check the dual-cone calculation, especially the use of the partial-sum vectors
`s_N`, and the separation argument showing that a bounded base is incompatible
with the norm-one weakly null sequence.

## Novelty status

On 2026-08-09, the run's cheap indexes, exact/core web searches, the current
arXiv and published records, and later citing papers were checked. No later
resolution or this construction was found. This is a bounded novelty check,
not a certification of priority.

Ledger:
`runs/fa_banach_001/ledger/results/2401.10102_qgstar_maximality_closed_cone_counterexample.json`
