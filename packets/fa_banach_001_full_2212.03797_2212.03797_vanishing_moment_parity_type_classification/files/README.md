# Parity classification for the vanishing-moment type inequality

Status: `candidate full solution likely valid`

Source: Kristin Kirchner and Christoph Schwab, *Monte Carlo convergence rates
for kth moments in Banach spaces*, arXiv:2212.03797; Journal of Functional
Analysis 286 (2024), Article 110218. The target is the necessity question in
Remark 3.18, pages 14--15, concerning inequality (3.18).

## Result

Let (E) be a real Banach space, (1\le p\le2), (q\ge p), and (k\ge2).
Consider the property that a uniform constant (C) makes

\[
 \left\|\sum_{j=1}^M\eta_j^{\otimes k}\right\|_
 {L_q(\Omega;\otimes_{\varepsilon_s}^{k,s}E)}
 \le C\left(\sum_{j=1}^M
 \|\eta_j\|_{L_{kq}(\Omega;E)}^{kp}\right)^{1/p}
\]

hold for every finite independent family with
\(\mathbb E[\eta_j^{\otimes k}]=0\).

- If (k) is odd, this property is equivalent to (E) having Rademacher
  type (p).
- If (k) is even, every admissible random variable is zero almost surely.
  The property is therefore vacuous for every real Banach space, and
  (E=\ell_1) gives a counterexample to necessity for every (p>1).

This completely answers the type-necessity question, with an exact parity
dichotomy. It does not claim to settle the separate sharpness problem for the
i.i.d. Monte Carlo convergence rate in Theorem 3.16.

## Proof Intuition

Even orders collapse because scalar evaluations of a zero tensor moment are
expectations of nonnegative even powers. For odd orders, Rademacher signs make
every deterministic pure tensor an admissible zero-moment random tensor.
The missing linear information is recovered by placing (x_j) in a
codimension-one hyperplane, adjoining a fixed transverse vector, and extracting
the coefficient linear in (x_j) from a degree-(k) pure-power curve. The
scaling \(\|x_j\|^{1/k}\) makes the tensor inequality reproduce exactly the
(p)-power sum required for Rademacher type.

## Verification

- `main.tex` contains the complete theorem and proof.
- `solution_packet.pdf` is the rendered review packet.
- `source_paper.pdf` is the original arXiv source PDF.
- `figures/open_problem_page14_crop.png` and
  `figures/open_problem_page15_crop.png` reproduce Corollary 3.17 and the
  complete two-page Remark 3.18.
- `code/verify_interpolation.py` checks the exact rational coefficient
  extraction for orders (1\le k\le20). This only verifies the algebraic
  interpolation identity; the Banach-space proof is analytic and does not
  depend on computation.
- `VERIFICATION.md` records the adversarial proof audit.

## Novelty and scope

The bounded search checked the run indexes; the current arXiv and published
versions of arXiv:2212.03797; exact searches for “vanishing kth moment,”
“Rademacher type,” “injective tensor,” and the wording of Remark 3.18; and the
related 2026 follow-up arXiv:2605.24620. No source recording this parity
classification or polarization argument was found. This is not a novelty
guarantee.

Human review recommendation: **send as a likely-valid full answer to the
necessity question**. Check the tensor symmetrization normalization, the
interpolation coefficient identity, and the hyperplane norming-functional
bound.

