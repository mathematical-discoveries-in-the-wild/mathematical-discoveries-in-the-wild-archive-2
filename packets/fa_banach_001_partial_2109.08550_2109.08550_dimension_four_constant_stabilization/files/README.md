# Three variables suffice for commuting row contractions on `C^4`

Status: `substantial_partial_result_likely_valid`.

This packet proves

```text
C_{d,4}=C_{3,4}  for every d>=3,
```

where `C_{d,n}` is the optimal constant in the row-contractive von Neumann
inequality for commuting `d`-tuples of `n x n` matrices.  Equivalently, the
dimension-four uniform constant is already attained with three variables.

## Source question

Michael Hartz, Stefan Richter, and Orr Moshe Shalit, *von Neumann's
inequality for row contractive matrix tuples*, Mathematische Zeitschrift 301
(2022), 3877-3894; arXiv:2109.08550.

Remark 4.8 on page 12 asks whether `C_{2,n}<C_{d,n}` for any `n>2`.
Dariusz Piekarz later proved `C_{d,3}=C_{2,3}` for every `d>=2`
(arXiv:2310.12908).  The packet treats the next matrix dimension.

## Main mechanism

- After moving one joint spectral point to zero by a ball automorphism,
  every tuple with multiple spectral points has a coordinate span of
  dimension at most three.
- A one-point-spectrum tuple has commuting nilpotent coordinates spanning at
  most four dimensions.
- If that span has dimension four, Schur maximality makes it an algebra, and
  an elementary centralizer argument proves that the algebra is square-zero.
- Square-zero row contractions obey the constant-one inequality: only the
  value and gradient of the test function survive, and a disk automorphism
  matches that first jet.

Thus every tuple either reduces unitarily to three variables or satisfies a
stronger constant-one estimate.

## Boundary

The original question remains open in matrix dimension four precisely at

```text
C_{2,4} ?= C_{3,4}.
```

The packet neither decides this comparison nor computes the constant.

## Files

- `main.tex` and `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source evidence from Remark 4.8, page 12.
- `code/verify_dimension_four_nilpotent_algebra.py`: exact finite-field
  stress test of the maximal nilpotent lemma.
- `verification.md`: analytic checklist, verifier output, novelty boundary,
  and PDF QA.
