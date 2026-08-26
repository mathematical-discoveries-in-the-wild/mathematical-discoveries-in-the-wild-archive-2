# Literature answer: isotropicity is unnecessary for decomposition

- **Source:** P. Bonicatto, E. Pasqualetto, T. Rajala,
  *Indecomposable sets of finite perimeter in doubling metric measure spaces*,
  arXiv:1907.10869; Calc. Var. PDE 59 (2020), 63.
- **Answer:** P. Lahti, *A note on indecomposable sets of finite perimeter*,
  arXiv:2103.14459; Adv. Calc. Var. 16 (2023), 559--570.
- **Model:** GPT5.6
- **Disposition:** `literature_already_answered`.

## Exact match

The source asks whether isotropicity is needed for its decomposition theorem.
Lahti's abstract says the condition can be removed, and Theorem 1.1 states the
same conclusion for every PI space: a unique finite or countable
perimeter-additive partition into positive-measure indecomposable pieces,
with the pieces maximal among indecomposable finite-perimeter subsets.

The later proof replaces isotropic perimeter-density arguments by hereditary
perimeter-additivity and localization lemmas derived directly from BV lattice
identities and weak upper gradients.

## Files

- `source_1907.10869.tex`: locally cached official arXiv source.
- `supporting_source_2103.14459.tex`: official arXiv source downloaded and
  inspected for the exact theorem.
- `source_paper.pdf` and `supporting_paper_2103.14459.pdf`: local compilations
  of those exact source files; the environment blocked direct PDF download.
- `main.tex` and `solution_packet.pdf`: compact question-to-theorem status
  note.
- `verification_report.md`: source, theorem-label, build, and visual checks.

## Scope boundary

This is a complete literature answer to the decomposition question, not a new
proof. It does not remove isotropicity from every result in arXiv:1907.10869;
Lahti explicitly preserves that distinction for results on simple sets.

