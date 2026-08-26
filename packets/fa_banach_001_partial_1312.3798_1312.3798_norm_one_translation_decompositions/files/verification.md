# Verification report

Status: `candidate strong partial result; likely valid`

## Mathematical audit

1. Rational independence of the reciprocal periods is exactly the condition
   needed for density of the real one-parameter orbit in the full torus.
2. In the full-product case the infimum and supremum of the sum are the sums
   of the component infima and suprema.  The midpoint-capacity inequality is
   an exact scalar interval calculation.
3. For pairwise incommensurable triples, every two-coordinate projection of
   the compact orbit closure is onto.  Haar disintegration therefore turns
   each shifted component into a contractive conditional average of `f`.
4. Simultaneous pairwise minima and maxima give the stated capacity
   inequalities; the final corrections are constants and preserve periods.
5. When exactly one pair is commensurable, the two aggregate periods are
   incommensurable.  The first split changes the aggregate only by a constant,
   so the source's sharp two-period theorem applies without losing membership
   in the original two summand spaces.
6. Sharpness uses uniqueness of Bohr/Fourier coefficients on disjoint
   nonzero frequency lattices.

## Computational audit

The code directory records eight-attempt falsification work.  In particular:

- exhaustive vertices for representative cyclic order-12 triples have
  quotient norm exactly one;
- sampled cyclic four-component systems through order 48, finite-torus
  character systems, and continuous piecewise-linear ridge systems produced
  no norm inflation;
- the arbitrary-partition control immediately produces quotient norm `3/2`,
  demonstrating that the search can detect a genuine obstruction.

All six bundled scripts were rerun from the final packet.  The exact cyclic
vertex audit reported maximum quotient one for all four order-12 systems; the
four-component cyclic scan through order 48 ended with `final best (1.0,
None)`; all finite-torus and continuous-ridge scans reported quotient one or
`no witness`; and the negative control reported its `3/2` witness.

These computations are evidence about the unresolved boundary only and are
not used in either theorem.

## Source and literature audit

- The exact problem is transcribed from cached source lines 491--499 into
  `source_excerpt.pdf`.  The original source requires an unavailable
  `svmult.cls`, and the sandbox could not resolve the arXiv PDF host, so the
  transcription is explicitly labeled rather than represented as an original
  source PDF.
- Exact local-corpus and run-index searches found no duplicate result.
- The only adjacent local arXiv item is 1401.1226; it does not answer the
  constant-one question.  Bounded web searches returned only the source paper
  and that adjacent semigroup paper.

## Reviewer focus

The main review points are Haar disintegration on the compact orbit closure,
the signs in the minimum/maximum capacity estimates, and use of the known
two-period constant in the mixed commensurability case.

## PDF audit and checksums

- `solution_packet.pdf` has 3 letter-sized pages.  Its final LaTeX log has no
  warnings or overfull boxes.  All three pages were rendered at 140 dpi and
  individually inspected; an initially visible missing-backslash artefact was
  corrected and the affected page was rebuilt and re-inspected.
- `source_excerpt.pdf` has 1 letter-sized page.  Its final LaTeX log has no
  warnings or overfull boxes, and the rendered page was visually inspected.
- `solution_packet.pdf` SHA-256:
  `7c3aa19b9889d131a57b0b171b9717d42b6f6d2d726ddfa9e4868d84652a6850`.
- `source_excerpt.pdf` SHA-256:
  `3d5c494b62bc5467c1c7f120939b735e709d6c3c4173e7510b7a5ae6e97638bf`.
