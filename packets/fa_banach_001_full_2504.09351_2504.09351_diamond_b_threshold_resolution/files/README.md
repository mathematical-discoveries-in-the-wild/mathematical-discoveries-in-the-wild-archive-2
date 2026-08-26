# 2504.09351: a threshold construction under diamond(b)

Status: `full_solution_likely_valid`

Source: Arturo Mart\'inez-Celis and Adam Morawski, *A small Radon-Nikod\'ym compact space from a parametrized diamond*, arXiv:2504.09351.

## Result

Assuming `diamond(b)`, there is a Radon--Nikod\'ym compact space of weight `aleph_1` with a continuous image that is not Radon--Nikod\'ym. Minami's Corollary 4.7(ii) supplies a model of `diamond(b)` in which

```text
c = non(M) = cov(M) = aleph_2.
```

Consequently the answer to Question 1 on page 9 of the source paper is affirmatively consistent with ZFC.

## Idea

The source's `diamond(non(M))` construction guesses one exact Cantor cylinder for every dyadic cell on infinitely many levels. The packet replaces exact strings by integer thresholds. At dyadic level `n`, the guessed integer `m_beta(n)` is used in a tail-shift map

```text
sigma -> t concatenated with shift_{m_beta(n)}(sigma),   t in 2^n.
```

Every cylinder of length at most `m_beta(n)` maps onto the full dyadic interval belonging to `t`. A `diamond(b)` sequence selects an almost-disjoint ladder fan with infinitely many points in every required small-diameter fiber cylinder. The images of the maps at level `n` still have diameter at most `2^{-n}`; this is the feature that preserves the RN proof for the Cantor resolution. The dyadic chaining argument then proves that the interval resolution is not RN.

## Why the first naive threshold idea is not used

A map that sends a small cylinder directly onto all of `[0,1]` at infinitely many unrelated levels would also break the Reznichenko-metric proof that the domain is RN. The packet instead keeps the source construction's shrinking dyadic ranges and uses one fixed shift threshold on each entire dyadic cell.

## Novelty check

The bounded check covered the run's registry, solution, attempt, and proof-gap indexes; exact searches for arXiv:2504.09351, the wording of Question 1, `diamond(b)`, `non(M)`, and small RN compact continuous images; the source's citation neighborhood; and later arXiv/web records available through 2026-08-09. No later paper explicitly resolving Question 1 was found. Minami's 2008 paper was found as the consistency input, not as an answer to the topology question.

## Files

- `main.tex`: full construction and proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2504.09351.
- `supporting_minami_2008.pdf`: primary consistency source.
- `figures/open_problem_crop.png`: source Question 1 and its suggested `diamond(b)` route.
- `code/make_crop.py`: reproducible crop generator.

## Review focus

Check the Borel coding in Lemma 1, especially the single `diamond(b)` coordinate simultaneously (i) fixes the threshold for its own dyadic level and (ii) adds a new good ladder point to every earlier cell. Then check the Reznichenko separation argument for the case of two distinct points over the same `beta`.
