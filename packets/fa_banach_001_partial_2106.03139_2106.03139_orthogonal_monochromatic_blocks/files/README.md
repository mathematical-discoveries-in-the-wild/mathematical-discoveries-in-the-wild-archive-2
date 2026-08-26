# arXiv:2106.03139 — orthogonal monochromatic-block partial result

Status: `candidate substantial partial result, likely valid`

Source:

- Rafał Latała and Witold Świątkowski, *Norms of Randomized Circulant
  Matrices*, arXiv:2106.03139.
- Exact target: Proposition 1.5 and the following sentence on source PDF page
  4, asking whether the `sqrt(log(p+1))` loss in the sparse spectral-norm
  comparison is necessary.

Result:

- The constant-factor comparison is stable under arbitrary orthogonal direct
  sums.
- Consequently, the logarithmic factor is unnecessary for every matrix that,
  after independent row and column permutations, is block diagonal with each
  block an arbitrary scalar multiple of a `0-1` matrix.
- The constant is independent of the number of blocks, their sizes, their
  masks, and the dynamic range of their scalar weights.

The proof decomposes the test vectors into their row and column blocks,
applies the source paper's sharp `0-1` theorem in each block, and uses
Cauchy--Schwarz to prevent any accumulation over blocks.

This does not settle the full problem.  If magnitude levels overlap in rows
or columns, the key square-summability step disappears.  The main circulant
case has maximal overlap of this kind.

- Proof packet: `solution_packet.pdf`
- Original source PDF: `source_paper.pdf`
- Open-question evidence: `figures/open_problem_crop.png`
- Verification: `verification_report.md`
- Deep attempt history:
  `runs/fa_banach_001/attempts/2106.03139_sparse_rademacher_direct_sum_upgrade.md`
- Ledger:
  `runs/fa_banach_001/ledger/results/2106.03139_orthogonal_monochromatic_blocks.json`

