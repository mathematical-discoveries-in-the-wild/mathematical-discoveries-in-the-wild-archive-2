# A uniform threshold for moderately growing tree degree

Source: Dylan J. Altschuler, Pandelis Dodos, Konstantin Tikhomirov, and
Konstantinos Tyros, *A universal threshold for geometric embeddings of
trees*, arXiv:2504.15212v2 (17 April 2026).

Status: **candidate substantial partial result; likely valid, pending human
review.**

## Result

Let `kappa in (0,1)` be the absolute thin-shell exponent in Theorem 2.2 of the
source. Define

```
D = log(Delta-1),
H = log N / D,
q(N,Delta) = log N / log(2+H).
```

For every sequence `N -> infinity`, `3 <= Delta <= N-1`, satisfying

```
log(Delta-1) = o(q(N,Delta)^(kappa/2)),
```

the scale `q(N,Delta)` answers Problem 1.6 up to universal constants:

- every `N`-vertex tree of maximum degree at most `Delta` embeds
  geometrically into every normed space of dimension at least `ceil(64q)`;
- the truncated complete rooted `Delta`-bounded tree on `N` vertices does not
  embed into any normed space of dimension at most `q/2`.

At cardinalities of a full complete rooted tree, the lower-bound witness is
the full complete tree. In particular, the result applies to every fixed
`beta < kappa/2` when `Delta <= exp((log N)^beta)`.

## Mechanism

The source proves the fixed-degree theorem using an asymmetric Lovasz local
lemma. Tracking the degree dependence reveals only one real obstruction:
short paths have probability `exp(-m^(kappa/2))` but dependency neighborhoods
of size polynomial in `Delta`. The displayed growth condition makes the
former dominate the latter. For intermediate paths, the worst dependency
term is

```
(H/log H) log(Delta) ~ log N/log H ~ q,
```

and for paths longer than `H`, `m log H` is of order `log N`. The Gaussian
completion of the source proof is degree-free and remains uniform for
`m` between constant multiples of `log N/loglog N` and `log N`.

The matching obstruction is volumetric: at least `N/2` mutually nonadjacent
vertices give disjoint radius-`1/2` balls inside a ball of radius at most
`H+3/2`, forcing dimension at least `(1-o(1))q`.

## Scope

This is a partial answer to Problem 1.6, not a full solution:

- degrees outside `log(Delta-1)=o(q^(kappa/2))` remain untreated;
- the constants `1/2` and `64` are not optimized;
- Problem 1.5 on the optimal fixed-degree constants remains open;
- the proof imports the source paper's thin-shell, slicing, small-ball, and
  local-lemma estimates.

## Novelty check

A bounded search on 9 August 2026 used the arXiv id, exact title, exact phrase
"Trees of growing maximal degree", and combinations of "geometric
embeddings", "trees", "growing degree", and "normed space". It found the
source but no separate answer to Problem 1.6 or statement of this uniform
range. Novelty confidence is moderate because v2 is recent.

## Files

- `source_paper.pdf`: local copy of arXiv:2504.15212v2.
- `figures/open_problem_crop.png`: Problem 1.6 on source PDF page 3.
- `main.tex`: complete review packet source.
- `solution_packet.pdf`: rendered partial-result packet.
- `tmp/`: build, source-extraction, and rendering intermediates.

## Human review recommendation

Prioritize the uniformity audit in the three local-lemma path regimes and the
claim that every later Gaussian estimate is uniform for
`c log N/loglog N <= m <= C log N`. Also confirm the intended scope of
"complete tree" in Problem 1.6; the packet gives a full complete tree at its
natural cardinalities and a breadth-first truncation for arbitrary `N`.

