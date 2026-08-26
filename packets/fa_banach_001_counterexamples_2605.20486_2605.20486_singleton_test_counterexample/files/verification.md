# Verification record

Status: `candidate_counterexample_likely_valid`

## Source and target

- Source: arXiv:2605.20486v1, submitted 2026-05-19.
- Exact target: printed page 25, Question 1.
- Source evidence: `figures/open_problem_crop.png`.
- Cheap-index duplicate check: no hit for this arXiv id or exact singleton test.
- Bounded primary arXiv search on 2026-08-11: source v1 only; no later answer
  or close counterexample located.

## Independent proof audit

1. **Compactness.** Any sequence within one branch has a convergent
   subsequence. If branch indices tend to infinity, dogleg points converge to
   the root and tail points converge, after selecting their first coordinates,
   to the straight limit arc.
2. **Intrinsic metric.** Distinct finite branches lie in distinct half-planes
   through the first coordinate axis. A fixed finite branch minus the root is
   locally isolated from every other branch; a continuous path leaving it must
   pass through the root. Hence intrinsic distance is the arclength tree
   metric used in the proof.
3. **Finite-branch singleton slopes.** Locally, singleton distance is affine
   with coefficient `+1` or `-1` in arclength. Each incident polygonal piece is
   straight, including the one descent direction at a vertex, so the Euclidean
   descent quotient is at most and attains one.
4. **Root singleton slopes.** For a fixed target, only its own branch (or the
   straight limit branch) decreases distance near the root. All rotating
   branches increase it. The fixed descent segment is straight.
5. **Limit-branch singleton slopes.** A tail point `(r, eps_n^2 v_n)` has
   intrinsic depth `r+c_n`, where `c_n>0`. Thus every cross-branch positive
   descent numerator is bounded above by `(t-r)_+`, while the Euclidean
   denominator is at least `|t-r|`. A straight limit-branch direction attains
   one.
6. **Closed-set failure.** Finite endpoint depth is `L_n>1`, whereas the limit
   endpoint has depth one. At the post-dogleg point `y_n`, the nearest endpoint
   is its own branch endpoint at distance `1-2 eps_n`. The resulting descent
   quotient tends to two.

## Computational check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2605.20486_singleton_test_counterexample/code/check_parameters.py
```

The script checks the first 40 branches in double precision, including dogleg excess, total branch
length, the closed-set descent quotient, and representative cross-branch
upper bounds. The proof is analytic and does not depend on this finite check.

Observed output on 2026-08-11:

```text
checked branches: 40
minimum sampled dogleg excess: 2.6837821849277146e-14
last closed-set descent quotient: 2
all checks passed
```

`latexmk` compiled the packet without undefined references, overfull boxes, or
LaTeX warnings in the final pass. All five rendered pages were inspected at
150 dpi; no clipping, overlap, broken glyphs, or illegible evidence was found.

## Human-review focus

- Confirm that relative local isolation of every fixed finite branch is enough
  to force any path leaving it through the root.
- Confirm the two cases in the limit-branch slope estimate, especially when
  the fixed target also lies on the limit branch.
- Confirm use of the source characterization: one closed countable set with
  slope unequal to one proves the space is not eikonal.
