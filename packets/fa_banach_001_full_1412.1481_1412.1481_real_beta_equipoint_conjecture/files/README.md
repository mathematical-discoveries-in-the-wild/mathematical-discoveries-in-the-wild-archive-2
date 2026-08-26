# Full Solution Packet: Real Beta Equipoint Conjecture

Run: `fa_banach_001`

Result type: `full`

Current verdict: `likely valid` (candidate full solution, pending human review)

## Source Problem

- J. William Helton, Igor Klep, Scott McCullough, and Markus Schweighofer,
  *Dilations, Linear Matrix Inequalities, the Matrix Cube Problem and Beta
  Distributions*, arXiv:1412.1481; Memoirs of the AMS 257 (2019), no. 1232.
- Exact location: Conjecture 1.13, printed/PDF page 13 of
  `source_paper.pdf`; parsed source lines 1758--1766.
- Evidence crop: `figures/open_problem_crop.png`.

For real `s >= t > 0`, the source conjectures that the beta equipoint
`e_{s,t}` satisfies

```text
e_{s,t} <= s/(s+t).
```

Equivalently, if `B_{a,b}` denotes a beta random variable, the conjecture is

```text
P(B_{s,t+1} >= s/(s+t))
    <= P(B_{s+1,t} <= s/(s+t)).
```

## Candidate Result

The conjecture is true for every pair of real parameters `s >= t > 0`.
Equality holds exactly when `s=t`; the inequality is strict when `s>t`.

## Proof Intuition

Put `q=s/t`. After the odds substitution `z=x/(1-x)`, followed by scaling
the lower tail and inverting the upper tail, the difference between the two
probabilities has the sign of

```text
integral_0^1 (P(u)-Q(u)) du,

P(u) = u^s/(1+qu)^(s+t+1),
Q(u) = u^t/(q+u)^(s+t+1).
```

The ratio `P/Q` starts below one, crosses one exactly once, and remains above
one until it returns to one at the endpoint. The key extra identity is

```text
integral_0^1 ((1-u)/u) (P(u)-Q(u)) du = 0.
```

It is simply the equality of the lower and upper first absolute deviations
about the mean `q` of a beta-prime distribution. Since `(1-u)/u` is strictly
decreasing, it gives greater weight to the negative part of `P-Q` than to its
positive part. A weighted integral of zero therefore forces the unweighted
integral to be strictly positive.

## Verification Summary

- The beta-function normalizations and both changes of variables were checked
  independently.
- The logarithmic derivative of `P/Q` reduces to a quadratic with reciprocal
  roots; exactly one root lies in `(0,1)`.
- The weighted cancellation follows from
  `B(s+1,t)/B(s,t+1)=s/t`.
- `code/verify_equipoint.py` checks direct incomplete-beta values, the
  transformed integral, weighted cancellation, and the one-crossing pattern.
  A fixed-seed scan of 250,000 parameter pairs over six orders of magnitude
  found no contradiction (roundoff-scale values occur near `s=t`).

## Scope

- This completely resolves Conjecture 1.13.
- It does not address the distinct monotonicity Conjecture 1.16 on the next
  page of the source.
- The result is mathematical progress produced in this run, not a literature
  identification.

## Novelty Check

The cheap run indexes were searched for arXiv:1412.1481, `equipoint`,
`Conjecture 1.13`, `Simmons theorem`, and the incomplete-beta inequality. A
bounded external search used the exact conjecture label and wording, the
source title/authors, the equipoint notation, and close incomplete-beta
phrases. It found the source arXiv/AMS/author versions and adjacent literature
on normalized incomplete beta functions, but no later proof, counterexample,
or claim resolving Conjecture 1.13.

## Human Review Recommendation

Send to human review as a candidate full solution. The most important checks
are the common positive normalization after the two tail substitutions and
the direction of the final decreasing-weight argument.

