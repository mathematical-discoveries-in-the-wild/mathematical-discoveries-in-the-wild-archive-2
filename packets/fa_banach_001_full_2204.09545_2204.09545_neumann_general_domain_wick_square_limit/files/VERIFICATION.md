# Verification record

## Mathematical checks

1. The partial-fraction/heat-kernel identity
   `1/[mu(a+epsilon mu)] = a^{-1} integral_0^infinity
   (1-exp(-as/epsilon)) exp(-mu s) ds` was checked algebraically.
2. The free diagonal heat kernel contributes
   `(8 pi)^{-1} log(1/epsilon)` because the covariance has the additional
   factor `1/2`.
3. The Neumann boundary remainder is uniformly `L^2`: its collar majorant is
   the truncated function `min(log(1/epsilon),1+|log d(x)|)`, whose square is
   uniformly integrable in the normal coordinate.  The lower-order
   `O(s^{-1/2})` heat-parametrix remainder is integrable in heat time and
   contributes only a uniform constant.
4. The off-diagonal covariance and Bessel Green kernels are bounded by
   `C(1+|log |x-y||)`.  Their product in the Wick variance is dominated by a
   logarithmic cube, integrable in two dimensions.
5. In the eigenbasis, all coefficients in the Wick-variance sum are
   nonnegative.  Replacing nonstationary variances by stationary ones is
   therefore legitimate without a pointwise kernel comparison.
6. The transient mean is bounded by
   `C sigma_epsilon^2(1+|log t|)`, which lies in every finite time `L^p`.
7. Vector-valued second-chaos hypercontractivity supplies every finite
   probability moment needed by the source's residual theorem.

The verifier computes the average stationary covariance on the unit square
from Neumann eigenvalues and confirms convergence of the logarithmic
coefficient to `1/(8 pi)`.  On the four smallest cutoffs tested, fitting and
thereby removing the finite Green-trace offset gives slope `0.0407347841`,
within `2.38%` of `1/(8 pi) = 0.0397887358`; the built-in threshold passes.

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_square_spectral_constant.py
```

The computation is a normalization sanity check only.  The heat-kernel and
Wick arguments in the packet are the proof.

## Literature and novelty checks

- Source: Dirk Blömker and Jonas M. Tölle, *Singular limits for stochastic
  equations*, arXiv:2204.09545, Section 6, PDF page 18.
- The standard boundary-locality input is Liangpan Li and Alexander
  Strohmaier, *Heat kernel estimates for general boundary problems*, Journal
  of Spectral Theory 6 (2016), 903--919, arXiv:1604.00784.
- The run registry and local full sources were searched for the source id,
  title, `Neumann`, `general domain`, `stochastic convolution`, and `Wick
  square`.
- A bounded web search through 2026-08-13 used the exact source phrase and
  close variants involving the CH/AC homotopy.  It found no later explicit
  resolution.  This is not an exhaustive priority determination.
- Mathematical confidence is high subject to specialist confirmation of the
  quoted Neumann heat-kernel boundary estimate; novelty confidence is
  moderate.

## Artifact and PDF checks

- The source PDF was downloaded from arXiv and archived locally.
- Source PDF page 18 was rendered at 180 dpi; the full-width crop includes the
  complete open statement and surrounding stochastic-convolution setup.
- The solution packet was compiled with all build artifacts under
  `tmp/build/`; each page was rendered and visually inspected.
- The final LaTeX log was checked for undefined references, missing
  citations, overfull boxes, and fatal warnings.

## Human review recommendation

Likely valid as a full solution of the smooth general-domain Neumann
stochastic-square estimate.  Review first Lemma 1's uniform `L^2` boundary
remainder and then the identity turning the Wick variance into
`integral G_1 Q_epsilon^2`; all later estimates are short consequences.
