# Verification notes

## Claim audited

The general upper bound `p <= dim(H)` for the number of trajectory atoms in
the source representer theorem is universally sharp.  For each `D`, the packet
constructs a source-admissible problem with `H=R^D` whose unique minimizer has
minimal atomic complexity `D`.

## Internal proof checks

1. **Admissible operator.**  Each coordinate of `A` is integration against a
   continuous function at the single sampling time `t_0`.  This is continuous
   for exactly the pointwise weak-star convergence required by the source.

2. **Connected domain.**  The construction works on `Omega=(0,1)`.  It does
   not exploit disconnected components; the measurement bumps merely have
   pairwise disjoint supports.

3. **Mass estimate.**  Finite Benamou--Brenier energy forces `rho >= 0`.
   The homogeneous continuity equation makes total mass independent of time.
   Since the sum of measurement bumps is at most one,
   `J(rho,m) >= alpha sum_j (A rho)_j`.

4. **Equality case.**  Equality forces zero kinetic energy, hence `m=0`, and
   the continuity equation makes `rho_t` constant.  The unit level set of the
   bump sum consists exactly of the selected `D` points, so equality localizes
   the fixed measure there.

5. **Unique minimizer.**  The lower bound reduces the objective coordinatewise
   to `alpha s + (s-(alpha+1))^2/2`, whose unique nonnegative minimizer is
   `s=1`.  Equality then identifies the unique stationary measure with unit
   mass at each selected point.

6. **Atom lower bound.**  At the sampling time, every trajectory is at one
   spatial point.  Pairwise disjoint bump supports imply that its measurement
   vector has at most one nonzero coordinate.  Summing to the all-ones vector
   therefore needs at least `D` positive atoms.

7. **Attainment.**  The `D` constant trajectories at the selected points are
   normalized extreme atoms after multiplying each by coefficient `alpha`.
   Their sum is the unique minimizer, so the minimal count is exactly `D`.

## Literature check

Cheap run indexes contained no result for arXiv:1907.11589 or this exact
sharpness question.  Focused arXiv searches on 2026-08-09 found the source and
the authors' later generalized conditional-gradient paper, but no paper
settling the optimal number of trajectory atoms.  The later paper uses the
trajectory-atom characterization algorithmically and does not supersede the
sharpness construction recorded here.

## Computational dependence

None.  The counterexample and uniqueness proof are entirely analytic.
