# Verification report

Verdict: `likely_valid`  
Confidence in the mathematics: 98/100  
Confidence that the source intended the uniform-in-`lambda` reading: 78/100

## 1. Functional normalization and domain

The local functional in arXiv:2507.00842 is

```text
Phi_{lambda,Q}(u)
 = lambda^p intint_{E_{lambda,gamma/p,Q}(u)}
                  |x-y|^{-N+gamma} dx dy.
```

This normalization is also forced by Theorem 1.3 and equation (1.30). A single
global definition in the TeX source omits `lambda^p`; that occurrence is
inconsistent with the rest of the paper. Open Question 3 gives `u` only on
`Q`, so its `Phi_lambda(u)` is naturally read as the local functional.

## 2. Premise check: positivity of kappa

Let `h(x)=(x_1+...+x_N)/sqrt(N)`. For any family `h_lambda -> h` in measure on
`Q`, define the clipping map

```text
T(t)=min(max(t,0),sqrt(N)).
```

Then `T(h)=h`, `T(h_lambda)->h` in measure, and
`|T(a)-T(b)|<=|a-b|`, hence

```text
Phi_{lambda,Q}(T(h_lambda)) <= Phi_{lambda,Q}(h_lambda).
```

The clipped functions are uniformly bounded, so convergence in measure on the
finite-measure cube implies convergence in `L^1(Q)`. Theorem 1.1 of
Gobbino--Picenni (arXiv:2311.05560) therefore yields

```text
liminf Phi_{lambda,Q}(h_lambda)
 >= C^geom_{N,p} c_gamma F_p(h,Q)
 =  C^geom_{N,p} c_gamma > 0,
```

where `c_gamma=log(2)/(2^{gamma+1}-1)`. Taking the infimum over all families
in Nguyen's cell formula proves `kappa_{N,p,gamma}>0` for every `gamma>0`.

Checks: clipping direction correct; convergence topology upgraded correctly;
`|grad h|=1`; both `p>1` and `p=1` cases give `F_p(h,Q)=1`.

## 3. Left-hand side

For `u(x)=x_1` on `Q=(0,1)^N`, Fubini reduces the oscillation to

```text
int_0^1 int_0^1 |s-t|^p ds dt
 = 2 int_0^1 int_0^s (s-t)^p dt ds
 = 2/((p+1)(p+2)).
```

This is finite and strictly positive for every `p>=1`.

## 4. Local energy

For `gamma>0`, the diagonal singularity is integrable. Since
`Q-Q` lies in the ball of radius `sqrt(N)`,

```text
nu_gamma(QxQ)
 <= |S^{N-1}| int_0^{sqrt(N)} r^{gamma-1} dr
 =  |S^{N-1}| N^{gamma/2}/gamma.
```

The exceedance set is a subset of `QxQ`, so

```text
0 <= Phi_{lambda,Q}(u)
   <= lambda^p |S^{N-1}| N^{gamma/2}/gamma.
```

Thus the proposed right-hand side tends to zero as `lambda->0+`, in direct
contradiction with the fixed positive left-hand side.

## 5. Global zero-extension stress test

Let `U=u` on `Q` and `U=0` outside. Then `|U(x)-U(y)|<=1`, and every pair in
the exceedance set has at least one endpoint in `Q`. The exceedance condition
forces

```text
|x-y| < R_lambda := lambda^{-p/(p+gamma)}.
```

Double-counting the possible endpoint in `Q` gives

```text
Phi_lambda(U)
 <= 2 lambda^p |Q| |S^{N-1}| R_lambda^gamma/gamma
 =  (2 |S^{N-1}|/gamma) lambda^{p^2/(p+gamma)} -> 0.
```

Hence the counterexample is not an artifact of choosing the local notation.

## 6. Quantifier audit and limitations

The question contains a free `lambda` and asks for a constant not depending on
it, so the standard mathematical reading is uniformity for all `lambda>0`.
This also matches the preceding Nguyen Poincare theorem, whose threshold is
uniform. Nevertheless, the paper does not literally print `for every
lambda>0` in Open Question 3. Since positive `gamma` is naturally associated
with `lambda->+infinity`, the author may have intended an asymptotic
restriction. The packet states this limitation prominently.

No assertion is made about `gamma<=-1` or the sufficiently-large-`lambda`
repair.

