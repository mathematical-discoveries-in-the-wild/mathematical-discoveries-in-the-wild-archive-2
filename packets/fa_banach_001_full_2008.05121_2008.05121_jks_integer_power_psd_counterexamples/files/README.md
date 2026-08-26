# Full solution packet: all JKS integer-power PSD counterexamples

Status: `candidate_full_likely_valid`

Source: Apoorva Khare, *Multiply positive functions, critical exponent
phenomena, and the Jain--Karlin--Schoenberg kernel*, arXiv:2008.05121v2,
Question 5.5 on printed page 19.

## Result

For every integer `m >= 0`, set `n=m+3`, choose

```text
pi/(2(n-1)) < delta < pi/(2(n-2)),
u_j = (j-(n+1)/2) delta,
x_j = tan(u_j).
```

Then the symmetric matrix

```text
(max(1+x_j x_k,0)^m)_{j,k=1}^n
```

has negative determinant. Thus it is not positive semidefinite and the
kernel power is not `TN_(m+3)`. This answers both the ordinary and the
stronger symmetric parts of Question 5.5 for every integer exponent.

The exact identity behind the result is

```text
det A = -cos(L)^(2m) det B < 0,
```

where `A=([cos(u_j-u_k)]_+^m)`, `L=(n-1)delta`, and `B` is the middle
`(m+1)`-square principal block of the untruncated cosine-power matrix. The
untruncated matrix has Fourier rank `m+1`, while `B` is a positive-definite
Vandermonde Gram matrix.

Combined with Theorem C of the source, this yields the full classification:
for every `p>=2` and `alpha>=0`, `K_JKS^(circ alpha)` is `TN_p` on the full
plane if and only if `alpha>=p-2`.

## Files

- `main.tex`: self-contained proof, classification corollary, and audit.
- `solution_packet.pdf`: rendered expert-facing packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: readable crop of Question 5.5.
- `code/verify_jks_family.py`: 180-digit audit for `m=0,...,16`.
- `verification.md`: proof, numerical, source, render, and novelty checks.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Review focus

The proof is elementary and exact. Human review should check the sign of the
two-corner determinant coefficient and the final use of the source's Theorem
C. Novelty is plausible, not certified: exact-question and close-literature
searches through 2026-08-17 found no later resolution, and the current
author-hosted PDF still states Question 5.5.

Ledger:
`runs/fa_banach_001/ledger/results/2008.05121_jks_integer_power_psd_counterexamples.json`
