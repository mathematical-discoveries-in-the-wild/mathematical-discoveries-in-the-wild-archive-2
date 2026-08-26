# Structural-stability spectral obstructions

Status: `candidate_substantial_partial_likely_valid`

Source: Nilson C. Bernardes Jr. and Ali Messaoudi, *Shadowing and structural stability in linear dynamical systems*, arXiv:1902.04386 (2019), Questions 13, 15, and 16.

This packet proves two general necessary conditions that sharpen the open terrain. Ordinary structural stability forces `I-T` to be onto; consequently an expansive structurally stable operator has `1` in its resolvent. Strong structural stability on a complex Banach space excludes every unit-circle eigenvalue of the adjoint. Combined with Theorem 6(a) of the source paper, this proves that every expansive strongly structurally stable operator is hyperbolic, without the weighted-shift restriction in source Proposition 14.

For the original ordinary-stability Question 15, any counterexample is reduced to a very narrow form: all unit-circle spectral points are nontrivial residual points, hence adjoint eigenvalues, and the conjugacies witnessing stability cannot be normalized close to the identity by the routes tested here. The packet also gives a conditional completion if structural stability passes to every unimodular rotation of `T`.

The full ordinary-stability questions and the `GL(X)`-relative question remain open.

## Files

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/question_13_crop.png`: source Question 13.
- `figures/questions_15_16_crop.png`: source Questions 15 and 16.
- `code/crop_source.py`: reproducible source-page crop script.
- `tmp/`: LaTeX and rendering intermediates.

## Verification and review recommendation

The main checks are: (i) the fixed-point argument for constant affine perturbations; (ii) the scalar cutoff's global boundedness and Lipschitz bound; and (iii) the use of uniform expansivity to turn a unit-circle spectral point into an adjoint eigenvalue. Human review is recommended, with highest attention on the conjugacy orientation in the resonant recurrence.

The bounded novelty search covered the run indexes and exact/near-exact web and arXiv phrases through 2026-08-17, including arXiv:2101.02989, 2206.00353, and 2403.02843. No exact match was found; novelty confidence remains provisional.
