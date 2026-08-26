# Verification report

Verified on 17 August 2026.

## Mathematical regression check

Command:

```text
conda run --no-capture-output -n sandbox python code/check_rank_two_family.py
```

The script verified the exact matrix, determinant, trace, and
`lambda_minus < 2`, and printed diverging ratios through `N=1000`.  Final
status:

```text
PASS: left tail diverges while the second squared H^(1,0) singular value is < 2
```

The script is a regression check, not part of the proof.

## Packet build

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
completed successfully.  The final log contains no warning, undefined-reference,
overfull-box, or underfull-box lines.

## PDF QA

- Final packet: `solution_packet.pdf`
- SHA-256: `2ee5f87b2573f69c49a35a971292e8f25cce083a861b01cf73ebfaa6dd40f42d`
- Pages: 3
- Source PDF present: yes, 17 pages
- Open-question crop present: yes, source PDF page 3
- All three final pages rendered at 150 dpi and visually inspected: yes
- Layout defects, clipped equations, or unreadable text found: none
- Extracted-title and page-count sanity check after final rebuild: passed

## Review priorities

1. Recompute the `H1` Gram matrix of the rotated constant/high-frequency
   pair.
2. Confirm that squared `H^(1,0)` singular values are the eigenvalues of
   `diag(2,1) G_N diag(2,1)`.
3. Check the bound on the smaller eigenvalue via determinant divided by the
   larger eigenvalue.
4. Confirm that the source question is intended uniformly in `u`.
