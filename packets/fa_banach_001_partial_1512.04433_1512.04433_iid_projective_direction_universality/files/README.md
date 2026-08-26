# Exact iid universality for unshifted binary embeddings

Status: candidate substantial partial result, likely valid.

Source target: Samet Oymak and Benjamin Recht, *Near-Optimal Bounds for Binary
Embeddings of Arbitrary Sets*, arXiv:1512.04433.

## Result

For hyperplane-nondegenerate iid rows, the unshifted sign/Hamming embedding has
exactly the same joint pairwise-distance process as iid Gaussian rows on every
finite set and for every number of rows if and only if the row's unoriented
direction is Haar-uniform in real projective space.

Equivalently, equality of every population separation probability with
normalized spherical angle already forces projective Haar uniformity.  Thus a
non-Haar projective row law has a two-point population bias, and sufficiently
accurate embedding of that pair fails with probability tending to one.

An explicit obstruction shows why linear-universality hypotheses do not
suffice: iid Rademacher rows are isotropic and bounded subgaussian, but a fixed
two-point set has empirical Hamming distance zero for every row count while
its angular distance is positive.

## Scope

This is a sharp answer to an exact iid-row formalization of the source's broad
universality question.  It does not classify dependent fast transforms, nor
ensembles that only match Gaussian distortion rates up to constants.  The
source's broader structured-matrix question therefore remains open.

## Files

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source passage on page 16.
- `code/check_gegenbauer_coefficients.py`: finite symbolic and discrete sanity
  checks; it is not used as proof.
- `verification.md`: proof and computation audit.

## Reviewer focus

The main point to verify is the injectivity argument: nonvanishing of every
odd Funk--Hecke coefficient and the fact that products of odd harmonics span
the even spherical polynomials.

