# Verification report

Status: `candidate_full_likely_valid`

## Exact target

- Source: arXiv:1302.6369v2, Example 3.3 and Question 3.5(1), source page 12.
- Question: Is the explicitly constructed space `Y2` hereditarily
  Dunford--Pettis?
- Answer proved here: No. A closed subspace of `Y2` is isomorphic to the
  Pełczyński--Szlenk space `Y1`, which fails the Dunford--Pettis property.

## Proof audit

1. `A_p(x) -> 0` implies `x in c0`, because for `k>p`, filler coordinates
   tending to infinity give `|x_p| <= A_p(x)` and
   `|x_p+x_k| <= A_p(x)`, hence `|x_k| <= 2A_p(x)`.
2. For the tail `P_p x`, `A_p(P_p x)=A_p(x)`.
3. Every sum defining `A_q(P_p x)` with `q<p` is bounded by `2A_p(x)` by
   completing its nonzero indices with far-out coordinates tending to zero.
4. Therefore `A_p(x) <= ||P_p x||_{X_p} <= 2A_p(x)`.
5. The map `Jx=(P_p x)_p` is linear, lands in the `c0`-sum because its
   component norms tend to zero, and satisfies `||x|| <= ||Jx|| <= 2||x||`.
   Its range is closed.
6. The source's Example 3.3 records weakly null sequences in `Y1` and `Y1*`
   with pairing one, so `Y1` lacks the Dunford--Pettis property. Hence `Y2`
   is not hereditarily Dunford--Pettis.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1302.6369_y2_not_hereditarily_dunford_pettis/code/verify_tail_embedding.py
```

The script tests the key two-sided inequality on 28,000 finitely supported
random vector/tail pairs. It is bookkeeping evidence, not a proof.

## Novelty audit

A bounded search on 2026-08-11 used the exact question, the source title,
`Y2 hereditarily Dunford-Pettis`, `c0-sum of the spaces X_n`, and close tail
embedding phrases. The 2015 journal version and the arXiv source still state
the question; no later explicit answer or this embedding was found. Novelty
confidence is moderate because the construction is elementary and may be
unindexed folklore.

## Reviewer focus

Check the filler-coordinate limit in the upper bound for `A_q(P_p x)`, the
well-definedness into the `c0`-sum, and whether an answer has appeared under
different notation after the bounded search.
