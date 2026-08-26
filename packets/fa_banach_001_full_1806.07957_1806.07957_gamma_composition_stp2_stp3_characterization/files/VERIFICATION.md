# Verifier report

Verdict: likely valid full resolution; suitable for human review.

Analytic checks:

- The source statement was verified in Remark 4.4 on PDF page 15.
- With `q_u(p)=F_u^{-1}(p)` and `x_u(v)=q_u(1-v)`, direct implicit
  differentiation gives
  `partial_v C_c(u,v) = Gamma(u)/Gamma(u+c) * x_u(v)^c`.
- Saunders and Moran's Theorem 1 applies to every positive gamma shape and
  states strictly that `q_u(alpha)/q_u(beta)` decreases with `u` whenever
  `0<beta<alpha<1`.
- For `u_1>u_2` and `v_1>v_2`, applying that theorem with
  `beta=1-v_1` and `alpha=1-v_2` gives
  `x_{u_1}(v_1)/x_{u_2}(v_1) > x_{u_1}(v_2)/x_{u_2}(v_2)`. Thus the
  derivative kernel is STP2 in the same decreasing-order convention as the
  source.
- The elementary integral-ratio identity in the packet proves that integrating
  the derivative from zero preserves strict TP2.
- The boundary qualification was checked directly: `C_c(u,0)=0`, so a minor
  using `v=0` vanishes.

Certified numerical check:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1806.07957_gamma_composition_stp2_stp3_characterization/code/interval_certificate.py
```

The script uses the positive series
`P(s,x)=x^s exp(-x)/Gamma(s+1) sum_{n>=0} x^n/(s+1)_n`, proves a geometric
tail bound, brackets every inverse gamma quantile by monotonicity, encloses all
nine kernel entries with outward-rounded interval arithmetic, and returns

```text
determinant interval
-0.000121058521276380747056567349942251156033
-0.0001210585212763807470565673499421244358716
```

The upper endpoint is strictly negative.

Artifact checks:

- `source_paper.pdf` is the official arXiv PDF.
- `supporting_paper_saunders_moran_1978.pdf` is a valid nine-page PDF extracted
  from the official ANU repository copy of Saunders's thesis; it contains the
  complete paper as Appendix B.
- The packet compiled without LaTeX warnings.
- Every rendered page and the source-statement crop were visually inspected.

The strongest remaining human-review task is a line-by-line check of the
strict ratio-to-determinant orientation. The interval computation is
independent of the positive proof and directly disproves STP3 in general.
