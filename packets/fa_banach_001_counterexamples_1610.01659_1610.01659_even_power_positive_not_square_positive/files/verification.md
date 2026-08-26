# Verification record

## Mathematical audit

- Base form: weighted AM-GM proves
  `a^(2d)-a^(2d-2)b^2+b^(2d)` is positive definite for every `d>=2`.
- Negative square: its generating moment satisfies
  `m_2=-1/binom(2d,2)<0`.
- Stage indexing: in the term containing `k<2d` copies of the new monomial,
  the largest moment index is `2d*N+k<2d*(N+1)`. The new top moment therefore
  occurs only in the pure new-coordinate term.
- Uniformity: positive definiteness of the old form gives a positive minimum
  on the finite-dimensional unit sphere; every mixed form is bounded there.
- Absorption: weighted Young inequalities split each mixed monomial between a
  prescribed small fraction of the old coercive term and a finite multiple of
  the pure new-coordinate term.
- Globalization: every polynomial has finite degree and is covered by one
  stage of the construction.
- Discontinuity: the chosen top moments are unbounded, whereas continuity for
  the coefficient `ell^1` norm would bound every `L(x^j)`.

`code/verify_structure.py` checks the base coefficient and degree identities
for `2<=d<=10` and stages `1<=N<=30`.

## Bounded novelty search

Checked through 2026-08-11:

- the run registry, solution, attempt, and proof-gap indexes;
- exact Question 2.9 wording, arXiv id, title, and authors;
- later infinite-dimensional moment-problem literature returned by searches;
- combinations of `positive on 2d-th powers`, `square positive`, `Hankel
  form`, `Hankel tensor not strong`, and `continuity`.

Related finite-dimensional PSD Hankel tensors that are not strong were found,
including the well-known quartic base vector. No all-degree completion, global
functional on `R[x]`, or explicit answer to the source question was found.

## Human review focus

1. Check the index bound in the binomial expansion.
2. Check the uniform Young-inequality absorption.
3. Confirm that the scope is read as a full negative answer to deleting
   continuity, not a classification of all possible weakenings.

Verdict: `candidate_counterexample`, likely valid.
