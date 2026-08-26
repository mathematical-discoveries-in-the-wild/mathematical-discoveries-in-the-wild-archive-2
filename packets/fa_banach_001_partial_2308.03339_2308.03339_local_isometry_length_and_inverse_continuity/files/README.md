# Rigidity reductions for nonseparable Scottish Book Problem 155

**Status:** substantial partial result, likely valid; the full nonseparable
bijection problem remains open.

For every locally distance-preserving surjection `U:X->Y` between Banach
spaces, the packet proves:

- `U` is globally 1-Lipschitz and preserves the length of every rectifiable
  path;
- continuity of `U^{-1}` at a single point forces `U` to be a global affine
  isometry;
- otherwise every complete local image is closed nowhere dense, yielding a
  density/category criterion that extends Mori's separable Baire argument;
- in particular a Baire-class-one inverse suffices.

It also constructs an exact uniformly locally isometric, injective,
globally contracting self-map of nonseparable `ell_infty`. This shows that
surjectivity is the genuine remaining rigidity input.

Files:

- `solution_packet.pdf`: theorem, proofs, obstruction, and construction.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: Mori's arXiv:2308.03339 source.
- `supporting_basso_2308.08400.pdf`: comparison with the stronger local
  isometry hypothesis.
- `figures/open_problem_crop.png`: source question and context.
- `code/crop_source.py`: reproducible crop.
- `code/verify_tent_embedding.py`: numerical transcription audit of the
  exact tent-wave construction.
- `tmp/`: build and rendered-page QA artifacts.

Bounded exact/current searches found no later full resolution. Novelty
confidence for the elementary partial theorem is moderate-low; validity
confidence is high.

