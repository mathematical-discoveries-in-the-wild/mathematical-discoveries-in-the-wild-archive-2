# Fractional Trudinger integrability removes part of the subexponential barrier

Status: `candidate_partial_likely_valid`.

Source: Tian Liang and Yuan Zhou, *Orlicz-Besov extension and Ahlfors
`n`-regular domains*, arXiv:1901.06186, Remark 1.3 on source PDF page 3.

## Result

Let `n>=2`, and let `phi` satisfy the source's nontriviality condition.  Assume
that for some `p>n` and `a>0`,

```text
phi(t) >= a t^p  for every t>=0,
log(1+phi(t)) = o(t^(p')),
p' = p/(p-1).
```

Then every homogeneous `B^phi` extension domain in `R^n` is Ahlfors
`n`-regular.

The source required `log phi(t)=o(t)`.  Since `p'>1`, the new condition permits
genuinely exponential and mildly superexponential growth.  In particular it
covers:

- `phi(t)=t^p exp(c t^alpha)` for `p>n` and `1<=alpha<p/(p-1)`;
- `phi_gamma(t)=exp(t^gamma)-sum_{j=0}^{floor(n/gamma)}
  t^(gamma*j)/j!` for `1<=gamma<1+1/n`.

Thus it reaches the first exponential families explicitly excluded by the
source theorem.

## Proof mechanism

The lower power bound makes the Orlicz--Besov seminorm dominate the critical
fractional seminorm `W^{n/p,p}`.  A localized fractional Moser--Trudinger
inequality then improves the source's John--Nirenberg estimate from
`exp(|u-c|)` to `exp(|u-c|^(p'))`.

For the source's nested cutoff functions this changes the dyadic estimate to

```text
(b_j-b_(j+1))^n
  <= 2^(-j) rho phi(C [log(C 2^j/rho)]^(1/p')),
rho = |B(x,r) intersect Omega|/r^n.
```

The new growth condition turns the last factor into at most
`C(2^j/rho)^(1/2)`.  The increments therefore sum to
`b_1 <= C rho^(1/(2n))`, and the source's recentering argument forces a
uniform positive lower bound on `rho`.

## Scope

This is a substantial partial result, not a proof of the unrestricted
conjecture.  It does not cover growth at or above `exp(t^(p'))`, nor Young
functions without a global lower power of order greater than `n`.  Eight
upgrade attempts and the precise obstruction are recorded in the companion
attempt note.

Human review should focus on the localized Moser--Trudinger lemma, the passage
from the cutoff norm estimate to the dyadic recurrence, and the final
large-radius reduction.

## Files

- `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: arXiv:1901.06186.
- `supporting_parini_ruf_1607.07681.pdf`: fractional Moser--Trudinger source.
- `figures/open_problem_crop.png`: source Remark 1.3.
- `figures/fractional_trudinger_crop.png`: Parini--Ruf Proposition 3.1.
- `code/verify_exponents.py`: exact/sample parameter and recurrence checks.
- `novelty.md`, `verification.md`: bounded search and audit reports.

