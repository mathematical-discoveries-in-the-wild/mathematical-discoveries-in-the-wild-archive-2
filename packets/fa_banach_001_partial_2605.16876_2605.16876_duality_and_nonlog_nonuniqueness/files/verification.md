# Verification report

Verdict: `candidate_substantial_partial_likely_valid`

## Duality audit

For `g^vee(x)=-g(x^{-1})`, order reversal under inversion followed by the
minus sign shows that `g^vee` is operator monotone.  It has
`g^vee(1)=0` and derivative one at `1`.

Self-duality of the metric geometric mean gives

```text
(A_i # X^{-1})^{-1}=A_i^{-1} # X.
```

With `Y=X^{-1}`, the `g^vee` equation for data `A_i` is exactly the `g`
equation for data `A_i^{-1}`.  This proves the solution-set identity in both
directions, not merely an implication.

## Unique endpoint audit

For `g_+(x)=x-1`, the equation is the standard Wasserstein equation

```text
sum_i w_i (A_i # X^{-1})=I,
```

which has unique solution `Omega(omega;A)`.  Since
`g_+^vee(x)=1-x^{-1}`, duality gives the unique solution

```text
Omega(omega;A_1^{-1},...,A_m^{-1})^{-1}.
```

## Operator-monotonicity audit

For `0<s<=1`, the principal map `z -> z^s` sends the upper half-plane into
itself, and the real Möbius map `(z-1)/(z+1)` also preserves the upper
half-plane.  Their positive scalar multiple

```text
g_s(z)=(2/s)(z^s-1)/(z^s+1)
```

is therefore a Pick function.  Loewner's theorem makes `g_s` operator
monotone.  Direct differentiation gives `g_s(1)=0`, `g_s'(1)=1`, and
`g_s(x^{-1})=-g_s(x)`.

## Exact first-solution audit

The matrices `S,T` satisfy `S^2=T^2=I` and `ST=-TS`.  Hence
`(aS+bT)^2=(a^2+b^2)I`, making every hyperbolic functional-calculus step in
the calibration exact.  The chosen `q_s` gives

```text
g_s(B_1)+g_s(B_2)+g_s(B_3)=0.
```

For `A_i=B_i X_0 B_i`, the Riccati characterization of `#` gives
`A_i # X_0^{-1}=B_i`; therefore `X_0` is an exact solution.

## Second-solution and interval audit

All constructed matrices have determinant one.  On the surface
`X(u,v)=exp(uS+vT)`, every `A_i # X(u,v)^{-1}` also has determinant one.
Self-duality of `g_s` makes its trace zero, so the matrix equation reduces to
two continuous scalar equations `F_1=F_2=0`.

The verifier uses the exact two-by-two identity

```text
A # B = (A+B)/sqrt(det(A+B))
```

when `det(A)=det(B)=1`, plus the closed functional-calculus formula for
`g_s`.  With 8,000 exact-decimal interval boxes per face, it reports for
`s=1/100`:

```text
u-: [ 1.590311067e-4,  1.673026521e-3]
u+: [-1.597948126e-3, -7.594924750e-5]
v-: [ 1.139349984e-4,  1.458285178e-3]
v+: [-1.375931389e-3, -2.788044879e-5]
```

Every interval on every face has the required strict sign; there are zero
failed subintervals.  Poincare–Miranda therefore gives a root in the stated
rectangle.  Since `(3,0)` is outside it, this solution is distinct from
`X_0`.

The same verifier certifies strict signs at the logarithmic limit.  Joint
continuity of the calibrated data and face functions then yields
nonuniqueness for every sufficiently small `s>0`.

## Scope and novelty audit

This does not provide necessary and sufficient conditions on arbitrary `g`.
It supplies a duality constraint, a second global uniqueness class member,
and a continuum of non-logarithmic failures.  The run indexes and bounded
web/arXiv searches found no matching resolution.  Search date: 2026-08-11.

## Packet render audit

The final packet has five pages.  All five pages were rendered to PNG after
the final compilation and inspected visually on 2026-08-11.  Equations,
tables, the source-question crop, references, and margins are readable; no
content is clipped.  Final PDF SHA-256:

```text
48eba56f0feff97ef613f1bbdaa9bfcce7eb82faba76469335dfd743191db2f7
```

## Human verifier focus

1. Check the Pick-function invocation of Loewner's theorem.
2. Check that the scalar inverse defining `q_s` has the correct factor `2/s`.
3. Re-run the interval script and inspect the exact-decimal partitioning.
4. Confirm that the source's global-uniqueness quantifier is interpreted as
   uniqueness for every dimension, weight vector, and input tuple.
