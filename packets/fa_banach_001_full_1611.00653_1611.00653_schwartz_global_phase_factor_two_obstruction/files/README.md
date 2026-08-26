# Global-phase Jacobian factor-two obstruction

Status: `candidate_full_negative_answer_likely_valid`.

Source: Andrea Carbonaro and Oliver Dragičević, *Convexity of power
functions and bilinear embedding for divergence-form operators with complex
coefficients*, arXiv:1611.00653, Discussion in Section 7.2.

## Result

The Schwartz-class variational construction requested in the source paper
does not exist. For every measurable `E` and every admissible global polar
factorization

```text
u = rho exp(i omega) in S(R^2),  rho > 0,  omega real,
```

one has

```text
2 integral_E J(rho^2, omega) <= integral_{R^2} |grad u|^2.
```

The source asks for the right-hand Jacobian integral to dominate the energy
up to every factor `1+delta`. Taking any `0 < delta <= 1` contradicts the
displayed universal bound, so the answer is definitively negative.

## Proof mechanism

Pointwise,

```text
|J(rho^2,omega)| <= |grad rho|^2 + rho^2 |grad omega|^2 = |grad u|^2.
```

The global phase gives

```text
J(rho^2,omega) = div(rho^2 omega_y, -rho^2 omega_x).
```

The vector field is integrable because `rho` and `rho grad omega` are in
`L^2`; a cutoff argument therefore shows that the total signed Jacobian is
zero. Its positive mass equals its negative mass, so the energy is at least
twice the Jacobian captured by any set `E`.

## Scope and novelty

This fully answers the exact displayed Schwartz/global-phase question. It
does not settle variants with boundary flux or a non-global phase, nor the
most general semigroup-contractivity characterization discussed around it.
Bounded exact-phrase and keyword searches through 2026-08-11 found the
source but no later answer. Novelty remains subject to expert review.

Files:

- `solution_packet.pdf`: human-facing proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `verification_report.md`: proof audit.

Ledger: `runs/fa_banach_001/ledger/results/1611.00653_schwartz_global_phase_factor_two_obstruction.json`.
