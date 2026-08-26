# Verification record

Date: 2026-08-13  
Agent: `agent_lane_09`  
Model: `GPT5.6`

## Analytic audit

- Verified that `d(x,y)=|x-y|^(1/2)` is a metric, so the assignment linear
  program is exactly `n` times the Kantorovich distance and admits the stated
  Hoelder dual.
- Verified the signed dyadic-tent estimate by splitting at the unique scale
  `2^(-(m+1)) < |x-y| <= 2^(-m)`.  The two geometric-series constants total
  less than `13.657`, hence the packet's safe constant `14`.
- Recomputed the tent moments `E phi=h/2`, `E phi^2=h/3` and
  `Var(phi(U)-phi(V))=2h/3-h^2/2 >= h/6`.
- Recomputed the fourth-moment and Paley--Zygmund constants.  When `nh>=12`,
  `nv>=2`, `E S^4 <= 4(nv)^2`, and `E|S| >= sqrt(nh)/(16 sqrt(12))`.
- Checked the level algebra: `2^j` cells, a `2^(-j/2)` coefficient, and a
  `sqrt(n 2^(-j))` cell discrepancy give exactly a constant multiple of
  `sqrt(n)` per level.  There are `1+floor(log_2(n/12))` eligible levels.
- Read the original source question on printed pages 3--4 and equation (12) of
  Bobkov--Ledoux's 2024 published correction on printed page 6.

## Computational regression

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2305.09234_critical_half_normalization_diverges/code/verify_multiscale_witness.py
```

Output:

```text
exact moment inequalities: PASS (levels 0..13)
sampled signed-sum Hoelder ratio: 6.502363 <= 14
primal-dual checks: PASS (20 trials per n)
n= 32  median((witness/14)/M)=0.050173  median(M/(sqrt(n) log n))=0.306349
n= 64  median((witness/14)/M)=0.078486  median(M/(sqrt(n) log n))=0.308955
n=128  median((witness/14)/M)=0.104304  median(M/(sqrt(n) log n))=0.283914
n=256  median((witness/14)/M)=0.122985  median(M/(sqrt(n) log n))=0.250555
All regression checks passed.  These checks supplement, not replace, the proof.
```

The Hungarian comparisons test 80 independent random assignment instances.
The sampled Hoelder test checks 12 random ten-level sign systems and three
million grid-point pairs.  Neither finite test is used as proof.

## Render verification

- Compiled twice with TeX Live 2026 `latexmk`/`pdflatex` using
  `-interaction=nonstopmode -halt-on-error`.
- Final PDF: A4, 8 pages, no unresolved-reference or box warnings.
- Rendered all eight pages to PNG at 130 dpi and visually inspected every page.
- Source and correction crops are readable and unclipped; the open question's
  two-page continuation is present.
- Ghostscript text extraction finds the theorem, both lemmas, and references.

## SHA-256

```text
8aa6a4e875f77e8e2b09cdaae588a896cb36be042d22b2961d3a667738dfb264  solution_packet.pdf
930be4f238c702e62b05a083628b7db2c7a6ee2f2e0d7e906a1c2d81e5323eb8  source_paper.pdf
8100b316ca6f595d6a481e5e0d602dcf60bda17d75304c2460e8e93d64ff57c0  supporting_bobkov_ledoux_2024_correction.pdf
c331d8ab95f9058d5514d89305b927432fe71828805491c0439b0b872326324c  figures/open_problem_crop_part1.png
e26d1f5cda0817a80fb2b5b9389e64296130000a8cd6f75305122dadc64ff09f  figures/open_problem_crop_part2.png
97308a09547d87fe756530ae1c13840b1dce49bbb7097b3cfb8727f210eec738  figures/correction_notice_crop.png
120f0b08bd0d63a0d5f0b0827fa86c5dd53c047acc9ecc988518052a82500260  figures/corrected_bound_crop.png
92e8ce93084854b90742af7edfdb12d1ba9009dbb620021b87f7831497f74757  code/verify_multiscale_witness.py
6bbc88337e3326fc60fd24c2babb41d88584fb5b20fdf5a4a369e029a5d8e243  main.tex
```

## Human-review focus

1. Confirm the use of pointwise, sample-dependent dual witnesses.
2. Recheck the arbitrary-sign Hoelder constant and the Paley--Zygmund step.
3. Confirm equation (12) of the 2024 correction has precisely the transport
   normalization used here.
4. Preserve the wording caveat: the result refutes the intended finite limit,
   while the extended-real limit for the uniform law is `+infinity`.
