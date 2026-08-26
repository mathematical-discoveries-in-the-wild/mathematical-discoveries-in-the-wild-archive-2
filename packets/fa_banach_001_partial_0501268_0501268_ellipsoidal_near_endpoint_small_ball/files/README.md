# Near-endpoint small-ball exponent for ellipsoidal cylinders

Status: `partial_result_likely_valid`

Source: Rafał Latała and Krzysztof Oleszkiewicz, *Small ball probability
estimates in terms of width*, Studia Mathematica 169 (2005), 305–314,
arXiv:math/0501268. Conjecture 1 appears on PDF page 2.

## Claimed contribution

Conjecture 1 is true for every centered ellipsoid, and more generally for
every ellipsoidal cylinder

```text
K={x in R^n: sum_{i=1}^r lambda_i x_i^2 <= 1},  lambda_i>0.
```

For each `kappa in (0,1)`, one may take

```text
eta = (1+kappa)/2,
C(kappa) = exp(1/eta),
w0(kappa) = max(2 sqrt(2)/(1-kappa), sqrt(2 log 2)).
```

Then every such `K` with `gamma_n(K)<=1/2` and inradius `w(K)>=w0`
satisfies

```text
gamma_n(tK) <= (C(kappa)t)^{kappa w(K)^2} gamma_n(K)
```

for all `0<=t<=1`.

## Proof mechanism

The B-inequality first enlarges `K` to Gaussian measure `1/2`. For the
normalized ellipsoid, dilation is the lower tail of
`X=sum lambda_i g_i^2`, with every `lambda_i<=w^{-2}` and median equal to
one. A one-sided second-moment estimate forces

```text
m := E X >= 1-sqrt(2)/w.
```

The exact Laplace transform of the weighted chi-square variable then gives

```text
P(X<=t^2) <= exp(w^2/2) t^{m w^2}.
```

As `w` grows, `m` approaches one, which yields every exponent coefficient
strictly below the conjectured endpoint `1`.

## Verification and upgrade attempts

The proof is analytic and exact. The verification report audits the
half-measure reduction, the inradius/weight relation, the median-to-mean
estimate, the concavity step in the Laplace product, and every constant.

Two further upgrade routes were checked. Optimizing the source paper's
Gaussian-isoperimetric anchor is intrinsically capped at coefficient `1/4`.
For a general norm, the weighted-chi-square factorization is replaced by a
correlated Gaussian supremum; no comparison preserving the sharp relative
probability and inradius was found. Thus the packet remains a partial result.

## Novelty and scope

The bounded search on 11 August 2026 covered the four run indexes, the exact
arXiv id and title, exact-statement searches using `gamma_n(tK)` and
`kappa w^2`, and close searches combining `Gaussian small ball`, `inradius`,
`ellipsoid`, and `weighted chi-square`. Later sources were found that still
quote the `w^2/4` theorem, but no explicit near-endpoint ellipsoidal result or
full resolution of Conjecture 1 was located. This supports but does not
certify novelty.

The theorem covers centered quadratic sublevel sets, including unbounded
ellipsoidal cylinders. It does not handle arbitrary symmetric convex bodies.

Human review recommendation: send to a Gaussian probability/asymptotic
geometric analysis reviewer. The key audit points are the B-inequality
normalization and the direction of the concavity estimate for
`log(1+2s lambda_i)`.

Files:

- `source_paper.pdf`: arXiv:math/0501268.
- `figures/open_problem_crop.png`: Conjecture 1 on source PDF page 2.
- `main.tex`, `solution_packet.pdf`: formal partial-result packet.
- `verification.md`: step-by-step proof audit.

