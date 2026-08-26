# Verification record

## Analytic audit

The packet checks the following points explicitly.

1. Each compact subset of `R` meets finitely many cells, so both weights are
   strictly positive and compact-bounded despite jumps in their common
   factor.
2. The common factor cancels from the quotient. The quotient equals one near
   every cell boundary and is piecewise Lipschitz, hence locally Lipschitz.
3. Reflection across each cell center exchanges the endpoint weights and
   fixes the block. Thus the two endpoint block norms are exactly equal.
4. The core endpoint mass is

   ```text
   1/3 + (M-1)/(3 M log M) + 1/(3M),
   ```

   while both collars contribute at most `(65/4) M^{-3}`. Therefore the
   common endpoint block norm squared lies in `[1/3,1.005)`.
5. Comparing the full-core average with the average on the high-weight third,
   and then using the fundamental theorem of calculus, gives a common
   projection estimate with squared norm below `6.03` on both endpoints.
6. Its endpoint ranges coincide with the same weighted `ell^2` block space.
7. Coefficients `1/n` lie in that endpoint space, while each auxiliary
   logarithmic-gradient block contributes exactly

   ```text
   12 n^{-2} (log M_n)^2 M_n^{3/2},
   ```

   which diverges.
8. The geometric-mean block norm squared is at most
   `M_n^{-1/2}+(65/4)M_n^{-7/2}`. Hence coefficients `n^{-1/2}` give a
   geometric-mean Sobolev function. If it belonged to the endpoint sum, the
   common projection would force the divergent series
   `sum B_n/n` to converge.

The source paper's Theorem 1.21 supplies the full auxiliary-space inclusion on
`U=R`, so the first witness establishes the exact proper inclusion asked on
PDF page 47.

## Computational sanity check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1807.10790_block_projection_weighted_sobolev_counterexample/code/verify_blocks.py
```

Observed output:

```text
reflection identities: checked on 12,006 points
n  core mass       endpoint B upper  middle D upper   P norm^2 upper
1   4.668772167361e-01   1.003967285156e+00    2.509918212891e-01    6.023803710938e+00
2   3.945128963911e-01   1.000000968575e+00    6.250006053597e-02    6.000005811453e+00
4   3.633941076611e-01   1.000000000000e+00    3.906250000000e-03    6.000000000000e+00
8   3.483614067500e-01   1.000000000000e+00    1.525878906250e-05    6.000000000000e+00
endpoint d witness, first 200 blocks (upper): 1.643914073341
auxiliary d witness, first 8 block terms:
  5.904e+03 3.778e+05 2.418e+07 1.548e+09 9.905e+10 6.339e+12 4.057e+14 2.597e+16
middle c witness, first 200 blocks (upper): 0.288673924010
projected c endpoint lower sums, N=400 and 4000: 2.189976563726, 2.957130099932
all checks passed
```

The script checks explicit formulas and finite samples only; it is not the
proof.

## Packet rendering

`solution_packet.pdf` was compiled with resolved references and no LaTeX
overfull/underfull warnings. All six pages were rendered to PNG and visually
inspected. The source screenshot is readable, and no clipping or layout defect
was found.

Final PDF SHA256:

```text
20448701cf076ce75d98023df7a8c9233057775ad44c05657650b6467933e5b1
```

## Human-review focus

The most consequential check is that the same core-average formula defines a
bounded projection on both endpoint spaces and therefore on their algebraic
sum. Review also the source-theorem hypothesis match: the weights themselves
may jump, while their quotient is locally Lipschitz, exactly as permitted by
the compact-bounded framework of arXiv:1807.10790.

