# Exact algebraic envelope for the four-by-four interior-eigenvalue case

Status: `candidate_partial_likely_valid`.

Source: Kennett L. Dela Rosa and Hugo J. Woerdeman, *Location of Ritz values
in the numerical range of normal matrices*, Linear and Multilinear Algebra 69
(2021), 2749--2778, arXiv:2004.05288.

## Result

The source asks how to characterize `conv B_A(mu)` when a normal matrix has
eigenvalues in the interior of its numerical range.  This packet gives:

1. an explicit characteristic polynomial for every directional Hermitian
   compression in arbitrary dimension; and
2. an exact low-degree envelope solution when `A` is `4 x 4`, has four
   distinct noncollinear eigenvalues, and `mu` is not an eigenvalue.

For a direction `theta`, the weight polytope is a line segment `t(s)`.  Its
directional support is the largest candidate obtained from the two endpoint
quadratics and the interior systems

```text
P_theta(s,x)=partial_s P_theta(s,x)=0,
P_theta(s,x)=partial_x P_theta(s,x)=0.
```

Generically, both interior systems reduce to equations of degree at most four.
The convex hull is recovered as the intersection of the resulting supporting
half-planes.

## Scope

This fully handles the first missing four-dimensional interior-spectrum case,
including the structural phenomenon in the source's Figure 2.  It does not
give a comparably simple geometric description for `n >= 5`, does not handle
the singular parameter case `mu in sigma(A)`, and does not solve the separate
`k >= 3` Ritz-tuple problem.  It is therefore classified as a substantial
partial result.

## Verification

`code/verify_envelope.py` passed 600 comparisons against direct nullspace
compressions and 45 numerical stationary-point checks.  The worst root error
was `1.443e-15`; the worst normalized stationary residual was `5.434e-10`.
The source-like example also shows a positive `0.055372249026` support gap
between the exact envelope and endpoint ellipses alone.

See `verification.md` for the command, complete output, and proof-versus-code
boundary.  The mathematical result is proved in `solution_packet.pdf`.

Human review should focus on the complementary-minor normalization and on the
exhaustion of endpoint, simple-stationary, and multiple-root maxima.
