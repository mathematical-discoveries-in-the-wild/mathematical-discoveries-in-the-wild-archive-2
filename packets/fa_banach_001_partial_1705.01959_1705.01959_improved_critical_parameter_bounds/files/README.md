# Improved bounds for the multiplicative-Hilbert critical parameter

Status: `candidate_partial_likely_valid`

Source: Karl-Mikael Perfekt and Alexander Pushnitski, *On the spectrum of the
multiplicative Hilbert matrix*, arXiv:1705.01959.

## Result

For the source paper's critical parameter `a_*`, which separates the regime
where the Helson matrix

`M(g_a) = {1/(sqrt(mn)(a+log(mn)))}_{m,n>=1}`

has one eigenvalue above `pi` from the regime where it has none, this packet
proves

`1/3 < a_* <= 2 gamma = 1.154431...`,

where `gamma` is Euler's constant.  This strictly improves the source bounds
`1/pi <= a_* <= 2`.

The lower bound is elementary: at `a=1/3`, the `2 x 2` compression to the
first two coordinates already has an eigenvalue above `pi`.  The proof uses
only `pi < 22/7` and `log 2 < 7/10`.

For the upper bound, the source identifies `M(g_a)` with the integral Hankel
operator of kernel `h_a(t)=exp(-at/2) zeta(1+t)`.  Theorem 5 of Garcia,
Grenie, and Molteni, arXiv:2607.08342, says that
`zeta'(s)/zeta(s)+1/(s-1)` decreases on `(1,infinity)`.  Integrating from the
pole gives `t zeta(1+t) <= exp(gamma t)`.  Hence `h_a(t)<=1/t` for
`a>=2 gamma`, and comparison with the norm-`pi` Carleman operator gives
`||M(g_a)||<=pi`.

## Scope

This is a substantial partial answer to the source's request to compute
`a_*`; it does not determine `a_*` exactly and does not explicitly
diagonalize `M(g_a)` or the multiplicative Hilbert matrix `M_2(g_0)`.

The separate bounded-symbol question is already represented in this run by
`attempts/2005.11951_multiplicative_hilbert_h1_endpoint_attempt.md`; this
packet does not repeat that endpoint investigation.

The upper-bound mechanism is sharp for pointwise Carleman domination:
`t zeta(1+t)=1+gamma t+O(t^2)`, so `h_a(t)<=1/t` fails near zero whenever
`a<2 gamma`.

## Evidence and files

- `source_paper.pdf`: arXiv:1705.01959.
- `supporting_paper_2607.08342.pdf`: the zeta logarithmic-derivative monotonicity theorem.
- `figures/open_problem_crop.png`: source PDF page 3, displaying the open problem and old bounds.
- `main.tex`, `solution_packet.pdf`: full proof packet.

Bounded exact-phrase searches for the critical value, `a_*`, `1/3`, and
`2(1-log(3/2))` located the source paper but no later improvement of its
bounds.  The supporting 2026 zeta theorem was not found applied to this
operator family.  Novelty confidence is moderate pending expert review.

