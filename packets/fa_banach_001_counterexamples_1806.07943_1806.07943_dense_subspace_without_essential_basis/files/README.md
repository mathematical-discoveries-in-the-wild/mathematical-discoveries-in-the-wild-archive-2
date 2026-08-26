# Candidate counterexample: an incomplete separable normed space with no essential basis

Status: **candidate full counterexample, likely valid, needs expert review**

Source: Vinicius Coelho, Joilson Ribeiro, and Luciana Salgado, *A note on
Basis Problem in normed spaces*, arXiv:1806.07943 (current source dated 2024).
The two questions are Problems 1 and 2 on PDF pages 5--6.

## Result

Both source questions have a negative answer.

Let `B` be a separable Banach space without a Schauder basis, for example an
Enflo space. Choose a countable dense subset of `B` and let `X` be its
algebraic linear span with the inherited norm. Then:

- `X` is separable and dense in `B`;
- `X` is proper, because an infinite-dimensional Banach space cannot have
  countable Hamel dimension by the Baire category theorem;
- `X` is incomplete, and its completion is `B`.

If `X` had an essential Schauder basis, the source paper's Theorem A would
make the same sequence a Schauder basis of the completion `B`, a
contradiction. Thus `X` has no essential Schauder basis. Since an essential
unconditional basis is, by the source's Definition 8, first of all an
essential Schauder basis, `X` has no essential unconditional basis either.

## Files

- `solution_packet.pdf`: source screenshots, theorem, proof, verification,
  and novelty bounds.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/problem_1_crop.png`: source Problem 1.
- `figures/problem_2_crop.png`: source Problem 2.
- `VERIFICATION.md`: proof audit and reviewer checklist.

No computational code is included because the construction and obstruction
are purely structural.

## Human-review priority

Verify the use of Theorem A in the source: when an essential Schauder basis
spans all of `X`, item (ii) implies item (i), so it is a basis of the
completion of `X`. Then check that the source's Definition 8 explicitly makes
every essential unconditional basis an essential Schauder basis.

## Novelty status

A bounded search on 11 August 2026 covered the four run indexes, exact arXiv
id and title, exact problem phrases, the 2024 published version, and searches
combining dense subspaces, completions, Enflo spaces, and essential Schauder
bases. The current version still asks both problems and no explicit answer was
located. This is provisional novelty evidence, not an exhaustive originality
determination.
