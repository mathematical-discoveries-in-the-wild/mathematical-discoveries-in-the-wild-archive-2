# Uniform-L2 stereographic scaling limits: a complete classification

Status: **candidate full resolution, likely valid; human review required**.

Zahariev's arXiv:1701.05569 asks whether its stereographic infinite-volume
construction contains non-Gaussian measures.  The packet resolves the scope
ambiguity in that question.

1. The unrestricted compactness construction does contain non-Gaussian
   limits.  A uniformly positive bounded cosine tilt of one transported field
   coordinate converges to the corresponding non-Gaussian tilt of the free
   massive field.
2. Every translation-invariant limit satisfying the source's uniform
   `L1/L2` density estimates equals the free massive Gaussian.  In particular,
   all `O(d+1)`-invariant bounded self-interaction examples advertised as
   Euclidean/Glimm--Jaffe theories are Gaussian.

The second assertion follows because the source's uniform estimate passes to
the common weak limit and gives an `L2` Radon--Nikodym density relative to the
free Gaussian.  The massive free field is strongly mixing under translations,
so an invariant density must be constant.

## Files

- `main.tex` and `solution_packet.pdf`: complete construction and theorem.
- `VERIFICATION.md`: adversarial mathematical and render audit.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source title and exact abstract question.
- Attempt history:
  `runs/fa_banach_001/attempts/1701.05569_uniform_l2_ergodic_gaussianity.md`.

## Novelty check

Cheap-index and bounded exact-title, exact-question, citation, and keyword
searches through 2026-08-13 found no explicit resolution of the source's exact
scheme.  arXiv:2311.04137 constructs a genuinely non-Gaussian sphere-to-plane
model by a different stochastic-quantization compactness mechanism;
arXiv:2502.07546 obtains nontrivial connected functions after a different
renormalization.  Neither supplies this classification.  Novelty remains
provisional pending specialist review.

## Human-review recommendation

Check the transport identity for the cosine tilt, the limiting `L2`
domination lemma, the free-field mixing calculation, and the precise scope of
the source's Euclidean-invariance proposition.
