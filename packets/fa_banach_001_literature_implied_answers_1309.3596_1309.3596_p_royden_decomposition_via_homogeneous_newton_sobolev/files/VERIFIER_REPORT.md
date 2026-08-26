# Verifier report

Verdict: likely valid literature-implied full answer; human review requested.

## Claim audited

Under the standing assumptions of Lucia--Puls (complete, locally compact,
noncompact, doubling, positive finite ball measures, and a `(1,p)`-Poincare
inequality with `1<p<infinity`), Conjecture 5.1 follows from Theorem 1.1 of
Shanmugalingam, arXiv:2311.17356.

## Logical audit

1. The finite-domain minimizers `h_i` have a uniform supremum bound and
   globally bounded Dirichlet energy. Since `h_i=f` outside `Omega_i` and
   minimizes energy inside, `||h_i||_D <= ||f||_D`. Thus
   `u_i=f-h_i` is bounded in the homogeneous quotient.

2. The supporting theorem explicitly gives *tail* convex combinations, not
   merely arbitrary convex combinations. Therefore their local-uniform limit
   remains `g=f-h`.

3. Strong convergence in the homogeneous quotient only determines a limit up
   to constants. Poincare on a fixed base ball normalizes representatives;
   local-uniform convergence of the same convex combinations makes the
   normalizing constants Cauchy and identifies the quotient limit with `[g]`.
   This justifies convergence of the Dirichlet seminorm of `v_k-g` to zero.

4. A finite-domain error is Newtonian and compactly supported but may have a
   quasi-everywhere boundary representative rather than a globally continuous
   one. The packet does not assume this away. For each tail combination
   `v_k`, all component domains contain `Omega_k`, so `v_k` is continuous on
   `Omega_k`. Bounded compactly supported Lipschitz density in `N^{1,p}`, plus
   a cutoff supported inside `Omega_k`, produces a genuine `BD_c^p` function
   equal to `v_k` on an expanding compact set and arbitrarily close in energy.
   The product upper-gradient estimate is sufficient.

5. The resulting approximants are uniformly bounded (use bounded Lipschitz
   approximants obtained by truncation), locally uniformly convergent to `g`,
   and energy convergent. This matches the source definition of `BD^p`
   convergence, including its uniform-boundedness clause.

6. For arbitrary continuous data, the p-harmonic limits must be chosen
   compatibly. A diagonal extraction across the countable approximating family
   gives one exhaustion subsequence for every datum. Finite-domain comparison
   then passes pointwise to all pairwise limits and yields a uniform Cauchy
   sequence on the whole space. The boundary trace follows by a three-term
   epsilon estimate.

## Scope checks

- The proof resolves the two existence assertions of Conjecture 5.1.
- It does not prove uniqueness of a nonlinear `g+h` decomposition. The source
  mentions uniqueness in its proposed stronger decomposition, but uniqueness
  is not needed for the conjecture.
- If the p-harmonic boundary is empty, the continuous-data assertion is
  vacuous and the `BD^p` assertion is satisfied, for example, by `h=0` on the
  boundary level; the exhaustion proof remains available.
- No global `(p,p)`-Sobolev inequality or fixed-radius lower volume bound is
  used.

## Literature audit

Theorem 1.1 and the definition of tail convex-combination subsequence were
checked in the supporting PDF and source. The supporting paper does not cite
arXiv:1309.3596 or advertise the Royden-boundary implication. Local run
indexes and bounded arXiv searches for the exact id and core phrases found no
explicit prior resolution. Classification as `literature_implied_answer` is
appropriate; no exhaustive novelty claim is made.

## Recommended reviewer focus

Check the precise bounded `Lip_c` density citation used in the gluing lemma,
the Poincare normalization argument modulo constants, and the simultaneous
diagonal selection for continuous boundary data. These are the only steps not
already explicit in the two source papers.
