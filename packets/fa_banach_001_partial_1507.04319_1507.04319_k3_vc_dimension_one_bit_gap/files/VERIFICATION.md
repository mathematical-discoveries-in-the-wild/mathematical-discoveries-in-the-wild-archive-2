# Verification report

Status: `candidate partial; likely valid; ready for human mathematical review`

## Mathematical audit

- The source definition and Problem 8 were checked in the official arXiv PDF,
  page 7.
- The proof translates Walsh signs to algebraic normal form over `F_2`,
  classifies all two-variable affine threshold dichotomies, and uses uniqueness
  of algebraic normal form for the exact count.
- The lower-bound construction was checked symbolically: affine interpolation
  fixes labels on `0,e_1,...,e_n`, and the decomposable quadratic part realizes
  the independently prescribed second differences on the edges of
  `K_{2,n-2}`.
- The upper bound uses only the exact class count and the elementary fact that
  shattering `m` points requires at least `2^m` distinct functions.
- The upgrade to exact VC dimension for `n>=4` is not claimed. Its remaining
  exterior-algebra quotient obstruction is stated explicitly in the packet.

## Independent finite checks

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1507.04319_k3_vc_dimension_one_bit_gap/code/verify_low_sparsity.py
```

Observed result: `all checks passed`.

The script checked:

- `C_{n,2}=C_{n,1}` for `1<=n<=5` using strict two-term signs;
- `|C_{n,3}|=2^{n+1}(1+[n choose 2]_2)` for `1<=n<=5`;
- every labeling of the explicit shattering set for `3<=n<=6`, including all
  `32768` labelings when `n=6`;
- exhaustive exact values `VC(C_{n,3})=2,4,7,9` for `n=1,2,3,4`.

These checks are independent sanity checks, not dependencies of the general
proof.

## Build and visual audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed with no final warnings, undefined references, overfull boxes, or
  underfull boxes.
- The final packet has 3 letter-size pages.
- Every final page was rendered at 150 dpi to an RGB PNG (`1275x1650`) and
  visually inspected. No clipping, overlap, unreadable glyph, broken formula,
  or malformed page transition was found.
- The source crop is a real render from source page 7 and contains the entire
  statement of Problem 8 together with its surrounding bound.
- Extracted final PDF text contains no unresolved `??` marker.

## SHA-256

```text
e8fbffe1779ae114e16d5bed761e0d0163e3aca3b44573a9971ff1c8aa55d729  solution_packet.pdf
7e823952ecec31e4e89da9aa1b3547ba8079bdab74ab62af5479419f97560140  source_paper.pdf
973288652e68eb4beb517dee9b224503fd5d26c2ff86591270bae3c476030fb0  figures/open_problem_crop.png
40271718192b0e7ea6c272bf280294f1dff793a27d2a9fa6c082348545ac6a9c  main.tex
32174d59b4cf714bd890bf03df8b1beb8fcaf63219bb6712c2a6a1d17e40fc33  code/verify_low_sparsity.py
```

## Human-review focus

Check that the 14 linearly separable dichotomies on the Boolean square split
as claimed, that a nonzero binary decomposable bivector uniquely identifies
its two-plane, and that the `K_{2,n-2}` coefficient assignment realizes both
edge second differences for every right vertex.

