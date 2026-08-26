# Gaussian kernels fail on every positive-dimensional closed manifold

Status: `candidate_full_likely_valid`.

Source: Siran Li, *Gaussian kernels on non-simply-connected closed Riemannian
manifolds are never positive definite*, arXiv:2303.06558.

## Full result

For every positive-dimensional closed Riemannian manifold `(M,g)` and every
`lambda > 0`, the intrinsic Gaussian kernel

```text
k_lambda(x,y) = exp(-lambda d_g(x,y)^2)
```

is not positive definite.  Thus `Lambda_+(M,g)=empty`, including for simply
connected closed manifolds.

The proof uses any nonconstant closed geodesic.  If the kernel were positive
definite, its RKHS feature map along that geodesic would be locally congruent
to the entire Gaussian feature curve on the real line.  It is therefore real
analytic.  Analytic continuation forces the line-Gaussian correlation for
all time differences, contradicting periodicity of the closed geodesic.

The packet also proves an abstract obstruction for any metric space containing
a periodic locally isometric copy of an interval.

## Reproduction

Run the numerical consistency check with:

```bash
conda run --no-capture-output -n sandbox python \
  code/verify_gaussian_feature_curve.py
```

The script checks the explicit feature-series identity and the positive
feature-space separation between times `0` and `L` that periodicity would
force to coincide.
