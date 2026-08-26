# Verification

## Claim audit

- The exact reverse-inequality question and its holomorphic-family
  reformulation were checked in the parsed source and on official PDF page 7.
- Every `u_m` has Fourier support in a finite union of smooth compact balls
  separated from the origin, so it belongs to the stated test class.
- An admissible dyadic resolution can be flat on the normalized frequency
  balls and exclude all other selected bands because `R=2^K>=8`. Its
  equivalence constants do not depend on `m`.
- The selected square-function terms give the lower bound
  `c sqrt(m)||phi||_p`.
- Splitting the lacunary series at `R^j r=1` gives a uniform `r^s` bound.
  The decay/mean-value estimate for `phi` is global and uses
  `w(x)=(1+|x|)^(-M)` with `M>N/p`.
- The distribution of `w(x)/|x-y|^(N/p)` was evaluated exactly by Fubini and
  the volume of a ball; the symmetric sum follows by a two-set union bound.
- The holomorphic-family conclusion would imply the failed reverse estimate
  by the definition of complex interpolation and
  `[L^p,Wdot^{1,p}]_s=Fdot^s_{p,2}` on the frequency-localized class.

## Independent stress check

`verify_geometric_series.py` sampled logarithmic spatial scales for up to 256
frequency bands at `s=0.10,0.25,0.50,0.75,0.90`. The normalized maxima
stabilized in every case (largest observed value `30.626637`) and the
frequency-support separation assertions passed. This script is a regression
check for the geometric split, not a substitute for the analytic proof.

## Mathematical scope

The result disproves the reverse inequality for every fixed `N>=1`,
`1<p<infinity`, and `0<s<1`, exactly the source's stated range. It uses
complex-valued Schwartz functions, which are natural in the source's complex
interpolation formulation. No claim is made about excluded endpoints.

## Artifact checks

- [x] Official arXiv PDF is present, readable, and has 17 letter-size pages.
- [x] Exact question crop is an unaltered RGB rendering of source PDF page 7.
- [x] Geometric-series stress checker passes.
- [x] `main.tex` compiles without errors, undefined references, or box
  warnings.
- [x] Final PDF metadata and text extraction are healthy (4 letter-size
  pages, 9,170 extracted text characters).
- [x] Every final page was rendered at 150 dpi, confirmed RGB, and visually
  inspected for clipping, collisions, bad breaks, and legibility.
- [x] SHA-256 hashes are recorded below.

## SHA-256

```text
fcee8a2ff065071f659202a30fa84ef7e0d7a284aada3dbae8164ad4211494d6  main.tex
686a9e01674fbf0976ca6977483d76f6474cdb7bc18cece5571ba92dfe7a5f91  README.md
998d9b7417b1542560c6b5aed2543f5c1fd2d2bc5352549a1c139ae9a58ff463  verify_geometric_series.py
3a24debd277ffd45778b14992ac6b53654434449971e0da43dd79a308c57c440  solution_packet.pdf
959dc9a8eb2e147ea525386ccc6d2bdb9aa1e3d41ee8b71accec6693f2b1d937  source_paper.pdf
3544973432328189bf1fb9ee4189ffab1ec6438602915a82888a3e095bb9587d  evidence/source_question_crop.png
```

Verification completed at 2026-08-13T15:32:40Z.
