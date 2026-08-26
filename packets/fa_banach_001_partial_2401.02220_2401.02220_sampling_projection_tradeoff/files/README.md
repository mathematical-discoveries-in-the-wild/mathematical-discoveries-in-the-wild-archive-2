# Near-critical sampling-projection tradeoff

Status: `candidate_partial_likely_valid`

Source: David Krieg, Kateryna Pozharska, Mario Ullrich, and Tino Ullrich,
*Sampling projections in the uniform norm*, arXiv:2401.02220v2, open problem
on page 2.

## Result

Let `Pi(n,m)` be the worst-case smallest norm of a sampling projection onto
an `n`-dimensional subspace of `B(D)` using at most `m` values. For
`1 <= k <= n`, the packet proves

```text
max{ n/sqrt(n+k), floor(n/(k+1)) }
    <= Pi(n,n+k)
    <= n+1.
```

For `k >= 2`, it also proves

```text
Pi(n,n+k)
 <= sqrt(n+2) (sqrt(n+k)+sqrt(n+1))/(sqrt(n+k)-sqrt(n+1))
 <= 4(n+k)sqrt(n+2)/(k-1).
```

Consequences:

- `Pi(n,n+1) = Theta(n)`, fully resolving the source problem's endpoint
  `alpha=0`.
- For `0 < alpha < 1` and `k=ceil(n^alpha)`,
  `n^max(1/2,1-alpha) <= Pi <= n^min(1,3/2-alpha)` up to constants.
- The improved upper bound is nontrivial for `alpha>1/2`; the source paper's
  unweighted bound only becomes nontrivial for `alpha>2/3`.

## Mechanisms

The Euclidean lower bound is a trace plus random-phase argument. The
near-critical lower bound uses `k+1` disjoint copies of the zero-sum
hyperplane in `C^(q+1)`: with only `k` extra samples, one block is sampled at
exactly its dimension, forcing norm `q`.

The upper bound adjoins the constant function, uses the source paper's
Kiefer--Wolfowitz design, applies complex weighted BSS sparsification, and
then takes the weighted least-squares projection. The constant function
controls the total sparse weight.

## Files

- `main.tex`: exact problem, intuition, formal proofs, upgrade attempts,
  novelty assessment, and limitations.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source-problem screenshot.
- `code/verify_finite_witnesses.py`: finite consistency checks.
- `VERIFICATION.md`: verification record.

The full exponent curve for `0<alpha<1` remains open. The weighted upper
ingredient is closely implicit in the 2026 Dai--Kosov--Temlyakov survey; the
packet does not present it as a wholly new sparsification theorem. The
block-hyperplane lower bound and one-extra-sample resolution were not found
in bounded searches through 2026-08-11.
