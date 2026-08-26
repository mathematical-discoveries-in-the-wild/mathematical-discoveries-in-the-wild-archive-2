# Smoothing-unitary counterexample to the claimed spectral inequality

Status: candidate counterexample, likely valid; send to human review.

Source: Duván Cardona, *Spectral inequalities for elliptic
pseudo-differential operators on closed manifolds*, arXiv:2209.10690.

## Claimed contribution

Theorem 1.4 of the source is false under its stated interpretation of
`E(x,xi)>0` as positivity of the principal symbol (the interpretation used
again in the source proof). On the symmetric closed manifold `S^1`, for every
order `nu>0` and a proper open sensor arc `omega`, there is a positive,
self-adjoint, invertible elliptic operator `E in Psi^nu_{1,0}(S^1)` with the
same positive principal symbol as `(I-d^2/dx^2)^{nu/2}` and with a normalized
smooth eigenfunction supported outside `omega`. The right side of the claimed
spectral inequality is then zero while the left side is one.

The construction is exact. A Householder unitary `U=I-2P_w`, differing from
the identity by a rank-one smoothing operator, sends the constant eigenfunction
of the model elliptic operator to a chosen bump function `f`. Conjugating by
`U` preserves positivity and the spectrum, while changing the eigenfunction to
`f`. Since smoothing perturbations do not change the principal symbol, all
stated microlocal hypotheses remain true.

## Relation to the extracted open problem

Section 3, page 18 asks whether the restriction `rho >= 1-delta` can be
removed on manifolds with symmetries under a suitable symbol-positivity
condition. This counterexample proves that positivity of the operator together
with positivity of the principal symbol is insufficient even in the already
allowed `(rho,delta)=(1,0)` class. It does not refute the logically weaker
existential wording “under a suitable positivity condition.”

A separate status packet records that Cardona–Delgado–Ruzhansky,
arXiv:2209.12092, gives an affirmative compact-Lie-group theorem under the
stronger assumption that the global matrix-valued symbol is nonnegative.
This packet does not claim that the counterexample satisfies that stronger,
quantization-specific condition.

## Verification

- `source_paper.pdf` is a local compilation of the exact stored arXiv source.
- `figures/open_problem_crop.png` is a real full-width render from physical
  page 18 and contains both source open problems in full.
- The proof is algebraic; no numerical computation is used.
- `VERIFICATION.md` checks the Householder identities, smoothing-class
  preservation, positivity, eigenfunction equation, and final contradiction.

## Attempt history

1. The boundary-value problem has an immediate Navier subcase: powers of the
   Dirichlet Laplacian retain its eigenfunctions. This does not reach the
   clamped/polyharmonic boundary conditions asked for and was not promoted.
2. The stronger finite-rank smoothing-conjugation obstruction was then found
   and upgraded to the complete counterexample recorded here.

## Bounded novelty check

On 2026-08-11 the arXiv/web search covered the exact source title and id with
`correction`, `erratum`, and `counterexample`, plus the phrases `spectral
inequality elliptic pseudo-differential counterexample`, `polyharmonic spectral
inequality boundary`, and `Lebeau-Robbiano higher-order boundary`. No correction
or matching smoothing-unitary counterexample was found. The close papers
arXiv:2209.12092 and arXiv:2309.02181 were inspected. The former answers the
source's second open problem under stronger global-symbol positivity; the
latter concerns fourth-order boundary problems. Novelty confidence is
moderate: finite-rank smoothing conjugation is standard operator folklore, but
this exact application was not located.

## Human review focus

Check that the source's symbol hypothesis is indeed the principal-symbol
hypothesis stated in Theorem 1.4 and used in its proof. Then verify that
`UAU-A` is smoothing and that the chosen bump eigenfunction belongs to the
spectral subspace at threshold one. These are the only decisive points.

