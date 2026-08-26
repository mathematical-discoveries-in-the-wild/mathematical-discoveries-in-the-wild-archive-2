# Verification notes

## Claim audited

For the sharp constant

```text
K_N = sup ||f_xy||_1 / (||f_xx||_1 + ||f_yy||_1)
```

over nonzero trigonometric polynomials of coordinate degree at most `N` on
`T^2`, the packet proves

```text
K_N >= c log N / log log N
```

for all sufficiently large `N`.

## Internal proof checks

1. **No zero `x`-frequency.**  For a frequency in the `k`-th block,
   `q_x = sigma M^k + s_x`, with
   `|s_x| <= sum_{j<k} M^j < M^k/(M-1)`.  Thus `q_x != 0` for `M>=3`, so
   division by `q_x^2` is legitimate.

2. **Pure `xx` derivative.**  Defining
   `hat W(q)=-hat R(q)/q_x^2` gives `W_xx=R` exactly.

3. **Block multiplier errors.**  On a signed half of the `k`-th block, write
   `u=s_x/(sigma M^k)`, `v=s_y/(sigma M^k)`, and
   `epsilon_k=(-1)^k`.  Then

   ```text
   q_y/q_x = (epsilon_k+v)/(1+u).
   ```

   The power-series expansions of this expression minus `epsilon_k` and of
   its square minus one converge on the block.  The one-variable `L1`
   Bernstein inequality applied successively in the two variables gives norm
   at most `delta^(r+s)` to each normalized monomial multiplier, where
   `delta < 1/(M-1)`.  Summing the series gives `O(1/M)` per block and
   `O(n/M)` in total.

4. **Riesz main term.**  For each fixed `y`, apply Meyer's theorem to the
   `x`-frequencies `M^k`.  In the independent model the remaining phases are
   `t_k+epsilon_k M^k y`; Haar translation in each `t_k` removes them, so the
   comparison is uniform in `y`.  The lacunarity sum is `(n-1)/M`, hence the
   comparison constant is universal for `M=n`.  Summation by parts then
   converts the alternating martingale differences into a linear combination
   of finite independent Riesz products whose coefficient variation is
   comparable to `n`.  The Latała lower inequality gives `L1` norm at least
   `c n`.

5. **Degree.**  Every coordinate frequency has magnitude at most
   `sum_{k<=n} M^k <= 2M^n`.  With `M=n`, the construction has degree at most
   `2n^n`.

6. **Inversion.**  Taking
   `n=floor(log N/(2 log log N))` for large `N` gives `2n^n<=N`.  Monotonicity
   of `K_N` yields the claimed bound for every sufficiently large `N`, not
   only a subsequence.

## Literature check

Cheap run indexes contained no packet for arXiv:2206.13666 or the exact mixed
derivative question.  Focused searches on 2026-08-09 for the exact paper title,
quantitative Ornstein non-inequalities, and the mixed-derivative logarithmic
bound found the source preprint and its 2024 journal publication, but no later
paper closing or improving its `sqrt(log N)` lower bound.

## Computational check

`code/verify_small_cases.py` constructs the finite Fourier coefficients
exactly, applies the three derivative multipliers, and estimates the `L1`
norms by uniform-grid quadrature for small `(n,M)`.  It is a sign/index sanity
check only; the proof is fully analytic.
