# Finite Intermediate-Dimensional Subspaces Are Not Unique

Source: A. Fernández-Bertolin, K. Gröchenig, and P. Jaming, *From
Heisenberg uniqueness pairs to properties of the Helmholtz and Laplace
equations*, arXiv:1711.05520; J. Math. Anal. Appl. 469 (2019), 202–219.

Status: candidate full negative solution, likely valid.

## Result

For every finite family of linear subspaces `E_j` of `R^d` with
`dim E_j <= d-2` and every real wave number `lambda`, there is a nonzero
real entire solution of

```text
(Delta + lambda^2)u = 0
```

that vanishes identically on their union. This fully answers the source's
open intermediate-dimensional linear-subspace case in the negative.

At degree `m`, ambient homogeneous harmonics have dimension of order
`m^(d-2)`, whereas restriction to a `k`-plane has rank at most order
`m^(k-1)`. A finite direct sum of restrictions therefore has a nonzero
kernel whenever `k <= d-2` and `m` is large. An explicit regular radial
power series upgrades the common kernel harmonic to every Helmholtz wave
number. Funk–Hecke also produces two distinct positive sphere measures
whose Fourier transforms agree on the same finite union, so the associated
Heisenberg uniqueness pair fails.

## Files

- `main.tex`: exact theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source PDF.
- `figures/open_question_crop.png`: page-18 open-question crop.
- `code/verify_dimension_and_radial.py`: exact arithmetic consistency checks.
- `verification.md`: reproducibility, checksum, and visual-QA record.

## Human Review Recommendation

Confirm that the open sentence inherits the finite-family setting of the
preceding general problem and check the elementary restriction-rank bound.
The remainder is a direct asymptotic dimension gap and an exact radial
coefficient recurrence.

