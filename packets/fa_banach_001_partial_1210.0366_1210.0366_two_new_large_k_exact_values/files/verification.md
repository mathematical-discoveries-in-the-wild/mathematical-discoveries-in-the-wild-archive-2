# Verification and limitations

## Mathematical checks

- The matrix is constructed only from norming functionals, so its rank is at
  most the ambient dimension and its diagonal is exactly one.
- Passing to an `m`-member subfamily is valid because `k` is fixed and every
  `k`-subset inequality is inherited.
- The scalar normalization `|x_j|<=1` is proved before reducing the four kinds
  of complement-pair inequalities to the two ordered inequalities.
- The vertex list includes the all-equal cases and both end cases; the
  quadratic is strictly convex, so equality cannot occur at a nonvertex.
- Exact rational arithmetic gives `q_18(5)=q_18(6)=2`, with no other equality,
  and `q_42(13)=5`, with no other equality.
- Equality in the trace-Frobenius rank inequality is used only after both the
  rank and every row bound are forced to be equalities.
- In the 18-by-18 case, symmetry really does prevent mixed row types: the
  possible off-diagonal values `{1/2,-1/4}` and `{3/7,-2/7}` are disjoint.
- Once the row type is uniform, the row sum is nonzero and hence is an
  eigenvalue, contradicting the unique allowed nonzero eigenvalue.
- The lower bound `k+1` follows from `k+1` unit vectors summing to zero: each
  `k`-sum is the negative of the omitted unit vector.

## Computational check

`code/check_endpoint_maxima.py` uses `fractions.Fraction` to enumerate the
integer jump positions, verify the equality cases, row sums, and rank
thresholds. It is a reproducibility check, not part of the proof.

## Upgrade limits

For `(d,k)=(6,15)` and `(7,39)`, exact integer optimization makes the rank
lower bound round up to `d` but does not force equality in the rank inequality.
The symmetry/eigenvalue contradiction therefore cannot be invoked. A scan of
the endpoint formula through `m<2000` found no further exact rank-equality
hits. The full Conjecture 28 remains open.
