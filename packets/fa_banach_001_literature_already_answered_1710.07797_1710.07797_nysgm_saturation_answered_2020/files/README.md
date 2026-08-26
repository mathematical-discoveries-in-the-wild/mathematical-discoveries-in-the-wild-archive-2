# Literature answer: NySGM beyond the saturation threshold

Status: `literature_already_answered`

This is an exact later-literature match, not a new proof produced by the run.

## Source question

Junhong Lin and Lorenzo Rosasco, *Optimal Rates for Learning with Nystrom
Stochastic Gradient Methods*, arXiv:1710.07797v1 (2017), Section 4, PDF page
10, observe that their NySGM analysis saturates at the source exponent
`r=1/2` and conjecture that a different subsampling technique should recover
optimal error bounds for `r >= 1/2`.

## Supporting answer

Junhong Lin and Volkan Cevher, *Convergences of Regularized Algorithms and
Stochastic Gradient Methods with Random Projections*, JMLR 21(20):1-44
(2020), explicitly cites the source as Lin and Rosasco (2017a).

The decisive locations are Section 4, PDF pages 12-14:

- Theorem 2 proves optimal projected-SGM rates without an upper restriction
  on the smoothness exponent.
- Corollary 5 supplies approximate-leverage-score (ALS) Nystrom subsampling.
- Corollary 7 applies Theorem 2 to the Nystrom projections and sample sizes of
  Corollaries 4 and 5.
- Remark 5(2) explicitly identifies the 2017 predecessor and its restricted
  smoothness range.

The notations match after setting the 2020 source exponent `s=r+1/2`. The
2020 rate at `a=0` is

```text
n^(-2s/(2s+gamma)) = n^(-(2r+1)/(2r+gamma+1)),
```

which is the source paper's optimal rate. Thus the formerly saturated range
`r>1/2` becomes `s>1` and is included.

## Scope

This answers the saturation/subsampling conjecture in the least-squares
Hilbert/RKHS setting under the assumptions of the 2020 theorem and ALS
corollary. It does not answer the source's other broad future directions,
including simultaneous cross-validation of all parameters, unbounded kernels,
preconditioning, random features, or acceleration.

## Search evidence

The bounded search checked the four run indexes, the exact arXiv id and title,
the phrases `NySGM saturation zeta subsampling` and `Nystrom stochastic
gradient optimal rates`, and the citation trail from arXiv:1710.07797. The
JMLR paper explicitly knows and extends the source result, so this belongs in
`literature_already_answered`, not `literature_implied_answers`.

Files:

- `source_paper.pdf`: arXiv:1710.07797v1.
- `supporting_paper_jmlr_2020_19-083.pdf`: the decisive JMLR paper.
- `main.tex`, `solution_packet.pdf`: compact status note.
