# Verification record

Status: candidate full counterexample, likely valid, pending expert review.

## Mathematical checks

- `H=C(T,R)` is a closed translation-invariant subspace.
- `u(f)=||f||_infinity` fixes the base point and has Lipschitz norm one.
- The Lipschitz `p`-summing inequality holds with constant one by choosing
  the single test function `v=u` in the defining supremum.
- Constant functions show the optimal summing constant is one.
- Translation invariance follows because circle translations are bijections.
- The peak functions are continuous on the circle and satisfy exactly
  `integral |f_n|^p d sigma = 1/(pi*n*(p+1))`.
- Applying any proposed Haar domination inequality to `(f_n,0)` yields a
  contradiction as `n` tends to infinity.
- The argument disproves domination with every finite constant, so it covers
  both common Pietsch-measure constant conventions.

## Literature checks

- The exact question is repeated as open on PDF page 2 of arXiv:2603.27851
  (March 2026).
- That paper's remark after its partial theorem conjectures that the smaller
  `B_{H*}` result is best possible.
- Exact-title, arXiv-id, and core-keyword web searches on 2026-08-09 found no
  later primary-source resolution.

## Artifact checks

- `main.tex` compiled without LaTeX errors.
- The final three-page PDF was rendered at 150 dpi and every page was
  visually inspected; no clipping, overlap, or illegible material was found.
- The source PDF was rendered through page 4; PDF page 2 contains the exact
  displayed open problem quoted in the packet.
