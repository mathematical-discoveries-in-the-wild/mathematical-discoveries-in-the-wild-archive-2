# Verification Report

Candidate: arXiv:2207.08090, spectral inclusion for induced lattice homomorphisms on free complex Banach lattices.

## Claim checked

For every complex Banach space `E` and bounded operator `T:E->E`, the induced lattice homomorphism `bar T` on `FBL_C[E]` satisfies `sigma(T) subset sigma(bar T)`.

## Verdict

`candidate_full_solution_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Source PDF page 17 asks verbatim whether `sigma(T)` is always contained in `sigma(bar T)`. The following results cover positive spectral values, moduli, and lattice-homomorphic `T`, but not arbitrary `T`. |
| Functional representation | valid | The source construction gives `delta_E(x)(Re z*)=z*(x)` and `(bar T f)(Re w*)=f(Re T*w*)`; the source itself uses the second identity in Proposition 6.4. |
| Evaluation boundedness | valid | For fixed `w*`, the defining free-lattice norm and positive homogeneity yield `|f(Re w*)| <= ||w*|| ||f||`. The rotated evaluations therefore have a uniform bound. |
| Fourier functional existence | valid | For each `f`, the rotation-orbit evaluation is continuous and periodic. Multiplication by `e^(-it)` and scalar integration defines a bounded complex-linear functional. |
| Nonvanishing | valid | On `delta_E x`, the integrand becomes `e^(-it)e^(it)z*(x)=z*(x)`, so `Phi(delta_E x)=z*(x)` and `Phi != 0`. |
| Adjoint eigenvalue | valid | If `T*z*=r e^(i theta)z*`, positive homogeneity extracts `r`; shifting `s=t+theta` contributes `e^(i theta)` because the Fourier weight is `e^(-it)`. Thus `bar T* Phi=lambda Phi`. |
| Approximate-spectrum branch | valid | `delta_E` is an isometry and intertwines `T` with `bar T`, so every approximate eigenvector for `T` transfers verbatim. |
| Nonapproximate-spectrum branch | valid | Bounded below implies closed range. A spectral nonapproximate point is not surjective, so Hahn-Banach yields a nonzero annihilator `z*` and hence `T*z*=lambda z*`. |
| Spectral conclusion | valid | An eigenvalue of `bar T*` belongs to `sigma(bar T*)=sigma(bar T)` (as sets under the complex-linear dual convention). Equivalently, `lambda-bar T` cannot have dense range. |
| Zero case | valid | If `lambda=0`, the same annihilator exists and `bar T* Phi=0`; no choice of argument is needed. |

## Stress tests and rejected overclaims

- Reversing the Fourier weight to `e^(it)` would yield the conjugate phase; the packet uses and checks `e^(-it)`.
- The proof does not infer that residual spectral points become eigenvalues of `bar T`; it only produces eigenfunctionals of `bar T*`, which is sufficient.
- No complementability of the canonical copy `delta_E(E)` is assumed.
- The scalar integral is taken after evaluation, so no unproved norm continuity of the dual-valued orbit is needed.
- The spectrum of a Banach adjoint equals the original spectrum; under alternate conjugate-linear dual-pairing conventions one must translate eigenvalue notation consistently. The source uses complex-linear functionals and `T*z*=lambda z*`, matching the packet.
- The separate real free-lattice reconstruction problem in the introduction is outside this result.

## Novelty check

On 2026-08-11, the exact arXiv id/title and the terms `free complex Banach lattices`, `spectrum`, `sigma(T)`, `induced lattice homomorphism`, and `Fourier evaluation` were checked in the run registry, solution, attempt, and proof-gap indexes. External arXiv searches found the source and related free-lattice papers but no later primary-source resolution. This is a bounded search, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 21-page arXiv PDF.
- `figures/open_question_crop.png` is rendered from source PDF page 17 and contains the exact question and source partial result.
- The proof packet is self-contained after the two explicit functional-representation identities from the source construction.
- No computation is used as mathematical evidence.

Confidence: 96/100.

Recommended action: high-priority review by a Banach-lattice/operator-theory specialist. The proof is short; the decisive audit is the Fourier-mode identity `Phi bar T=lambda Phi`.
