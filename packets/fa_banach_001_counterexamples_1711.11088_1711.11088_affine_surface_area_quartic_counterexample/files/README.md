# 1711.11088 — quartic counterexample to the floating-function inequality

Status: candidate counterexample, likely valid, human review needed.

Model: GPT5.6.

Source: Li, Schütt, and Werner, *Floating functions*, arXiv:1711.11088, the conjecture following Corollary 1 on source PDF page 7.

## Result

The conjectured affine isoperimetric inequality for general convex potentials is false in every dimension.

For fixed n at least 1, set

    psi_epsilon(x) = |x|^2/2 + epsilon*x_1^4.

This potential is smooth, even, strongly convex, integrable after exponentiation, and has minimum zero. If R(epsilon) is the affine-surface-area side divided by the conjectured upper bound, then

    R(0) = 1,
    R'(0+) = 6/(n+2) > 0.

Hence R(epsilon) is greater than one for every sufficiently small positive epsilon.

## Stronger-than-literal feature

An additive constant already refutes the literal generalization: for psi_a=|x|^2/2+a, the ratio is exp(-2a/(n+2)), which exceeds one when a<0. The quartic perturbation rules out dismissing the failure as a missing height normalization: it keeps min psi=0 and changes the shape.

## Verification and novelty

The verification report checks the determinant, Gaussian moments, differentiation under the integral, normalization exponents, strictness, and scope relative to the distinct affine functional numbered (16) in the source. Bounded local-index and web/arXiv searches found no recorded answer to the exact conjecture. Novelty remains subject to specialist review.

## Files

- main.tex: full all-dimensional counterexample proof.
- solution_packet.pdf: compiled human-review packet.
- verification_report.md: adversarial proof audit.
- source_paper.pdf: official 24-page arXiv PDF.
- figures/open_problem_crop.png: source PDF page 7 crop containing the corollary and conjecture.

## Human review recommendation

Review as a likely valid full counterexample. The highest-value check is the first-variation calculation for the normalized ratio; every term is explicit and uses only the standard Gaussian moments E G_1^2=1 and E G_1^4=3.
