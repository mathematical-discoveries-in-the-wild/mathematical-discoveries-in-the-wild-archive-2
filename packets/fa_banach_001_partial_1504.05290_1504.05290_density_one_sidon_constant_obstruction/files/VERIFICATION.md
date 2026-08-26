# Verification report

Verdict: `candidate_partial_result_likely_valid`

## Algebra checked

From the definitions in Section 9 of arXiv:1504.05290,

```text
Psi = (1 + log(n)/n)^(-1)
      [1 + log(n)/n^2 (sum_i r_i)^2],
```

so the common factor in every `phi_i`, `1 <= i <= n`, is exactly

```text
[Psi(1 + log(n)/n)]^(-1/2)
  = [1 + log(n)/n^2 (sum_i r_i)^2]^(-1/2).
```

For a retained set `B` and omitted set `K`, the checks used in the proof are:

```text
|sum_{i in B} sigma_i W_i|
  <= |sum_{i=1}^n sigma_i W_i| + |sum_{i in K} sigma_i W_i|
  <= 6 sqrt(n) + |K|,

|sum_{i=1}^n r_i|
  >= (|sum_{i in B} r_i| - |K|)_+.
```

If `x=|sum_B r_i|` and `k=|K|`, then

```text
x / sqrt(1 + (log n/n^2)(x-k)_+^2)
  <= k + n/sqrt(log n).
```

This follows separately from `x<=k`, and from writing `x=k+y` when
`x>k` and using `y/sqrt(1+(log n/n^2)y^2) <= n/sqrt(log n)`.

## Quantifiers checked

If a subsystem `A` of the full `n+1` family contains `phi_0`, assigning
coefficient zero to `phi_0` is allowed in the Sidon inequality.  Thus it is
enough to use equal coefficient one on `B=A intersect {phi_1,...,phi_n}`.
When `|A| >= (1-epsilon)(n+1)`, one has

```text
m=|B| >= (1-epsilon)n-epsilon,
k=n-m <= epsilon n+epsilon.
```

All remaining error terms divided by `m` tend to zero, leaving
`epsilon/(1-epsilon)`.

## Scope checked

The theorem does not claim a negative answer for any fixed `epsilon>0`.
It rules out a uniform lower constant along subsystems with deficit `o(n)`
and gives an upper restriction on any possible fixed-`epsilon` constant.

No numerical computation is used, and the proof does not rely on the later
Pisier tensor theorem.
