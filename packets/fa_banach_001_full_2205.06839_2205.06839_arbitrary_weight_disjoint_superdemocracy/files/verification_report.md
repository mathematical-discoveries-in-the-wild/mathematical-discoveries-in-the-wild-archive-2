# Verification report

verdict: likely valid

result checked: arbitrary-weight disjoint superdemocracy implies
arbitrary-weight superdemocracy for the semi-normalized Schauder bases and
set weights of arXiv:2205.06839, Definition 1.2.

## Hypothesis audit

1. The source works with a semi-normalized Schauder basis, so
   `M = sup ||e_n|| < infinity` and `M* = sup ||e_n*|| < infinity` are
   available.
2. The source weight takes values in the totally ordered extended interval
   `[0,infinity]`, is zero at the empty set, and is strictly positive at
   every nonempty set. No monotonicity or additivity was used.
3. The disjoint-superdemocracy hypothesis was invoked only for genuinely
   disjoint finite supports and in the direction dictated by the weight
   inequality.

## Proof audit

1. If all signed constant-coefficient sums are bounded by `D`, every
   nonempty denominator has norm at least `1/M*`, by applying any coordinate
   functional indexed by its support. Thus the ratio is at most `D M*`.
2. If signed sums are unbounded, deleting a fixed finite support cannot make
   all remaining signed sums bounded: restoring the deleted coordinates
   changes every sum by at most `|F| M`.
3. A fresh signed sum of norm greater than `t+M` exists outside `F`. The first
   partial sum whose norm exceeds `t` has norm at most `t+M`, because its last
   increment has norm at most `M`. This proves the bridge lemma without any
   monotonicity assumption on partial-sum norms.
4. Under the negation of the claimed bound,
   `a > (K^2 + K M M*) b` and `b >= 1/M*` imply
   `K b + M < a/K`. The bridge lemma with `t=K b` therefore gives
   `K b < c < a/K` on a support disjoint from both original supports.
5. If `w(A) <= w(C)`, disjoint superdemocracy gives `a <= Kc < a`, so total
   ordering forces `w(C) < w(A)`. Hence `w(C) < w(A) <= w(B)`, and the
   disjoint comparison of `C` with `B` gives `c <= Kb`, contradicting the
   bridge inequality.
6. The same ordering argument remains valid when one or more weights equal
   infinity.
7. Empty supports are harmless: the numerator is zero when `A` is empty; if
   `A` is nonempty and `w(A) <= w(B)`, then `B` cannot be empty.
8. The proof works over both real and complex scalars because all signs have
   modulus one.
9. No Schauder expansion or partial-sum projection is used. The proof remains
   valid for every uniformly bounded biorthogonal system; the source's
   Schauder-basis hypotheses are more than sufficient.

## Scope and checks

- No computational experiment or external theorem is used as proof.
- The source question and definitions were checked directly in the local
  TeX source and source PDF.
- The final PDF was rendered page by page; no clipping, overlap, missing
  glyph, broken reference, or LaTeX warning remains.
- Bounded local-index, local-source, exact-phrase, and forward-citation
  searches found no exact later solution as of 2026-08-09. Crossref and
  OpenAlex returned no citing works for the published DOI. Semantic Scholar's
  sole returned item was checked directly and does not actively cite or
  discuss the source question. Novelty remains subject to expert literature
  review.

review focus: verify the fresh-support bridge lemma and the strict ordering
`w(C) < w(A) <= w(B)`; these are the only non-routine steps.

