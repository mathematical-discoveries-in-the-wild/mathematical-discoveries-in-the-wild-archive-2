# Cross-polytope counterexample to the conjectured random-section radius

Status: `literature_implied_answer_full_counterexample_needs_human_review`

Source: arXiv:1601.02254v2, Giannopoulos--Hioni--Tsolomitis,
*Geometry of random sections of isotropic convex bodies*, Question 1.1.

## Result

The conjectured universal estimate

```text
R(K cap F) <= C n L_K / sqrt(k)
```

is false, even for origin-symmetric isotropic bodies and even if “random” is
weakened to “there exists”.

Let `K_n = a_n B_1^n`, where `a_n = (n!/2^n)^(1/n)`, so that `|K_n|=1`.
The cross-polytope is isotropic and

```text
L_(K_n)^2 = 2 a_n^2 / ((n+1)(n+2)).
```

The sharp Gelfand-width lower bound for `ell_1^n -> ell_2^n` implies that
every codimension-`k` subspace `F` satisfies

```text
R(K_n cap F) >= c a_n min{1, sqrt((1 + log(n/k))/k)}.
```

For `k=floor(sqrt(n))`, the ratio of this lower bound to
`n L_(K_n)/sqrt(k)` grows like `sqrt(log n)`. Thus every such subspace
violates the proposed estimate for sufficiently large `n`.

## Supporting input

The Gelfand-width estimate is Theorem 1.1 of Foucart--Pajor--Rauhut--Ullrich,
arXiv:1002.0672v2 (Journal of Complexity 26 (2010), 629--640). Their theorem
states, for `p=1`, `q=2`, that

```text
d^k(B_1^n, ell_2^n) ~= min{1, sqrt((1+log(n/k))/k)}.
```

Since the width is the infimum over all codimension-`k` kernels, its lower
bound applies to every `F`.

## Novelty and duplicate checks

The four cheap run indexes were searched for arXiv:1601.02254 and the core
phrases `random sections`, `isotropic cross-polytope`, `Gelfand width`, and
`n L_K / sqrt(k)`. No existing packet, attempt, or proof gap for this question
was found. Bounded arXiv/web searches found the source paper, the width theorem,
and later general papers on random sections of ellipsoids, but no explicit
resolution of Question 1.1 by this counterexample.

The width theorem itself predates the question. The promoted result is the
short application combining that theorem with the exact volume and isotropic
normalization of the cross-polytope. Human review should confirm that the
source's intended probability convention does not impose any hidden change of
quantifiers; the counterexample is stronger because it fails for every `F`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv source paper.
- `supporting_paper_1002.0672.pdf`: official arXiv supporting width paper.
- `figures/open_question_crop.png`: actual crop of Question 1.1.
- `verification_report.md`: compilation, formula, source, and visual checks.
