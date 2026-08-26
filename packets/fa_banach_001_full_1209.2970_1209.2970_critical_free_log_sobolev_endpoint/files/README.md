# Critical local free log-Sobolev endpoint

Status: `candidate full solution, likely valid`.

## Result

Open Problem 1 in Section 6 of Popescu's arXiv:1209.2970 has a positive
answer. For probability measures `mu, nu` on `[-2,2]`,

`H(mu,nu) <= C (integral |Hmu-Hnu|^(3/2) d alpha)^(4/3)`.

Equivalently, the source's weighted sine-series inequality holds at
`p=3/2`. The source already proves failure for every `p<3/2`, so the smallest
admissible exponent is exactly `3/2`; this also disposes of Open Problem 2.

The new observation is conformal. Weighted duality produces an
`L^3(dt/sin t)` trace inequality. The map from the upper half-disk to a fixed
strip sends `dt/sin t` to ordinary Lebesgue measure, preserves Dirichlet
energy, and turns the coefficient norm into the strip trace `H^(1/2)` norm.

## Files

- `solution_packet.pdf`: self-contained proof packet.
- `main.tex`: packet source.
- `source_paper.pdf` and `source_paper.tex`: original paper.
- `figures/open_problem_crop.png`: source page 16, Open Problems 1--2 and the
  equivalent sine-series formulation.
- `VERIFICATION.md`: proof, search, and artifact audit.
- `code/numerical_sanity.py`: optional finite-polynomial sanity check; not used
  in the proof.

## Review recommendation

Recommended for expert review as a full solution. The two points most worth
checking are the Abel-regularized logarithmic-energy identity for arbitrary
measure differences and the zero-frequency part of the strip trace estimate.
Neither is a conditional dependency.
