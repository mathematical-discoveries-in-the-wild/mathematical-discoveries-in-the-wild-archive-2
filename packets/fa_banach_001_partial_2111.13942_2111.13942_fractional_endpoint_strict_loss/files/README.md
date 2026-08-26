# Fractional endpoint products: strict-loss theorem and a local Hardy subcase

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

Source question: Giovanni E. Comi and Giorgio Stefani, *Leibniz rules and
Gauss--Green formulas in distributional fractional spaces*, arXiv:2111.13942,
Remark 4.6.

## Result

For every `0<beta<alpha<1` and every

```text
f,g in S^{alpha,1}(R^n) intersect L-infinity,
```

the product satisfies

```text
fg in W^{beta,1}(R^n) subset S^{beta,1}(R^n).
```

The packet gives the explicit estimate

```text
||nabla^beta(fg)||_1
 <= mu_(n,beta) n omega_n
    [ ||g||_infinity A_(alpha,beta)(f)
      + ||f||_infinity A_(alpha,beta)(g) ],

A_(alpha,beta)(u)
 = gamma_(n,alpha)/(alpha-beta) ||nabla^alpha u||_1
   + 2/beta ||u||_1.
```

By the source's exact equivalence, the weak nonlocal `beta`-gradient exists in
`L1` and the weak Leibniz formula holds.  This is a full-class result with an
arbitrarily small loss of differentiability.

At the exact order `alpha`, the packet proves the implication on the natural
local Hardy--Sobolev subclass

```text
F^{alpha}_{1,2}(R^n) intersect L-infinity.
```

Sickel's Theorem 1 gives the algebra estimate in `F^{alpha}_{1,2}`, and a
frequency-split multiplier argument embeds that local space into
`S^{alpha,1}`.  This subclass strictly contains the global Hardy--Sobolev
space `(I-Delta)^(-alpha/2)H^1` used in arXiv:2011.03928.

## Important limitation

The exact question whether all of
`S^{alpha,1} intersect L-infinity` is an algebra remains open.  The estimates
available from the hypotheses retain exact `B^{alpha}_{1,infinity}`
regularity, but the strict-loss bound diverges as `beta` tends to `alpha` and
does not restore the missing endpoint Riesz-transform cancellation.

## Files

- `solution_packet.pdf`: review packet with proof and limitations.
- `source_paper.pdf`: arXiv:2111.13942.
- `supporting_paper_sickel_1993.pdf`: W. Sickel, *Pointwise multiplication in
  Triebel--Lizorkin spaces*, Forum Math. 5 (1993), 73--92.
- `figures/open_problem_crop.png`: source Remark 4.6 and the open implication.
- Attempt log:
  `runs/fa_banach_001/attempts/2111.13942_fractional_endpoint_algebra_loss.md`.

Human review should focus on the normalization in the difference-integral
estimate and on the low/high-frequency proof of
`F^{alpha}_{1,2} subset S^{alpha,1}`.
