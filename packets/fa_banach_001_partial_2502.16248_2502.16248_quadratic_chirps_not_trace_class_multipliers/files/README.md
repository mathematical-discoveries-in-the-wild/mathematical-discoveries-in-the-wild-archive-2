# Quadratic chirps are not trace-class Fourier--Wigner multipliers

**Status:** `candidate_substantial_partial_result_likely_valid_needs_human_review`

**Source:** Helge J. Samuelsen, *Fourier-Wigner multipliers and the
Bochner--Riesz conjecture for Schatten class operators*, arXiv:2502.16248v2
(7 March 2025), Question 1 on source PDF page 21.

## Candidate result

The source asks whether every trace-class Fourier--Wigner multiplier is the
symplectic Fourier transform of a finite complex measure.  It singles out

`m(z) = sin(pi*|z|^2)`

as a possible counterexample.  This packet proves that the candidate is not a
trace-class multiplier.  More generally, every nonconstant radial quadratic
chirp `exp(pi*i*c*|z|^2)`, `c != 0`, fails at the trace-class endpoint.

For normalized squeezed Gaussians `g_r`, the rank-one inputs
`G_r = g_r tensor g_r` have trace norm one, while the output trace norms grow
at least like `r^(d/2)`.  The proof is explicit: the output is a complex
Gaussian integral kernel, Schur's test makes its operator norm decay, and its
Hilbert--Schmidt mass stays positive.

The source's full classification question remains open.

## Contents

- `solution_packet.pdf` — theorem, proof, limitations, and novelty audit
- `source_paper.pdf` — arXiv:2502.16248v2
- `figures/open_question_crop.png` — source candidate and Question 1
- `verification.md` — mathematical, computational, literature, and rendering checks
- `code/verify_gaussian_bounds.py` — exact-formula and numerical sanity checks
- `code/make_open_question_crop.py` — reproducible source-page crop

**Human-review focus:** Check the centered kernel formula, the Schur-test
constant, and the oscillatory Gaussian integral in the sine estimate.

