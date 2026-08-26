# The Lorentz limiting ODE has finite support exactly off the diagonal

**Status:** candidate substantial partial result, likely valid; human review
needed.

**Source:** Zakhar Kabluchko, Joscha Prochno, and Mathias Sonnleitner,
*A probabilistic approach to Lorentz balls*, arXiv:2303.04728, Conjecture 1
on source PDF page 7.

The packet proves the explicit support-radius clause of Conjecture 1 for every
solution satisfying the conjecture's ODE and boundary conditions:

`r_{p,q}=infinity` if and only if `p=q`.

When `p=q`, the ODE is integrated exactly and gives the normalized
`p`-Gaussian.  When `p<q`, writing `u=1-G`, `w=G'`, and
`beta=1-p/q` yields the exact inverse-variable identity

`w(x)=integral_0^{u(x)} x(v)^(p-1) v^(-beta) dv`.

If the endpoint were infinite, this identity would force `u^beta` to become
negative in finite time.  Hence the endpoint is finite.  It also gives the
sharp edge law

`1-G(x) ~ [((q-p)/p) r^(p-1)(r-x)]^(q/(q-p))`

and the corresponding density exponent `p/(q-p)`.  The special case `p=1`
recovers the source's known endpoint `r=1/(q-1)` and initial slope `G'(0)=q`
exactly.

## Scope

This is not a proof of the full empirical-measure conjecture.  It also does
not establish existence or uniqueness of the critical shooting solution.
Rather, it proves the entire support dichotomy and endpoint asymptotics for
every admissible boundary solution.  Eight focused attempts audited shooting,
variational, and large-deviation upgrade routes; the missing compactness and
Gibbs-conditioning steps remain substantial.

## Contents

- `solution_packet.pdf`: expert-facing theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Conjecture 1 on source PDF page 7.
- `tmp/`: LaTeX and visual-QA intermediates.

## Verification and novelty

The proof was checked against the exactly solvable `p=q` and `p=1` cases, and
a two-sided finite-endpoint bound independently recovers the asserted leading
constant.  Cheap run indexes and bounded exact-title, quoted-conjecture,
support-radius, and general-`p` searches through 12 August 2026 found no later
resolution of this clause.

## Human-review recommendation

Verify first the orientation of the inverse variable `x(v)` in the integral
identity and then the integration sign in the contradiction for an infinite
endpoint.  These are the two short steps carrying the support dichotomy.  The
edge asymptotic then follows directly from the same identity.
