# All-dimensional upper-triangular completion by recursive defect matching

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Nikola Sarajlija and Dragan S. Djordjević, “Completion problem of upper
  triangular 3x3 operator matrices on arbitrary Banach spaces,”
  arXiv:2202.04960v4 (2025).
- Open question: Section 3, PDF page 10.
- Local source: `source_paper.pdf`.
- Source evidence: `figures/open_problem_crop.png`.

## Claimed contribution

The packet gives a necessary-and-sufficient invertible-completion criterion
for every finite matrix size `n` and arbitrary Banach spaces, assuming only
that the interior diagonal operators are inner regular.

After splitting every regular diagonal into its invertible range part and its
kernel/cokernel defects, Schur elimination shows that completion is equivalent
to an invertible upper-triangular map

```text
N(D_2) + ... + N(D_n)
    -> coker(D_1) + ... + coker(D_{n-1}).
```

Existence of that triangular isomorphism is characterized recursively: split
a left-invertible first diagonal block and a right-invertible last diagonal
block, pass to the two residual quotients, and repeat with one fewer row and
column. This terminates after finitely many steps.

For `n=3`, the recursion is exactly condition 1(c) of the source’s Theorem
2.1. The packet therefore also proves that the source’s condition 1 is
necessary as well as sufficient for condition 2.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: complete higher-dimensional question.
- `code/verify_recursive_completion.py`: finite-matrix defect-recursion and
  Schur checks; not part of the proof.
- `verification.md`: commands, results, and expert review priorities.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Literature and novelty check

A bounded local-index, full-source, and web search on 17 August 2026 covered
arXiv:2108.12153, 2110.07387, 2112.02350, and 2202.04960, plus exact-title and
core completion queries. The cited all-n theorem in arXiv:2108.12153 gives a
stronger adjacent-defect-isomorphism sufficient condition and a weaker
Hilbert-space necessity condition. The other located works address spectral
stability or Fredholm/Weyl completion. No exact recursive Banach criterion or
the 3x3 necessity upgrade was found. Novelty confidence is moderate pending a
specialist search of block-operator monographs.

## Human review focus

Please check:

- strict upper-triangularity of the defect Schur complement;
- the recursive Gaussian peeling lemma and quotient identifications;
- the comparison with condition 1(c) in source Theorem 2.1.
