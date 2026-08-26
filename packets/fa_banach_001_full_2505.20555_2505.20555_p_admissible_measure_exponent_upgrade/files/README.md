# Exponent Upgrade for All p-Admissible Measures

Result type: `full`

Status: candidate full resolution of the p-admissible-measure extension in
Remark 8.2, likely valid pending expert review.

Source paper:

- Behnam Esmayli and Riddhi Mishra, “On Removable Sets for Weighted Sobolev
  Functions,” arXiv:2505.20555v2 (2025); *Potential Analysis* 64, article 18
  (2026), DOI 10.1007/s11118-025-10270-9.
- General question: PDF page 14, Question 2.21.
- Exact measure-valued extension: PDF page 32, Remark 8.2.
- Local source: `source_paper.pdf`.
- Evidence crops: `figures/open_problem_crop.png` and
  `figures/measure_variant_crop.png`.

## Claimed contribution

The packet proves that absolute continuity is unnecessary in Proposition 8.1.
For every p-admissible Borel measure `mu` on Euclidean space, every
`1 <= p < s < infinity`, and every open `Omega`,

```text
u in H^{1,p}(Omega;mu),  u in L^s(Omega;mu),
and |grad u| in L^s(Omega;mu)
```

imply `u in H^{1,s}(Omega;mu)`, with the same Sobolev gradient.

The proof retains the source paper's discrete convolution and its gradient
bound.  It replaces the source's potentially circular `L^s`-Poincare step by
the doubling differentiation theorem and Hardy--Littlewood maximal bound:
the discrete averages converge pointwise and are dominated in `L^s` by the
maximal function.  Thus every step uses only the Borel measure, doubling, the
original `p`-Poincare inequality, and functional analysis.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: the original arXiv PDF.
- `figures/open_problem_crop.png`: Question 2.21 on PDF page 14.
- `figures/measure_variant_crop.png`: Proposition 8.1 and Remark 8.2 on PDF
  page 32.
- `verification.md`: adversarial proof audit and novelty bounds.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

The final journal version, published 10 December 2025, still states Remark
8.2 as unresolved.  Searches through 11 August 2026 used the exact wording of
Remark 8.2 and combinations of “p-admissible measure,” “H^{1,p},” “H^{1,s},”
and “discrete convolution.”  They found the source article and standard
background on p-admissible measures, but no later answer or this maximal-
function repair.  The run's cheap indexes contained no result for
arXiv:2505.20555.  Novelty confidence is moderate pending a specialist
citation search.

## Scope limitation

This resolves the exact extension proposed in Remark 8.2.  It does **not**
resolve Open Problem A.18 asking whether every p-admissible measure on
`R^n`, `n>=2`, is absolutely continuous with respect to Lebesgue measure.

## Human review focus

Please check:

- maximal domination and pointwise convergence of the off-center grid
  averages for a possibly singular doubling measure;
- the average-difference estimate and bounded-overlap integration;
- gradient identification after Mazur convexification;
- the local-to-global partition-of-unity lemma.

