# arXiv:1610.01659 — even-power positivity without square positivity

Status: `candidate_counterexample` to the continuity-removal part of Question
2.9, pending expert review.

Source: Maria Infusino and Salma Kuhlmann, *Infinite dimensional moment
problem: open questions and applications*, arXiv:1610.01659 / Contemporary
Mathematics 697 (2017), Question 2.9 on printed page 6.

## Result

For every fixed integer `d >= 2`, the packet constructs a linear functional
`L` on `R[x]` such that

- `L(q^(2d)) > 0` for every nonzero polynomial `q`, but
- `L(x^2) < 0`.

Thus positivity on sums of `2d`-th powers does not imply positivity on sums of
squares when continuity is removed. The functional cannot have a nonnegative
representing measure.

## Main mechanism

The moments are constructed recursively. The initial two-variable Hankel form
is

`a^(2d) - a^(2d-2)b^2 + b^(2d)`,

which is positive definite by weighted AM-GM although its second moment is
negative. At each new polynomial degree, all new moments except the top one
are set to zero. Finite-dimensional coercivity and Young's inequality show
that a sufficiently large top moment makes the enlarged `2d`-Hankel form
positive definite. Iteration covers every polynomial.

The top moments are also forced to grow, making `L` discontinuous for the
submultiplicative coefficient norm on `R[x]`.

## Scope

This completely rules out deleting continuity for every `d >= 2`. It does not
classify which assumptions strictly weaker than continuity might suffice.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: Corollary 2.8 and Question 2.9.
- `code/verify_structure.py`: finite checks of base and degree bookkeeping.
- `verification.md`: proof and novelty audit.
- `evidence_sources/README.md`: source provenance.

Associated attempt:
`attempts/1610.01659_even_power_positive_not_square_positive_attempt.md`.
