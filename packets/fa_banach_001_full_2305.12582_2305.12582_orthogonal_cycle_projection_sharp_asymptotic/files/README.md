# Sharp asymptotic for the orthogonal cycle projection on the two-dimensional torus

**Status:** candidate full solution of the `P_orth` branch of Question 32 in
arXiv:2305.12582, subject to human review.

Dilworth, Kutzarova, and Ostrovskii ask for improved asymptotic estimates for
the norm of the minimal invariant cycle projection and/or the orthogonal cycle
projection on `T_n = Z_n^2`.  This packet proves the sharp formula

```text
||P_orth||_{ell_1(E_n) -> ell_1(E_n)} = (4/pi) log n + O(1).
```

Thus the orthogonal-projection branch has logarithmic growth, with its leading
constant determined.  The asymptotics of the genuinely minimal invariant
projection `P_min` remain open.

## Idea of the proof

The complementary projection is the discrete Helmholtz projection
`Q_n = I-P_orth = d Delta^dagger d^*`.  A column of `Q_n` is therefore the
dipole kernel, or a second difference of the torus Green function.  A local
Fourier analysis shows that, up to an absolutely summable error and a bounded
torus-periodization term, its two components are

```text
-(1/(2 pi r^2)) cos(2 theta),
-(1/(2 pi r^2)) sin(2 theta).
```

Taking absolute values and summing on lattice annuli gives

```text
(1/(2 pi)) * integral (|cos 2 theta|+|sin 2 theta|) dtheta
* integral_1^n dr/r
= (4/pi) log n + O(1).
```

The source's invariant-projection identity, reproved in the packet, changes
the complementary norm by exactly `1/n^2`.

## Verification

`code/verify_fft.py` independently evaluates the exact finite Fourier
multiplier.  It reproduces the source values `19/9`, `41/16`, `69/25`, and
`3839/1260` at `n=3,4,5,6`.  Up to `n=512`, the residual after subtracting
`(4/pi) log n` remains bounded and stabilizes numerically near `0.712`.  This
is a sanity check, not part of the proof.

The proof's principal review point is Lemma 2: the Abel-regularized aliasing
step and the uniform boundedness of the periodized homogeneous Hessian.
Both are expanded in the packet, including the cancellation on symmetric
lattice squares.

## Novelty and scope

The run's cheap indexes and targeted web searches through 2026-08-09 found no
answer to this exact orthogonal-projection asymptotic.  Searches used the paper
title, arXiv id, Question 32, `orthogonal cycle projection`, `discrete torus`,
`Green function`, and the proposed `4/pi log n` constant.  The published
author offprint still states the problem as Question 32.  Novelty is plausible,
not certified.

Files:

- `solution_packet.pdf`: compiled candidate proof.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: Question 32 on source PDF page 18.
- `main.tex`: packet source.
- `code/verify_fft.py`: finite Fourier sanity check.

Ledger:
`runs/fa_banach_001/ledger/results/2305.12582_orthogonal_cycle_projection_sharp_asymptotic.json`.
