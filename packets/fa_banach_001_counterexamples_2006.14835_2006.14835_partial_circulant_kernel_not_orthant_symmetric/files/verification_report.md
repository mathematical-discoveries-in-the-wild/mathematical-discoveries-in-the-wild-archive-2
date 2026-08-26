# Verification report

Verified on 17 August 2026.

## Mathematical regression check

Command:

```text
conda run --no-capture-output -n sandbox python code/check_plucker_obstruction.py
```

Output:

```text
PASS: Q vanishes identically on the partial-circulant row spaces
PASS: the coordinate-0 flip produces a nonzero polynomial
flipped Q = 2*(a**3*c - a**2*b**2 - 2*a*b*c*d + a*c**3 + b**3*d + b*d**3 - c**2*d**2)
witness at (1,0,1,0) = 4
```

The script is a regression check, not part of the proof.

## Packet build

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
completed successfully.  The final log contains no warning, undefined-reference,
overfull-box, or underfull-box lines.

## PDF QA

- Final packet: `solution_packet.pdf`
- SHA-256: `1b92fae80c0218d4ee3729cc20dc44c42a7e1b19e082b3bb1dc9917ea2ca0154`
- Pages: 4
- Source PDF present: yes, 15 pages
- Open-question crop present: yes, source PDF page 14
- All four final packet pages rendered at 150 dpi and visually inspected: yes
- Layout defects, clipped equations, or unreadable text found: none
- Extracted-text sanity check after the final rebuild: passed

## Review priorities

1. Recompute the six minors and the factorization giving `Q=0`.
2. Confirm that the coordinate-zero sign flip negates exactly
   `p01,p02,p03`.
3. Confirm that the flipped polynomial is nonzero and hence vanishes with
   probability zero under an absolutely continuous input law.
4. Confirm the orthogonal-complement transfer from row-space asymmetry to
   kernel asymmetry.
