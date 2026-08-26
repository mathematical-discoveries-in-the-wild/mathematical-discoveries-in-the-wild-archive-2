# Verification Report

Candidate: arXiv:2401.08483, Section 4 question on removing the norm
restrictions from Theorem 4.

## Claim checked

There are finite-rank operators `P_n,Q_n` on `ell_2`, both converging strongly
to the identity, such that for `T=I` the truncations `T_n=Q_n T P_n` converge
strongly to `T`, but `a_k(T_n)` fails to converge to `a_k(T)` for every fixed
positive integer `k`.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | Section 4 on arXiv PDF pages 13--14 asks whether Theorem 4 survives removal of `||P_n|| ||Q_n|| <= 1`. The 2025 journal version repeats the question in Section 4. |
| Spaces and topology | valid | `ell_2` is a dual Banach space. Strong operator convergence implies the weak-star operator convergence required in Theorem 4. |
| Finite-rank truncations | valid | `P_n=R_(2n)` and `Q_n=R_n+2(R_(2n)-R_n)` both have range in the first `2n` coordinates. |
| Strong convergence of `P_n` | valid | The error is the `ell_2` tail after coordinate `2n`. |
| Strong convergence of `Q_n` | valid | `||(Q_n-I)x||^2=sum_(j>n)|x_j|^2`, hence tends to zero for every `x`. |
| Factorization | valid | `Q_n R_(2n)=Q_n`, so `Q_n T P_n=Q_n` for `T=I`. |
| Norm hypothesis removed | valid | `||P_n||=1`, `||Q_n||=2`, hence the product equals `2`, not at most `1`. |
| Value `a_k(I)=1` | valid | The zero operator gives the upper bound. Every rank `<k` operator has a nonzero kernel vector, giving the lower bound. |
| Value `a_k(Q_n)=2` | valid | For `n>=k`, any rank `<k` operator has a unit kernel vector in the `n`-dimensional doubled block, where `Q_n=2I`; `||Q_n||=2` gives equality. |
| Failure of conclusion | valid | For each fixed `k`, `a_k(T_n)=2` for all `n>=k`, while `a_k(T)=1`. |

## Counterexample and edge-case checks

- The construction works simultaneously for all fixed approximation-number
  indices, not only for `k=1`.
- Both factors themselves converge strongly to the identity, matching the
  motivation in the source's concluding paragraph.
- Both factors and every `T_n` have finite rank, so the example remains a
  truncation example in the usual finite-section sense.
- The operators are uniformly bounded; the failure is not caused by an
  unbounded sequence hidden behind weak convergence.

## External dependencies

None beyond the source's definition of approximation numbers and its exact
question. All functional-analytic steps are proved directly in the packet.

## Novelty check

The bounded search on 9 August 2026 checked:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv` for the arXiv id, title, approximation numbers,
  truncations, and norm restrictions;
- exact-title and exact-phrase web searches;
- arXiv:2401.08483v2 and the official 2025 journal PDF;
- close searches for approximation-number truncation counterexamples without
  contractivity.

No later exact answer or matching counterexample was found. The search was
bounded, so priority/novelty remains subject to specialist review.

## Gaps

No mathematical gap found. The only material review question is semantic:
whether the source intended additional unstated restrictions beyond those in
Theorem 4. The packet neutralizes the most natural such restrictions by making
both factors finite rank and strongly convergent to the identity.

## Confidence

Score: 98/100 for mathematical correctness; moderate confidence on novelty.

## Human review recommendation

Send to an operator-ideals or approximation-numbers reviewer. Verify the
source interpretation first; the construction and kernel calculation should
then require only a short check.
