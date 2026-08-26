# Verifier report

Date: 2026-08-13

Status: `all_sanity_checks_passed`

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.16453_uniform_bv_mercer_absolute_convergence_counterexample/code/verify_counterexample.py
```

Output:

```text
PASS: b_n is decreasing and convex for n=0,...,5000
PASS: finite Fejer mass/coefficient telescoping identities
sampled sup tail N= 20, M=5000: 3.191314e-01
sampled sup tail N= 50, M=5000: 2.503794e-01
sampled sup tail N=100, M=5000: 1.644677e-01
sampled sup tail N=200, M=5000: 4.977230e-02
PASS: sampled sine-series tails decrease on a 401-point grid
absolute partial sum at (pi/4,pi/4), N=    100: 0.83398384
absolute partial sum at (pi/4,pi/4), N=   1000: 0.93518783
absolute partial sum at (pi/4,pi/4), N=  10000: 1.00710053
absolute partial sum at (pi/4,pi/4), N= 100000: 1.06288596
absolute partial sum at (pi/4,pi/4), N=1000000: 1.10846632
PASS: absolute partial sums grow; the proof supplies divergence
PASS: first 5000 positive singular coefficients are strictly decreasing
PASS: sampled coefficient square sum is finite
ALL SANITY CHECKS PASSED
```

## Scope

The high-precision checks cover strict monotonicity and discrete convexity
through index 5000 and exact finite forms of both telescoping identities for
several truncations and Fourier modes.  The floating-point checks sample 401
points for four sine-series tails, five absolute partial sums up to one
million terms, and the first 5000 singular coefficients.

These checks are not the proof.  In particular, finite growth does not prove
divergence, sampled tails do not prove uniform convergence, and finite
convexity does not prove convexity for every index.  The packet proves those
facts analytically via differentiation, telescoping, Abel summation, and a
comparison with the logarithmic harmonic series.

## Manual proof audit

- The factors `1/2`, `pi`, and `sqrt(pi)` in the Fejer mixture and SVD were
  checked against the standard Fourier-integral normalization on
  `[-pi,pi]`.
- The boundary terms in both telescoping identities were expanded at finite
  truncation before limits were taken.
- The primitive has matching endpoint values because its derivative is even
  and mean zero.
- The weak section derivatives integrate over exactly one full period, giving
  a common variation bound `||h||_1`.
- The constant, sine, and cosine subspaces exhaust `L2[-pi,pi]`, so the listed
  diagonal singular pairs exhaust all positive singular values.
- Strict decrease of `a_n` rules out rotations inside repeated positive
  singular subspaces.

Human review recommendation: check first equation (5), the finite coefficient
telescoping identity in the packet, and then the exhaustiveness paragraph
after equation (12).  No computational or unproved conditional dependency
remains.

