# Fourier criterion and phase engineering for quantum lifts

**Status:** candidate substantial partial result, likely valid.

**Source:** Bowen Li and Jianfeng Lu, *Speeding up quantum Markov processes
through lifting*, arXiv:2505.12187, open question after equation (4.22), source
PDF page 31.

The source asks which symmetric `Q`-matrices make its quantum lift optimally
quadratically fast.  This packet solves the classification for all
translation-invariant generators on finite abelian groups by an exact scalar
Fourier criterion.  It also proves:

- the canonical normalized hypercube lift has the sharp constant `3-2/d`;
- the canonical positive-square-root complete-graph lift has the sharp,
  divergent constant `N/2`;
- for complete graphs of prime order, cubic Hamiltonian phases preserve the
  same overdamped `Q` while restoring a dimension-free constant (`<=256`).

The general characterization of arbitrary symmetric `Q`-matrices remains
open, so this is a partial rather than full solution.

## Contents

- `solution_packet.pdf`: theorem statements and proofs.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: equations (4.18)--(4.22) and the question.
- `code/verify_fourier_examples.py`: independent finite-dimensional checks.
- `tmp/`: LaTeX and rendering intermediates.

## Verification

The verifier compares the Fourier formula with the predicted sharp constants
for complete graphs and hypercubes and reports the cubic-phase constants for
several primes.  The proof itself is symbolic; the computation is only a
regression check.  The direct complete-graph calculation, the Rademacher
fourth moment, and the cubic Weil bound were checked separately.

## Novelty and scope

The run's registry, solution, attempt, and proof-gap indexes were searched on
2026-08-11 for the arXiv id and the core quantum-lift/Fourier terms; no answer
was found.  No broad external literature search was performed, so novelty
confidence is moderate-to-low.  The source question is broad and remains open
outside the abelian Cayley class.

## Human-review recommendation

Check the Fourier-transform convention in the Gram-eigenvalue formula and the
application of the cubic Weil bound after deleting the `s=0` term.  Also check
that the source's abstract convergence theorem is applied to the phase-modified
self-adjoint Hamiltonian rather than only to its special positive-real choice.

