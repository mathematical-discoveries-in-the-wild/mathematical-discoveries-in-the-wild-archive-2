# Verification Record

- Target: the conjecture in Section 6.4 of arXiv:2207.14282v5 that the
  barycentric maximal Rényi divergence is strictly smaller than the maximal
  Rényi divergence for all noncommuting invertible inputs; the source proves
  only dimension two.
- The conjecture, the variational reduction, the derivative formula labelled
  Dmax derivative2, the scalar Lambda formula, and the two-dimensional
  proof were checked against the local parsed arXiv source.
- Cheap indexes and bounded exact-conjecture, title, arXiv-id, citation,
  barycentric-maximal, maximal-Rényi, and strict-inequality searches through
  17 August 2026 found the 2024 publication and later applications, but no
  proof beyond dimension two.
- Proof audit:
  1. the source kernel depends only on log(lambda_i/lambda_j);
  2. the hyperbolic decomposition into scaled copies of
     h(x)-1, h(x)=(x/2)coth(x/2), is exact;
  3. the partial-fraction series makes this kernel conditionally negative
     definite;
  4. the finite Schoenberg Gram matrix is positive semidefinite and yields
     squared distances exactly equal to Lambda-1;
  5. the Schur product with the squared-distance matrix is a sum of double
     commutators;
  6. diagonalizing the positive matrix S gives the claimed negative
     sum-of-squares trace identity;
  7. equality means S is block diagonal across equal eigenvalues of
     sigma^(-1/2)rho sigma^(-1/2), exactly the commuting case;
  8. the negative derivative is along a feasible state segment and therefore
     gives the strict variational inequality.
- Auxiliary command:

  conda run --no-capture-output -n sandbox python code/verify_cnd_derivative.py

  Result: hyperbolic decomposition, partial fractions, 5,280 random strict
  derivative tests in dimensions 2--12, Schoenberg reconstructions,
  double-commutator identities, and commuting equality tests all passed.
- The source-PDF download was denied by the environment's external-usage
  limit.  No mathematical evidence was lost because the full arXiv v5 TeX
  source is already local and was the version audited.

- `solution_packet.pdf` was compiled after the required PDF artifact marker.
  The final LaTeX pass has no warnings, errors, overfull boxes, underfull
  boxes, duplicate destinations, or undefined references.
- The final PDF has three letter-size pages.  Text extraction confirmed the
  theorem, both structural lemmas, full proof, novelty section, human-review
  recommendation, and reference.
- Every final page was rendered at 150 dpi and visually inspected after the
  latest source edit.  There is no clipping, overlap, malformed equation, or
  bad page break.

Final SHA-256: `5e90d33b5453557344ce64b13fe5ca30bf08a02354e7d1b2c1e4be11338adf89`.
