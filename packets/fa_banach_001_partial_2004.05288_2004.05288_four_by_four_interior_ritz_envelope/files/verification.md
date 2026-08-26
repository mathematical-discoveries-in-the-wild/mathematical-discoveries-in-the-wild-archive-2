# Verification report

## Symbolic argument audited

The proof reduces the problem to two exact facts:

- Cauchy--Binet plus complementary minors of a unitary matrix gives the
  directional compression polynomial `P_theta(t,x)/delta(t)`.
- On the compact one-dimensional weight segment for `n=4`, the maximum of the
  larger root occurs at an endpoint, a simple stationary root, or a multiple
  root.

Neither fact depends on numerical computation.

## Numerical consistency check

Run from the repository root with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2004.05288_four_by_four_interior_ritz_envelope/code/verify_envelope.py
```

Output on 2026-08-17:

```text
direct compression root checks passed: 600
interior stationary checks passed: 45
worst root error: 1.443e-15
worst normalized stationary residual: 5.434e-10
source-like endpoint-only support gap: 0.055372249026
gap direction theta: 4.246806689617
directions with an interior maximizing weight: 66/361
coefficient-slice relaxation maximum gap: 0.196837808229
```

The 600 root checks compare the two zeros of the claimed quadratic with the
eigenvalues of a directly constructed nullspace compression.  The stationary
checks numerically maximize the larger root and test `partial_s P=0` at
interior maximizers.  Random examples use triangular boundary spectra plus a
fourth interior eigenvalue; the deterministic seed is `20260817`.

## What the code does not prove

Floating-point tests cannot prove the complementary-minor identity, the
maximum classification, exact real-rootedness, or novelty.  They only test
the derived formulas and expose two tempting but false simplifications:
endpoint weights alone do not suffice, and the fixed-root coefficient-polytope
slice is a strict relaxation.

## Human-review focus

1. Check that `det(Q^*Q)=delta(t)` and that complementary minors contribute
   exactly `t_i t_j |lambda_i-lambda_j|^2/delta(t)`.
2. Check that a simple interior maximum of the larger root has `P_s=0`, while
   a nonsimple maximum has `P_x=0`.
3. Check the feasibility filters and leading-coefficient degeneracies in the
   generic quartic reduction.
