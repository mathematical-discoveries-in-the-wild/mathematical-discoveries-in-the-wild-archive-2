# Counterexample to the proposed Gaussian stability conditions

This packet gives a candidate full counterexample to the sufficient
conditions proposed in Appendix C of arXiv:2110.06008.

Define, on the full fundamental domain `D_+`,

`z2(x,y) = 1/2 - [4x(1-x)]^100/(8y^2)` and
`z1(x,y) = 1/2 - x z2(x,y)`.

The selector satisfies every displayed condition in the source, converges to
the hexagonal deep hole, and even has `partial_x z2 = 0` at `x=1/2`, the extra
boundary-criticality property discussed by the authors.  Nevertheless, at

`x=9/20`, `y=sqrt(319)/20`, `alpha=1`,

its theta value is strictly larger than the hexagonal deep-hole value.  A
directed-interval `5 x 5` lower sum and an analytic Gaussian tail bound certify
a reversed gap greater than `0.003847`.

## Files

- `main.tex` / `solution_packet.pdf`: theorem, proof, certificate, and scope.
- `verification.md`: adversarial proof audit.
- `code/check_counterexample.py`: reproducible interval certificate.
- `source_paper.pdf`: arXiv:2110.06008.
- `figures/open_problem_crop.png`: Appendix C conjecture and conditions.

## Status

`counterexample_likely_valid`; human review by an analyst familiar with theta
functions and rigorous numerics is recommended.

