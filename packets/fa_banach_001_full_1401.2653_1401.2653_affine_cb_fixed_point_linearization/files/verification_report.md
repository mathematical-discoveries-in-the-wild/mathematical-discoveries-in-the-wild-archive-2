# Verification report — 1401.2653 affine `CB(L)` question

Verdict: `likely valid full affirmative solution; human review needed`.

## Claim/hypothesis matching

- The source question assumes a compact topological group, a jointly
  continuous affine action on a Banach space, and continuity of the induced
  action on `CB(L)`.
- The packet keeps all three assumptions and concludes exactly `CB(L) in
  G-AE`.
- The source's Theorem 5.1 requires a Banach `G`-space, meaning a continuous
  linear action with invariant norm, plus continuity on `CB(L)`. The two
  reduction lemmas establish precisely these hypotheses.

## Adversarial checks

1. **Existence of the barycenter.** For fixed `x_0`, the orbit map has compact
   image in the metric Banach space `L`. That image is separable and bounded,
   so the continuous map is strongly measurable and Bochner integrable
   against normalized Haar measure, even if `G` is nonmetrizable.

2. **Affine maps commute with the integral.** Every continuous affine map on
   a real Banach space is `x -> Ax+b` with `A` bounded linear. Since Haar
   measure has total mass one, applying it to a Bochner barycenter commutes
   with the integral. Left invariance then proves the barycenter is fixed.

3. **Linearity after translation.** An affine map fixing zero is linear. The
   translated maps obey the group law and remain jointly continuous.

4. **Uniform equivalence of norms.** Each orbit is bounded. Uniform
   boundedness applied to `{rho_g:g in G}` yields a common operator-norm bound
   `M`. Thus `||x|| <= ||x||_G <= M||x||`; completeness follows.

5. **Invariance of the new norm.** Right multiplication permutes `G`, giving
   `sup_g ||rho_g rho_h x|| = sup_k ||rho_k x||`.

6. **No change of `CB(L)`.** Equivalent norms have the same closed and
   bounded sets; convexity is algebraic. Their pointwise inequalities pass to
   distance-to-set functions and then to Hausdorff metrics, yielding
   `d_H <= d_H^G <= M d_H`.

7. **Continuity is transported, not inferred.** Translation plus equivalent
   renorming gives a `G`-homeomorphism of hyperspaces. The question's
   continuity assumption therefore transfers to the renormed action. This
   avoids the false claim that hyperspace continuity is automatic.

8. **Final theorem use.** The renormed space is a Banach `G`-space exactly as
   defined in the source, and the induced `CB` action is continuous. Source
   Theorem 5.1 applies verbatim. `G-AE` is invariant under `G`-homeomorphism.

## Residual review risk

The mathematical reduction is short and standard, which makes the source's
failure to use it surprising. A specialist should therefore re-check whether
the published terminology intended any nonstandard meaning of “affine
transformation.” The paper explicitly defines it by preservation of convex
combinations on the real linear space, and under that definition the packet's
linearization argument is valid.

The novelty search was bounded rather than exhaustive. No later resolution
was found, but priority should not be asserted without specialist review.
