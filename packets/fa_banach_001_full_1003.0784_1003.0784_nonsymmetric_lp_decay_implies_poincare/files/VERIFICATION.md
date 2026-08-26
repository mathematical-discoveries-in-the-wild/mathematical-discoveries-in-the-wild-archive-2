# Verification report

Verdict: `candidate_full_likely_valid`

## Formal audit

1. **Infinitesimal implication.** The prefactor `K_p=1` is essential: right
   differentiation at `t=0` gives the weighted generator inequality with no
   transient constant. Invariance and the diffusion chain rule convert it to
   the weighted carré-du-champ inequality.
2. **Centering parameter.** The regularizer is odd, continuous, and strictly
   increasing. Hence the integral of `psi_epsilon(g-c)` is continuous and
   decreasing in `c`, with opposite signs at the two ends; a zero exists.
   For bounded core functions it lies between the essential lower and upper
   bounds. The standard truncation/closure argument handles the form domain.
3. **Regularity.** For every fixed positive `epsilon`, the regularizer is
   smooth, with bounded first derivative, so the source's diffusion chain
   rule applies.
4. **Energy bound.** Direct differentiation gives
   `|psi|^(p-2) |psi'|^2 <= 1`. No singular factor remains at zero.
5. **Limit.** `|psi_epsilon(s)|^p <= |s|^2` and converges pointwise to
   `|s|^2`. With bounded `g` and bounded centering parameters, dominated
   convergence is immediate.
6. **Poincaré center.** The limit center need not equal the mean. This is
   harmless because variance is the minimum of `integral |g-a|^2` over
   constants `a`.

The proof uses neither symmetry nor interpolation. It uses exactly the
invariance, diffusion chain rule, and core hypotheses in the source's
nonsymmetric discussion.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1003.0784_nonsymmetric_lp_decay_implies_poincare/code/check_fractional_regularizer.py
```

Result: 1,159,968/1,159,968 scalar cases passed. The script checked positivity
of the derivative, `|psi_epsilon(s)|^p <= |s|^2`, and
`|psi_epsilon(s)|^(p-2)|psi_epsilon'(s)|^2 <= 1` over a logarithmic grid of
`p`, `epsilon`, and `s` values.

These tests guard against exponent/sign mistakes only. The displayed scalar
calculation and semigroup argument are the proof.

## Scope audit

- The result requires `p>2` and prefactor exactly one.
- It applies to invariant diffusion semigroups with the carré-du-champ chain
  rule. It does not claim the same for pure-jump semigroups, where the
  derivation identity fails.
- A finite prefactor `K_p>1` cannot be differentiated into the required
  inequality at time zero and is not covered.
