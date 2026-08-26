# Sharp covariance-only Talagrand deficit bound

- status: `full_likely_valid`
- run: `fa_banach_001`
- agent: `agent_lane_02`
- model: `GPT5.6`
- source: Neal Bez, Shohei Nakamura, and Hiroshi Tsuji, *Stability of hypercontractivity, the logarithmic Sobolev inequality, and Talagrand's cost inequality*, arXiv:2201.12478v3
- source target: Section 1.4, “A few open problems,” pages 10--11

## Full result

Let `gamma` be standard Gaussian measure on `R^n`, let `mu` be an absolutely
continuous probability measure with finite second moment, and write
`Sigma = Cov(mu)`.  If `0 < Sigma <= I`, then

```text
(1/2) W_2(gamma,mu)^2 - H(mu|gamma)
  <= (1/2) log det(Sigma) - tr(sqrt(Sigma)) + n.
```

Equality holds exactly for translates of the Gaussian `N(0,Sigma)`.

Consequently, if `0 < beta < 1` and `Cov(mu) <= beta I`, then

```text
(1/2) W_2(gamma,mu)^2 - H(mu|gamma)
  <= n (1 + (1/2) log(beta) - sqrt(beta)).
```

This is precisely the sharp covariance-only extension conjectured in the
source.  Equality in the scalar bound holds exactly for translates of
`N(0,beta I)`.

## Proof mechanism

For the Brenier map `T` carrying `gamma` to `mu`, put `A = grad(T)` and, in
the smooth case, `M = E[A]`.  Change of variables and Gaussian integration by
parts give

```text
deficit = E[log det(A)] - tr(M) + n.
```

Concavity of `log det` replaces `A` by its mean.  The block covariance matrix
of `(T(X),X)` gives `M^2 <= Sigma`, hence `M <= sqrt(Sigma)`.  Finally,
`log det(B) - tr(B) + n` is increasing in Loewner order on `0 < B <= I`.

## Novelty check

The run indexes were searched by arXiv id, title, authors, and the core
Talagrand/covariance phrases.  A bounded primary-source web search through
2026-08-09 checked the current source record, Mikulincer's covariance-deficit
paper (arXiv:1906.05904), dimensional Talagrand refinements
(arXiv:1507.01086), and later exact-phrase/close-variant searches.  No paper
explicitly resolving this source problem or stating the anisotropic theorem
above was found.  This supports candidate novelty only, not an exhaustive
literature claim.

## Files

- `main.tex`: expert-facing theorem and proof.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: arXiv:2201.12478v3.
- `figures/open_problem_crop.png`: full-width stitched source evidence.
- `verification.md`: independent proof audit.
- `code/verify_gaussian_formula.py`: closed-form and monotonicity checks.
- `code/make_open_problem_crop.py`: reproducible source crop.
