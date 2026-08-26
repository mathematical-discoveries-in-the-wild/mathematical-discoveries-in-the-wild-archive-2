# Boundary cone-projection counterexample

Status: `full_counterexample_pending_human_review`

Remark 5.2 of arXiv:0909.3712 asks whether Lemma 5.1 remains true at the
boundary slope `s_0=v`. It does not.

For every `u,v>0` and `N>1`, choose `1<alpha<N` and an `L2` Fourier function
with radial decay `|xi|^{-alpha}` supported in the exterior sector
`v<xi_2/xi_1<v+1`. Its inverse Fourier transform `g` satisfies
`P_{C_{u,v}}g=0`. Nevertheless, after multiplying by any cutoff equal to one
near the origin, convolution in frequency retains an `R^{-alpha}` leading
term on some fixed exterior ray in every neighborhood of slope `v`. Hence
`(0,v)` is not `N`-regular for `g`, although it is regular for its projection.

## Files

- `main.tex`, `solution_packet.pdf`: complete proof and scope analysis.
- `source_paper.pdf`: arXiv:0909.3712.
- `figures/lemma_5_1_crop.png`, `figures/remark_5_2_crop.png`: source statement
  and question.
- `verify_sector_counterexample.py`: support and exponent sanity checks.
- `references.md`, `verification_report.md`: search and QA records.

## Human review

- [ ] A human expert has independently checked the proof, interpretation, and
  novelty status.
