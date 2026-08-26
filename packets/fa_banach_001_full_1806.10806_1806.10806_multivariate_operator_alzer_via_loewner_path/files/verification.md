# Verification report

Status: candidate full solution; proof and equality characterization audited
symbolically and numerically, pending expert review.

## Formal proof checks

1. For `k_lambda(t)=t/(t+lambda)`, direct algebra gives
   `k(1)-k(0)-k'(1/2)=1/[4(1+lambda)(lambda+1/2)^2] > 0`.
2. At every matrix level, `S <= T` implies
   `P_j tensor I + Q_j tensor S <= P_j tensor I + Q_j tensor T`.
   Joint monotonicity of the recursive Kubo–Ando mean and compression by
   `u tensor identity` therefore prove operator monotonicity of each scalar
   path quadratic form.
3. The first derivative of `X #_alpha Y` at `(cI,cI)` is
   `(1-alpha)H+alpha K`; recursion gives uniform weights `1/n`.
4. The second derivative at the scalar diagonal is
   `(1-alpha)X''+alpha Y''-alpha(1-alpha)(X'-Y')^2/c`, which makes the
   equality induction a sum of negative squares.

## Computational sanity checks

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1806.10806_multivariate_operator_alzer_via_loewner_path/code/verify_theorem.py
```

The verifier checks the scalar kernel identity, the midpoint derivative by
centered finite differences, and random real/complex positive matrices for
several dimensions and variable counts.  The exploratory scripts additionally
performed 200,000-case searches in selected configurations and a bounded
differential-evolution/Powell search over real `2 x 2` triples.  All observed
defects were positive semidefinite up to floating-point roundoff.  Numerical
evidence is not used in the proof.

Observed verifier output:

```text
minimum scalar kernel gap: 2.500e-25
dim=2 n=3 complex=False trials=5000 min_defect=1.055e-05 max_midpoint_derivative_error=9.784e-11
dim=2 n=4 complex=True trials=5000 min_defect=1.313e-04 max_midpoint_derivative_error=2.395e-10
dim=3 n=3 complex=True trials=5000 min_defect=7.406e-05 max_midpoint_derivative_error=3.441e-10
```

## Review priority

The amplification/compression lemma is the decisive step.  The main inequality
is independent of the second-order equality analysis, so review those portions
separately.
