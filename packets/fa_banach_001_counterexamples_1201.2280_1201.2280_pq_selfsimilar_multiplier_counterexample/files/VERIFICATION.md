# Verification record

## Source

- The exact target was checked in local arXiv source and the official
  34-page arXiv:1201.2280 PDF.
- It is the remark immediately following Theorem 5.4(ii), asking whether
  the identity between multipliers and selfsimilar Besov spaces for
  `0<p=q<=1` can be generalized to `p!=q`.
- The source identifies estimate (5.13), TeX label `open-1`, as the point
  where its proof requires `p=q`.

## Mathematical audit

- The wavelet coefficient normalization was checked against the standard
  Besov wavelet quasi-norm: each selected scale contributes exactly one to
  the outer `ell^q` norm.
- After a source dilation by `2^(-J)`, component `j` is centered at
  `2^(J+j)` and has radius `O(2^(J-j))`.
- Consecutive support gaps remain uniformly larger than the source cutoff
  diameter, so each localization contains at most one component.
- For `j>=J`, wavelet scaling yields the bound
  `2^(-J(s-1/p))`.
- For `j<J`, Leibniz' rule and a uniform compact-support `C^K` estimate
  yield `2^(-j(s-1/p))`; derivatives landing on the fixed cutoff were
  included explicitly.
- Both estimates remain bounded at the endpoint `s=1/p`.
- The smooth test cutoffs remain disjoint after every translation used in
  an order-`r` finite difference, giving input norm `O(N^(1/p))`.
- Their products with the counterexample have wavelet norm comparable to
  `N^(1/q)`, which contradicts multiplier boundedness for `q<p`.
- The proof is on `R`; this suffices to refute a general extension on
  Euclidean spaces.

## Supporting literature and novelty

- Nguyen--Sickel arXiv:1703.03246 was checked from its official PDF and
  source.  Theorem 1.2 supplies the positive `p<=q`, `s>1/p` branch;
  Theorem 1.6 characterizes the `q<p` branch by a stronger localized
  space; Proposition 3.10 uses the compatible separated-wavelet tests.
- The later paper does not explicitly state membership of its separated
  wavelet sum in the dilation-sensitive selfsimilar space from
  arXiv:1201.2280.  That uniform scaling audit is supplied in the packet.
- Bounded exact-phrase, arXiv-id, and keyword searches found no explicit
  answer to the source's selfsimilar-space question.  No priority claim is
  made.

## Build and visual QA

- `main.tex` compiled to a two-page A4 PDF with no final LaTeX warnings,
  undefined references, or overfull/underfull boxes.
- The complete packet was extracted to text and checked for all proof
  steps and parameter restrictions.
- Both rendered packet pages were visually inspected at high resolution.
- Printed source page 29, containing Remark 5.5, was visually inspected.
- The supporting paper's printed pages 1, 3, 20, and 21 were visually
  inspected for Theorems 1.2 and 1.6 and the separated-wavelet argument in
  Proposition 3.16.
- Packet SHA256:
  `d9064ec3a6dcdc8482178d7639e56490ec8a94e36c7a8b48a812df300e74f7a4`.
- Source PDF SHA256:
  `7e639ba457006e0e5552169d823945ab313b5f599636d1ad763ab353e19a0a47`.
- Supporting PDF SHA256:
  `1cc32ba261370504c9216411b3976806fec999c97cca37f638998198a266a07a`.
