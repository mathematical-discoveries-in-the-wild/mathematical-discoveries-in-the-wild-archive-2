# Verification audit

## 1. Source match

The attached arXiv PDF dated 2022-03-09 states Conjecture 3.4 on PDF page 5
and Conjecture 3.15 on PDF page 11. It explicitly says that a Banach-space
version of Lemma 3.6 proves Conjecture 3.4. Proposition 3.20 proves that one
well-separating common complement implies prevalence.

## 2. Quotient norms

For `K=intersection ker(phi_j)` and `q:X->X/K`, each induced functional has
the same norm as `phi_j`, namely one. One inequality follows from contractivity
of `q`; the reverse follows by lifting quotient vectors with norm arbitrarily
close to their quotient norm.

## 3. Affine-slab constant

In dimension `n`, John position gives

```text
S(B_2^n) subset B_Y subset sqrt(n) S(B_2^n).
```

Thus every induced norm-one functional has Euclidean coefficient norm at least
`n^{-1/2}`. For `U` uniform on the Euclidean ball of radius `R=r/2`, an affine
slab of half-width `eta` has relative volume at most

```text
(2 eta/(aR)) (omega_{n-1}/omega_n)
<= 2 eta n/R
= 4 eta n/r.
```

Here `a>=n^{-1/2}` and `omega_{n-1}/omega_n<=sqrt(n)`. Summing over `N`
slabs and taking `eta=r/(8N^2)` gives total bad probability at most
`n/(2N)<=1/2`. The quotient point has norm at most `r/2`, so it has a lift of
norm strictly below `r`.

For the volume ratio, slicing gives
`omega_n/omega_{n-1}=integral_{-1}^1(1-t^2)^((n-1)/2)dt`. On
`|t|<=n^{-1/2}` the integral is at least
`2n^{-1/2}(1-1/n)^((n-1)/2)>=n^{-1/2}` for `n>=2`; `n=1` is immediate.

## 4. Perturbation tail

With `N_m=2^m`, `alpha_m=rho_m/(8N_m^2)`, and
`rho_{m+1}=alpha_m/8`,

```text
rho_{m+1}/rho_m = 1/(64N_m^2) <= 1/256.
```

Therefore

```text
sum_{k>m} rho_k
<= rho_{m+1}/(1-1/256)
= (32/255) alpha_m
< alpha_m/4.
```

Every lower bound imposed at stage `m` survives in the limit with margin
greater than `3alpha_m/4`.

## 5. Subexponential rate

The recurrence gives

```text
alpha_1=2^{-7},
alpha_{m+1}=alpha_m 2^{-(2m+8)},
alpha_m=2^{-(m^2+7m-1)}.
```

If `2^{m-1}<j<=2^m`, then `-log(alpha_m)=O(m^2)=O((log j)^2)`, so
`j^{-1} log(alpha_m)->0`. This is exactly the source's well-separating
condition.

## 6. Nonzero limit and normalization

The full perturbation series has norm below
`(1/4)/(1-1/256)=64/255<1`. Its first functional remains bounded below by a
positive margin, so its sum is nonzero. Dividing by its norm can only enlarge
all functional absolute values.

## 7. Arbitrary codimension and prevalence

The source's induction after Lemma 3.8 is explicitly carried out in an
arbitrary Banach space. The new transversality bound is a fixed constant times
the product of the codimension-`k` and codimension-one bounds, so it remains
subexponential. Proposition 3.20 is also a Banach-space theorem and yields
Conjecture 3.15 directly.

## 8. Scope

The source works over real vector spaces, and the proof matches that scope.
The functional theorem also implies the complex analogue by applying it to
the real norm-one functionals `Re(phi_j)` and observing
`|phi_j(x)|>=|Re(phi_j(x))|`.

## 9. Novelty search

Cheap-index searches found no duplicate. Bounded exact-title, exact-phrase,
author, and core-keyword web searches through 2026-08-13 found only the
source and later applications/restatements of the Hilbert theorem, not a
resolution of the Banach conjectures. This supports packet promotion but is
not a priority claim.
