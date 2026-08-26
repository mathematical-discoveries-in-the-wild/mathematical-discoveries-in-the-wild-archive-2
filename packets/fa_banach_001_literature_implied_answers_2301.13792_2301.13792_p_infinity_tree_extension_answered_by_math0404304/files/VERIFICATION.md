# Verification report

## Claim

The `p=infinity` endpoint question in arXiv:2301.13792 has a positive answer
with a universal norm bound, even for arbitrary tree shape and positive edge
lengths.

## Source audit

1. The exact question is item 1 of the final Remarks on printed/physical page
   23 of arXiv:2301.13792.
2. Brudnyi--Brudnyi define `lambda(M)` as the supremum, over all subsets
   `S` of `M`, of the least norm of a linear operator extending scalar
   Lipschitz functions from `S` to `M`.
3. Their Theorem 2.4 states, for direct `p`-sums of `n` arbitrary nontrivial
   metric trees and `p=1,infinity`, the upper bound `lambda <= c n` with an
   absolute `c`.  At `n=1`, this is precisely a universal bound for every
   metric tree.  The following paragraph attributes the one-tree theorem to
   Matousek.
4. Their definition of a metric tree explicitly permits arbitrary positive
   edge lengths.

## Deduction audit

- For edge lengths `ell_e`, the vertex Lipschitz seminorm is
  `max_e |Delta_e F|/ell_e`; on a tree, edge inequalities are equivalent to
  all-pairs path inequalities.
- Taking `ell_e=1/a_e` identifies this with the weighted endpoint seminorm
  `max_e a_e |Delta_e F|`.
- The trace seminorm equals the Lipschitz seminorm on the leaves: restriction
  gives one inequality and the scalar McShane extension gives the reverse.
- Apply the metric-tree linear extension theorem with `S` equal to the leaf
  set, and restrict the resulting function on the geometric tree to its
  vertices.
- If the source's endpoint is defined by a literal `p -> infinity` limit of
  `(sum W_e |Delta_e F|^p)^(1/p)`, use unit edge lengths instead.

## Scope

No assertion is made about `p=1`, the inhomogeneous norm, or the source's
non-radial conjecture in the open interval.  Those were separately attacked
and documented without a full resolution.

## Artifact QA

The source question on official PDF page 23, the definition of the linear
Lipschitz extension constant, and supporting Theorem 2.4 were independently
read from the two PDFs.  Setting one tree in Theorem 2.4 gives a universal
bound for every subset of an arbitrary positive-edge-length metric tree.

The interrupted build was not trusted.  `main.tex` was rebuilt on
2026-08-21, the resulting PDF was rendered page by page, and all pages were
visually inspected.  The source crop, formulas, references, and page breaks
are readable; no clipping, overlap, missing glyph, or placeholder remains.

## Provenance classification

Because the supporting theorem predates the source question and cannot claim
to answer it, the independently verified packet belongs under
`literature_implied_answers/`, not `literature_already_answered/`.
