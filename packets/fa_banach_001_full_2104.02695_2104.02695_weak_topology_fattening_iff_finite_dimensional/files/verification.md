# Verification report

Verdict: `likely_valid`, pending human review of the cited fragmentation theorem.

## Claim audited

For a Banach space `X`, the additive group with topology `sigma(X,X*)` is
fattening if and only if `X` is finite-dimensional.  If `X` is
infinite-dimensional, `B_X` is the explicit compactivorous but not strongly
compactivorous witness.

## Definition audit

1. In an additive abelian group, the source expression `gAh` is a single
   translate of `A`; the proof uses exactly such translations.
2. Fragmentation supplies an ambient weakly open `V` with `K cap V` nonempty,
   matching the source definition rather than merely supplying an arbitrary
   subset of `K`.
3. Strong compactivorousness asks for one closed neighbourhood `U` that works
   for every compact subset.  The proof refutes the property for every weak
   neighbourhood, which is stronger.

## Dependency audit

The only non-elementary input is the classical theorem that every weakly
compact subset of a Banach space is fragmented by the norm.  It applies to
arbitrary Banach spaces and arbitrary weakly compact subsets; no Schur,
separability, reflexivity, or metrizability hypothesis is needed.  The packet
cites Jayne--Namioka--Rogers, *Topological Properties of Banach Spaces*, Proc.
London Math. Soc. (3) 66 (1993), 651--672.

Only the weakest consequence is used: for any nonempty weakly compact `K` and
`epsilon > 0`, there is a nonempty relatively weak-open part of `K` having norm
diameter below `epsilon`.

## Proof audit

- With diameter below one and `k0` in the selected piece, every `k-k0` has norm
  below one.  Thus the translated piece lies in `B_X`.
- A basic weak neighbourhood contains `intersection ker(x_j*)`.  Finitely many
  functionals cannot separate every nonzero vector in an infinite-dimensional
  space, so this common kernel is nonzero and closed under arbitrary scaling.
- Selecting `||z|| > 1` in the common kernel puts `{-z,z}` inside the given
  neighbourhood.  This finite set is weakly compact.
- Translation preserves its diameter `2||z|| > 2`, while every subset of `B_X`
  has diameter at most two.  Hence no translate fits.
- In finite dimension, weak and norm topology agree.  Applying
  compactivorousness to a compact ball yields a translate of a neighbourhood
  inside `E`, from which a closed strong witness neighbourhood is obtained.

## Edge cases

- The proof covers real and complex scalars.
- The zero and all finite-dimensional spaces fall under the locally compact
  direction.
- No closedness, convexity, measurability, or weak compactness of `B_X` is
  required by the definitions.
- The strict choice `||z|| > 1` avoids the diameter-equality boundary case.

## Novelty audit

The exact arXiv id, title, and combinations of `compactivorous`, `fattening`,
`weak topology`, and `without the Schur property` were searched in the run
indexes and through bounded web/arXiv queries on 9 August 2026.  No exact later
resolution surfaced.  This is a bounded search, not a guarantee of novelty.

No computational verification is relevant: the result is a structural
argument, and every step above was checked directly against the definitions.
