# Verification report

## Mathematical audit

- Checked the kernel inequality in both orderings of `W_i,W_j`: for
  `sigma>0` and weights in `[1,infinity)`,
  `kappa_sigma(W_i,W_j) >= W_i`.
- Checked the torus diameter `D_N=d floor(N/2)` for the paper's `l1` torus
  metric.
- Checked the invariant subspace entry by entry, including coordinates
  outside the universal set.
- Checked the Pareto count exactly: the sufficient saturated set has binomial
  law with parameter `D_N^(-alpha(tau-1))`.
- Used `Var(M_N)<=E[M_N]` for relative concentration; no unquoted tail theorem
  is needed.
- Audited all three regimes of `alpha(tau-1)` relative to `d`, plus the
  separate endpoint `alpha=0`.
- Checked consistency with the source's absolute-continuity theorem: the
  forced ESD mass tends to zero for every fixed `alpha>0`.
- For the Gaussian comparison, conditioned on a strictly positive variance
  profile and used the nonzero discriminant-polynomial argument.  The packet
  does not make this claim when truncation creates zero variances.

## Reproducible computation

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2502.09415_universal_vertex_spectral_spike/code/verify_spike.py
```

The script constructs a seeded KBRG instance, verifies every threshold vertex
is universal, checks the explicit difference-vector eigenbasis, compares the
full numerical multiplicity at `-1`, and reproduces the source-figure
calibration.  The recorded output is in `tmp/verification_output.txt`.

## Source and novelty audit

- The exact conjecture was checked on arXiv:2502.09415v2, PDF page 9.
- The current arXiv record was checked on 2026-08-11 and still lists v2 (14
  March 2025) as the latest version.
- The run's cheap indexes contained no prior packet, result, attempt, or proof
  gap for the target or its core keywords.
- A bounded web/arXiv search on 2026-08-11 using the exact title, arXiv id, and
  the keyword combinations `universal vertices spectral atom`, `eigenvalue
  -1`, and `scale-free percolation` found no later explicit resolution.
- Novelty remains provisional pending expert literature review.

## Packet/render QA

- `main.tex` was compiled twice with `pdflatex -halt-on-error`.
- The final PDF was checked for compilation diagnostics and text extraction.
- Every final page was rendered to PNG and visually inspected for clipping,
  overlap, illegible mathematics, and missing figures.
