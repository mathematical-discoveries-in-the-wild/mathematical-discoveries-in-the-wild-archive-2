# 2207.08090 — Fourier evaluation proves spectral inclusion

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: David de Hevia and Pedro Tradacete, *Free complex Banach lattices*, arXiv:2207.08090.

## Result

The source asks whether, for every bounded operator `T:E->E`, its induced lattice homomorphism on the free complex Banach lattice always satisfies

`sigma(T) subset sigma(bar T)`.

It proves approximate-spectrum inclusion and reduces general spectral points only to the inclusion of their moduli. This packet proves the full inclusion for every complex Banach space and every bounded operator.

## Proof mechanism

Approximate spectral points transfer through the canonical isometric embedding. If `lambda` is spectral but not approximate, `lambda-T` has closed proper range, so there is `z* != 0` with `T*z*=lambda z*`.

For the rotation-orbit evaluations define

`Phi(f)=(2pi)^(-1) integral_0^(2pi) e^(-it) f(Re(e^(it)z*)) dt`.

On the canonical copy of `E`, `Phi(delta_E x)=z*(x)`, so `Phi != 0`. The functional representation and positive homogeneity give `Phi(bar T f)=lambda Phi(f)`. Therefore `lambda` is an eigenvalue of `bar T*`, hence belongs to `sigma(bar T)`.

## Verification and novelty

The verification report checks boundedness and nonvanishing of the Fourier functional, the phase sign, the adjoint identity, the approximate/residual dichotomy, and the zero case.

A bounded local-index and external primary-source search on 2026-08-11 found the original paper and no later resolution of the exact spectral-inclusion question. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 21-page arXiv PDF.
- `figures/open_question_crop.png`: source page 17 crop containing the exact question and the positive-real partial result.

## Human review recommendation

Review as a likely valid full solution. Focus on the evaluation-composition identity and the sign in the first Fourier coefficient; both are written out explicitly in the packet.
