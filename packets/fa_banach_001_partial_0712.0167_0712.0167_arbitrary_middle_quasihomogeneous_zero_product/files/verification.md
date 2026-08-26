# Verification report

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

1. The source crop was rendered from page 2 of arXiv:0712.0167 and visually
   checked against Problem 1.1 and the paper's radial scope.
2. The supporting crop was rendered from page 2 of arXiv:2009.01951, current
   March 2026 revision. It shows the finite-character theorem, its endpoint
   arbitrary-symbol corollary, and the interacting-series obstruction.
3. Torus orthogonality gives one output monomial for a single-character
   quasihomogeneous symbol. All intermediate exponents are made nonnegative
   by choosing the two base multi-indices sufficiently large.
4. Positive monomial norm factors never vanish and are discarded only after
   evaluating the operator identity on integer indices; they are not silently
   analytically continued.
5. Each remaining weight is a translate of a multivariable Mellin transform.
   After coordinate dilation and a fixed monomial shift, it is bounded and
   holomorphic on the product of right half-planes.
6. A nonzero quasihomogeneous symbol gives a nonzero Mellin transform:
   identically vanishing moments would annihilate all polynomials on a cube,
   so Stone-Weierstrass forces the radial amplitude to vanish.
7. The positive integer lattice is a uniqueness set for bounded holomorphic
   functions on a product of half-planes. The proof iterates the one-variable
   non-Blaschke uniqueness theorem one coordinate at a time.
8. For every angular difference, the product of the nonzero outer Mellin
   factors and the arbitrary symbol's fixed-frequency Mellin transform
   vanishes on the lattice. Holomorphic integral-domain uniqueness forces the
   latter transform to vanish identically.
9. Polynomial moment uniqueness makes every radial Fourier coefficient zero;
   countability of the torus characters and Fourier uniqueness then give
   `f=0` almost everywhere.
10. Eight distinct upgrade attempts were recorded. The packet does not use
    the failed finite-angular-sum or two-arbitrary-symbol routes.

Human review should verify the cumulative degree convention in the left and
right weighted-shift coefficients and the standard Laurent-monomial
decomposition on a general bounded Reinhardt domain. No numerical evidence
is part of the proof.
