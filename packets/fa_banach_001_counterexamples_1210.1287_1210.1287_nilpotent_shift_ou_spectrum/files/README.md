# 1210.1287 — nilpotent-shift OU spectrum counterexample

Status: `candidate_full_counterexample_human_review_needed`.

Model: `GPT5.6`.

Source: Rostyslav Kozhan, *L1-spectrum of Banach space valued
Ornstein-Uhlenbeck operators*, arXiv:1210.1287.

## Result

The source asks whether its full-left-half-plane `L1` spectrum theorem extends
when `sigma_p(A*)` is empty. The literal extension is false.

Take the nilpotent left-shift semigroup on `E=L2(0,1)` and an injective
Hilbert-Schmidt noise `B e_n=2^-n e_n`. Then `A*` has no eigenvalues and the
invariant Gaussian covariance is trace class with dense range. For `t>=1`, the
OU semigroup is exactly the expectation projection. On the mean-zero subspace
it is nilpotent and its generator has entire resolvent; on constants the
generator is zero. Therefore the full generator spectrum is exactly `{0}`.

## Files

- `main.tex`: complete construction and spectrum proof.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof and scope audit.
- `source_paper.pdf`: target paper.
- `supporting_prior.pdf`: van Neerven–Priola paper containing the earlier
  nilpotent-shift semigroup identity.
- `figures/`: source theorem/question and supporting-example screenshots.

## Scope and prior overlap

The earlier paper records `P(t)=P(s)` after time one for the same nilpotent
drift, but does not state the resulting `L1` generator spectrum. This packet
makes that inference self-contained and supplies explicit nondegenerate noise.
The example has empty `sigma(A)`; the stronger problem with nonempty
`sigma(A)` but empty `sigma_p(A*)` remains open.

A bounded local and external search on 2026-08-13 found no paper stating this
spectral counterexample. Specialist proof, attribution, and scope review remain
appropriate.
