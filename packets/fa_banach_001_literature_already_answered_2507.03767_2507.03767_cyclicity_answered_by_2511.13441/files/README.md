# Literature answer: the missing bidisk cyclicity range

status: `literature_already_answered`

source: Pouriya Torkinejad Ziarati, *Cyclicity in Poletsky-Stessin
Weighted Bergman Spaces*, arXiv:2507.03767.

supporting answer: Rajkamal Nailwal and Aljaz Zalar, *Cyclic polynomials
in Dirichlet-type Spaces of the unit bidisk*, arXiv:2511.13441.

packet: `runs/fa_banach_001/solutions/literature_already_answered/2507.03767_cyclicity_answered_by_2511.13441/`

ledger: `runs/fa_banach_001/ledger/results/2507.03767_cyclicity_answered_by_2511.13441.json`

## Identification

Open Problem 1 on page 18 of arXiv:2507.03767 asks whether

```text
f(z1,z2) = 1 - (z1+z2)/2
```

is cyclic in the sum-weight Poletsky-Stessin space
`D_beta(D^2)` for `3/2 < beta <= 2`.

Nailwal--Zalar explicitly cite this problem. Their Theorem 3.1 proves that
`2-z1-z2` is cyclic in the equivalent sum-weight Dirichlet-type space for
every `alpha <= 2`. Multiplication by the nonzero scalar `1/2` does not
change the generated invariant subspace, and their weights
`(k+l+1)^alpha` are equivalent to the source weights
`(k+l+2)^alpha`. This is therefore a full affirmative answer to the exact
source question.

Their Theorem 1.3 is stronger: for `1 < alpha <= 2`, every irreducible
polynomial without bidisk zeros is cyclic exactly when its zero set on the
distinguished boundary is empty or finite.

## Search evidence

The exact paper title, exact polynomial, `Poletsky-Stessin`, and the missing
parameter range were searched in the local run indexes and on the web. The
later paper was found through a 2026 cyclic-polynomial survey/reference hit
and then verified in arXiv:2511.13441. Its abstract says it solves the
Torkinejad Ziarati problem, its Question 1.2 restates the problem, and its
Theorem 3.1 gives the affirmative answer.

## Files

- `solution_packet.pdf`: compact status note.
- `source_paper.pdf`: arXiv:2507.03767.
- `supporting_paper_2511.13441.pdf`: exact later answer.
- `figures/open_problem_crop.png`: page 18 source question.
- `figures/supporting_answer_crop.png`: Theorem 3.1 in the supporting paper.

## Scope

This packet settles only Open Problem 1 of arXiv:2507.03767 by literature
identification. Open Problem 2, concerning one-dimensional boundary zero
sets on complex ellipsoids, is not addressed here.

