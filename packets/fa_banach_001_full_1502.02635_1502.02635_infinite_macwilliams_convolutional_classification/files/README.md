# Infinite-coordinate MacWilliams classification

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Marita Ferrer, Margarita Gary, and Salvador Hernández, “Weight-preserving
  isomorphisms between spaces of continuous functions: The scalar case,”
  arXiv:1502.02635v1 (2015).
- Open target: page 2, the sentence “It remains open the representation of
  general F-isometries defined between convolutional codes.”
- Local provenance copy: `source_paper.pdf`.

## Claimed contribution

The packet proves an infinite-coordinate MacWilliams theorem. If
`V <= F^(I)` and `W <= F^(J)` consist of finitely supported functions, every
linear Hamming isometry `T: V -> W` is a weighted coordinate permutation on
the active coordinates. Neither the spaces nor the coordinate sets need be
finite.

Flattening a polynomial vector into its time-coordinate coefficients gives the
complete representation requested for arbitrary F-linear isometries of
polynomial convolutional codes:

```text
[z^t](Phi(c))_r = u_(t,r) [z^s]c_k,
```

where `(t,r) -> (s,k)` is a bijection of active time-coordinate supports and
every `u_(t,r)` is nonzero. Module linearity is not assumed.

The proof localizes to finite-dimensional subspaces, recovers the multiplicity
of every projective coordinate-functional class by an invertible incidence
matrix, and then uses pointwise finiteness to isolate each global class inside
one finite-dimensional test space.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width source evidence from page 2.
- `code/verify_incidence.py`: exact small-field checks of the incidence Gram
  formula.
- `verification.md`: verification record and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Scope and novelty

This fully answers the quoted question for polynomial convolutional codes. It
does not settle the source paper's broader weighted-composition question on
arbitrary nondiscrete measured spaces, nor Laurent-series settings with
infinite support.

Bounded searches on 11 August 2026 covered the run indexes, exact quoted
phrases, infinite-length/finitely-supported MacWilliams variants, arXiv
0902.2235, 1507.05212, and 1709.06070. No exact prior theorem was found.
Novelty confidence is moderate because this concise extension may be folklore
under different terminology.

## Human review focus

Please check the finite projective-incidence count and the globalization step
that isolates a global functional class simultaneously in both pointwise
finite coordinate families. A specialist literature search should precede any
publication-level novelty claim.
