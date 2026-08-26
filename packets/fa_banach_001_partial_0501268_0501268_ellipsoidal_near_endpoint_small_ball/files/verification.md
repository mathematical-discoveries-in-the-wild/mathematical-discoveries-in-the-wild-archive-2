# Verification report

Verdict: `likely_valid`  
Confidence: 96/100

## 1. Geometry-to-probability translation

After an orthogonal change of coordinates, an ellipsoidal cylinder is

```text
K={x: sum_{i=1}^r lambda_i x_i^2 <= 1}, lambda_i>0.
```

Its inradius is `w=(max_i lambda_i)^(-1/2)`. If `G` is standard Gaussian and
`X=sum lambda_i g_i^2`, then `gamma_n(tK)=P(X<=t^2)`. Free cylinder
coordinates integrate out and introduce no additional factor.

## 2. Half-measure normalization

For `gamma_n(K)<=1/2`, choose `a>=1` with `gamma_n(aK)=1/2`. Concavity of
`s -> log gamma_n(e^s K)` implies, for `0<t<=1`,

```text
gamma_n(tK)/gamma_n(K)
 <= gamma_n(taK)/gamma_n(aK).
```

The inradius increases from `w` to `W=aw`. For `Ct<=1`, replacing `W` by the
smaller `w` only enlarges `(Ct)^{kappa W^2}`. For `Ct>=1`, the desired bound
is immediate from `tK subset K`.

## 3. Median forces the spectral mass

In the normalized case, `P(X<=1)=P(X>=1)=1/2`. Put

```text
m=E X=sum lambda_i,
v=Var X=2 sum lambda_i^2 <= 2m/W^2.
```

If `m<1`, Cantelli's inequality gives

```text
1/2=P(X-m>=1-m) <= v/(v+(1-m)^2),
```

so `(1-m)^2<=v<=2m/W^2<=2/W^2`, hence
`m>=1-sqrt(2)/W`. If `m>=1`, this lower bound is automatic.

Cantelli's inequality itself follows by applying Markov's inequality to
`(Y+v/a)^2` for a centered variable `Y` and threshold `a>0`, so no unproved
probabilistic input is hidden here.

## 4. Laplace-transform bound

For `s>0`,

```text
P(X<=t^2)
 <= exp(s t^2) E exp(-sX)
 = exp(s t^2) product_i (1+2s lambda_i)^(-1/2).
```

Let `L=W^{-2}`. Because `f(x)=log(1+2sx)` is concave with `f(0)=0`, for
`0<=x<=L`,

```text
f(x) >= (x/L) f(L).
```

Therefore

```text
sum_i log(1+2s lambda_i)
 >= m W^2 log(1+2s/W^2).
```

Choosing `s=W^2/(2t^2)` yields

```text
P(X<=t^2)
 <= exp(W^2/2) (1+t^{-2})^{-mW^2/2}
 <= exp(W^2/2)t^{mW^2}.
```

All inequality directions have been checked.

## 5. Constants

Fix `kappa in (0,1)` and put `eta=(1+kappa)/2`. If
`W>=2sqrt(2)/(1-kappa)`, then `m>=eta`. Let `C=exp(1/eta)`. For
`0<t<=1/C`,

```text
P(X<=t^2) / ((Ct)^{kappa W^2}/2)
 <= 2 exp(W^2/2) C^{-mW^2}
 <= 2 exp(-W^2/2).
```

This is at most one when `W>=sqrt(2 log 2)`. For `t>=1/C`, monotonicity gives
`P(X<=t^2)<=1/2<=(Ct)^{kappa W^2}/2`. The case `t=0` is immediate.

## 6. Scope and adversarial checks

- Rank-deficient quadratic forms are allowed; at least one positive weight is
  forced by the measure hypothesis, and the Gaussian law of `X` is continuous.
- No finite-dimensional factor is silently lost in cylinder directions.
- The base comparison after rescaling is used only where `Ct<=1`.
- The proof needs centered ellipsoids; translations destroy symmetry and are
  outside the source conjecture.
- The factorized Laplace transform is the nontrivial special structure. No
  claim is made for general convex bodies.

