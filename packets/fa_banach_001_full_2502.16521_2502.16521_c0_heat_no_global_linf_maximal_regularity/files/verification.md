# Verification report

Status: `candidate_full_likely_valid`

## Exact target

- Source: arXiv:2502.16521v1, Remark 3.4(c), PDF page 40.
- Question: does the part of `-Delta` in
  `(C_0(R^n),D(-Delta))_{theta,infinity}` have global
  `L^infinity`-maximal regularity?
- Answer proved: no, for all `n>=1` and `0<theta<1`.

## Proof audit

1. The real interpolation norm is equivalently
   `||f||_infinity + sup_s s^{1-theta}||calA H_s f||_infinity`.
2. If the non-densely defined part `A` had maximal regularity, then its part
   `A_0` on `Y=closure(D(A))` would inherit it. A strong solution with a
   `Y`-valued force is `Y`-valued, its derivative is `Y`-valued almost
   everywhere, and hence so is `Au`.
3. The restricted heat semigroup on `Y` is bounded analytic and strongly
   continuous, so the necessity direction of Kalton--Portal applies.
4. For a fixed smooth bump, heat scaling and Gaussian derivative estimates
   give `F_m(u)<=C min(1,u^{-m-n/2})`, `m=0,1,2`.
5. With radii `R_j=2^j`, squared scales `r_j=4^j`, and
   `x_N=sum_j phi(x/R_j)`, one has `||x_N||>=x_N(0)=N`.
6. The base part of `tAH_t x_N` is controlled by the uniformly summable
   dyadic profile `min(u,u^{-n/2})`.
7. The homogeneous part is controlled by
   `min(u^{2-theta},u^{-n/2-theta})`, again uniformly summable over scales.
8. For each fixed `N`, the heat orbit `H_t x_N` tends to zero in the thermic
   norm. The homogeneous term is bounded scale-by-scale by
   `C R_j^n t^{-theta-n/2}` for large `t`.
9. Kalton--Portal would bound `N` independently of `N`, a contradiction.

## Source evidence

`figures/source_question_page.png` was rendered from page 40 of the official
arXiv PDF and contains the exact open question.

## Novelty audit

The run's cheap indexes and parsed corpus were searched for the arXiv id,
the exact question, the `C_0(R^n)` interpolation space, and global
`L^infinity` maximal regularity. Exact-title and exact-question searches
through 11 August 2026 found the source but no later primary-source answer.
Novelty confidence is moderate because an unindexed antecedent remains
possible.

## Artifact audit

The packet is compiled from `main.tex` with references resolved. The PDF log
is checked for missing references, overfull boxes, and other layout warnings.
Every rendered page is visually inspected. The source-page image is rendered
from the official PDF rather than reconstructed.

## Reviewer focus

Check the inheritance lemma on `closure(D(A))`, the squared-scale powers in
the homogeneous estimate, and the optimization in the large-time thermic
bound. No computation or numerical evidence is used.
