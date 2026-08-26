# Four-step gap rigidity for a Bergman Toeplitz commutant

**Status:** substantial partial result, likely valid; pending human review.

**Source:** Hashem Alsabi and Issam Louhichi, *On the commutativity of a
certain class of Toeplitz operators*, arXiv:1704.04757, especially the open
problem quoted on PDF page 2 and the right-terminating theorem in Section 3.

## Result

Let `A=T_{z^2+\bar z^2}` on the Bergman space of the disk and let
`f=sum_k e^{ik theta} f_k(r)` be bounded.  Join two nonzero Fourier indices
when they differ by 4.

- If every connected component of this four-step support graph is finite and
  `T_f` commutes with `A`, then `f=alpha(z^2+\bar z^2)+beta` almost everywhere.
- More strongly, if `sum_k ||f_k||_infinity<infinity`, it is enough that every
  residue class modulo 4 have arbitrarily large missing Fourier indices.

These hypotheses allow infinitely many positive and negative angular modes.
The proof decomposes the exact commutator into independent four-step blocks;
each block is itself a right-terminating commuting symbol, so the source
theorem applies block by block.  Only the constant block and the joint
`{-2,2}` block can survive.

## Scope

This does not settle the unrestricted bounded-symbol problem.  In the angular
Wiener class, it reduces any possible non-affine counterexample to an
eventually gapless positive Fourier ray in at least one residue class modulo
4.  Eight focused upgrade attempts, including spectral-multiplier,
compactness, boundary-asymptotic, and norm-tail routes, are recorded in
`runs/fa_banach_001/attempts/1704.04757_unrestricted_commutant_upgrade_attempts.md`.

## Files and verification

- `main.tex` and `solution_packet.pdf`: theorem, proof, limitations, and
  novelty boundary.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: actual full-width rendering of the open
  question on source PDF page 2.

The proof is analytic and has no computational dependency.  The key
verification points are the index placement in the homogeneous commutator
identity and the boundedness of a lower-infinite block under the angular
Wiener hypothesis.

## Novelty and review

A bounded search on 17 August 2026 covered the run indexes, the source's exact
title and citation neighborhood, Le--Tikaradze (arXiv:1706.01510), and the
2024 quasihomogeneous-sum paper (arXiv:2409.14361).  The located results retain
right-termination or finite-sum hypotheses; no explicit statement of this
four-step gap theorem was found.  Novelty confidence is moderate because the
proof is a short structural consequence of the source theorem.

Recommended human review: verify weak-operator Fourier extraction of the
commutator, endpoint separation of each support block, and use of uniform
angular summability for a lower-infinite block.
