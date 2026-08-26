# Verification report

Verdict: likely valid exact stabilization theorem; complexity counterexample
is conditional on the standard `P != NP` interpretation.

## Formal proof checks

- If `G=V V*` has rank `r`, then `I +/- epsilon H` is positive definite for
  all sufficiently small epsilon and every fixed Hermitian `H`.
- The diagonal perturbation is `v_i* H v_i`, which is the trace pairing with
  `v_i v_i*`. Thus an extreme correlation matrix forces these projectors to
  span `Sym_r` or `Herm_r` over the reals.
- The corresponding real dimensions are exactly `r(r+1)/2` and `r^2`.
- For subcorrelations, only diagonal inequalities at value one are active.
  All inactive inequalities stay strict under a sufficiently small two-sided
  perturbation, so the same rank bound follows.
- The explicit real vectors `e_i` and `(e_i+e_j)/sqrt(2)` have projectors
  spanning `Sym_r`. Adding `(e_i+i e_j)/sqrt(2)` spans `Herm_r` in the complex
  case. Appending duplicate vectors does not destroy spanning or rank.
- A full-correlation extreme point is also subcorrelation-extreme: a convex
  average of diagonal entries bounded above by one can equal one only when
  every summand has unit diagonal.
- For sharpness of the absolute support functions, diagonal entries rule out
  representing the chosen extreme correlation matrix with negatively signed
  rank-`d` matrices. Strict separation then gives a norm gap.
- `rho_R(n) <= d` is equivalent to `n < (d+1)(d+2)/2`; `rho_C(n) <= d` is
  equivalent to `n < (d+1)^2`. Intersecting these with the conjecture's claimed
  hard ranges gives exactly the displayed overlap bands.
- The source identity with the Hermitian block matrix transfers the sufficient
  stabilization threshold to the rectangular norm.

## Complexity audit

The full elliptope and subelliptope support functions are semidefinite
programs; the absolute value requires two objectives. Complex Hermitian SDPs
can be realified with polynomial overhead. This establishes computation to
arbitrary precision in polynomial time, matching the source paper's own
claim. It does not establish a rational exact-output algorithm.

An in-P problem can be NP-hard if `P=NP`; the packet therefore distinguishes
the unconditional SDP theorem from the conventional complexity disproof.
Likewise, the overlap is infinite only when `d` is allowed to scale. For a
single fixed `d`, it contains finitely many dimensions.

## Literature and novelty audit

The bounded search covered local title/keyword/claim indexes, arXiv and web
queries for the exact paper title and Conjecture 2.18, and the phrases
`Grothendieck d-norms NP-hard`, `stabilization rank correlation matrices`, and
`extreme bipartite correlation matrices`. It found the classical extreme-rank
theorems and no explicit erratum or correction. The source's currently
available author copy still displays the `+1` rank bound.

## Scope

The exact if-and-only-if characterization is for universal stabilization of
the symmetric `gamma,d` and `Gamma,d` norms. The rectangular theorem in this
packet is only sufficient; sharper bounds from bipartite-correlation geometry
may exist. No hardness result is claimed in the corrected strict range.
