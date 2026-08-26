# Verification report

## Mathematical checks

The proof was checked symbolically for:

1. the tensor-product telescoping identity;
2. the uniform scalar Cesaro estimate;
3. the Abel summation identity used to obtain the Kreiss bound;
4. invariance of the finite coordinate compression;
5. the power witness on `e_L tensor e_2^(tensor m)`;
6. conversion from dimensions `2^m L` to every integer dimension by padding
   with a zero block;
7. strict monotonicity and endpoint limits of the final exponent function.

## Finite numerical checks

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2512.10025_polynomial_lower_bounds_all_kreiss_constants/code/verify_tensor_shift.py
```

Results:

- tensor telescoping passed for `a in {0.04,0.12,0.21}`, `m=1,...,4`, and
  three coordinate intervals;
- the scalar averaging coefficient stayed below the proved bound for
  `a in {0.02,0.08,0.16,0.24}`, nine averaging lengths through `200`, and
  all tested coordinate indices through roughly eight times the averaging
  length;
- power-witness formulas passed for three finite tensor shifts of dimensions
  `36`, `80`, and `96`;
- sampled resolvent/Kreiss ratios on nine radii and 48 angles stayed below
  the rigorous bounds in those three examples.

All checks passed.  Floating-point sampling is not a proof and does not
establish the global resolvent supremum; the analytic averaging and Abel
arguments do that.

## Literature check

The local lightweight indexes and bounded current arXiv/web searches found no
answer using the tensorized construction.  Novelty remains unconfirmed.

## Verdict

`candidate_full_solution_likely_valid_novelty_unconfirmed`

