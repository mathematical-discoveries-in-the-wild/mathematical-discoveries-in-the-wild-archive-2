# Full solution: arbitrary set weights need no extra hypothesis

status: full_solution_likely_valid

source: Hùng Việt Chu, *On weighted greedy-type bases*, arXiv:2205.06839.

target: Question 2 in Section 6 asks whether every
`omega`-disjoint superdemocratic basis is `omega`-superdemocratic when
`omega` is an arbitrary set weight in Definition 1.2, and, if not, which
extra conditions on `omega` suffice.

packet: `runs/fa_banach_001/solutions/full/2205.06839_arbitrary_weight_disjoint_superdemocracy/`

ledger: `runs/fa_banach_001/ledger/results/2205.06839_arbitrary_weight_disjoint_superdemocracy.json`

## Result

The answer to Question 2 is affirmative for every set weight in Definition
1.2. No structuredness, additivity, monotonicity, or other extra condition on
the weight is needed.

More quantitatively, let `K` be the disjoint-superdemocracy constant and set

```text
M  = sup_n ||e_n||,
M* = sup_n ||e_n*||.
```

If signed constant-coefficient sums are unbounded, the basis is
`omega`-superdemocratic with constant at most

```text
K^2 + K M M*.
```

If those sums are bounded by `D`, superdemocracy is automatic with constant
at most `D M*`.

The argument is slightly stronger than the source question: it never uses
convergence of basis expansions or bounded partial-sum projections. It applies
verbatim to every uniformly bounded biorthogonal system `(e_n,e_n*)` with
`sup ||e_n|| < infinity` and `sup ||e_n*|| < infinity`.

## Main idea

Suppose two possibly overlapping signed sums have norms `a` and `b`, their
weights are ordered in the required direction, and `a` is much larger than
`b`. If all signed sums are bounded, the conclusion is immediate from the
uniform lower bound on every nonempty signed sum.

Otherwise, outside any prescribed finite set one can build a fresh signed
sum whose norm first crosses any target `t`; adding one basis vector changes
the norm by at most `M`, so the crossing norm lies in `(t,t+M]`. Taking
`t=K b` produces a set `C` disjoint from both original supports with

```text
K b < ||1_C|| < a/K.
```

Disjoint superdemocracy first forces `w(C) < w(A)`, while the assumed order
`w(A) <= w(B)` and disjointness of `C,B` force `||1_C|| <= K b`, a
contradiction.

## Verification and novelty check

- The proof checks empty supports and weights equal to infinity explicitly.
- The fresh-support bridge lemma was checked for real and complex signs; it
  uses only the triangle inequality and semi-normalization.
- The cheap run indexes were searched for the arXiv id, title, and the core
  phrases `disjoint superdemocratic` and `superdemocratic`.
- The local arXiv source corpus and bounded web searches were checked using
  the exact Question 2 wording, the paper title plus `Question 2`, and close
  variants involving weights on sets. No exact later solution was found as
  of 2026-08-09. This is a bounded, not exhaustive, novelty check.
- A forward-citation audit used DOI `10.1007/s00574-023-00367-3` in Crossref,
  OpenAlex, and Semantic Scholar. Crossref and OpenAlex returned zero citing
  works. Semantic Scholar returned only arXiv:2207.10136; its local TeX source
  contains the source paper solely as a commented-out bibliography item and
  contains no discussion of Question 2. Thus no active forward citation
  answering the question was found.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source page 14 crop containing Question 2.
- `verification_report.md`: explicit line-by-line verifier report.
- `citation_audit.md`: reproducible forward-citation and novelty audit.

## Human-review recommendation

Review as a candidate full solution. The highest-value check is the bridge
lemma and the two strict weight-order deductions in the unbounded case.
