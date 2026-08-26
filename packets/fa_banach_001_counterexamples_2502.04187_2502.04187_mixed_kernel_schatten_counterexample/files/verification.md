# Verification report

## Exact proof checks

- On the four length-two cylinders, the special kernel is constant off the
  diagonal cylinder blocks and zero on them.
- With normalized indicators, the operator matrix is exactly `A_c/4`.
- The limiting matrix is real antisymmetric with Frobenius norm squared 12
  and Pfaffian 1, yielding singular values `sqrt(2)+1` and `sqrt(2)-1`, each
  twice.
- The logarithmic comparison function has value zero at `p=2` and derivative
  strictly less than `log(1+sqrt(2))-log(3)<0`; hence the failure is strict
  for every `1<p<2`.
- Since `d_f=log(2)/log(1/r)`, the same small-`r` choice can enforce the
  source's desired range `p>d_f/(1-2 alpha)`.

## Computational check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2502.04187_mixed_kernel_schatten_counterexample/code/verify_counterexample.py
```

Output:

```text
limit singular-value error 4.440892098500626e-16
p=1.10 limit_ratio=1.314614197611 c=256_ratio=1.314592386666
p=1.25 limit_ratio=1.210370404138 c=256_ratio=1.210363167126
p=1.50 limit_ratio=1.103891989714 c=256_ratio=1.103889686658
p=1.75 limit_ratio=1.040823284949 c=256_ratio=1.040822577214
p=1.90 limit_ratio=1.014429942170 c=256_ratio=1.014429720495
p=1.99 limit_ratio=1.001348039791 c=256_ratio=1.001348020462
Hadamard n= 2 orthogonality_error=2.22e-16 ratio_error=2.22e-16
Hadamard n= 4 orthogonality_error=0.00e+00 ratio_error=2.22e-16
Hadamard n= 8 orthogonality_error=1.11e-16 ratio_error=2.22e-16
Hadamard n=16 orthogonality_error=0.00e+00 ratio_error=2.22e-16
Hadamard n=32 orthogonality_error=1.11e-16 ratio_error=6.66e-16
```

The numerical checks are not used as proof.

## Source and visual checks

- `source_paper.pdf` is the official arXiv PDF for 2502.04187v1.
- `figures/open_problem_crop.png` is rendered from PDF page 20 and contains
  the full displayed inequality (2.12), its `p>=2` context, and Remark 2.18.
- The final packet PDF was rendered page by page and visually inspected.

## Expert review priorities

1. Check the convention for the binary ultrametric and the resulting sibling
   weight `c=2 r^(-1/4)`.
2. Check the finite-rank reduction and all normalization factors of 4.
3. Decide whether the source's phrase “inequality (2.12)” intended the exact
   constant-one inequality or merely some bound up to a multiplicative
   constant.  The packet proves the former false; the latter remains open for
   the special fractional kernels.

