# Verification report

## Source check

- Cached source: `data/parsed/arxiv_sources/1003.0108/source.tex`.
- Lines 1768--1784 define the printed property `(P')` and leave its validity
  in the abstract setup for future work.
- The displayed wording is copied faithfully into the packet.

## Mathematical checks

1. `R=S=C` with trivial index satisfies (A1)--(A4).
2. The factorizations `0=0/1`, `1=(1/sqrt(2))/(1/sqrt(2))`, and
   `C=0/1` are normalized and coprime.
3. `G^*G0=1/sqrt(2)` is invertible, so the finite branch of the metric
   definition applies.
4. `tilde(G0)G=-1/sqrt(2)`, hence the metric is exactly `1/sqrt(2)`.
5. `H(0,0)` has operator norm one, hence the nominal margin is exactly one.
6. `H(1,0)` has entries in `C`, hence the zero controller stabilizes `P=1`.
7. With threshold `m=1/2`, both hypotheses of the printed implication hold
   and the conclusion fails strictly.

## Interpretation check

The counterexample also belongs to the rational setting. It therefore flags a
quantifier/formulation mismatch with the source's statement that rational
plants satisfy `(P')`. The packet explicitly limits its conclusion to the
literal implication and does not claim a negative answer to a corrected
whole-ball or metric-minimality theorem.

## Packet QA

- `main.tex` compiles without errors or unresolved references.
- The final PDF was text-extracted and visually inspected page by page.
