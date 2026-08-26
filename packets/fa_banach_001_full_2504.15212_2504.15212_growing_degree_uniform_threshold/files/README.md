# Full solution packet: growing-degree tree threshold

## Status

`candidate full solution; likely valid; human review requested`

This packet upgrades the earlier moderate-growth partial result to the full
range (3\leq\Delta\leq N-1). It gives a constant-factor answer to
Problem 1.6 of:

- Dylan J. Altschuler, Pandelis Dodos, Konstantin Tikhomirov, and
  Konstantinos Tyros, *A universal threshold for geometric embeddings of
  trees*, Combinatorica 46 (2026), article 20; arXiv:2504.15212v2.

## Claimed result

Define

\[
q(N,\Delta)=
\frac{\log N}{\log\!\left(2+\frac{\log N}{\log(\Delta-1)}\right)}.
\]

There is a universal constant (A<\infty) such that, for all sufficiently
large (N), uniformly over (3\leq\Delta\leq N-1):

1. every (N)-vertex tree of maximum degree at most \(\Delta\) geometrically
   embeds into every normed space of dimension at least \(Aq(N,\Delta)\);
2. the breadth-first truncated complete rooted degree-\(\Delta\) tree on
   \(N\) vertices does not embed below dimension \(q(N,\Delta)/4\).

At full complete-tree cardinalities the lower-bound witness is the full
complete tree. Thus the explicit threshold function is (m(N,\Delta)=q(N,\Delta))
up to universal factors.

## New mechanism

The source proof's only nonuniform step was its short-path probability
\(\exp(-m^{\kappa/2})\). The packet replaces this with a uniform
\(Ce^{-cm}\) bound:

- condition on all but two uniform edge vectors;
- apply the Brascamp--Lieb--Luttinger/Riesz rearrangement inequality to the
  two unit balls and the translated enlarged target ball;
- reduce to two independent points in a Euclidean ball;
- use a radial estimate and a spherical-cap estimate.

This pays for sparse \(\Delta^{O(1)}\) dependency neighborhoods. In the
dense regime, the tree height is bounded and (q\asymp\log N), so it also
pays for the source's (N^2) dependency bound. The remaining path ranges
and the Gaussian completion are those of the source paper.

## Packet contents

- `main.tex`: full theorem and proof.
- `solution_packet.pdf`: compiled seven-page review packet.
- `source_paper.pdf`: local source paper.
- `figures/open_problem_crop.png`: readable source crop of Problem 1.6.
- `history/partial_packet_2026-08-09/`: preserved earlier moderate-growth
  partial packet.
- `tmp/`: LaTeX and rendered-page verification artifacts.

## Verification performed

- Checked the new rearrangement lemma for arbitrary translations and all
  path lengths (k\geq2).
- Audited all four local-lemma ranges: short/sparse, short/dense,
  long/sparse, and long/dense.
- Checked uniformity of the source's Gaussian estimates on
  \(c\log N/\log\log N\leq m\leq C\log N\).
- Compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Rendered every final PDF page with Poppler and visually inspected all pages;
  no clipping, overlap, missing glyphs, or unresolved references remain.
- No numerical experiment is used as proof.

## Novelty search

The bounded search on 9 August 2026 used arXiv:2504.15212, the published
Combinatorica page, the exact paper title, the exact Problem 1.6 phrase, the
authors, and keyword combinations involving geometric embeddings, growing
maximum degree, normed spaces, rearrangement, and kissing probability. It
found the source and the classical 1974 rearrangement theorem, but no separate
resolution or occurrence of the displayed threshold. Novelty confidence is
moderate because the source problem is recent.

## Human-review focus

First check the translated-third-set application of rearrangement in Lemma 2.
Then check the four local-lemma comparisons and the claimed uniformity of
Section 4.3 of the source. The constant (A) is intentionally not optimized;
Problem 1.5 remains outside the scope of this packet.
