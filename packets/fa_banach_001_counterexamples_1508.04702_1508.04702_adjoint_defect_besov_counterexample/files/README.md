# A counterexample to the Besov adjoint-defect problem

Run: `fa_banach_001`

Agent: `agent_lane_14`

Status: `candidate_counterexample_likely_valid`

## Result

Problem 2 of Aleksandrov--Peller (arXiv:1508.04702, PDF pages 18--19)
asks whether every real-valued
`phi in B^1_{infinity,1}(R^2)` satisfies

```text
phi(A,B)^* - phi(A,B) in S_1
```

for all bounded self-adjoint `A,B` with `[A,B] in S_1`, where `phi(A,B)` is
their ordered double-operator-integral calculus.  The packet gives an explicit
negative answer.

On the `k`-th scale, a rotated `2 x 2` block has commutator trace norm
`h_k^2`, but a localized real Besov atom makes the adjoint defect have trace
norm `h_k/k^2`.  Repeating that block `k 2^k` times with
`h_k=2^(-k-4)` makes the total commutator norm equal `1/128`, while the defect
norm is `(1/16) sum 1/k = infinity`.

## Scope

This fully answers Problem 2 negatively.  It does not settle the independent
almost-multiplicativity Problem 1 in the same section.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1508.04702_adjoint_defect_besov_counterexample/code/verify_blocks.py
```

The checker verifies the exact `2 x 2` adjoint-defect identity on 1,000 random
tables and the convergent/divergent partial-sum formulas.

## Files

- `main.tex`: theorem, construction, and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:1508.04702.
- `figures/open_problem_crop.png`: source Problem 2 excerpt.
- `code/verify_blocks.py`: independent finite-block regression check.
- `code/crop_open_problem.py`: reproducible source-excerpt crop.

## Review recommendation

Prioritize the dyadic scaling estimate proving `phi in B^1_{infinity,1}` and
the sign/order in the four-corner double-operator-integral identity.  Both are
spelled out in the packet; the latter is also regression-tested.

