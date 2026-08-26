# The isotropic mean-norm question now has a sharp literature answer

Status: **literature_implied_answer (full answer to the extracted mean-norm question)**

Original source: Giorgos Chasapis, Apostolos Giannopoulos, and Nikos
Skarmogiannis, *Norms of weighted sums of log-concave random vectors*,
arXiv:1906.03719 (2019), PDF page 3.

Supporting source: Pierre Bizeul, *Optimal MM* bounds for convex bodies*,
arXiv:2607.29458 (2026), Theorem 1.4 on PDF page 3.

## Identification

The 2019 paper asks whether a volume-one isotropic centrally symmetric convex
body `K` satisfies

```text
L_K sqrt(n) M(K) <= c (log n)^b
```

for absolute constants. Bizeul's Theorem 1.4 states that every convex body
`K_0` in probabilistic isotropic position satisfies

```text
M(K_0) <= C sqrt(log(n)/n).
```

The conventions match by a one-line rescaling. In the source convention the
uniform distribution on `K` has covariance `L_K^2 Id`. Thus
`K_0=L_K^{-1}K` is probabilistically isotropic, and gauge homogeneity gives
`M(K_0)=L_K M(K)`. Therefore

```text
L_K sqrt(n) M(K) <= C sqrt(log n).
```

This answers the extracted question affirmatively with `b=1/2`. The supporting
paper also notes that the estimate is sharp, using the cube.

The supporting authors do not identify arXiv:1906.03719 as the question being
answered. The relation is an agent-identified scaling implication, so the
packet is classified as `literature_implied_answer`, not
`literature_already_answered` and not a new run proof.

## Files

- `main.tex`, `solution_packet.pdf`: compact identification note.
- `source_paper.pdf`: arXiv:1906.03719.
- `supporting_paper_2607.29458.pdf`: decisive supporting theorem.
- `tmp/`: LaTeX and visual-QA intermediates.

## Scope

This packet answers only the explicit isotropic mean-norm estimate on source
PDF page 3. It does not claim that every broader problem discussed in the 2019
paper is resolved.

Ledger:
`runs/fa_banach_001/ledger/results/1906.03719_isotropic_mean_norm_answered_by_2607.29458.json`.
