# Verification audit

Status: `candidate substantial partial; likely valid; human review requested`

## Mathematical audit

- The exact open question was checked in the official arXiv PDF of arXiv:1901.03883, in the abstract and on source p. 2.
- The completely polynomially bounded case uses Paulsen's equivalence between complete polynomial boundedness and similarity to a contraction, followed by Uchiyama's contraction criterion. The two-sided kernel estimate is preserved under the invertible similarity.
- The weighted-shift proof was checked directly from `X e_n=P_n^(-1)S^nX e_0`: boundedness of `X` gives a uniform lower bound on `|P_n|`, and power boundedness gives the upper bound needed for a diagonal similarity.
- The interpolating-sequence proof uses only finite sign data. Exact polynomial interpolation with norm arbitrarily close to the `H^infinity` interpolation constant follows by radial dilation, a finite Lagrange correction, uniform disk-algebra approximation, and a second arbitrarily small correction.
- The Riesz estimate follows from uniform sign-change bounds and Rademacher averaging. The final bounded-below conclusion also uses the standard Riesz-sequence characterization of normalized Hardy kernels on an interpolating sequence.
- The cluster--orthogonality inequality was checked from the exact identity `|<u_lambda,u_mu>|=sqrt(1-rho(lambda,mu)^2)`.
- In arXiv:2412.14130, Theorem 6.3 puts `2^(N+1)` distinct lower diagonal eigenvalues into a compact subdisk. Their adjoint eigenvectors occupy mutually orthogonal coordinate-chain subspaces. A common disk automorphism preserves both those eigenspaces and pseudohyperbolic distances.
- The final Corollary 2.3 shift extension is polynomially bounded and a quasiaffine transform of `S`. The standard defect-one theorem, applied after disk automorphisms, makes each adjoint eigenspace one-dimensional. Hence every candidate intertwiner maps a root kernel into the same finite-block line as the canonical intertwiner.
- Compact pseudohyperbolic packing forces a pairwise distance tending to zero because the number of lower-block roots tends to infinity, contradicting the uniform separation forced by cluster--orthogonality.
- The packet does not use the unproved cyclic-Jordan perturbation route or the failed corona route.

## Scope and novelty audit

- Proved: the completely polynomially bounded case.
- Proved: the unilateral weighted-shift case under the weaker assumption of power boundedness and one nonzero intertwiner.
- Proved: Riesz rigidity and a bounded-below restriction on every interpolating kernel span.
- Proved: the direct arXiv:2412.14130 Theorem 6.3 / Theorem 7.1 / Corollary 2.3 shift extension cannot satisfy the source lower estimate for any intertwiner.
- Not proved: the full polynomially bounded criterion.
- A bounded search used the exact title, author, arXiv id, and the phrases `polynomially bounded`, `holomorphic eigenvectors`, and `similar to the unilateral shift`. No later paper explicitly resolving the exact question was found.
- arXiv:2412.14130 explicitly answers a different question of Kerchy and does not claim to resolve arXiv:1901.03883.

## Artifact audit

- `source_paper.pdf`: 14-page official arXiv PDF; SHA-256 `35387b871e7291a1e11e606cc68ce825bb26f7d1b9ad165a60b552e805d96650`.
- `supporting_paper_2412.14130.pdf`: 26-page official arXiv PDF; SHA-256 `473095d3241e7d58d33767b7626db16e37a8470a492df653b95826c8c9898073`.
- `figures/open_problem_crop.png`: rendered from source PDF p. 2 at 180 dpi and visually checked; SHA-256 `443656e05996c3d035727d42dcfaa053e4f58a55bf4bafc977af708a79270e6f`.
- `solution_packet.pdf`: 6 A4 pages; SHA-256 `df2868876b29b6d9a8b9b6301e605803a7b48032fc6473d4f888f4b38e384bae`.
- Final LaTeX compilation completed without warnings, bad boxes, undefined references, or duplicate destinations.
- Ghostscript parsed the final PDF successfully.
- Bundled `pypdf` reopened all six pages and extracted the status, principal construction-audit theorem, and references.
- All six final pages were rendered at 170 dpi and inspected at original detail; no clipping, overlap, illegible text, or broken crop was found.

