# Verification record

## Analytic checks

For data `(lambda_1,lambda_2)=(1,2)` and `(w_1,w_2)=(0,r)`, the classical
Pick determinant is

```text
(1-|r|^2)/8 - 1/9 = (1-9|r|^2)/72.
```

It is strictly positive for `|r|<1/3`. The zeta Pick determinant has the sign
of

```text
1-|r|^2 - zeta(3)^2/(zeta(2)zeta(4)).
```

The source proves the zeta ratio is below `8/9`, so this determinant is also
strictly positive for `|r|<1/3`.

For the Bohr points, direct algebra gives

```text
rho(p^{-1},p^{-2}) = p/(p^2+p+1).
```

Its derivative as a real function is `(1-p^2)/(p^2+p+1)^2`, so it decreases
for `p>1`; among primes its maximum is `2/7`.

Finally, `B(z)=(1/2-z)/(1-z/2)` is a disk automorphism with
`B(1/2)=0` and `B(1/4)=2/7`. Its geometric expansion after substituting
`z=2^{-s}` converges on `Re(s)>0`, proving the sharp sufficiency statement.

## Computational check

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2505.02098_bohr_metric_two_point_counterexample/code/verify_two_point.py
```

The script checks the rational determinant at `r=3/10`, evaluates the zeta
ratio at 80 decimal digits, checks monotonicity over the first 25 primes, and
verifies the explicit interpolant values and its first 200 boundary samples.
These computations are sanity checks only; the packet proof is analytic.

Observed output:

```text
classical determinant at r=3/10: 19/7200
zeta ratio: 0.811604744850967630427533958323
largest prime-coordinate distance: 0.285714285714285714285714285714
explicit B values: B(1/2)=0, B(1/4)=2/7
all checks passed
```

The four-page `solution_packet.pdf` was compiled twice with resolved
cross-references and visually inspected page by page. No clipping or layout
defect was found. Its SHA256 digest is
`509c62a19328ece5c63818ba9e437a427428c624a351f4332acff3e71a19050d`.

## Human-review focus

Confirm that the standard Bohr-transform isometry applies to the source class
`H^infty(H_0) \cap D` exactly as used. The coordinatewise automorphism and
Banach-ball Schwarz lemma are then enough for the metric contraction. All
matrix and threshold inequalities are strict and elementary.
