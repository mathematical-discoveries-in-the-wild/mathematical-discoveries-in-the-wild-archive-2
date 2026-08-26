# Verification report

Status: candidate partial result, likely valid, pending human review.

## Analytic checks

- Checked that `h(u)=((1-c)delta^p+c|u|^p)^(1/p)` is an even convex
  function and is 1-Lipschitz, including the piecewise-linear case `p=1`.
- Checked that monotonicity of `u-h(u)` and `u+h(u)` reduces the common-center
  condition to the two endpoints of each feasible interval.
- Checked the exact algebra converting each scalar decoder inequality into
  the arbitrary-`n` upper bound.
- Checked that the lower-bound cap remains in the first two coordinate
  directions and that the two antipodal inputs are both compatible with the
  same zero datum.

## Computational sanity check

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2510.23213_noisy_diagonal_one_measurement_and_upper_bound/code/verify_scalar_center.py
```

The script checks a deterministic parameter grid and 20,000 seeded random
instances, with 101 input-coordinate samples per nonempty feasible interval.
It reports the largest positive inequality violation and exits nonzero on a
violation above roundoff. It passed 48,413 parameter instances; the largest
positive violation was `1.1102230246251565e-16`. This is not used as proof.

The attempt-level script
`runs/fa_banach_001/attempts/2510.23213_noisy_diagonal_numeric_probe.py`
also compared coordinate information with 150 random two-row Euclidean
measurement systems in each of four three-dimensional cases. It found no
sampled improvement over coordinate information. This probe is evidence only
and no general-`n` lower bound is claimed.

## Literature check

On 11 August 2026, exact-title, exact-notation, arXiv-id, and core-keyword
searches located the source arXiv record and the revised Journal of Fourier
Analysis and Applications article (published 16 March 2026). The journal
version still states the exact-value question as open in Section 5.2. No later
answer for the one-measurement formula or the sharper upper bound was found.
The search was bounded, not exhaustive.

## Human-review recommendation

Check the interval-intersection lemma, the definition of the nonlinear
reconstruction for every consistent datum, and the intermediate-value step on
the `ell_p^2` unit-sphere cap. The unresolved multi-slab lower bound should
remain clearly separated from the proved upper bound.
