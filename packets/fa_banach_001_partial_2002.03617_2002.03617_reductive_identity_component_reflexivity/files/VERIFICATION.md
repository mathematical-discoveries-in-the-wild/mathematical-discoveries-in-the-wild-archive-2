# Verification

## Source and dependency checks

- Source PDF checked: arXiv:2002.03617v3, PDF page 7, Conjecture 1.5.
- Source Corollary 3.10 checked on PDF pages 13--14: dense restriction
  `O_exp(G) -> O_exp(G_0)` with connected linear `G_0` implies that
  `O_exp(G) -> O(G)` is an Arens--Michael envelope.
- Source Proposition 3.6 checked on PDF page 11: this envelope property is
  equivalent to holomorphic reflexivity of `O(G)`.
- Source Corollary 3.5 checked on PDF page 11: a subgroup on which every
  exponential-type function is constant lies in the generalized linearizer.
- Source Proposition 4.1 checked on PDF page 15: holomorphic reflexivity for a
  Stein group forces the generalized linearizer to be trivial.
- arXiv:1903.08080, Theorem 5.9, checked: for connected linearly complex
  reductive `H`, `O_exp(H)=R(H)` as locally convex algebras.
- arXiv:2304.00507, Theorem 1, checked on PDF page 1: for every connected
  linear complex Lie group, `R(H)` is contained and dense in `O_exp(H)`.

## Internal proof audit

- Translation invariance gives the algebraic coproduct explicitly: for a
  regular `a`, its finite right-translate span has a basis `v_i`; evaluating
  at finitely many points expresses the coefficient functions in that
  expansion as linear combinations of left translates of `a`.  Thus both
  tensor factors lie in the restriction algebra.
- The common-kernel argument was checked at the level of finite-dimensional
  subcoalgebras.  Zariski Noetherianity reduces the trivial intersection to
  finitely many kernels.  Their direct sum is a faithful algebraic
  representation whose matrix coefficients lie in the Hopf subalgebra.
- In characteristic zero, a faithful morphism of affine algebraic groups is a
  closed immersion.  Its matrix entries together with inverse-matrix entries
  generate the coordinate ring; the latter are present because the Hopf
  subalgebra is antipode invariant.
- The source counterexample with identity component `C^x` does not contradict
  the theorem: the source proves that all exponential-type functions are
  constant on that component, so its generalized linearizer is nontrivial.
- No numerical computation is used or needed.

## Novelty audit

- Cheap run indexes had no hit for arXiv:2002.03617 or the reductive subcase.
- Exact arXiv/web searches and the bounded citation neighborhood through 2025
  found the source and one later HFG-Hopf citation, but no statement of this
  theorem.
- The 2023 density note supplies a dependency, not the new restriction-image
  argument.

## Render audit

- The final PDF was compiled with all intermediates in `tmp/`, text-extracted,
  rendered page by page, and visually inspected on 2026-08-11.
- The source crop includes the complete statement of Conjecture 1.5 and its
  listed previously known cases.

