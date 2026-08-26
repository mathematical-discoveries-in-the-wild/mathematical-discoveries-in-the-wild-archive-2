# Counterexample packet: exponential STFT concentration does not force a Poincare inequality

Status: candidate full counterexample, likely valid, needs human review.

Source: Martin Rathmair, *Stable STFT phase retrieval and Poincare inequalities*, arXiv:2407.00398; published in IMRN 2024.

Question: Conjecture 1.18 on page 7 asks whether exponential concentration of
`V_g f`, for `g(t)=exp(t-exp(t))`, forces the strictly positive weight
`w=(|V_g f|^2 * gamma)^2` to have finite Poincare constant.

Result: no. For every `a,b>0`, a lacunary sum
`f=sum_n exp(-kappa R_n) T_{R_n}g`, with `R_n=L 2^n` and sufficiently small
`kappa>0`, has exponentially concentrated STFT but `C_P(w)=infinity`.

Mechanism: each translate creates an island of `w`-mass comparable to the
fourth power of its coefficient. The distance to the preceding island doubles,
and exponential smoothing leaves a midpoint bottleneck whose conductance is an
extra exponentially small factor. Smooth step functions across the midpoints
have unbounded variance-to-energy ratio.

Novelty check: on 2026-08-11, exact-title, exact-conjecture-number, and phrase
searches were run on the web and in the local arXiv source corpus. They surfaced
the source/published paper but no later resolution or matching construction.

Files:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: compiled and visually checked packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: source page crop containing Conjecture 1.18.
- `VERIFICATION.md`: explicit analytic and visual verifier report.

Review recommendation: verify the separated-sum convolution estimate, the
uniform dominance on each island, and the variance identity for the step tests.
No numerical or conditional dependency is used.
