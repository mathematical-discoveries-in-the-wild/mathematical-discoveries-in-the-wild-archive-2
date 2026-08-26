# Exact variation formula on finite convex polygons

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `candidate_full_solution_likely_valid_human_review_needed`

## Source question

After Theorem 2.25 of Doust--Leinert--Stoneham,
*The Banach algebras AC(sigma) and BV(sigma)*, arXiv:2206.00986, the authors
ask whether their lower bound (2.1) is always exact when `sigma` has more than
three convex-polygon vertices.

## Full affirmative answer

If `z_1,...,z_m` are the vertices in cyclic order and `f:sigma->C`, then

```text
var(f,sigma) = (1/2) sum_{i=1}^m |f(z_i)-f(z_{i+1})|,
z_{m+1}=z_1.
```

For real-valued functions, layer cake writes every list variation as an
integral of level-set transition counts. A level set has `k` cyclic runs, and
each run can be strictly separated from the other vertices by one line, so
its transitions are bounded by the list's variation factor. This proves the
upper bound. The Cauchy projection identity averages this real result over all
directions and gives the complex-valued theorem. The source already supplies
the matching lower bound.

The result also yields the exact finite formula

```text
||f||_BV = max_i |f(z_i)|
           + (1/2) sum_{i=1}^m |f(z_i)-f(z_{i+1})|.
```

## Files

- `main.tex`: complete expert-facing proof packet.
- `solution_packet.pdf`: rendered packet for review.
- `source_paper.pdf`: local copy of arXiv:2206.00986.
- `figures/open_problem_context.png`: Theorem 2.24 and source bound (2.1), PDF page 15.
- `figures/open_problem_crop.png`: exact open question, PDF page 16.
- `code/verify_cyclic_cut.py`: deterministic combinatorial stress tests.
- `verification.md`: proof and computation audit.
- `novelty_search.md`: bounded novelty-search record.
