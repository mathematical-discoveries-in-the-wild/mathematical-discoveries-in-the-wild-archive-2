# Verification report

Verdict: `candidate_partial_likely_valid` for the algebraically atomic
subclass of the `VL_IP` direct-limit question in arXiv:2208.13813.

## Proof audit

- For a linear map out of `c00(A)`, interval preservation is equivalent to
  sending every coordinate atom to an atom or zero.  Necessity follows by
  applying the interval equality to one coordinate; sufficiency follows from
  finite support, grouping proportional image atoms, the Riesz decomposition
  property, and splitting one scalar interval among the coordinates.
- Each connecting map is therefore monomial on atoms, although several source
  atoms may merge onto one target ray.
- The surviving atomic rays in the algebraic vector-space direct limit span.
  A finite relation can be moved to one common later stage, where distinct
  surviving rays land on distinct coordinate atoms, proving independence.
- Coordinatewise order on those rays makes the colimit a `c00(C)` vector
  lattice, and each canonical map is interval preserving by the same lemma.
- For any compatible interval-preserving cocone, its unique vector-space
  factor sends each colimit coordinate atom to an atom or zero.  The lemma
  therefore proves that the factor is interval preserving, establishing the
  universal property in `VL_IP`.
- The finite-dimensional corollary is explicitly restricted to Archimedean
  vector lattices.  The source allows non-Archimedean lattices, which need not
  have an atomic basis.

## Upgrade attempts and obstruction

1. The initial finite-dimensional coordinate argument was upgraded to
   arbitrary objects `c00(A_i)` and arbitrary directed index sets.
2. Extending the corollary to non-Archimedean finite-dimensional lattices was
   examined and rejected: lexicographically ordered examples need not be
   spanned by atoms.
3. Extending the construction to order-theoretically atomic spaces such as
   `l-infinity(A)` was examined and rejected because their atoms do not
   algebraically span the space.
4. Normed and Banach variants require additional control of quotient norms and
   completion; the source itself records that interval preservation can fail
   at the completion inclusion.

## Packet and visual checks

- `latexmk` completed after two passes with no unresolved references,
  overfull boxes, underfull boxes, or final logged warnings.
- The final packet contains three A4 pages.
- Every page was rendered at 160 DPI and inspected at original resolution.
  The source crop is readable, all formulas and proof endings are visible, and
  no text, image, margin, or page number is clipped.
- Text extraction finds the main theorem, universal-property discussion, and
  finite-dimensional Archimedean corollary.

## SHA-256

```text
bd6509b76e30b7a024ed9dc4d7d4375b040831c2cf98d9b8977cd00842c3367a  solution_packet.pdf
9ff3413c021f300eea9b68b4ad269789b2be97ae792569d4e8da93ad254d1a98  source_paper.pdf
e79a72a779a1b4715ade0cf9ef12e90ade435168be501764a101ef09c5b3f70a  figures/open_problem_crop.png
```

## Human-review recommendation

Check the common-later-stage independence argument and the atomic-map lemma,
especially its sufficiency for arbitrary target vector lattices.  If accepted,
the packet gives a broad partial theorem, not a solution of the six-category
general question.
