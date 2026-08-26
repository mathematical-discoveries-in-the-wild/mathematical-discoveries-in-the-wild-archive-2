# Verification report

Status: candidate full solution; the defect reduction and recursive criterion
were checked algebraically and by finite-matrix sanity tests, pending expert
review.

## Formal proof checks

1. For each regular diagonal `D_i`, the restriction from a kernel complement
   to the range is an isomorphism. After reordering all such pieces, the
   corresponding block `P` is a finite upper-triangular matrix of isomorphisms
   and hence invertible.
2. The Schur complement `W - V P^-1 Q` has block `(i,j)` equal to zero for
   `i >= j`. The direct term has this pattern, and every correction path has
   indices `i < k <= l < j`.
3. Every strict upper-triangular defect map is realizable: project `X_j` onto
   `N(D_j)`, apply the desired defect block, and include a chosen cokernel
   complement into `X_i`. This sets the two mixed Schur blocks to zero.
4. For an invertible ordinary upper-triangular map, its first diagonal block
   has an explicit bounded left inverse obtained by inclusion, the global
   inverse, and first-coordinate projection. The last diagonal block has an
   analogous bounded right inverse.
5. Splitting those two ranges and applying triangular Gaussian operations
   decouples two isomorphism summands. The residual operator has one fewer row
   and column and retains the upper-triangular zero pattern.
6. At two defect rows (`n=3` in the source problem), the terminal recursive
   condition is exactly the quotient isomorphism in source Theorem 2.1(1c).

## Computational sanity check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2202.04960_all_n_recursive_defect_completion/code/verify_recursive_completion.py
```

The verifier constructs an invertible triangular defect map with unequal
individual block dimensions, embeds it as a prescribed Schur complement,
checks the forbidden defect blocks for a random four-level system, and samples
an obstructed prefix-dimension pattern. Numerical evidence is not used in the
proof. A nontrivial one-sided defect of a square diagonal operator is
inherently infinite-dimensional, so finite square matrices cannot model the
entire source theorem directly.

Observed output:

```text
positive defect determinant=1.000000e+00
positive reduced determinant=1.599774e+06
positive reduced minimum singular value=9.805164e-01
random Schur maximum forbidden block entry=0.000000e+00
random Schur determinant identity error=0.000000e+00
obstructed pattern maximum rank over 500 trials=3 of 5
```

## Review priority

The two decisive points are preservation of the strict zero pattern under the
Schur correction and preservation of ordinary upper triangularity after the
recursive endpoint peeling. Once those are confirmed, both directions of the
main theorem are constructive.
