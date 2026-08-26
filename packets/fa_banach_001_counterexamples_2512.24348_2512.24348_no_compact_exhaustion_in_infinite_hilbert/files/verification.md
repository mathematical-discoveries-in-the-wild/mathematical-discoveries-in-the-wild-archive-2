# Verification report

## Claim checked

A real or complex Hilbert space has a norm-compact exhaustion exactly when
it is finite-dimensional. Consequently, the proposed compact exhaustion of
a nonseparable Hilbert space in arXiv:2512.24348 is impossible in the norm
topology.

Verdict: candidate counterexample/full negative classification; likely
valid.

## Topological audit

- An exhaustion by norm-open sets with compact closures gives a countable
  cover by norm-compact sets.
- A compact subset of an infinite-dimensional normed space has empty
  interior. Otherwise translation and dilation would make the closed unit
  ball compact, contradicting Riesz's lemma.
- Compact subsets are closed, hence nowhere dense in the
  infinite-dimensional case.
- Hilbert spaces are complete, so Baire category prohibits a countable cover
  by these compact sets.
- In finite dimension, open balls have compact closures and give the desired
  nested exhaustion. This proves the exact iff classification.
- Independently, every compact metric space is separable; a countable union
  of separable subsets is separable. This immediately excludes the stated
  nonseparable case.

## Interpretation and scope audit

- The source explicitly models its proposal on norm/local-topology compact
  exhaustion of a Riemannian manifold. The packet therefore states its
  theorem for the Hilbert norm topology.
- Closed norm balls are weakly compact, but have empty weak interior in
  infinite dimension and do not provide relatively compact weak
  neighborhoods. Weak-topology heat-kernel convergence would be a different
  problem.
- A sequence of separable or finite-dimensional subspaces cannot have dense
  union in a nonseparable Hilbert space.
- Uncountable directed nets can cover the space, but lose the sequential
  domain exhaustion and require an independent compatibility and convergence
  theory.
- The packet does not claim that every heat semigroup, measurable kernel, or
  alternative approximation on a nonseparable Hilbert space is impossible.

## Upgrade-attempt log

- Attempt 1 found the immediate sigma-compact-implies-separable obstruction.
- Attempt 2 upgraded it to the exact finite-dimensional classification via
  Baire category and Riesz's lemma.
- Attempt 3 ruled out sequential separable/Galerkin replacement in the
  nonseparable case.
- Attempt 4 separated weak-topology and net reinterpretations from the
  claimed manifold-style norm-compact exhaustion.

## Novelty audit

Bounded primary-source searches through 2026-08-11 used the exact title and
proposal together with `nonseparable Hilbert space`, `compact exhaustion`,
and `heat kernel`. They found the source and classical manifold uses, but no
later primary source addressing the proposal. The underlying Baire/Riesz
classification is classical; novelty is claimed only for applying it as a
sharp correction to this new heat-kernel proposal.

## Source and render audit

- `source_paper.pdf` is the official 37-page arXiv:2512.24348v1 PDF.
- Source page 34 was visually inspected and fully reproduced.
- The packet compiled without warnings, overfull boxes, underfull boxes,
  undefined references, or multiply defined labels.
- The final packet has 4 pages; every page was visually inspected after the
  last edit.
- Final packet SHA-256:
  `a5721ce5efbb6f5f077a28f41b1a745b60f095e7195f9c14f0edfb7251598ace`.
- Source PDF SHA-256:
  `d93b80a3862fdce41c37e4182c86ce73611de64ec40aa55a289a92e5f3739276`.
- Source page image SHA-256:
  `548ff9c4d2b77ac8d4d014898b76b0718e1d2cbd475dcab985288c6cd9c246ee`.

## Human verifier focus

Confirm the norm-topology reading of “compact exhaustion.” Under that
reading, check the Baire-category implication and the finite-dimensional
converse.

