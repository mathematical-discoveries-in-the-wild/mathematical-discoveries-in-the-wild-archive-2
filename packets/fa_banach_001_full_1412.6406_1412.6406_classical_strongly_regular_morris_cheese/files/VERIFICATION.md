# Verification report

Verdict: **likely valid candidate full answer**, pending specialist review.

## Scope checked

The theorem answers only the existential sentence “Can `R(X_B)` be regular?”
in Question 1 of arXiv:1412.6406.  It strengthens “regular” to “strongly
regular” and retains all properties of source Theorem 8.3.  It makes no claim
about the word “Must,” Question 2, or Question 3.

## Proof checks performed

1. **Cayley geometry.** For `Phi_a(z)=(a-z)/(a+z)`, the unit circle maps to
   the imaginary axis, the unit disk to the right half-plane, `a` to zero,
   and `-a` to infinity.  On a fixed small disk about zero, `Phi_a^{-1}` and
   its derivative have rotation-independent upper and lower bounds.  Möbius
   images of disks remain disks, so radius and boundary-gap ratios are
   comparable by an absolute constant.

2. **Antipodal removability.** Izzo's weighted local function is
   `h(w)=f(rho/w)` with `f(0)=1` and its first two derivatives zero.  Hence
   `h(w)=1+O(w^-3)` at infinity.  Therefore `h(Phi_a(z))` is removable at
   `z=-a`, and multiplying by `(z-a)^3` gives the claimed local approximation.

3. **Budget counts.** Interior covers cost `O(n^2 delta_n/sigma_n)` after
   weighting; boundary covers cost `O(delta_n/rho_n^2)`.  The scale and error
   sequences are fixed first, and each free `delta_n` can then be made small
   enough for summability.  No circular dependence is used.

4. **Classicalisation invariant.** A current aggregate disk of radius `R`
   containing allocated original disks has `R <= sum r_i`.  If `d_*` is the
   least original gap and `e` its own gap, containment gives
   `e <= d_i <= e+2R <= d_*+2R`.  With total original weight `theta<1/6`,
   `R>=d_*/4` would imply `1<=36 theta R<=36 theta^2<1`.  Thus `e>d_*/2`, so
   no aggregate reaches the outer circle.  The same inequalities give the
   factor-nine weighted bound after summing disjoint allocations.

5. **Strong-regularity inheritance.** The packet does not rely on a blanket
   hereditary claim.  It passes separately the two ideal relations
   `closure(J_x) superset M_x^3` and `closure(M_x^2)=M_x` by restriction to a
   compact subset, exactly as in Izzo's subset lemmas.  They imply
   `closure(J_x)=M_x`.

6. **Nonzero derivation.** The source Cauchy estimate applies to the final
   weighted family.  For a point `q` in a deleted disk,
   `f(z)=1/(z-q)` and `g(z)=z-q` give integral `-2 pi i`, so the derivation is
   not merely bounded but nonzero.

## Artifact checks

- The source paper was compiled from the repository's exact arXiv source
  release and the open-question crop was rendered from page 18.
- The decisive Izzo paper was likewise compiled from its exact local arXiv
  source release.
- The packet is compiled with all intermediates in `tmp/` and its rendered
  pages are visually inspected.

## Highest-priority expert checks

- Confirm that Izzo's rational approximants remain admissible after the
  half-plane discard and Cayley composition.
- Confirm that the allocation invariant is available at limit stages of the
  chosen standard classicalisation implementation.
- Check the cited lemma numbering against the final published revision of
  arXiv:2211.14684.

