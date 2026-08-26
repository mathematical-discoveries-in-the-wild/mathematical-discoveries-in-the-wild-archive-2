# Verification report

Status: `candidate_full_solution_likely_valid`

## Source checks

- The exact source statement was checked in arXiv:1711.05624v3 source and PDF.
- Lemma 2.2 uses `m=C_r n^(1-1/r)`, `N=n^m`, norm
  `||A||=O_r(Delta(H))`, and prefactor `n/(c_r N)`.
- Remark 2.3 first asks whether this `m` is optimal, then separately proposes
  an arbitrary common nonlinear lift of dimension `N=o(n^m)`.

## Proof checks

- Fourier normalization was checked: the required single-edge coefficient of
  the unscaled quadratic form is exactly `c_r N/n`.
- Tensor-word parity satisfies
  `E_x chi_{pi(u) triangle pi(v) triangle S}(x)=1` exactly on the stated
  relation and zero otherwise.
- Grouping the transition matrix by parity gives disjoint all-ones blocks;
  each contributes one singular value `sqrt(c_a c_{a triangle S})`.
- Hellinger affinity increases under marginalization; the proof uses direct
  Cauchy–Schwarz grouping, so the inequality direction is explicit.
- A parity pattern of weight `h` needs at least `h` hits in the edge.
- The binomial factorial-moment tail bound is valid also at the endpoint
  `h=0`, where the probability bound is 1.
- The case `m>n/(4r)` directly implies the desired asymptotic lower bound.
- In the arbitrary-lift theorem, Schatten duality, the
  `trace <= sqrt(N) Frobenius` inequality, and entrywise Parseval have the
  stated normalizations.

## Computational spot checks

- `code/verify_parity_affinity.py` enumerates small word spaces.
- It checks the parity-count Hellinger formula against a numerical nuclear
  norm of the full transition matrix.
- It checks the projected-affinity inequality and prints the factorial-tail
  upper bound.

## Novelty checks

- Cheap run indexes had no hit for arXiv:1711.05624 or this matrix lemma.
- Bounded searches covered the exact Remark 2.3 sentence, source title/id,
  tensor-power and parity/Hellinger lower bounds, Gaussian-width improvements,
  and later three-query LDC literature.
- No later claimed answer to the isolated `m`-optimality question was found.
- Novelty confidence is moderate; expert review remains essential.

## Rendering checks

- Compiled with two LaTeX passes; all citations and references are resolved.
- The final log has no overfull boxes, underfull boxes, undefined references,
  or warnings.
- All four rendered pages were inspected at original resolution.
- No clipping, overlap, malformed mathematics, illegible text, or bad page
  break was found.
