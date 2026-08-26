# Verification record

## Mathematical checks

1. The normalization
   `e_alpha(z)=z^alpha/sqrt(alpha!)` was checked against Gaussian monomial
   orthogonality, giving the exact matrix action with no missing factorials.
2. The coefficient transform from Fock space to `ell^2(N_0^n)` is unitary,
   so boundedness and the operator norm transfer in both directions.
3. Coherent vectors have squared norm `exp(|z|^2)` and dense span; hence the
   finite kernel inequality is sufficient, not merely necessary.
4. For the obstruction kernel, every block row and column has norm one, while
   the block operator norm is `sqrt(k)`.
5. The slice estimate is summable because block size `k <= i+1` on the block
   containing index `i`; factorial decay then gives
   `(1+|z|^2)exp(|z|^2)`.

Run the verifier with:

```bash
conda run --no-capture-output -n sandbox python code/verify_kernel_matrix.py
```

Expected output consists of four `PASS` lines for the block norms, coherent
inequality, and Gaussian moment normalization.

## Source evidence

`figures/source_question_crop.png` is cropped from page 13 of
`source_paper.pdf`.  It contains the full open problem and the preceding
`T(1)` motivation, with no neighboring result substituted for the question.

## Packet QA

The final PDF is compiled into `tmp/`, copied to the packet root, checked for
LaTeX warnings, rendered page-by-page, and visually inspected.

- Final length: 4 pages.
- Final warning scan: no warnings, overfull boxes, underfull boxes, undefined
  references, or multiply defined labels.
- Ghostscript null-device validation: passed.
- All four RGB page renders at 160 dpi were visually inspected; no clipping,
  overlap, malformed equations, missing glyphs, or incomplete source crop was
  found.
- `solution_packet.pdf` SHA-256:
  `a45b1663dac4db290e215124bae5d071a56672de049c9592b31984103b52f0c0`.
- `source_paper.pdf` SHA-256:
  `67a6b453e6ad0a101efb2968dc1139b2c42baeee94376c1fee382ac1a478ec69`.
