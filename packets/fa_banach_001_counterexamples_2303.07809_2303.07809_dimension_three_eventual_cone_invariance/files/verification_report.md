# Verification report

Verdict: **candidate full counterexample and minimal-dimension resolution;
likely valid**.

## Main counterexample checks

1. The cone is exactly the cone of real symmetric `2 x 2` positive-semidefinite
   matrices, so closedness, convexity, pointedness, and nonempty interior are
   immediate.
2. `A^3=0` and direct multiplication gives
   `exp(tA)=[[1,4t,2t^2],[0,1,t],[0,0,1]]`.
3. Expanding the determinant condition gives exactly
   `y1*y3-y2^2=(x1*x3-x2^2)+2t*x2*x3+t^2*x3^2`.
4. When `x3=0`, positivity forces `x2=0` and the ray is fixed.  When
   `x3>0`, taking `t>=max(0,-2x2/x3)` makes the last two terms nonnegative;
   together with the original determinant inequality this proves permanent
   cone membership.
5. For each `t>0`, `(t^2,-t,1)` is a boundary vector and is mapped to
   `(-t^2,0,1)`, which fails even the first coordinate condition.  Thus there
   is no positive time at which the whole cone is preserved.
6. Every proper closed cone with interior in dimension two has exactly two
   boundary generators.  Taking the maximum of their individual eventual
   times proves uniformity, so the dimension-three example is minimal.

## Six-dimensional upgrade checks

1. `u=(1,0,1)` and `phi(x)=x1+x3` are interior primal/dual cone elements, so
   `U=u tensor phi` is strongly positive and interior in the ambient positive
   operator cone.
2. The two chains `{I,A,A^2}` and `{U,AU,A^2U}` make their span invariant under
   left multiplication by `A`.
3. Direct matrix-unit inspection (and an independent exact SymPy rank check)
   gives dimension six.
4. The positive-extension step is the standard finite-dimensional order-unit
   Hahn--Banach theorem: an ordered subspace containing an ambient interior
   point admits positive extensions of its positive functionals.
5. The source's Proposition 2.3 then reduces weak eventual nonnegativity to
   finitely many evaluations on vectors `Mx in K`, where the main individual
   result applies.
6. The orbit of the positive vector `I` is `exp(tA)`, which is never a positive
   operator for `t>0`; individual eventual nonnegativity therefore fails.

No numerical computation is used in either proof.
