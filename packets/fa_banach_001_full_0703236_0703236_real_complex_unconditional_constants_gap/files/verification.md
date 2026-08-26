# Verification report

## Static certificate

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/0703236_real_complex_unconditional_constants_gap/code/verify_gap.py
```

Observed output:

```text
complex witness grid upper: 0.526309881899435
certified complex constant lower bound: 1.893901515151515
worst normalized real sign: +-++-
worst corrected real certificate: 1.887887419718339
CERTIFIED: K_C > 49999/26400 > 1.89 > 1.888 > K_R
certified gap lower bound: 779/132000
```

The checker uses exact integers and rationals for all stored coefficients,
atoms, and final comparisons.  Trigonometric values and accumulated residual
bounds use outward-rounded `mpmath.iv` intervals.  The real certificates are
made exact by the six-root DFT correction proved in the packet.

## Proof audit

- The complex multiplier norm is reduced to the coefficient `l1` ratio.
- The rational witness coefficient-modulus brackets are exact integer-square
  comparisons.
- The 4096-root interval bound is extended to the full circle using the exact
  derivative upper bound and `pi<22/7`.
- Each real sign multiplier norm equals the corresponding sign-functional
  norm by rotation invariance of the supremum norm.
- All 16 sign patterns with first sign positive are present; global sign
  reversal covers the remaining 16 patterns.
- Every approximate representing measure is corrected to exact moments, with
  correction total variation at most the `l1` moment residual.
- The final gap is the exact rational identity
  `49999/26400 - 236/125 = 779/132000`.

## Rendering audit

`main.tex` compiled with `latexmk -pdf` without overfull boxes, underfull
boxes, or unresolved-reference warnings.  The final five-page PDF was
rendered to PNG at 144 dpi with Ghostscript, and every page was visually
inspected.  The source excerpts are readable, equations and the certificate
table fit their margins, page order is correct, and there are no clipped or
blank pages.  Ghostscript text extraction also recovered the theorem,
certificate output, exact gap, open-status sentence, and bibliography.

## SHA-256

```text
f75bdb6034c27d55b2ceabe1dd1e282727a3b3ae07e83824271755717d4a62fa  solution_packet.pdf
5391285283299f7ccb1795f69c4bca7ccec79e1a4cee0318c8b3038c7cabffa0  code/verify_gap.py
eaedcf63c6add8db7b6c5b1f1b12c543596dbb28c7b708adab6cb6b9fb556ab5  source_paper.pdf
470b0c0c0a189de45689031be6895e4363f27ed5df7adc0778638df4185c6ad5  supporting_status_paper_2603.28229.pdf
43b965a3b2f8e0dbdc71d6e81fd215467031c54a3041e723b90a4525c5adcb23  figures/source_open_question.png
83dda8c50ca5e318aeee4ea88e8f727b70f56d0002c36b54cb48f1570df9013f  figures/support_open_status.png
```
