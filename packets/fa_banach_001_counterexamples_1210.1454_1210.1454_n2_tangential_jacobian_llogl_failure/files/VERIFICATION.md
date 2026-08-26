# Verification report

Verdict: `candidate_counterexample_likely_valid` for equation (4.1) of
arXiv:1210.1454 as literally printed without excluding dimension `n=2`.

## Proof audit

- Take the smooth domain `Omega=B_2(0) subset R^2` and the fixed compact
  rectangle `K=[-1/4,1/4] times [-1/2,1/2]` in its interior.
- Put `A_k=exp(k^2)` and `ell_k=1/(k A_k)`.  The continuous ramp
  `u_k(x)=psi_k(x_1)`, with slope `A_k` on `(0,ell_k)` and constant value
  `1/k` thereafter, lies in `W^{1,1}(Omega)`.
- Since the ambient dimension is two, the printed tangential determinant is
  the scalar `det' nabla u_k=partial_1 u_k=A_k 1_{0<x_1<ell_k}`, hence it is
  nonnegative.
- The support-strip estimate gives `||nabla u_k||_1 <= 4 A_k ell_k=4/k`,
  while `||u_k||_1 <= 4 pi/k`.  Thus `u_k` converges strongly, and therefore
  weakly, to zero in `W^{1,1}`.
- For `gamma(s)=s log^+ s`, the rectangle has vertical height one, so
  `integral_K gamma(det' nabla u_k)=ell_k A_k log A_k=k`.  This diverges.
- The construction contradicts both a uniform bound on a bounded Sobolev
  family and the equation's literal per-index right-hand side with continuous
  `C`, because the Sobolev norms tend to zero while the left side diverges.

## Upgrade attempts and scope

1. The source's anisotropic normal-derivative mechanism was checked; it does
   not rescue the printed `n=2` endpoint because there is only one tangential
   derivative.
2. Truncation and reflection/Hardy approaches were tested for a direct
   higher-dimensional construction but did not preserve all required signs
   and scales.
3. Diagonal embeddings of the one-dimensional ramp into `n>=3` introduce
   additional derivative cost that cancels the entropy gain.
4. Separated-variable and shrinking-bubble constructions face the same
   determinant-versus-`W^{1,n-1}` scaling obstruction.
5. The successful endpoint example was strengthened from bounded weak
   convergence to strong convergence in `W^{1,1}`.

Accordingly, the packet claims only a counterexample to the unqualified
printed statement at `n=2`.  It does not settle the genuinely compensated
case `n>=3`; if that range was silently intended, the result is a scope
correction rather than a solution of the intended problem.

## Literature audit

- The exact statement and surrounding dimensional convention were checked in
  the official arXiv PDF, source page 12.  Example 4.1 immediately following
  the question explicitly begins with `n>=2`.
- Exact-phrase and keyword searches were run for the equation, tangential
  Jacobians, boundary null Lagrangians, and endpoint `L log L` estimates.
- The OpenAlex citation graph exposed twelve citing papers through 2020; none
  stated this endpoint counterexample or answered the higher-dimensional
  question.
- No later primary source directly resolving the printed question was found.
  Novelty confidence is therefore moderate, while the elementary endpoint
  calculation has high mathematical confidence.

## Reproducibility and visual checks

- `code/verify_scaling.py` checked `k=2,4,8,16,32`; its exact outputs confirm
  the decaying `W^{1,1}` upper bounds and entropy values equal to `k`.
- `latexmk` completed with resolved references and no overfull boxes,
  underfull boxes, undefined references, or final warnings.
- The final packet has three A4 pages.  Every page was rendered at high
  resolution and visually inspected after the final source edit.  The source
  crop, theorem, proof, equations, caveat, references, margins, and page
  numbers are readable and unclipped.
- PDF text extraction confirms the source equation, theorem statement,
  explicit construction, and the `n>=3` limitation.

## SHA-256

```text
5f3053784c795458e61701db068bdc82fbee4f8b27ce4b2ef5fb1593e6462457  solution_packet.pdf
f5fde0905efe5e2957add7f58960f050654468737f87b1ca5f403d5a181db4c4  source_paper.pdf
4d4aaba1d78d2286bfd36ed251ac12336171c75178000e73717f0bfc7d71bde5  figures/open_problem_crop.png
10c710e832ed9f99e1f7dfffa8ef4ca4ab4261e3a1efb95d0b07e7b714053797  code/verify_scaling.py
```

## Human-review recommendation

Check the source's intended dimensional quantifier independently and verify
that its notation `det'` indeed reduces to `partial_1 u` in dimension two.
Before dissemination, repeat the novelty search outside arXiv and OpenAlex.
