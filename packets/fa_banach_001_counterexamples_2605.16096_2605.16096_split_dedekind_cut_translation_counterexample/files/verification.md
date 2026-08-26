# Verification record

## Mathematical audit

1. **Intrinsic topology.** Proposition 4.4(1) of arXiv:2605.16096 identifies
   the intrinsic median topology of a chain with its interval topology.
   Therefore `X=Q` belongs to the source class `(T^m_2)`.
2. **Compactification.** Splitting `alpha=sqrt(2)` in the compact extended real
   order leaves a complete order with first and last points, hence a compact
   LOTS.  It is second countable and therefore metrizable.
3. **Dense proper embedding.** Because `alpha` is not rational, the subspace
   topology on `Q` is its usual order topology.  Rational points approach both
   new cut points from their respective sides, so `Q` is dense.  The inclusion
   is order preserving and hence median preserving.
4. **Topological median.** In a LOTS, `min` and `max` are continuous; the median
   is the lattice term
   `max(min(x,y),min(y,z),min(z,x))`.
5. **Action on the dense algebra.** The discrete group `Z` acts jointly
   continuously on `Q` by increasing order (hence median) automorphisms.
6. **Failure of extension.** If `q_j` increases to `alpha` and `r_j` decreases
   to `alpha`, then in the split order `q_j -> alpha^-` and
   `r_j -> alpha^+`, while both translated sequences tend to the unique
   unsplit point `alpha+1`.  Continuity forces the generator to collapse the
   split pair; a group translation must be a homeomorphism.

## Citation audit

- Question 7.2 occurs on page 25 of the locally compiled official source for
  arXiv:2605.16096.
- The cited ordered theorem is stated in arXiv:2512.17314 under the hypothesis
  that the proper compactification already admits extended continuous
  `g`-translations.
- The underlying Theorem 3.18 in arXiv:2201.13426 likewise assumes the ordered
  compactification is a `G_discr`-compactification, equivalently that its
  ordered proximity is `G`-invariant.  Its conclusion upgrades this to a
  jointly continuous `G`-compactification.  It does not prove invariance of
  every proper compactification.

## Build and visual QA

The source PDF was compiled from the downloaded official arXiv source with:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/private/tmp/median2605_build median150526.tex
```

The solution packet is built with the analogous command from this directory.
The final packet has four pages.  `tmp/main.log` contains no unresolved
references, multiply defined labels, overfull/underfull boxes, or LaTeX/package
warnings.  PyMuPDF extracted nonempty text from every page.  All four pages
were rendered at 140 dpi and inspected individually: the source crop is fully
readable, the split-cut diagram is unobstructed, all displayed formulas are
correct (including both translated limits), and no clipping or overlap was
found.
