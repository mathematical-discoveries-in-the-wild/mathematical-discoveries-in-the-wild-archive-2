# Verification report

Status: `candidate_full_likely_valid`

## Claim audited

For every `0 < lambda <= 1` and finite `beta >= 0`, the packet realizes
`dim_loc(mu*nu)(0)=beta` with `lower_dim mu >= lambda`, an exactly countably
infinite fibre, and product lower dimension at least `lambda` at every fibre
point.

## Structural audit

### Common geometry

- The weights `p_n=(1-q)q^(n-1)` sum to one.
- Centre ratios are chosen at most `1/4`, while all packet lengths/radii are
  at most `x_n/16`; packets are disjoint and accumulate only at zero.
- If an off-diagonal pair meets `B(0,r)`, the larger centre is at most `2r`.
  Thus both indices lie in a geometric tail and their total product mass is
  the square of that tail mass.

### The range `0 < beta <= 1`

- Uniform packets give local dimension one at every packet point.
- Packet masses and locations are both `p_n`, so `mu` and `nu` have local
  dimension one at zero.
- The fibre identity is exact because `nu` contains only the aligned atoms
  and their accumulation point.
- Aligned convolution mass is exactly
  `sum p_n^2 min(1,r/ell_n)`.
- Since `p_n^2=tau^(-beta)ell_n^beta`, geometric summation bounds this between
  constant multiples of `r^beta` for `beta<1`; at `beta=1` the upper bound is
  `O(r log(1/r))`, which has the same logarithmic exponent.
- Off-diagonal mass is `O(r^2)` and cannot alter any exponent at most one.

### The value `beta=0`

- Widths are `tau exp(-n^2)` while aligned tail masses decay only
  geometrically.
- If `ell_N <= r < ell_(N-1)`, the exponent is nonnegative and at most
  `O(N)/Theta(N^2)`. This controls every sufficiently small radius, so the
  actual local dimension exists and equals zero.

### The range `beta>1`

- Parameters satisfy `D>max(lambda,beta/2)`, `a=lambda`, and
  `b=beta-lambda>0`.
- The left endpoint of each `mu` packet has dimension `a=lambda`, other packet
  points have dimension one, and zero has dimension `D`.
- Equal-index supports represent zero only at their left endpoints. Packet
  separation excludes every unequal-index representation.
- Product dimensions are `a+b=beta` at nonzero fibre points and `2D` at the
  accumulation pair.
- The aligned endpoint integral is exactly
  `a*Beta(a,b+1)*(r/ell_n)^beta` for `r<=ell_n`.
- Aligned mass lies between `c r^beta` and
  `C(1+|log r|)r^beta` at all small scales.
- Off-diagonal mass is `O(r^(2D))=o(r^beta)`.

### Averaged rescue criterion

- Splitting the convolution integral into good and bad centres gives an upper
  bound on ball mass; division by negative `log r` correctly yields the lower
  local-dimension bound.
- The strictness model has bad-atom tail `2^(-c L^(4/3))` at radius `2^(-L)`,
  yet every proposed uniform cutoff leaves a positive-mass bad atom.

## Computational status

`code/check_construction.py` checks normalization, separation margins,
parameter inequalities, selected-scale slopes, the `beta=0` every-scale
envelope, and beta-integral constants for representative target dimensions.
It reports `all_checks_passed`. These checks are not used as proof.

The final LaTeX packet must compile without warnings and every rendered page
must be visually inspected before delivery.

## Reviewer recommendation

Recommended status: `candidate_full_likely_valid`. Review the tail-index
implication in the separation lemma, the direction of logarithmic
inequalities, and the transition from geometric aligned sums to every-scale
two-sided bounds.
