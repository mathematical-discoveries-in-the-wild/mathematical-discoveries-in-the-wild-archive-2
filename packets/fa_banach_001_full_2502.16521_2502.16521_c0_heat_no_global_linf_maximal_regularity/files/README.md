# 2502.16521: no global L-infinity maximal regularity for the C0 heat operator

- Status: `candidate_full_likely_valid`
- Model: `GPT5.6`
- Source: Sebastian Krol, Mieczyslaw Mastylo, and Jaroslaw Sarnowski,
  *Maximal regularity estimates for the abstract Cauchy problems*,
  arXiv:2502.16521v1
- Target: Remark 3.4(c)
- Answer: no, for every `n>=1` and every `theta in (0,1)`

## Result

Let `calA=-Delta` on `C_0(R^n)` and let `A` be its part in

`X_theta=(C_0(R^n),D(calA))_{theta,infinity}`.

The packet proves that `A` does not have `L^infinity`-maximal regularity on
all of `R_+`. The test functions are sums of nested dilates of one compactly
supported smooth bump. Their `X_theta` norms grow linearly with the number of
scales, while `sup_t ||t A exp(-tA)x||_{X_theta}` stays uniformly bounded and
the semigroup orbit tends to zero at large time. Passing to the closure of
the non-dense domain permits use of the Kalton--Portal characterization.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_question_page.png`: source page containing Remark 3.4(c).
- `verification.md`: proof, source, novelty, and rendering audit.
- `attempts/2502.16521_c0_heat_linf_maximal_regularity/attempts.md`: attack
  and upgrade log.

## Review recommendation

Recommended for expert review as a full negative solution. The main review
points are passage of maximal regularity to the closure of the domain, the
heat scaling in the homogeneous interpolation seminorm, and the large-time
decay in the equivalent thermic norm.
