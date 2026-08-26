# Strict small-smoothness Morrey entropy: logarithmic resolution

Status: `candidate_substantial_partial_likely_valid`

This packet closes the epsilon gap in Theorems 3.13(ii) and 4.4(ii) of
arXiv:1902.04945 throughout the strict range

\[
\frac{p_1}{u_1}\left(\frac1{p_1}-\frac1{p_2}\right)
<\frac{s_1-s_2}{d}<\frac1{p_1}-\frac1{p_2}.
\]

The exact entropy order is

\[
e_k\asymp k^{-\alpha}(\log(e+k))^\alpha,
\qquad
\alpha=\frac{u_1}{u_1-p_1}
\left[\frac{s_1-s_2}{d}
-\frac{p_1}{u_1}\left(\frac1{p_1}-\frac1{p_2}\right)\right].
\]

The lower bound is a dyadic q-ary packing with one spike per mesoscopic
block. The matching upper bound retains the source's finite-level Schuett
estimate (printed equation (3.35)) and allocates covers level by level.

At the limiting face `(s1-s2)/d = 1/p1-1/p2`, the packet proves the stronger
lower bound `k^{-D}(log(e+k))^D`, which rules out a pure power, but it does not
claim the exact endpoint upper bound. This is why the packet is stored under
`solutions/partial/` despite being complete in the strict open range.

Files:

- `solution_packet.pdf` — expert-facing proof packet
- `source_paper.pdf` — original arXiv paper
- `figures/open_problem_crop.png` — the printed question and epsilon-gap estimate
- `main.tex` — packet source
- `tmp/` — LaTeX build artifacts and rendered QA pages

Ledger:
`runs/fa_banach_001/ledger/results/1902.04945_strict_small_smoothness_logarithmic_entropy.json`
