# Verification report

## Source audit

- The downloaded arXiv:2306.13111 PDF has 6 pages and SHA-256
  `30f6b6ea1869090739cb38510b9cf8a44929fb158b3ff07af36353ea8a4c28bb`.
- PyMuPDF extraction locates the exact open sentence on PDF page 5:
  the relationship between alpha_A and beta_A for n>2 is still an open
  problem.
- The source separately mentions neural-network implementation of sorting.
  The packet explicitly excludes that second problem from its claimed scope.

## Later-literature audit

- The included arXiv:2510.22186v2 PDF has 37 pages and SHA-256
  `b3bcc810aa1a269bc1b23409203684008c5e82628377a50f6302536b24ef7bf5`.
- Its Theorems 4 and 5 give, respectively, the full-spark upper bound
  D >= n(d-1)+1 and a logarithmic noninjectivity bound.
- PyMuPDF extraction locates on PDF page 29 the numerical nonseparation list
  (n,d,D)=(3,2,3),(3,3,5),(3,4,7).  The text describes these as outcomes of
  random experiments, not a theorem.  The packet proves the full pattern
  n>=3, d>=2, D=2d-1 for every full-spark frame.
- Exact-title, exact-question, universal-key, phase-retrieval, sorting-encoder,
  and discrete-tomography searches through 2026-08-11 found no statement of
  the packet's frame-uniform theorem, D>=2d corollary, or scaled-isometric
  slice.  Novelty confidence is moderate.

## Proof audit

1. The antipodal embedding X_x=(x,-x,0,...,0) is well defined on the sign
   quotient.
2. Expanding the optimal assignment cost gives
   d_Sn(X_x,X_y)^2=2 d_pm(x,y)^2; matching both nonzero antipodal rows attains
   the maximal inner-product sum 2|<x,y>|.
3. Each sorted projected column is (-|s|,0,...,0,|s|), giving the exact
   sqrt(2) encoder-norm identity and transfer of admissible Lipschitz
   constants.
4. At D=2d-1, real phase retrieval is equivalent to full spark by the real
   complement property.
5. In the partition I dot-union J dot-union {k}, the two block normals exist
   and have nonzero pairing with a_k by full spark.
6. The prescribed scaling gives r1+r2+r3=0 and makes every frame column
   orthogonal to at least one r_i.
7. The block normals cannot be collinear: their common hyperplane would
   contain 2d-2 columns and hence a dependent d-subset.
8. Every measurement sees {0,t,-t}, so the two antipodal three-point clouds
   have identical sorted projections.
9. The clouds are not row permutations because an odd sign-invariant
   multiset of vectors must contain zero, whereas all three r_i are nonzero.
10. Adding equal zero rows preserves both equality of encodings and
    inequivalence for every n>3.

No logical gap was found in this audit.

## Exact computation

Command:

    conda run --no-capture-output -n sandbox python code/verify_switching_construction.py

The checker:

- verifies every maximal minor of Vandermonde frames with 2d-1 columns for
  d=2,...,8;
- constructs the block normals and r1,r2,r3 exactly with SymPy rationals;
- verifies equality of every projection multiset and inequivalence of the
  point clouds; and
- checks the scaled metric identity on representative exact vectors.

All checks passed.

## PDF and render audit

- Final PDF SHA-256:
  `55983410bacb6a82af40a4ed452f5f860616afd2b5f584666a1421417ce866c7`.
- Final packet: 5 letter-size pages.
- Latexmk completed after two passes with no warnings, undefined references,
  overfull boxes, or underfull boxes.
- PyMuPDF reopened the final PDF and extracted nonempty text from all pages.
- All five pages were rendered at 144 dpi after the final edit and inspected
  individually.  Titles, theorem statements, displayed equations, the
  classification table, citations, URLs, and page boundaries are legible;
  no clipping, overlap, or broken glyphs was found.
