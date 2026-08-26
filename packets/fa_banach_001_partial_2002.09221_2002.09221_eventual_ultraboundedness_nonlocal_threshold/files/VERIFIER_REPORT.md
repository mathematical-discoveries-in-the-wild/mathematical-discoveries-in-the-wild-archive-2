# Verifier report

## Claim checked

For the normalized torus `T^d`, the conservative symmetric Markov semigroup

```text
P_t = (I-Delta)^(-t)
```

has a bounded transition kernel if and only if `t>d/2`.

## Independent proof checks

- The multiplier identity
  `(1+lambda)^(-t) = Gamma(t)^(-1) integral_0^infinity
  s^(t-1) exp(-s) exp(-s lambda) ds` proves positivity, preservation of
  constants, self-adjointness, and the semigroup law.
- For `t>d/2`, the Fourier coefficients are summable over `Z^d`; the Fourier
  series therefore converges absolutely and uniformly to a bounded kernel.
- For `t<=d/2`, retaining the zero translate in the periodized Gaussian heat
  kernel and integrating over `|z|^2 <= s <= 1` gives
  `K_t(z) >= c integral_[|z|^2,1] s^(t-1-d/2) ds`.  This tends to infinity as
  `z` tends to zero, with a power singularity below the threshold and a
  logarithmic singularity at the threshold.
- For any symmetric Markov density, the semigroup identity and
  Cauchy--Schwarz give
  `r_T(x,y)^2 <= r_T(x,x) r_T(y,y)`.  Therefore a uniform diagonal bound at
  time `T` is a full kernel bound at that time and persists for all later
  times.

## Scope check

The construction is deliberately not claimed to be a Langevin diffusion.
Its generator is `-log(I-Delta)`, which is nonlocal.  It settles the broad
reversible-Markov implication negatively and isolates locality as the
remaining issue, but it does not construct a smooth potential `V` on
Euclidean space with the requested behavior.

## Literature/novelty check

Exact run-index searches found no prior packet on arXiv:2002.09221 or this
threshold question.  Bounded external searches found established general
theory of eventual ultracontractivity under subordination (Bendikov--Coulhon--
Saloff-Coste; Gentil--Maheux).  The torus specialization and proof are included
for completeness, but novelty is not asserted.  The scoped contribution is
the exact identification of this mechanism with the source's diagonal
question and the proof that the unresolved content is specifically local.

Recommendation: verify the source-scope boundary and the endpoint
`t=d/2`; do not promote this packet to a full answer without a local
second-order diffusion construction or a proof that eventual
ultraboundedness implies immediate ultraboundedness in that class.
