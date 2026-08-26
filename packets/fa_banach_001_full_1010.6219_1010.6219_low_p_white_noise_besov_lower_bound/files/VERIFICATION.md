# Verification report

Verdict: `candidate_full_likely_valid`

## Formal audit

1. **Pointwise law.** For the canonical white noise and
   `Z_j=2^{-jd/2}W_j`, each `Z_j(x)` is a centered complex Gaussian of variance
   `v_j=2^{-jd} sum_k |varphi_j(k)|^2`, independent of `x`.
2. **Uniform nondegeneracy.** The source assumes `varphi_j=1` on the annulus
   `2^{j-1/2} < |k| <= 2^{j+1/2}`. Standard lattice counting gives at least
   `a_d 2^{jd}` points there for all large `j`. Support inside
   `|k| <= 2^{j+1}` gives at most `b_d 2^{jd}` contributing points. Hence
   `0<a_d<=v_j<=b_d<infinity`.
3. **First moment.** With `m_p=E|gamma|^p` and torus volume `V`, Fubini and
   Gaussian scaling give `E Y_j=V m_p v_j^{p/2}>=A_{p,d}>0`.
4. **Second moment.** Cauchy--Schwarz gives
   `E(|Z_j(x)|^p|Z_j(y)|^p)<=m_{2p}b_d^p`. Double integration yields the
   uniform bound `E Y_j^2<=B_{p,d}<infinity`. No independence across spatial
   points is assumed.
5. **Positive probability.** Paley--Zygmund at one half of the mean gives
   `P(Y_j>=A/2)>=A^2/(4B)>0`, uniformly for all large `j`.
6. **Scale independence.** `varphi_j` is supported in
   `{2^{j-1}<=|k|<=2^{j+1}}`; the supports for `j=3n` are disjoint. Therefore
   the relevant events are independent.
7. **Almost-sure conclusion.** Their probabilities have divergent sum, so
   the second Borel--Cantelli lemma gives infinitely many successful scales.
   The supremum defining the critical Besov norm is consequently at least
   `(A/2)^{1/p}` almost surely.
8. **Generality.** The source's Lemma 3.2 and its finite-dimensional/Riemann-
   sum argument show that the Besov norm of an arbitrary Gaussian white noise
   has the same law as that of the canonical Fourier-series model.

All steps hold for the endpoint `p=1`. The proof uses only finite Gaussian
moments, Fubini/Tonelli, Cauchy--Schwarz, Paley--Zygmund, elementary lattice
counting, and Borel--Cantelli.

## Source and build verification

The local source archive already contained the complete 2010 arXiv TeX file.
It compiled successfully to the 14-page `source_paper.pdf`; the source theorem
and open remark occur together on page 7. The evidence crop was generated
from that page and visually inspected.

The solution packet was compiled with `latexmk`, checked for undefined
references and serious layout warnings, rendered page by page, and visually
inspected. No numerical experiment is used: the proof is exact and has no
computational dependency.

## Scope and novelty audit

- The theorem closes exactly Remark 3.5(i), including `p=1`.
- It uses the Littlewood--Paley cutoff fixed by the source. Equivalent Besov
  norms preserve positivity of a deterministic lower bound.
- It does not claim a sharp value of the constant.
- Bounded index and web/arXiv searches on 2026-08-17 found no explicit later
  resolution. This is not an exhaustive literature review.
