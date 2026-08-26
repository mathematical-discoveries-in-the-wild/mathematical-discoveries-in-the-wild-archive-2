# Verification report

Verdict: `candidate full solution, likely valid, human review requested`.

## Mathematical dependency audit

1. For strict `*`-cyclicity, the conjugate-linear map
   `Q_xi(a)=a^*xi` is a bounded surjection from the norm-closed operator
   algebra onto the Hilbert space.
2. The open mapping theorem applies after replacing the domain by its
   conjugate Banach space. It supplies a uniform bound on the norm of a
   preimage of every unit vector; no linear right inverse is asserted.
3. If `K_n` is invariant for the algebra and `y_n in K_n`, then
   `a_n y_n in K_n`, so pairing `a_n^*xi=y_n` with `y_n` only sees the
   component `P_n xi`.
4. For decreasing closed subspaces, strong convergence of their orthogonal
   projections to zero is equivalent to trivial intersection. Thus the
   abstract tail obstruction has no compactness or separability dependency.
5. In a regular unitarily invariant Hilbert function space, the homogeneous
   Taylor subspaces form an exhaustive orthogonal decomposition and every
   degree occurs. Consequently the high-degree tails are nonzero and their
   projections converge strongly to zero.
6. Multiplication by an analytic multiplier cannot lower homogeneous degree,
   so every multiplier preserves every high-degree tail. This proves the
   statement for the full multiplier algebra and therefore for every
   norm-closed subalgebra, including `A(H)`.
7. The corollary invokes source Theorem 5.11 only after the new theorem has
   supplied its hypothesis (i); the source's independent hypothesis (ii),
   existence of a nonempty totally null set, is retained.

No unproved lemma, computational premise, or external theorem beyond the open
mapping theorem and the source's stated Hilbert-space structure remains.

## Scope audit

- Fully answered: within the source's class of regular unitarily invariant
  Hilbert function spaces, `A(H)` never admits a strictly `*`-cyclic vector.
- Strengthened: the same nonexistence holds for `M(H)` and each norm-closed
  subalgebra of it.
- Consequence: hypothesis (i) of source Theorem 5.11 is automatic.
- Not claimed: nonexistence of ordinary dense/topological cyclic vectors.
- Not claimed: an analogous statement for finite-dimensional truncated
  analytic spaces without arbitrarily high nonzero homogeneous tails.

## Novelty audit

On 13 August 2026, the bounded search covered the exact source title, arXiv id,
authors, and close phrases combining `strictly *-cyclic vector`, `strictly
star-cyclic`, `multiplier algebra`, `Hilbert function space`, and `unitarily
invariant`. The current arXiv v2 source, updated September 2025, still contains
the open statement. Located hits concern forward strict cyclicity of weighted
shifts or general strictly cyclic algebras, not this adjoint multiplier-algebra
question or the homogeneous-tail obstruction. No explicit later answer was
found. Novelty confidence remains provisional pending expert review.

## Human-review focus

- Confirm that the source's definition of a regular unitarily invariant
  Hilbert function space gives the exhaustive orthogonal homogeneous
  decomposition with nonzero pieces in arbitrarily high degree.
- Confirm the uniform-preimage consequence of the conjugate-linear open
  mapping theorem.
- Confirm that source Theorem 5.11 is quoted with all remaining hypotheses
  unchanged.

## Artifact verification

- `latexmk` completed successfully; the final log has no warnings, undefined
  references, overfull boxes, or underfull boxes.
- `solution_packet.pdf` is a four-page A4 document. Ghostscript parsed it
  successfully, and `pypdf` reopened all pages and extracted text from each.
- All four final pages were rendered at 170 dpi and inspected at original
  detail; the source crop, prose, equations, bibliography, and page boundaries
  are clean and legible.
- SHA-256 of `solution_packet.pdf`:
  `ac75396b248918dd449d7027fbfbcc164829845c6ec107aadaa22f0655980402`.
- SHA-256 of `source_paper.pdf`:
  `5e8e5bf42058ed15b24199f19cb271b3e41f998a9eead5935b3a143b5ad35e9d`.
- SHA-256 of `figures/open_problem_crop.png`:
  `a201ff3f787adc5a66242cbb5009c647581d3c4eb1756a1c0552a23c134410ff`.

