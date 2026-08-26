# Extra residual spectral point on the Barlow--Perkins lattice

Status: `candidate_counterexample_likely_valid`

Source: Shiping Cao, Yiqi Huang, Hua Qiu, Robert S. Strichartz, and
Xiaohan Zhu, *Spectral analysis beyond ell-2 on Sierpinski lattices*,
arXiv:1910.01771, Section 3.3 (PDF page 14).

## Result

The source asks whether its complete `ell^1` spectral classification for a
one-sided Sierpinski lattice with boundary also holds on the two-sided
Barlow--Perkins lattice. The answer is no.

The periodic Julia value

`lambda = 3 - sqrt(3)`

is an `ell^infinity` eigenvalue on the Barlow--Perkins lattice. It lies outside
`{0} union Sigma_4 union Sigma_5 union Sigma_6`. By adjoint duality it is a
residual spectral point on `ell^1`, whereas the proposed extension of the
source theorem would classify it as continuous spectrum.

## Construction

Reflection splits the Barlow--Perkins graph into a Neumann half and a
Dirichlet half. The orbit of `lambda` under `R(t)=t(5-t)` is the two-cycle

`3-sqrt(3) <-> 3+sqrt(3)`.

The corresponding two-level spectral-decimation extension has nine explicit
`3 x 3` child matrices. For

`P = I - (sqrt(3)/6) J`,

all nine satisfy `M^T P M <= 9P`. Outer boundary values scaled by
`(-1/3)^n` therefore give consistent finite Dirichlet eigenfunctions with a
uniform bound. Their union is a bounded nonzero Dirichlet eigenfunction; odd
reflection produces the bounded eigenfunction on the full lattice.

## Scope and novelty

This is a full negative answer to the specific Barlow--Perkins yes/no
question. It does not classify every residual or bounded eigenvalue, and it
does not solve the broader problem for arbitrary boundaryless Sierpinski
lattices.

A bounded search used the exact source sentence and combinations of
`Barlow--Perkins`, `Sierpinski lattice`, `ell^1 spectrum`, `ell^infinity
eigenvalue`, `generating sequence`, and `3-sqrt(3)`. No later answer or this
specific eigenvalue construction was found. Novelty is plausible but not
certified.

## Packet contents

- `main.tex`, `solution_packet.pdf`: complete counterexample proof.
- `source_paper.pdf`: arXiv:1910.01771.
- `figures/open_problem_crop.png`: source question and graph.
- `code/verify_matrix_certificate.py`: exact symbolic matrix verification.
- `code/finite_level_probe.py`: independent finite-level numerical check.
- `VERIFICATION.md`: mathematical, computational, literature, and rendering
  checks.

Human review should prioritize the two-step extension order, the nesting
consistency identity, and the adjoint residual-spectrum conclusion.
