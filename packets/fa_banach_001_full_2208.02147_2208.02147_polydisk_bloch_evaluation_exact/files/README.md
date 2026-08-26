# Exact Bloch evaluation extremal on the unit polydisk

Status: `candidate full solution, likely valid pending expert review`

Source: Robert F. Allen, *Weighted composition operators from the Bloch
space to weighted Banach spaces on bounded homogeneous domains*,
arXiv:2208.02147.  Open Question 1 on PDF page 9 asks for a closed form of
`omega(z)` on the unit polydisk and whether its Poincare-distance upper bound
can be sharpened.

## Claimed result

For every `z=(z_1,...,z_n)` in the unit polydisk,

```text
omega_0(z) = omega(z) = rho(z,0)
           = (sum_j arctanh(|z_j|)^2)^(1/2).
```

Thus the source's upper bound is exact and cannot be sharpened.  The formula
is stronger than requested because the same supremum is obtained from the
star-little Bloch space.

The lower bound uses the explicit extremal

```text
F(w) = sum_j a_j arctanh(eta_j w_j),
a_j = arctanh(|z_j|) / rho(z,0),
eta_j z_j = |z_j|.
```

The product-metric dual norm gives `beta_F <= ||a||_2=1`, while
`F(z)=rho(z,0)`.  Replacing each argument by `s eta_j w_j`, `s<1`, gives
functions holomorphic past the closed polydisk and proves the `omega_0`
identity by taking `s` to one.

## Consequences

Substitution into the source's exact abstract norm theorem yields a closed
symbol formula for every bounded weighted composition operator from the
Bloch or star-little Bloch space to `H_mu^infinity`.  It also rewrites the
polydisk compactness criterion using the Euclidean norm of the coordinate
hyperbolic distances instead of the source's comparable sum.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2208.02147.
- `figures/open_question_crop.png`: Open Question 1 from PDF page 9.
- `verification.md`: proof audit and bounded novelty check.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

Bounded searches on 9 August 2026 used the exact question, source title and
identifier, and combinations of `Bloch`, `polydisk`, `point evaluation`,
`omega(z)`, `Poincare distance`, and `arctanh`.  Neither the cheap run indexes
nor arXiv search located a later answer.  Novelty confidence is moderate
pending specialist review.

## Human review focus

Check that the paper's Poincare distance is the path distance of its displayed
product Bergman metric.  The packet proves the corresponding product-distance
formula directly, so no unspoken metric convention is needed beyond the
source's definition.

