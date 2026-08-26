# Verification report

Verdict: likely valid candidate full negative answer, pending expert review.

## Proof audit

1. **Quantifiers and block recursion.** For an arbitrary fixed `f:N->N`, each
   boundary `N_(k+2)` is chosen after taking a maximum over the finite set
   `1 <= n < N_(k+1)`. Thus the recursion is legitimate for every finite-valued
   `f`, without monotonicity assumptions.
2. **Window locality.** If `n` is in block `B_k`, then `n < N_(k+1)`, hence
   `f(n) < N_(k+2)`. An allowed `m` satisfies `m >= n` and `m < N_(k+2)`, so it
   belongs to `B_k` or `B_(k+1)` and no later block.
3. **Same-block case.** The two vectors have identical directions. Since
   `n+m >= n`, its slack is no larger than the common block slack, giving
   `r_(n+m) <= r_n+r_m` directly.
4. **Adjacent-block radial budget.** The slack drop is exactly
   `2c^2/k^2`. Since `n+m` lies no earlier than the second block,
   `D=r_n+r_m-r_(n+m) >= 2c^2 n/k^2`. Multiplying by
   `r_n+r_m+r_(n+m) >= m` yields the budget `2c^2 nm/k^2`.
5. **Angular loss.** The angle is exactly `c/k` and
   `2(1-cos x) <= x^2`. With `c=1/4`, the maximal slack is
   `s_1=pi^2/48`, so `(1+s_1)^2<2`. The angular loss is therefore strictly
   below the radial budget.
6. **Nonconvergence.** Slack tends to zero, while angles have increments
   `c/k`. Harmonic divergence lets one find arbitrarily late directions almost
   `pi` apart; the vanishing increments make the overshoot tend to zero. The
   block-beginning subsequence is not Cauchy.
7. **Ambient space.** The construction is in Euclidean `R^2`, which is a
   uniformly convex Banach space. One counterexample space suffices for a
   negative answer to the source question.

## Finite sanity check

Run:

```bash
python code/verify_construction.py
```

The script checks the numerical constant, builds several initial blocks for
`f(n)=n^2+1`, and exhaustively verifies every required pair in a finite prefix
whose sum remains inside the constructed blocks. It is only a regression check;
the proof above handles arbitrary `f` and all indices.

## Novelty check

Bounded searches through August 11, 2026 used arXiv:2411.17380, the exact
paper title, the wording of Question 3.2, and combinations of “Banach-valued
Fekete lemma,” “window function,” “uniformly convex,” and “superlinear.” The
official arXiv result remains v1 and no later primary paper resolving this
question was found. Novelty confidence is moderate-to-high, subject to expert
review and broader citation-database checking.
