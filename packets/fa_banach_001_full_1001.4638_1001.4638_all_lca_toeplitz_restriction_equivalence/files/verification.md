# Verification report

Status: proof-dependency audit passed; candidate full result pending expert
review.

## Source audit

The published source PDF was checked at:

- page 26: statement of Theorem 7.5;
- pages 27–28: proof of Theorem 7.5;
- page 28: Remark 7.6(i), explicitly stating that the Euclidean/toral
  hypothesis is used only in `(iii) => (i)` through the Lebesgue density
  theorem;
- page 33: Problem 2.

Before the density-point invocation, the source proof derives

```text
E_f subset null P(Gamma(U,V)).
```

The new lemma replaces only the subsequent density-point paragraph.

## New-lemma audit

The following potential failure modes were checked directly:

1. `U` and `V` may have infinite Haar measure. Countable finite-measure
   exhaustions handle this and make every indicator tensor legitimate.
2. Pairwise almost-everywhere convergence would be too weak. The summable
   `L^1` error construction gives one subsequence converging almost everywhere
   for every exhaustion piece, producing a Cartesian product of conull sets.
3. The overlap must have positive Haar measure, not merely be nonempty.
   Positive integral against an `L^1` density implies positive Haar measure.
4. The source orientation is
   `P(1_A tensor 1_B)(s)=mu(A intersect (B+s))`; the proof uses `s=u-v`,
   giving exactly `mu(U_k intersect (V_l+u-v))`.
5. No use remains of balls, a metric, a doubling estimate, a group structure
   theorem, or a differentiation basis.

## Literature audit

Searches on August 9, 2026 covered the exact source title, theorem and problem
labels, core multiplier phrases, arXiv, and the authors’ later work. The
closest later paper, arXiv:1401.2620, was downloaded and text-searched. It
uses the 2011 paper but addresses closable multipliers on group C*- and von
Neumann algebras, not Problem 2’s restricted-rectangle theorem. No prior
answer was found.

## PDF QA

Completed on August 9, 2026:

- `latexmk` produced a five-page PDF with no warnings, undefined references,
  overfull boxes, or underfull boxes in the final log;
- all five pages were rendered at 150 DPI and inspected individually;
- both source crops are complete and readable at normal review zoom;
- equations, margins, page numbering, section transitions, and references are
  clean, with no clipping or overlap.
