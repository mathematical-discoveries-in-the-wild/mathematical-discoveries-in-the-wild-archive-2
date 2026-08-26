# Multiplier algebra of the coefficient-weighted Bergman/Dirichlet scale

**Status:** full literature-implied answer at the level of an exact
function-theoretic criterion; not a new result.

**Source:** Eva A. Gallardo-Gutiérrez and Jonathan R. Partington,
*Multiplication by a finite Blaschke product on weighted Bergman spaces:
commutant and reducing subspaces*, arXiv:2105.07760.

## Source question

On source PDF page 3, after defining

`A_alpha = {sum a_n z^n : sum |a_n|^2 (n+1)^alpha < infinity}`,

the paper says that identifying its multiplier algebra `M_alpha` for general
`alpha` is open.

## Literature-implied phase diagram

- If `alpha <= 0`, then `M_alpha = H^infinity`.
- If `0 < alpha <= 1`, then `g` is in `M_alpha` exactly when `g` is bounded
  analytic and
  `|g'(z)|^2 (1-|z|^2)^(1-alpha) dA(z)` is a Carleson measure for `A_alpha`.
- If `alpha > 1`, then `M_alpha = A_alpha`.

This covers every real parameter. The middle criterion is the classical
Kerman--Sawyer multiplier characterization after identifying the source norm
with the standard weighted Dirichlet norm. Taylor (1966), Stegenga (1980),
Kerman--Sawyer (1988), and later summaries all predate the source.

## Contents

- `solution_packet.pdf`: compact status note, parameter translation, and
  self-contained verification.
- `main.tex`: LaTeX source.
- `verification.md`: detailed audit of the three parameter regimes.
- `source_paper.pdf`: arXiv:2105.07760.
- `supporting_sources/jupiter_redett_2006.pdf`: primary paper recording the
  endpoint phase results and their one-variable provenance.
- `supporting_sources/bao_lou_qian_wulan_2015.pdf`: primary paper explicitly
  recording the Kerman--Sawyer criterion.

## Provenance caution

The supporting papers do not present themselves as replies to arXiv:2105.07760;
indeed they predate it. This is therefore stored under
`literature_implied_answers`, not as a new solve or a later explicit answer.

