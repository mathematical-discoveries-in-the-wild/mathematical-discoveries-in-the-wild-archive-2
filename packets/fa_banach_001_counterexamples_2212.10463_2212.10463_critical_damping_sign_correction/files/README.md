# Critical-damping sign correction for arXiv:2212.10463

Status: `candidate_full_counterexample_likely_valid`

Source: Nelson Faustino and Jorge Marques, *Structurally damped
σ-evolution equations with power-law memory*, arXiv:2212.10463v2.

## Result

The paper's Lemma 4.3(iii) prints

```text
α E^2_{α,β}(z)
  = E_{α,β-1}(z) - (1+α-β) E_{α,β}(z).
```

The sign must be `+`. This propagates to the two repeated-root (`μ=2`)
kernels for the forcing term and initial velocity. The corrected formulas,
with `z=|ξ|^σ t^α`, are

```text
t^(β-1)/α [E_{α,β-1}(-z) + (1+α-β)E_{α,β}(-z)],
t/α       [E_{α,1}(-z)   + (α-1)E_{α,2}(-z)].
```

The initial-displacement kernel printed in the paper is correct.

This is not merely a cosmetic identity. For every `1/2 < α < 1`, take
`μ=2`, zero initial displacement and forcing, and nonzero band-limited
Schwartz initial velocity `u_1`. The paper's stated solution satisfies

```text
∂_t u(0) = ((2-α)/α) u_1 ≠ u_1.
```

Hence the critical case of its hyperbolic solution theorem is false as
printed. Direct Laplace inversion proves that the corrected kernels repair
both solution representations.

## Scope and novelty caveat

The correction is verified against the current arXiv v2 source. The
source's Prabhakar forms before the erroneous two-parameter reduction are
correct, so the repair is exact and local. Later norm estimates may survive
because many use absolute values; they were not claimed here.

Exact web searches and a bounded local full-source search found no erratum
or independent correction. Novelty remains provisional pending specialist
review.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: algebra, Laplace, literature, and render checks.
- `source_paper.pdf`: official arXiv v2 PDF.
- `source_material/source_2212.10463.tex`: inspected source TeX.
- `source_material/verify_sign_identity.py`: independent coefficient and
  numerical checks.
- `figures/printed_false_identity_crop.png`: real crop of source page 9.
- `figures/printed_critical_kernels_crop.png`: real crop of source page 23.
