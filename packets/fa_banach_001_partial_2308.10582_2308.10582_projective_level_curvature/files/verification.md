# Verification record

## Analytic proof audit

- At a regular affine point `u0`, set `a=grad phi(u0)`, `r0=1`,
  `x_-=-a`, and `x_d=u0 dot a`. Direct differentiation confirms that
  `(u0,1)` is stationary for the source transformed phase.
- The full frequency Hessian is exactly the bordered matrix
  `[[H phi,-a],[-a^T,0]]`.
- In a basis adapted to `a^perp`, two cofactor expansions show that its
  determinant is nonzero exactly when `H phi|_(a^perp)` is nondegenerate.
- The implicit-function theorem now supplies the same local stationary-point
  graph required by the source proof; localized uniform stationary phase and
  the `x -> tx` scaling give the claimed `L^p` exponent. Duality covers
  `p>=2`.

## Geometric proof audit

- A regular affine level has tangent space `a^perp` and second fundamental
  form proportional to `H phi|_(a^perp)`.
- In `d=3`, vanishing at every point makes each regular level component
  locally a projective line, hence a great-circle arc on `S^2`. Connectedness,
  compactness, and local continuation make it a whole great circle.
- A nonconstant smooth function on `S^2` has two distinct regular values in
  the interior of its range by Sard. Great-circle components at those values
  must intersect, contradicting disjoint level sets.
- For an even phase, descent gives embedded compact regular-level components
  in real projective space. The supporting scan was checked directly: its
  Theorem 1 states that compact developable smooth hypersurfaces in `RP^3` or
  `RP^5` are projective hyperplanes. This yields the `d=4,6` intersection
  contradiction.
- The same scanned page states that nontrivial compact examples exist in
  `RP^4, RP^7, RP^13, RP^25`; the higher-dimensional limitation is therefore
  genuine.

## Artifact checks

- [x] `main.tex` compiles without errors or warnings.
- [x] `solution_packet.pdf` has 4 pages.
- [x] Every packet page rendered at 160 DPI and visually inspected.
- [x] Source paper reconstructed from cached arXiv source.
- [x] Source paper has 9 pages; the question is on PDF page 8.
- [x] Exact source crop visually inspected.
- [x] Supporting Ishikawa scan downloaded from Hokkaido University repository
  and theorem page visually inspected.

## Human-review priorities

1. Check that the source stationary-phase proof requires only local
   invertibility of the bordered Hessian and no hidden positivity assumption.
2. Check projective-chart invariance of the nondegenerate second fundamental
   form and the great-circle continuation step.
3. Confirm applicability and bibliographic attribution of the
   Ishikawa--Morimoto theorem to embedded regular-level components.
4. Search for prior uses of the bordered-Hessian criterion before making any
   novelty or priority claim.
