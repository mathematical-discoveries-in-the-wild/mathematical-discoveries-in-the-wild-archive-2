# A rectangle counterexample to weighted log-submodularity

Status: `candidate_counterexample_likely_valid`

Source: Matthieu Fradelizi, Dylan Langharst, Mokshay Madiman, and Artem
Zvavitch, *Weighted Brunn-Minkowski Theory II: Inequalities for Mixed Measures
and Applications*, arXiv:2402.10314v3 (2026).

Target: the conjecture following equation (44), page 27 of the current arXiv
PDF.

## Result

The conjecture is false for a full-dimensional log-concave probability measure
on `R^2` and full-dimensional symmetric zonotopes.

Put `delta=1/10` and parameterize a parallelogram by

```text
(x,y)=(u+v,u-v),  |u|<=4, |v|<=delta.
```

Let `mu` be normalized area measure on this parallelogram. Its density is a
constant times the indicator of a convex body, so `mu` is log-concave. Choose

```text
A=[-1,1] x [-1,1],
B=[-1,1] x [-delta,delta],
C=[-delta,delta] x [-1,1].
```

These are origin-symmetric rectangles and hence full-dimensional zonotopes.
Exact area calculations give

```text
mu(A)       = 19/80,
mu(A+B)     = 11/40,
mu(A+C)     = 11/40,
mu(A+B+C)   = 41/80.
```

Consequently,

```text
mu(A) mu(A+B+C) - mu(A+B) mu(A+C) = 59/1280 > 0,
```

which is the strict reverse of the conjectured inequality.

## Scope

This refutes the source's assertion for **any** log-concave measure. It does
not address narrower variants imposing radial symmetry, Gaussianity, or
Lebesgue measure. The example is already absolutely continuous and supported
on a two-dimensional convex body. By convolving with a sufficiently small
nondegenerate Gaussian, the strict counterexample also persists for a smooth,
everywhere-positive log-concave density.

## Files

- `solution_packet.pdf`: review-ready statement, exact proof, limitations, and
  novelty record.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: official current arXiv PDF.
- `figures/open_problem_crop.png`: rendered page-27 crop containing equation
  (44) and the conjecture.
- `VERIFICATION.md`: quantifier and computation audit.
- `code/check_exact_measures.py`: exact rational arithmetic check.

## Novelty and review

The local run indexes were searched for arXiv:2402.10314, weighted
Brunn-Minkowski theory, log-submodularity, symmetric zonoids, and log-concave
measures. Bounded web searches on 2026-08-11 used the exact source title with
`symmetric zonoids` and `counterexample`, the arXiv id with
`log-submodularity conjecture`, and the authors with the same terms. They found
the current v3 source and adjacent results for Lebesgue volume, but no later
answer or this measure counterexample. Novelty remains subject to expert
review.

Human review should focus on the source quantifier "any log-concave measure"
and on the elementary area table. All three test sets have nonempty interior,
so the construction is independent of conventions allowing lower-dimensional
zonoids.
