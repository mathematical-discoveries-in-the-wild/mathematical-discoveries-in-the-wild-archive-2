# Tight OGF decomposition into mutually unbiased tight subframes

Status: `candidate_partial_result_likely_valid`.

Source: John I. Haas IV and Peter G. Casazza, *On the structures of
Grassmannian frames*, arXiv:1703.01787, p. 3, Section II.B, Question 2.

## Result

In the orthoplex regime, equality between the ordinary and tight
Grassmannian constants has an exact structural certificate. Every tight OGF
canonically decomposes into mutually unbiased unit-norm tight subframes. The
blocks are the connected components of the graph whose strict edges satisfy

```text
|<phi_i,phi_j>| < 1/sqrt(m).
```

If `d=m^2` over `C` and `d=m(m+1)/2` over `R`, then a canonical decomposition
of an `n`-vector tight OGF has `r` blocks satisfying

```text
block size >= m,    r >= n-d+1,    n-r <= d-1.
```

Consequently,

```text
n <= m(m+1)       over C,
n <= m(m+2)/2     over R.
```

At maximal complex cardinality the frame must be a union of `m+1` mutually
unbiased orthonormal bases. At the real integral endpoint it is a union of
`m/2+1` such bases.

The converse is also proved: any union of pairwise mutually unbiased
unit-norm tight subframes, each having internal coherence at most
`1/sqrt(m)`, is a tight OGF whenever `n>d`.

## Scope

This is a strong structural partial answer, not a parameter-only existence
table. The remaining existence problem contains the complete-MUB problem at
maximal cardinality. A companion upgrade report records eight focused routes
and why they do not remove that obstruction.

Human-review recommendation: review as a likely-valid substantial partial
answer, with particular attention to the weighted-Laplacian rank step and the
bounded novelty assessment.

Files:

- `solution_packet.pdf`: proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:1703.01787.
- `figures/open_problem_crop.png`: full-width source crop containing Question 2.
- `supporting_paper_1605.02012.pdf`: traceless zero-sum embedding source.
- `supporting_paper_1509.05333.pdf`: mutually unbiased tight-frame constructions.
- `verification_report.md`: independent checklist of every proof step.

Ledger: `runs/fa_banach_001/ledger/results/1703.01787_tight_ogf_mutually_unbiased_decomposition.json`.
