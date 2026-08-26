# Verification record

## Analytic audit

The proof uses only the following direct facts.

1. For `g(t)=t^2 sin(1/t)`, `g'(t)=2t sin(1/t)-cos(1/t)` on `(0,1]`,
   hence `g` is Lipschitz.
2. The shear `h(x,y)=(x+g(y),y)` has inverse
   `h^{-1}(u,v)=(u-g(v),v)`, and both maps are Lipschitz.
3. The restriction of a function affine on a finite triangulation to one
   polygon edge is a finite piecewise-affine function.
4. The derivative of a scalar Lipschitz function at a differentiability point
   is bounded by its Lipschitz seminorm.

The sequences `1/(2*pi*n)` and `1/((2*n+1)*pi)` make `g'` exactly `-1`
and `+1`, respectively.  Therefore no constant boundary slope can reduce the
Lipschitz error below one.

## Numerical sanity check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/0806.3366_lipschitz_endpoint_oscillatory_shear/code/verify_shear.py
```

The script evaluates both oscillatory sequences for 500 indices and seven
candidate affine slopes, and checks the explicit shear/inverse identities on
a deterministic `101 x 101` grid.  This is a floating-point stress test, not
part of the proof.

Observed output:

```text
oscillatory slope checks: 3500
shear/inverse grid checks: 10201
all checks passed
```

## Human-review focus

Confirm that the paper's `piecewise affine` convention uses a Euclidean
finite complex (PDF page 4), so the boundary restriction really has a first
affine interval.  Also confirm the exponent-one Holder seminorm is the usual
Lipschitz seminorm.  No subtle limiting or measure-theoretic step remains.

## Final artifact audit

The final packet has three letter-size pages.  All three were rendered at 144
dpi and visually inspected after the final compilation.  The source crop is
readable at normal review zoom, and there is no clipping, overlap, malformed
mathematics, missing figure, or layout warning.

```text
SHA-256(solution_packet.pdf) =
ba9c0b4af0a779bfa6acefa442bb3e8efbffd03989017faae3b3dafceb3c77bc
SHA-256(source_paper.pdf) =
28267b56804b6589ea4520d6307434cf5ef32b3d03ef937d276b0ee5881b045a
```
