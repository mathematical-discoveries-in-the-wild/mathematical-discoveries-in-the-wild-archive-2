# Centered fixed-trace GUE large deviations

Candidate new full solution to the conjecture on PDF page 35 of
arXiv:2508.13698 (Chaintron--Lacker).

## Result

For `M_n` uniform on `tr(M_n^2)=n^2`, the centered empirical eigenvalue law
of `M_n/sqrt(n)` obeys an LDP in `(P_1(R),W_1)` with speed `n^2` and the exact
rate conjectured by the source:

```text
J(mu) = I_log(mu) + (1-m_2(mu))/2
```

for centered `mu` with `m_2(mu)<=1`, and infinity otherwise.

The proof diagonalizes the matrix sphere, establishes the empirical-measure
LDP for the resulting spherical logarithmic gas, and contracts through the
2-Lipschitz centering map. The key lower-bound device is one eigenvalue of
order `sqrt(n)` which restores the exact trace constraint while disappearing
in `W_1` and contributing only `o(n^2)` logarithmic interaction.

## Files

- `main.tex`: complete statement and proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv source paper PDF.
- `figures/open_problem_crop.png`: exact conjecture on source PDF page 35.
- `tmp/`: build and page-render artifacts.

## Status

Candidate new full proof; human review is recommended for the standard
quantile-patch lower-bound lemma and literature novelty.
