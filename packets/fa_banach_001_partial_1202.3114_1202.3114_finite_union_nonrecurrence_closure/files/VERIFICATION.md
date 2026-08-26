# Verification report

Status: `candidate_partial_result_likely_valid`

## Mathematical checks

- Checked that finite products of weakly mixing probability-preserving
  systems are weakly mixing.
- Checked that a finite product of non-degenerate Gaussian measures on the
  Hilbert direct sum is again non-degenerate and invariant under the
  block-diagonal operator.
- Checked the witness identity
  `m(A intersect T^{-n}A)=product_j m_j(A_j intersect T_j^{-n}A_j)`.
- Checked that for every union time at least one factor is zero.
- Checked the residue-class split: consecutive ratios in stream `j` are
  exactly `n_(k+r)/n_k`, so each stream meets the source's Theorem 1.1.
- Checked the explicit example: adjacent ratios equal `2` infinitely often,
  while two-step ratios tend to infinity.

## Upgrade audit

Five focused routes were examined: current literature; trimming shifted
rigidity; countable-product amplification; symbolic hard-core processes; and
finite-union closure with a bounded-gap superlacunary corollary. The first
three full-resolution routes hit genuine rate, measure, or weak-mixing
obstructions.

## Literature check

Exact-phrase, title-citation, lacunary non-recurrence, and shifted-rigidity
searches located the source and adjacent work but no later general resolution
or exact statement of the finite-union corollary.

## Rendering check

Compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`. The
three-page PDF was rendered at 150 DPI with Ghostscript and every page was
visually inspected. There are no clipped elements, margin overflows,
unresolved references, or broken formulas.

## Human-review recommendation

Review as a correct scoped partial result. The product lemma is elementary;
the main novelty claim is the explicit `r`-step ratio corollary and its strict
separation from the source's one-step hypothesis.
