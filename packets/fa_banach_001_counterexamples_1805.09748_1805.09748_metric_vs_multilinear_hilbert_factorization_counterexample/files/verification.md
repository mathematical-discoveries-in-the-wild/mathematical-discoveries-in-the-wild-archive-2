# Verifier report

Date: 2026-08-09

Verdict: `likely valid`, suitable for human review as a candidate
counterexample to both Questions 1--2 of arXiv:1805.09748 over the real
scalars.

## Algebraic audit

- The normalized factor ambiguity is exactly simultaneous sign, so the
  quadratic feature `w tensor w / ||w||_2` is well-defined.
- The contraction argument proves `rho <= delta <= 8 rho` without a hidden
  compactness or differentiability assumption.
- The exact quadratic identity gives the quotient Hilbert bounds, and the
  radial calculation gives `Lip(F_m) <= 24 sqrt(2)` and
  `Lip(F_m^{-1}) <= 5 sqrt(m)`.
- The Rademacher expectation is exactly the sum of the squared coefficient
  norms, yielding `Gamma(J_m)=m`.
- The global diagonal projection is contractive in the projective tensor
  norm. Injectivity in each block makes the output map well-defined, and the
  `ell_2` target sum makes its Lipschitz constant at most one.
- Restriction to a block and coordinate projection preserve the multi-ideal
  bound, while the restricted norms tend to infinity.

No missing lemma was found in this audit.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1805.09748_metric_vs_multilinear_hilbert_factorization_counterexample/code/check_rank_one_factorization.py
```

Output:

```text
m= 2 trials= 20000 max(delta/rho)=2.3208 max(e/rho)=1.3897 max(rho/e)=1.4607 max(D/d)=1.7981 max(d/D)=1.4045
m= 4 trials= 20000 max(delta/rho)=2.0961 max(e/rho)=1.0538 max(rho/e)=1.9401 max(D/d)=1.4983 max(d/D)=1.8803
m= 8 trials= 20000 max(delta/rho)=1.9742 max(e/rho)=0.7151 max(rho/e)=2.3458 max(D/d)=1.2669 max(d/D)=2.2261
finite strict gap: m=32768, metric_bound=30720, Gamma(J_m)=32768
```

The random checks are not part of the proof.

## Render audit

The eight-page PDF was rendered page-by-page after the final build. The first
render exposed transparent source crops as black panels; the crops were
flattened onto white and the packet was rebuilt. The final render has readable
source evidence, no clipping or overlapping formulas, and no LaTeX overfull,
underfull, undefined-reference, or undefined-citation warnings.
