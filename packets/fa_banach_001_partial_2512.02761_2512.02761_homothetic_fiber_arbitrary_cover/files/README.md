# Arbitrary covers for aligned homothetic fiber profiles

**Status:** candidate substantial partial result, likely valid; human review
requested.

Conjecture 1.4 of arXiv:2512.02761 is a sharp local Liakopoulos--Meyer
inequality for an arbitrary uniform cover.  The source proves it when the
complementary cover is 1-reducible and in one special unconditional case.

This packet proves the exact conjectured inequality for every arbitrary cover
whenever the fiber-volume function over `H_sigma` has aligned homothetic
superlevel sets:

`F(x) = M psi(||x||_C)`.

The proof is short and exact.  Liakopoulos's geometric uniform-cover
inequality controls the common level-set body `C`; Lyapunov's moment
inequality controls the profile `psi`.  The result includes generally
nonunconditional, nonconstant-fiber bodies

`K = {(x,y): ||x||_C + ||y||_B <= 1}`

and applies to the triangle 2-cover `{12,13,23}`, the smallest cover excluded
by the source's reducibility hypothesis.

Files:

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/source_conjecture_crop.png`: source Conjecture 1.4.
- `code/crop_source.py`: reproducible source-page crop.
- `code/verify_triangle_factor.py`: exact symbolic check for the first
  nondecomposable cover and the `ell_1`-sum family.
- `tmp/`: build and rendered-page QA artifacts.

The unrestricted conjecture remains open.  Exact and current-literature
searches found no later resolution or the homothetic-profile theorem stated
here; novelty confidence is moderate and provisional.

