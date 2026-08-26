# Krawtchouk functions maximize every even moment on one Fourier level

Status: `candidate full solution; likely valid; human review requested`

Source: Yury Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014, source-only Appendix B.2, item 6.

## Result

For every Boolean cube dimension `n`, level `a`, and integer `m>=1`,

```text
sup_{0 != g in level a} ||g||_{2m}/||g||_2
  = ||K_a||_{2m}/||K_a||_2.
```

Consequently the exact operator norm of the Fourier-level projection is

```text
||Pi_a||_{L_2 -> L_{2m}} = ||K_a||_{2m}/||K_a||_2,
```

and both ratios asked about in the source are attained by the permutation-invariant Krawtchouk function `K_a`.

The proof first removes complex phases, then applies root-mean-square compression to pairs of Fourier coefficients joined by a Johnson-graph edge. For a fixed block of a `2m`-tuple moment expansion, the remaining coordinate choices form an even- or odd-parity tensor. Its sharp product bound proves that compression increases every even moment. Repeated compressions average squared coefficients to the constant vector.

## Literature boundary

Aaronson, arXiv:1805.05295, proves the exact `p=4` case by additive-energy compression. The packet's new mathematical claim is the extension to every even `p=2m`. Bounded searches through 2026-08-13 found later asymptotically sharp general-moment bounds, but no exact all-even-moment result.

## Source provenance

The question is in the official arXiv source tree under an appendix-only `\ifmapx` switch and is absent from the official 24-page PDF. `figures/open_problem_crop.png` comes from page 27 of a DVI/PDF build of that original source using its documented appendix job name `hc_hamming_apx`. `source_paper.pdf` is the official arXiv PDF; `source_question_build.pdf` is the source-enabled appendix build.

## Files

- `main.tex`, `solution_packet.pdf`: exact theorem, proof intuition, parity-tensor lemma, compression proof, verification, limitations, and novelty audit.
- `source_paper.pdf`: official arXiv PDF for 1309.3014.
- `source_question_build.pdf`: original source compiled with the appendix job switch.
- `supporting_paper_1805.05295.pdf`: Aaronson's exact fourth-moment result.
- `figures/open_problem_crop.png`: source Appendix B.2, including item 6.
- `code/`: numerical optimization and compression sanity checks.
- `verification.md`: mathematical and artifact audit.

Human-review focus: verify the parity reduction after deleting a coordinate pair, the parity-tensor normalization `2^(r/2-1)`, and convergence of the cyclic Johnson-graph averaging maps.
