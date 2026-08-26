# Partial result: near-linear Euclidean interval selections

Status: candidate partial result, likely valid, subject to human review.

Source: Pavel Shvartsman, arXiv:2503.19094, *Efficient Algorithms for
Lipschitz Selections of Set-Valued Mappings in R^2*, Remark 1.4 on physical
PDF page 4.

## Result

Remark 1.4 asks whether the source's quadratic Projection Algorithm can be
replaced, for an `N`-point subset of fixed-dimensional Euclidean space, by an
algorithm with `O(N log N)` operations and `O(N)` storage. It says the answer
is unclear even when the values are closed intervals in `R`.

The packet gives a full affirmative answer to that explicitly singled-out
interval case. For any fixed ambient dimension `n` and fixed `epsilon>0`, the
algorithm either:

- certifies correctly that no `lambda`-Lipschitz interval selection exists; or
- returns a selection with Lipschitz constant at most
  `(1+epsilon) lambda`.

It uses `O_{n,epsilon}(N log N)` work and `O_{n,epsilon}(N)` storage.

The mechanism is simple and exact. Build a linear-size
`(1+epsilon)`-Euclidean spanner with shortest-path metric `d_G`, and compute

```text
u(x) = min_y (b_y + lambda d_G(x,y))
```

by one multi-source shortest-path pass. Since Euclidean distance is at most
`d_G`, failure is a sound no-go certificate. Since `d_G` is at most
`(1+epsilon)` times Euclidean distance, success has the promised factor.

The theorem allows rays and the whole line. It also extends coordinatewise to
fixed-dimensional axis-aligned boxes in the `ell_infinity` norm. If the domain
is itself a subset of `R`, the sorted path is an exact stretch-one spanner, so
the returned selection is `lambda`-Lipschitz.

## Scope

This is a partial result for the source's broader problem. It does not provide
the requested near-linear algorithm for arbitrary half-planes or polygons in
`R^2`. Spanner edges reduce that case to a sparse linear feasibility system,
but a near-linear exact solver for the resulting varying-normal constraints is
not supplied.

Eight materially different upgrade attempts are recorded in
`../../../attempts/2503.19094_euclidean_interval_spanner_upgrade_attempts.md`.
Bounded searches of arXiv and primary publication pages found no later answer
to the interval subproblem or this spanner reduction.

## Files

- `main.tex`: exact source transcription, proof intuition, theorem, proof,
  corollaries, verification, references, and limitations.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source paper compiled from the stored arXiv source.
- `figures/open_problem_crop.png`: complete rendered Remark 1.4.
- `code/verify_spanner_interval_selection.py`: 1,200-case finite regression
  check.
- `VERIFIER_REPORT.md`: adversarial proof audit.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2503.19094_near_linear_euclidean_interval_selections/code/verify_spanner_interval_selection.py
```

The script prints `VERDICT: PASS`. It checks the theorem's implications, not
the standard external complexity theorem for constructing Euclidean spanners.

## Human review

Check the direction of the two spanner inequalities in the no-go and success
branches, and verify that the cited fixed-dimensional Euclidean spanner
construction matches the source's real-RAM model. The scalar selection proof
and shortest-path computation are otherwise elementary.
