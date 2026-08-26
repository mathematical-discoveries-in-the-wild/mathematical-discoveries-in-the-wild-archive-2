# Verification report

Status: candidate full structural result, likely valid pending human review.

## Mathematical audit

- Fourier convention: Ue_k=z^k gives UBU^{-1}=M_z for Be_k=e_{k+1}.
- Domain and closedness: the graph norm of maximal multiplication by F is
  exactly L2((1+|F|^2)dm), a complete space for a finite measure.
- Adjoint and normality: maximal multiplication gives
  M_F*=M_conjugate(F), with equal domains and commuting products.
- Core: trigonometric polynomials are dense in the weighted graph space
  because continuous functions are dense for finite regular Borel measures
  and trigonometric polynomials are uniformly dense in C(T).
- Taylor convergence: multiplication by a fixed trigonometric polynomial is
  bounded on L2, so H2 convergence of the Taylor sums implies convergence on
  c_00.
- Full-domain approximation: the tail integral of |Fh|^2 tends to zero for
  every h in the maximal domain.
- Resolvent: if 1/(F-lambda) is essentially bounded, then
  F/(F-lambda)=1+lambda/(F-lambda) is bounded, ensuring that the inverse maps
  all of L2 into the maximal domain.
- Scope: universal Taylor convergence on the entire maximal domain is not
  claimed; the packet identifies the exact uniform-boundedness obstruction.

## Novelty audit

Run-index and bounded web searches on 2026-08-13 used arXiv:2604.02336, the
exact future-work sentence, unbounded f(B), H2 bilateral shift, maximal
multiplication operator, graph core, and unbounded analytic Toeplitz
operator. Standard unbounded-multiplication and Toeplitz sources were found,
but no later explicit answer to this source item and no exact
bilateral-shift domain/core treatment. Novelty confidence is low-to-moderate.

## Artifact audit

- The final packet compiled with LaTeX twice through latexmk.
- The final log contains no warning, overfull-box, underfull-box, undefined
  reference, or undefined citation line.
- The output has four letter-size pages. All four were rendered at 144 dpi
  and visually inspected after the final edit; the source crop, formulas,
  theorem continuation, page breaks, margins, and references are legible.
- PDF SHA-256:
  aa626fa1844889bcf8baa61d1c3af41466ac42d6978b5a1b3a2fc316683b09e2.

