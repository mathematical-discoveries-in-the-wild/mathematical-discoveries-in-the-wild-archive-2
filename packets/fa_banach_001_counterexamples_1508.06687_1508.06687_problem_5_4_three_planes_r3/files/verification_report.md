# Verification report

Packet: `1508.06687_problem_5_4_three_planes_r3`

## Mathematical audit

1. The four-measurement map is a real linear map from the six-dimensional
   space of real symmetric `3 x 3` matrices, so its kernel contains a
   two-dimensional real subspace.
2. The determinant restricted to that subspace is a homogeneous cubic and is
   odd on its unit circle; hence it has a nonzero zero.
3. A positive or negative semidefinite kernel matrix is impossible because
   the first two projection kernels are `span(e1)` and `span(e2)`, whose
   intersection is zero.
4. The singular kernel matrix is therefore indefinite of rank two and yields
   a genuine pair `xx*`, `yy*` with equal measurements and `x` not
   phase-equivalent to `y`.
5. The partition proof exhausts all cases: every plane basis either lies in
   the two-dimensional second span or splits between the first line and the
   second plane.  Linear independence of the three normals forces exactly one
   plane to be the second span.  Each of the three possibilities violates an
   explicitly computed orthogonality relation.
6. All arguments remain valid over `C`: the lifted kernel is taken inside the
   real-symmetric subspace of Hermitian matrices, and the incidence argument
   uses complex spans with the same real representatives.

No missing case or division by a potentially zero quantity was found.  The
choice `M=N=3` makes the result insensitive to the source's apparent use of
`M` where the proof of Corollary 5.3 suggests `N`.

## Computational sanity check

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
```

Output:

```text
three plane projections verified exactly
partition dot-product obstructions: [1, 1, 1]
fourth-subspace samples checked: 102
all sampled lifted kernels contained an indefinite singular witness
```

The incidence calculations use exact SymPy arithmetic.  The random portion
samples rational subspaces of ranks 0, 1, 2, and 3 and numerically selects the
real root of the exact determinant polynomial.  It is not used as a proof of
the universal fourth-subspace claim.

## Artifact audit

- `source_paper.pdf` opens as a 19-page PDF.
- `figures/open_problem_crop.png` visibly contains Corollary 5.3 and all of
  Problem 5.4 from source page 18.
- The packet was compiled with `latexmk`, text-extracted, and every rendered
  page visually inspected.
- The final LaTeX log has no unresolved references or overfull boxes.

Verdict: `candidate_counterexample_likely_valid`; expert novelty review is
still required.
