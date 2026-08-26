# Q6 Lower-Half Semilocalizability Resolution

Source: Thierry De Pauw, *Undecidably semilocalizable metric measure spaces*,
arXiv:1909.10190v2, Question 6 (Section 11.6, PDF page 30).

Status: likely valid strong partial resolution, pending human review. The
packet answers Q6 for every `0<d<1/2`. The source already handles `d=1/2`, so
the whole range `0<d<=1/2` is settled. The range `1/2<d<1` remains open.

## Main result

For every `0<d<1/2`, the proposition

```text
([0,1], A_{H^d}, H^d) is semilocalizable
```

is undecidable in ZFC in the standard relative-consistency sense:

- CH implies semilocalizability by De Pauw's general theorem.
- `non(N_L1)<cov(N_L1)` implies nonsemilocalizability by the new construction.

## Construction

Put `r=2^(-1/d)`. Because `d<1/2`, one has `r<1/4`. Let `C_d` be the
two-branch ratio-`r` Cantor set, and fit four separated ratio-`r` pieces into
`[0,1]`, with attractor `K_d`. Pair the two binary addresses of
`C_d x C_d` digit by digit to obtain a bi-Lipschitz bijection

```text
Phi:C_d x C_d -> K_d.
```

Images of vertical and horizontal leaves have finite positive `H^d` measure,
meet in singletons, and satisfy the two null-incidence hypotheses in De
Pauw's vertical-horizontal theorem. Thus `K_d` is consistently not
semilocalizable.

The Caratheodory sigma-algebra and local-null ideal on `K_d` are the traces of
the corresponding interval objects. Therefore the quotient Boolean algebra
for `K_d` is the principal ideal below `[K_d]` in the interval quotient.
Order completeness passes to principal ideals, so nonlocalizability of `K_d`
forces nonlocalizability of `[0,1]`.

## Upper-half barrier

For `d>1/2`, the four equal-ratio pieces do not fit in an interval. Equivalently,
`dim_H(C_d x C_d)=2d>1`, so the product has no bi-Lipschitz copy in the real
line. This blocks this proof route only; it is not evidence that Q6 is false
above `1/2`.

## Files

- `main.tex`: self-contained statement and proof, modulo the two explicitly
  quoted source-paper inputs.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:1909.10190v2.
- `figures/open_problem_crop.png`: genuine source crop containing Q6.
- `verification.md`: adversarial audit.
- `tmp/`: LaTeX and page-rendering intermediates.

## Novelty check

A bounded run-index, exact-title, arXiv, web, and publication-record search
found no later paper explicitly answering Q6. The adjacent later paper
arXiv:2105.11331 concerns localizable locally determined measurable spaces
with negligibles but did not provide an answer to Q6 in the inspected
metadata/search evidence. Novelty remains provisional pending specialist
review.

## Human review recommendation

Preserve as a strong partial-resolution candidate. Review especially the
first-different-digit bi-Lipschitz bounds, the local-null leaf argument, and
the trace/principal-ideal passage. If those checks are confirmed, the result
is a clean new affirmative theorem for the entire lower half of Q6.
