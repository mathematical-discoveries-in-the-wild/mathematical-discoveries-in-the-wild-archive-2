# Reverse Minkowski main conjecture: literature answer

status: `literature_already_answered`

source_arxiv: `1606.06913`

supporting_arxiv: `1611.05979`

source_problem: Dadush--Regev, Conjecture 3.1 (Main conjecture), PDF page 14

answer: Regev--Stephens-Davidowitz, Theorem 1.2 (Reverse Minkowski
Theorem), PDF page 3

## Identification

The source defines `C_eta(n)` by

```text
eta(L) <= C_eta(n) max_W det(L* cap W)^(-1/dim W)
```

and conjectures `C_eta(n) <= polylog(n)`.  Equivalently, after scaling, if
every sublattice of `L*` has determinant at least one, then `eta(L)` is
polylogarithmic.

Regev--Stephens-Davidowitz prove that if every sublattice of a lattice
`Gamma` has determinant at least one, then

```text
sum_{y in Gamma} exp(-pi t^2 ||y||^2) <= 3/2,
t = 10(log n + 2).
```

Taking `Gamma=L*` says exactly that the source smoothing parameter satisfies
`eta(L) <= 10(log n+2)` in the normalized case.  Their scaling formula gives
the full bound

```text
C_eta(n) <= 10(log n + 2),
```

which is stronger than the requested polylogarithmic estimate.

## Evidence

- `source_paper.pdf`: Dadush--Regev, arXiv:1606.06913, 65 pages.
- `supporting_paper_1611.05979.pdf`: Regev--Stephens-Davidowitz,
  arXiv:1611.05979, 41 pages.
- Source TeX: `main_conjecture.tex`, Conjecture `con:maineta`.
- Supporting TeX: Theorem `thm:RM`; the introduction explicitly calls it a
  proof of Dadush's conjecture and cites the source paper as `DR16`.

This is a known literature answer, not a new proof from this run.  The source
contains other variants and related questions; this packet records the full
answer to its central Main Conjecture only.

