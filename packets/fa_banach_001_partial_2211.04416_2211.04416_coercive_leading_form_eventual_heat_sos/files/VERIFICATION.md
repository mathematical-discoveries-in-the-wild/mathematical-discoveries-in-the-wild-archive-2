# Verification report

Status: `candidate_partial_result_likely_valid_pending_human_review`

## Mathematical checks

- Decomposed `f=sum f_k` into homogeneous parts and checked directly that
  `t^{-d}(e^{t Delta}f)(sqrt(t)x)=sum_k t^{(k-2d)/2}e^Delta f_k(x)`.
- Homogenizing the last identity gives the displayed polynomial `Q_s` with
  `s=t^{-1/2}` and limit `e^{z^2 Delta}f_{2d}`.
- Checked the Gaussian identity using
  `E exp(sqrt(2)z G dot grad)=exp(z^2 Delta)`.
- The strict-Gram step is finite-dimensional: an interior SOS form has a
  positive-definite Gram matrix, whose Cholesky factors form a basis.
- The translation span is verified monomial by monomial: for
  `|alpha|+k=d`, choose `|beta|=k` and differentiate the translate of
  `x^(alpha+beta)` by the translation parameter `beta` times.
- Positive definiteness of the averaged Gram matrix follows because its
  generating coefficient vectors span the full degree-`d` form space.
- SOS membership is preserved under positive scalar multiplication,
  invertible linear scaling, homogenization, and dehomogenization.
- The proof is analytic and has no numerical dependency.

## Source and novelty checks

- Open Problem 5.1 was checked in arXiv:2211.04416, PDF page 26.
- Cheap run indexes and the parsed source corpus were searched for the arXiv
  id, title, exact problem wording, and core heat/SOS keywords.
- A bounded web search through 13 August 2026 found no exact answer.  The
  later arXiv:2506.16321 cites the source but does not settle the problem.

## Rendering checks

- `main.tex` compiled with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -outdir=tmp main.tex`.
- The source crop contains the complete problem and its context at readable
  resolution.
- Every rendered packet page was inspected manually.

## Human-review focus

Please verify the coefficient powers in the homogenization formula and the
claim that polynomial translates of a basis of degree-`d` forms span the full
degree-`d` space after adjoining the homogenizing variable.

