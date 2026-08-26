# Solution companion

Let `T` be the first exit time of standard one-dimensional Brownian motion,
started at zero, from `(-1,1)`, and let `S(t)=P(T>t)`.

## 1. The interval exit-time law is log-concave

Solving the elementary boundary-value problem for the Laplace transform gives

```text
E exp(-sT)=sech(sqrt(2s)).
```

Euler's product for `cosh` yields

```text
sech(sqrt(2s))
 = product_{n>=0} lambda_n/(lambda_n+s),
lambda_n=(2n+1)^2 pi^2/8.
```

Since the right side is the Laplace transform of the almost surely convergent
sum of independent `Exp(lambda_n)` variables, `T` has that law.  Exponential
densities are log-concave; convolution and weak limits preserve log-concavity.
Thus the law of `T` is log-concave.  Applying log-concavity of the measure to
the upper rays `(x,infinity)` and `(y,infinity)` proves

```text
S(theta x+(1-theta)y) >= S(x)^theta S(y)^(1-theta).
```

## 2. Balance the rectangle coordinate scales

Put `b_k=a_k^{-2}` and `bar b=(b_1+...+b_d)/d`.  Independence and Brownian
scaling give

```text
P_0(tau_{R_a}>t)=product_k S(b_k t).
```

Concavity of `log S` and Jensen's inequality give, pointwise in `t>0`,

```text
product_k S(b_k t) <= S(bar b t)^d
                    =P_0(tau_{Q_d}>bar b t).
```

Hence `tau_{R_a} <=_st tau_{Q_d}/bar b`.  Since

```text
lambda_1(R_a)=(pi^2/4) sum_k b_k,
lambda_1(Q_d)=pi^2 d/4,
```

we get the scale-free domination

```text
lambda_1(R_a) tau_{R_a} <=_st lambda_1(Q_d) tau_{Q_d}.
```

Taking the increasing function `x -> x^p` proves the desired inequality for
every `p>0`.

## 3. Equality

If not all `b_k` are equal, equality of one moment would force equality in the
pointwise Jensen bound for all `t`.  Then the concave function `log S` would be
affine on every interval `[t min b_k,t max b_k]`, hence affine on all of
`(0,infinity)`.  But the exponential-sum representation gives
`1-S(t)=O(t^2)` near zero, while `S(t)` tends to zero at infinity.  Thus
`log S` is not affine.  Every moment inequality is therefore strict unless all
side lengths are equal.

The center is the maximizing starting point for a rectangle: the interval
survival probability is even and nonincreasing in the absolute starting
position, and the rectangular survival probability is its coordinatewise
product.  Thus the same result applies to the source functional with the
supremum over starting points.
