# Verification report

Status: passed exact exhaustive checks within the stated finite scope.

## Command

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1207.2456_complete_graph_tight_cosparse_projection_dp/code/verify_complete_graph_projection.py
```

## Independent specification

The reference side enumerates every set partition of the coordinate set. For each partition it computes:

- the exact number of equal-coordinate pairs;
- the exact rational within-block sum of squares;
- the unconstrained block-mean projection;
- the zero-mean branch and its exact `n * mean(z)^2` penalty.

It then constructs the optimum cost at every admissible cosparsity for both the complete-graph incidence operator and the appended-DC tight operator.

The algorithm side independently runs the sorted-interval dynamic program, reconstructs the projected vector from backpointers, and checks its exact squared error and actual zero count.

## Tested scope

- Every vector in `{-1,0,1}^n` for `1 <= n <= 6`.
- Forty deterministic random integer vectors for each of `n=7` and `n=8`.
- Every cosparsity from zero through `binom(n,2)` for the incidence operator.
- Every cosparsity from zero through `binom(n,2)+1` for the tight completion.
- Exact `fractions.Fraction` arithmetic throughout.

Result:

```text
verified vector instances: 1172
verified optimum/projection comparisons: 35318
incidence example ell=4: cost=10, projection=[-1, -1, -1, -1, 5]
tight example ell=5: cost=10, projection=[-1, -1, -1, -1, 5]
all exhaustive comparisons passed
```

## Interpretation

This validates the implementation and probes repeated values, tied interval means, zero global mean, the maximum-cosparsity endpoints, and both tight-frame branches. It is not the proof; the proof is the contiguity lemma, recurrence, and orthogonal DC decomposition in `main.tex`.
