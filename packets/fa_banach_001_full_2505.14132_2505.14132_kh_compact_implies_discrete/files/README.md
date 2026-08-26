# Compactness implies discrete spectrum for arbitrary KH systems

Status: `candidate_full_likely_valid` for Remark 3.8 of arXiv:2505.14132.

## Result

For every Kaplansky--Hilbert dynamical system, every vector whose orbit is
uniformly totally order-bounded belongs to the discrete-spectrum part.
Consequently, order-density of conditionally almost-periodic vectors is
equivalent to discrete spectrum.  This affirmatively answers the abstract
implication `(ii) => (i)` left open by Haase--Kreidler.

The new mechanism starts from a finite-rank projection which approximately
contains an almost-periodic orbit.  Every conjugate of that projection
approximately fixes the original vector.  A cyclic convex minimum-norm lemma
in the Hilbert--Schmidt KH-module produces an invariant Hilbert--Schmidt
operator while preserving the approximation; the equivariant spectral
decomposition then places the approximating vector in the discrete part.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2505.14132v3.
- `figures/open_problem_crop.png`: full-width source page containing Remark
  3.8 (PDF p. 14).
- `verification.md`: proof and rendering audit.

## Novelty and review focus

The revised 9 February 2026 source still states the question as open.  Bounded
local and web/arXiv searches on 13 August 2026 found no later resolution of
the exact abstract implication.  Novelty confidence is moderate because the
cyclic convex fixed-point lemma may be known in Banach--Kantorovich language.

Human review should focus on the least lattice-norm element of the cyclic
convex hull, invariance of that hull under the semilinear implemented action,
and the final bridge from invariant Hilbert--Schmidt ranges to `E_ds`.
