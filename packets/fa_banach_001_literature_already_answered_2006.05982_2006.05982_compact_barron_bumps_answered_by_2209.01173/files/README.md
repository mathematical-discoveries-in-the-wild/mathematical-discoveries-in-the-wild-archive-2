# Compactly supported Barron functions exist

Status: `literature_already_answered`

The end of Section 5.2 of arXiv:2006.05982 asks whether compactly supported
Barron functions exist, or whether a nonnegative Barron function can decay
faster than `|x|^{-1}`. Theorem 3.1 of the later arXiv:2209.01173 constructs
nonnegative radial Barron bumps supported in the unit ball in every odd
dimension. Restricting the bump in dimension `d+1` to a coordinate hyperplane
handles every even dimension. The later paper explicitly states this
restriction property.

The theorem uses the full Barron space and has an explicit representation with
biases in `[0,1]`. Its parameter cost `|a|(|w|+|b|)` is equivalent to the
augmented Euclidean cost in arXiv:2006.05982, so there is no unregularized-bias
gap. Since the constructed function is nonnegative and compactly supported, it
answers both source questions simultaneously.

Files:

- `solution_packet.pdf` — compact literature-status note
- `source_paper.pdf` — official arXiv:2006.05982 PDF
- `supporting_paper_2209.01173.pdf` — decisive later theorem
- `main.tex` — status-note source

An independent Radon-inversion strengthening explored during the solve-first
phase is recorded at
`runs/fa_banach_001/attempts/2006.05982_radon_smooth_compact_support_upgrade.md`.
It is not promoted as novel because the source question is already resolved.

Ledger:

- `runs/fa_banach_001/ledger/results/2006.05982_compact_barron_bumps_answered_by_2209.01173.json`
