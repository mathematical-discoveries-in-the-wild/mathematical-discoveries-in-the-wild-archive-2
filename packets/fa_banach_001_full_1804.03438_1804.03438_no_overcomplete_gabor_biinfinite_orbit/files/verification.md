# Verification

Status: passed as a candidate full proof for the Gabor question.

## Mathematical checks

- A two-sided orbit is treated with a boundedly invertible generator, matching
  the source paper's `GL(H)` formulation for bi-infinite orbits.
- The Gabor frame operator commutes with each lattice time-frequency shift:
  conjugation reindexes the complete lattice orbit and projective phases
  cancel in the rank-one frame-operator terms.  Hence canonical tightening
  preserves the Gabor form with window `gamma=S^(-1/2)g`.
- Canonical tightening preserves overcompleteness because `S^(-1/2)` is
  invertible.
- The tightened orbit generator is unitary: the strong Parseval sum is the
  identity, and conjugation by the generator reindexes its two-sided terms,
  giving `U U*=I`; invertibility supplies the other side.
- For a Bessel unitary orbit, the scalar spectral measure is dominated by
  Lebesgue measure.  This follows directly by applying the synthesis bound to
  trigonometric polynomials.  Its autocorrelation sequence is therefore the
  Fourier sequence of an `L^infinity` function and tends to zero by
  Riemann--Lebesgue.
- The Weyl cocycle affects only phases.  Absolute Gabor correlations depend
  only on the displacement in `Z^2`, exactly as used in the graph definition.
- If the nonzero-correlation displacement subgroup has rank at most one, its
  Cayley graph on `Z^2` has infinitely many components.  A nonorthogonal
  unitary orbit has components equal to cosets of a nonzero subgroup `dZ`, so
  only finitely many.  The orbit cannot be orthogonal because a complete
  orthogonal Parseval frame would be a basis, contradicting overcompleteness.
- If the displacement subgroup has rank two, two independent nonzero
  correlations survive at one positive threshold.  The corresponding
  `Z^2` graph ball contains `1+2R(R+1)` points.  The orbit threshold step set
  is finite by correlation decay, so its radius-`R` ball in `Z` has at most
  `2MR+1` points.  A bijective Gram-preserving enumeration would be a graph
  isomorphism and cannot change these ball cardinalities.
- The two rank cases exhaust all subgroups of `Z^2`.  The theorem therefore
  covers every lattice density and every nonzero `L^2` window.
- The higher-dimensional extension uses the same dichotomy on `Z^(2d)`.
  The packet explicitly does not claim the wavelet half, whose correlation
  geometry is not stationary under an abelian `Z^2` action.

## Novelty and literature checks

- Cheap run-index searches found no existing packet or ledger for
  arXiv:1804.03438 or this Gabor conclusion.
- The source paper states on page 4 that the bi-infinite Gabor/wavelet problem
  was open.
- arXiv:2004.02152 gives negative answers only for irrational density and one
  compact-support class.  Its page 10 conclusion explicitly leaves rational
  density with general window support open.
- Bounded exact-phrase, title, rational-density, and operator-orbit searches
  located the source and arXiv:2004.02152, but no later full resolution.  This
  is a bounded novelty check, not a claim of exhaustive bibliographic proof.

## Source verification

- `source_paper.pdf`: 20 US-letter pages.  Rendered page 4 was visually
  inspected and contains the exact open bi-infinite Gabor/wavelet statement.
- `later_partial_result_2004.02152.pdf`: 12 A4 pages.  Rendered page 10 was
  visually inspected and contains Theorem 3.6 plus the explicit conclusion
  that the rational-density/general-support case remains open.

## Build and visual QA

- The final packet LaTeX log contains no warnings, overfull boxes, underfull
  boxes, undefined references, or errors.
- Final packet: 3 US-letter pages, 201831 bytes.
- All three packet pages were rendered at 130 dpi and visually inspected.
  The theorem, reductions, spectral calculation, graph dichotomy, scope, and
  references are clear; no text, equation, or margin is clipped or overlapped.
- Ghostscript text extraction finds the main theorem, both lemmas, the
  correlation-graph section, scope statement, and references.

## Artifact hashes

```text
source_paper.pdf                              8596ba81e472eb320c2ef0ed1011dfeefe7155eb1bc3d75eeda715ee3824465c
later_partial_result_2004.02152.pdf           c55a169b8661b2bdbcbabf9e91fc3136ef358feda3a44061a86359e278edbe56
source_question_page.png                      38f9ecec10228159e662dc5f350edb806335eba11c008a7367951f57dd227c20
later_open_page.png                           075b6f53a35bea69cb46c80f652da62fc03cc57ba15ed217e0f7380c26f8882d
solution_packet.pdf                           c32fd0c4e3de2ee06a5a0086915d21ce811e241c3643e5bf6c50af31b6ad9edf
1804.03438_gabor_biinfinite_orbit_growth_attempts.md
                                              4bf2a8160326d8c2bf572aae3f0acdfcce5e09c291699d56d6abfdd35a2af1d6
```
