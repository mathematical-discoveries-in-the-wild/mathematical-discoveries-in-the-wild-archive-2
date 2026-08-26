# Verification report

Verdict: **candidate likely valid; literature-implied full answer**.

## Primary-source checks

- `source_paper.pdf`, PDF page 3, contains the exact conjecture
  `f in Phi_1 \ Phi_2 => kappa_2^-(f)=+infinity` and states that only cases
  with additional conditions on the Schoenberg measure are proved there.
- `supporting_primary.pdf` is the complete twelve-page scan of Zoltan
  Sasvari, *On bounded functions with a finite number of negative squares*,
  Monatshefte fuer Mathematik 99 (1985), 223--234. Theorem 3.2 starts on
  journal page 229, continues through page 231, and gives exactly the signed
  Fourier-measure classification used in the packet.
- The proof of Theorem 3.2 explicitly concludes that the negative measure has
  support at the `k` distinguished characters and that the positive measure
  gives those points no mass.
- `supporting_restatement_1989.pdf`, journal page 319, restates the same
  theorem in plain language: bounded functions with `k` negative squares are
  Fourier transforms of measures negative at `k` points and nonnegative
  outside those points.

## Logical audit

1. `f in Phi_1` makes `t -> f(|t|)` positive definite on the line, so it is
   bounded. Consequently `g(x)=f(|x|)` is bounded on the plane.
2. If the integer supremum `kappa_2^-(f)` is finite, it is attained. Thus the
   planar translation-invariant kernel has exactly that many negative
   squares, matching Sasvari's definition.
3. Fourier--Stieltjes uniqueness transfers radial rotation invariance from
   `g` to the representing signed measure.
4. Uniqueness of Jordan decomposition transfers invariance separately to its
   positive and negative parts.
5. A finite rotation-invariant set in `R^2` is contained in `{0}`. Since
   `f notin Phi_2`, the negative part is nonzero and hence equals `a delta_0`.
6. The positive part has no atom at zero. If it assigned positive mass to a
   line through zero away from zero, countably many distinct rotated copies
   would be disjoint and have equal positive mass, contradicting finiteness.
7. Projection to a coordinate axis represents the line restriction, whose
   spectral measure is positive by Bochner uniqueness. Yet the projected
   measure has mass `-a` at zero, the contradiction.

No computation is part of the proof. The static audit script checks only the
presence of all stated dependencies and source artifacts; it is not offered
as mathematical evidence.

## Literature-status audit

Cheap indexes searched: `registry_index.tsv`, `solutions/index.tsv`,
`attempts/index.tsv`, and `proof_gaps/index.tsv`. Web searches used the exact
source title, exact conjectural notation, core keyword variants, and the
supporting theorem's title and DOI. No explicit later resolution was found.
Because the conclusion depends decisively on a pre-existing theorem but the
radial implication is agent-identified, the correct durable bucket is
`literature_implied_answers`.

## Human review focus

The reviewer should compare the packet's statement of Sasvari Theorem 3.2
against journal pages 229--231, then check the single measure-theoretic point
that rotation invariance forces the positive spectral measure to give every
line through the origin zero mass once its atom at zero is absent.

