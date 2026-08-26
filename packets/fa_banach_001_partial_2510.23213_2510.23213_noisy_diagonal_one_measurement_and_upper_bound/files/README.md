# Exact one-measurement recovery and a sharper general upper bound

Status: **candidate partial result - likely valid, pending human review**.

Source: David Krieg, Erich Novak, Leszek Plaskota, and Mario Ullrich,
*Noisy nonlinear information and entropy numbers*, arXiv:2510.23213; Journal
of Fourier Analysis and Applications 32, Article 36 (2026). The exact-value
question appears in Section 5.2 of the journal version and on PDF page 12 of
the arXiv version.

For every `1 <= p < infinity`, this packet proves the exact one-measurement
formula

`e_1^lin(D_sigma,delta)_p^p = delta^p sigma_1^p + (1-delta^p) sigma_2^p`.

For arbitrary `n`, it also proves the sharper upper bound

`e_n^p <= min_{0 <= k <= n} [sigma_{k+1}^p + delta^p sum_{i <= k}(sigma_i^p-sigma_{k+1}^p)]`.

The latter uses nonlinear scalar centers and improves the `p`th power of the
source's displayed coordinate-decoder bound by `n delta^p sigma_{n+1}^p`
when `k=n`. The full exact-value problem for `n >= 2` remains open.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question and surrounding bounds.
- `code/verify_scalar_center.py`: deterministic numerical sanity checks.
- `code/crop_open_problem.py`: reproducible source-page crop.
- `verification.md`: commands, outcomes, and limitations.

Human-review focus: the scalar interval-intersection lemma, the reconstruction
center's dependence on each noisy datum, and the two-dimensional cap argument
for the universal one-measurement lower bound.
