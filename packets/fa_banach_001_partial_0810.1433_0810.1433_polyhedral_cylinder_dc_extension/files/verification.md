# Verification audit

## Source match

The crop reproduces the end of the radial-retraction proof and Remark 2.4(a)
on source page 7. It confirms that the open issue is removal or essential
weakening of the renorming assumption in Theorem 2.3.

## Proof obligations

1. **Piecewise-affine control.** A finite continuous piecewise-affine scalar
   function becomes convex, with either sign, after adding a sufficiently
   large sum of absolute values of the subdivision's facet equations. This
   control is convex and globally Lipschitz. Finitely many coordinate controls
   combine to control a finite-dimensional vector map.
2. **Polyhedral projection.** Euclidean projection onto a closed convex
   polyhedron is 1-Lipschitz. On the normal region of each face it is the
   affine orthogonal projection onto that face's affine hull. Finitely many
   faces give a finite piecewise-affine decomposition.
3. **Lifted retraction.** A surjection onto a finite-dimensional space has a
   continuous linear right inverse. Formula (1) has `TR=pi_K T` and equals the
   identity on `T^{-1}(K)`.
4. **D.c. stability.** Linear pre/postcomposition, finite sums, and addition of
   affine maps preserve d.c. mappings; the controls scale by the operator
   norms.
5. **Composition exhaustion.** The globally Lipschitz retraction sends each
   bounded ball into a bounded convex part of `C`. The assumed bounded-part
   Lipschitz control verifies every hypothesis of source Lemma 1.12.

## Novelty and limitation

Cheap indexes and bounded arXiv searches found no later exact solution of
Remark 2.4(a) through 12 August 2026. The result is deliberately narrower than
Theorem 2.3 and may be unindexed folklore. It neither handles arbitrary convex
domains nor proves that the source's original local condition alone suffices.

## Build and visual QA

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
completed after two passes with no remaining warnings, undefined references,
or overfull/underfull boxes. The four-page PDF was rendered at 110 dpi and
every page was visually inspected. The proof, bibliography, and source crop
are legible and unclipped.
