# Verification report

Status: all listed checks passed on 2026-08-17.

## Source evidence

- Original PDF: `source_paper.pdf` (arXiv:2303.00076).
- The open problem is in Remark 2.3(3), source PDF page 5.
- `figures/open_problem_crop.png` was rendered at 220 dpi from that page and
  visually inspected. It retains the full readable page width, Theorem 2.2,
  all of Remark 2.3, the complete open question, and Figure 3 with caption.

## Numerical audit

Command, run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_bounds.py
```

Output:

```text
finite normalized cosine Gram spectra:
  N= 16: lambda_min=0.832500133726, lambda_max=1.186149288392
  N= 32: lambda_min=0.819547063132, lambda_max=1.207839486866
  N= 64: lambda_min=0.802672689337, lambda_max=1.231382695164
  N=128: lambda_min=0.794969059182, lambda_max=1.244571370586
  N=256: lambda_min=0.781324750716, lambda_max=1.267331772717
  N=512: lambda_min=0.773698855226, lambda_max=1.280150591375
worst cosine/sine spectral mismatch: 0.000e+00
8-prime, length-80 lower witness: 0.681311350825
8-prime limiting lower product: 0.677996360421
global sharp lower constant: 0.666666666667
8-prime, length-80 upper witness: 1.467744146372
8-prime limiting upper product: 1.474934171296
global sharp upper constant: 1.500000000000
```

The script checks six complete finite spectra, exact diagonal sign conjugacy
at floating-point precision, and two explicit finite tensor-product witness
families. It does not prove the theorem; the packet's primewise Fourier-symbol
and Euler-product argument is the proof.

## Analytic audit checklist

- Source normalization checked: diagonal entries of the normalized cosine and
  sine blocks are one.
- Different 2-adic valuation blocks are orthogonal by source Lemma 2.1.
- The odd kernel factorization was checked prime by prime.
- The one-prime symbol has extrema `(1-r)/(1+r)` and `(1+r)/(1-r)`.
- Odd-prime Euler products were checked as `8/pi^2` and `12/pi^2`, giving
  ratio `2/3` and reciprocal `3/2`.
- Sharpness uses finite supports, so the witness vectors embed in initial
  finite Gram matrices without any infinite-section assumption.
- The sine sign rule was checked against `chi_4(oddpart(k))`.
- The multivariate extension uses only the source's explicit inner-product
  lemma and unique decomposition into primitive oriented lattice rays.

## Rendering audit

The packet is rebuilt from `main.tex` during the 2026-08-21 interrupted-lane
recovery. The recovery audit checks the log for errors, undefined references,
and overfull boxes, renders every PDF page to PNG, and visually inspects every
page for clipping, unreadable figures, or malformed formulas. The exact build
and page count are appended after that rebuild.

The rebuild completed successfully: seven pages, with no LaTeX errors,
undefined references, or overfull boxes. Every page was rendered at 120 dpi
and visually inspected. No clipping, overlap, malformed formula, or unreadable
source figure was found. The numerical verifier was rerun in the `sandbox`
environment and reproduced the finite spectra, exact sign conjugacy, and the
`0.681311...` / `1.467744...` finite witnesses recorded above.
