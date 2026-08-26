# Verification report

Verdict: candidate substantial partial result, likely valid.

## Claim audited

For the exact explicit fractional difference equation and zero initial data of
arXiv:2406.15417, replacing the bounded coefficient by a closed operator A
does not yield an all-data classical maximal-regularity theory unless A is
already bounded.

## Critical checks

### 1. Fractional difference at time zero

With v=Delta^{-(3-alpha)}u=k^{3-alpha}*u and
u(0)=u(1)=u(2)=0, one has v(0)=v(1)=v(2)=0 and v(3)=u(3) because
k^{3-alpha}(0)=1. Hence
Delta^alpha u(0)=Delta^3 v(0)=u(3). This matches the explicit computation
inside the source's proof of Theorem 3.8.

### 2. Domain forcing

For impulse data f(0)=x, the equation at time zero gives u(3)=x. A
classical solution of the same equation for every nonnegative time must make
A u(3) meaningful at time three, so x is in D(A). Since x was arbitrary,
D(A)=X. If A is closed, the closed graph theorem applies.

### 3. Resolvent-sequence rigidity

At n=0, Definition 3.1 has
(k^{alpha-2}*S_alpha)(0)=S_alpha(0)=I and
S_alpha^lambda(0)=S_alpha(-lambda)=0. All other terms are bounded scalar
multiples of I or S_alpha(3). An identity in B(X) therefore writes A
as a bounded operator.

### 4. Diagonal frequency example

Let M=2^alpha+|gamma| and
A e_j=-(M+2+j)e_j on complex ell2. For every source symbol value
q(z)=z^{3-alpha}(z-1)^alpha-gamma z^{-lambda}, |q(z)|<=M, so
dist(q(z),sigma(A))>=3. Therefore the resolvents have norm at most 1/3;
the first numerator has modulus at most 2^alpha. Both families are norm
bounded, hence R-bounded on Hilbert space.

The vector x=(1/j) belongs to ell2 but not to D(A). The one-point
forcing f(0)=x lies in every ellp(N0;ell2), but the domain argument rules
out a classical solution.

### 5. No overclaim

The theorem concerns the literal all-data classical extension and the
source-style resolvent sequence. It does not rule out:

- compatible forcing in a scale of domains of powers of A;
- mild solutions whose equation is interpreted in an extrapolation space;
- a weaker regularity target not requiring A u to be X-valued;
- an implicit scheme with A acting at the newest time level.

## Recommended expert checks

1. Confirm that the intended unbounded “classical solution” requires
   u(n) in D(A) for every index at which A u(n) appears.
2. Confirm the source branch convention does not affect the elementary bound
   |z^{3-alpha}(z-1)^alpha|<=2^alpha.
3. Decide whether the result is best described in publication as a no-go
   theorem, a compatibility obstruction, or a motivation for an implicit
   reformulation.
