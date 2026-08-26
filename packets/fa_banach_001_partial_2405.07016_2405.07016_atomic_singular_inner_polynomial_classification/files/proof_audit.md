# Proof audit

**Verdict:** likely valid substantial partial result.  
**Scope:** exact classification for the atomic singular-inner family only; not a resolution of the source's existential question.

Checks performed:

1. **Kernel split.** Direct expansion verifies
   `K_{z^N S}=P_N+z^N \bar w^N K_S`. Raising this finite sum to the `m`th power gives positive kernel summands because every coefficient of `P_N^{m-j}` is positive.
2. **Completed-space representation.** Under `z=(s-1)/(s+1)`, the atomic singular factor becomes `e^{-as}`. The kernel factor is the Laplace kernel of the finite measure with density `1_[0,a]^{*j}`. Its feature-space range consists of compactly supported Laplace transforms and therefore of entire functions. This avoids assuming that an element of the completed Schur-power space is a finite product sum.
3. **Finite-sum RKHS decomposition.** Aronszajn's sum-of-kernels theorem gives an exact decomposition of every space element into the finitely many summand spaces, not merely a dense algebraic approximation.
4. **Pole order.** After the common `z^N` factor is removed, the largest possible denominator exponent is exactly `R=m(N-1)-N`. If `R=-1`, a nonzero polynomial produces a pole even after multiplication by `(s+1)^R`, so the remainder must vanish. If `R>=0`, its degree is at most `R`. The script `code/exponent_audit.py` verified the sharp exponent identity for 2,500 pairs `(m,N)`.
5. **Density conclusion.** The singular-inner model space is infinite dimensional, while the proved polynomial intersection is finite dimensional and hence closed. It cannot be dense.
6. **Numerical contradictions.** No numerical calculation is used in the proof. Separate exploratory probes of an infinite Blaschke product and a non-inner extreme outer candidate both supported, rather than contradicted, the obstruction; ill-conditioned values are explicitly not treated as evidence for the theorem.
7. **Literature/duplicate boundary.** Cheap run indexes and bounded primary-source searches through 2026-08-13 found neither a duplicate packet nor a reported resolution of Question 1 or this atomic classification.

Primary reviewer focus: confirm the feature-map range convention in equation (7), the exact use of the finite-sum RKHS theorem in equation (8), and the `R=-1` pole case. No unproved lemma is hidden in the promoted theorem.
