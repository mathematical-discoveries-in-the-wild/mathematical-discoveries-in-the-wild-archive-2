# Verification record

## Mathematical audit

- Fourier convention: the Walsh characters are orthonormal for uniform probability measure on `F_2^n`; hence `||K_a||_2^2=binom(n,a)`.
- Complex reduction: expanding `E|g|^(2m)` and applying the triangle inequality termwise gives the moment of the coefficientwise modulus, while Parseval preserves the denominator.
- Compression preserves coefficient `ell_2`: each pair of squares is replaced by its arithmetic mean.
- Tuple constraint: the moment expansion is indexed by `2m` level-`a` sets with empty total symmetric difference.
- For a fixed deleted-base tuple, the number `r` of flexible `10/01` lifts must be even. The two coordinate constraints reduce to one prescribed parity condition.
- Parity filter: the block is `(prod(u+v) +/- prod(u-v))/2`.
- Normalization: after setting `x=(u+v)/(sqrt(2)t)`, `y=(u-v)/(sqrt(2)t)`, one has `x^2+y^2=1`, and `prod|x|+prod|y|<=|x_1x_2|+|y_1y_2|<=1`.
- The compressed block has `2^(r-1)` equal summands of size `2^(-r/2) prod t`, hence exactly `2^(r/2-1) prod t`.
- Repeated squared-coefficient averaging is a finite doubly stochastic consensus process. Its edge union is the connected Johnson graph; the positive diagonal permits waiting, so repeated sweeps converge to the uniform vector.
- The second source ratio follows from `||Pi_a f||_2<=||f||_2`, with equality attained by `f=K_a`.

## Computational audit

- `code/level_extremizer_probe.py` numerically optimized the level coefficient sphere for all tested cases through `n=7`, at `p=4,6,8`; no value above the constant-magnitude orbit was found.
- `code/compression_probe.py` applied the exact coefficient compression to 20,000 random nonnegative coefficient arrays in each of nine configurations through `p=10`; no decrease was found.
- These computations are sanity checks and are not used as proof.

## Literature audit

- Exact-title/id and core-keyword searches found no prior run duplicate.
- Aaronson, arXiv:1805.05295, is the exact known `p=4` subcase.
- Kirshner--Samorodnitsky, arXiv:1801.08507, develops the fourth-moment problem and cites Aaronson's resolution.
- Kirshner--Samorodnitsky, arXiv:1909.11929, gives nearly sharp general-`p` moment bounds but not the exact all-even identity claimed here.
- Web/arXiv searches through 2026-08-13 used combinations of `Hamming sphere`, `Krawtchouk`, `even moments`, `L_6`, `higher additive energy`, and the citation neighborhood of arXiv:1805.05295. No exact all-even result was located.

## Artifact audit

- `source_paper.pdf` is the official 24-page arXiv PDF.
- The source question is appendix-only. The original TeX was compiled with job name `hc_hamming_apx`; page 27 contains the question and was rendered for the crop.
- The final packet is compiled from the packet directory with intermediates under `tmp/`.
- All final pages are rendered to PNG and visually inspected after the last meaningful edit.
- Final packet: 4 A4 pages, SHA-256 `8c7d262758e22e73809f503889a55c794d46bf85ee94052e5fc2743450196332`.
- Final LaTeX log contains no undefined-reference, overfull-box, or underfull-box warnings.
