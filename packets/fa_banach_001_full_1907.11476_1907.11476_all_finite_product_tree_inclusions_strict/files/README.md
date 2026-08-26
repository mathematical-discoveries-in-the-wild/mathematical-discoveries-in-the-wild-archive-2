# Every nontrivial finite product-tree inclusion is strict

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Ignacio Vergara, “Positive definite radial kernels on homogeneous trees and
  products,” arXiv:1907.11476v2 (2019), later Journal of Operator Theory 84
  (2020), 435-460.
- Open question: equation (7) and the paragraph immediately following it,
  page 6 of the arXiv PDF.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

For `q' >= q` and `N' >= N`, the source obtains the inclusion

```text
R_+(T_{q'}^{N'}) subset R_+(T_q^N)
```

and asks which such inclusions are equalities. The packet gives the complete
answer:

- if `q = q' = infinity`, all the cones are equal, as already observed in the
  source;
- identical parameter pairs give the tautological equality;
- every other inclusion whose smaller-side degree `q` is finite is strict.

Thus no nontrivial equality occurs at finite degree.

## New witness

For a real number `t`, define

```text
phi_t(0) = 1,  phi_t(1) = t,  phi_t(n) = 0 for n >= 2.
```

On any graph `X`, its radial kernel is exactly `I + t A_X`, where `A_X` is
the adjacency operator. The packet proves

```text
||A_(T_q^N)|| = 2 N sqrt(q).
```

Consequently, for finite `q`,

```text
phi_t in R_+(T_q^N)  iff  |t| <= 1/(2 N sqrt(q)).
```

The threshold strictly decreases whenever `q` or `N` increases, so a value of
`t` between the two thresholds witnesses every proper inclusion. For an
infinite-degree factor, any nonzero `t` fails on a sufficiently large finite
star.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: page-6 source crop containing equation (7),
  the open question, and Corollary 1.7.
- `code/verify_sparse_witness.py`: optional arithmetic sanity checks; not part
  of the proof.
- `VERIFICATION.md`: adversarial proof audit and reviewer focus.
- `tmp/`: LaTeX and PDF-QA intermediates.

## Novelty check

A bounded search on 2026-08-09 covered the run's cheap indexes, the exact
source title and arXiv id, the displayed inclusion, the author, and combinations
of “positive definite radial kernels,” “products of homogeneous trees,”
“strict inclusion,” and “adjacency operator.” It found the source paper and
related background on radial Schur multipliers, but no later paper answering
equation (7) or using this sparse adjacency witness. Novelty confidence is
moderate pending specialist review.

## Human review focus

Please check:

- the equivalence between positivity of the sparse radial kernel and
  positivity of `I + t A_X`;
- the self-contained computation `||A_(T_q)|| = 2 sqrt(q)`;
- additivity of the product adjacency norm;
- the endpoint and infinite-degree cases;
- the bounded novelty search.
