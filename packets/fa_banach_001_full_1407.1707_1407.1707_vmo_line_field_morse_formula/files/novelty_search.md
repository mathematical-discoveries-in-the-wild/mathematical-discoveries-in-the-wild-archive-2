# Bounded novelty and literature search

Search date: 2026-08-11.

## Sources checked

- The complete arXiv source of arXiv:1407.1707, especially the introduction,
  Sections 4--5, appendices, and bibliography.
- The run's `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv`.
- Exact and close web/arXiv searches for `VMO line field boundary`,
  `VMO line fields Morse`, `line field Morse formula boundary`,
  `Q-tensor relative Euler boundary`, and the exact source title with
  `line field`.
- OpenAlex's complete `cites:W2206196215` result for the published source DOI
  `10.1016/j.jfa.2015.09.005`.

## Findings

- No run-index duplicate was found.
- The source itself proves the two explicitly numbered questions, so those
  were treated as extraction false positives.  It does not prove the proposed
  line-field extension for surfaces with boundary.
- Exact-phrase searches returned the source paper and generic relative-Euler
  references, but no later paper stating or proving the VMO line-field Morse
  formula or its prescribed-boundary extension criterion.
- OpenAlex listed one citing work: Stuart Day and Arghir Zarnescu,
  *Sphere-valued harmonic maps with surface energy and the K13 problem*,
  DOI `10.1515/acv-2016-0033`.  Its topic and abstract do not concern the
  line-field boundary extension proposed here.

## Novelty assessment

No explicit later answer was located in this bounded search.  The continuous
relative-Euler backbone is classical; the candidate contribution is the
precise line-field boundary invariant, its exact Morse normalization, and the
VMO trace/extension theorem in the source's Q-tensor setting.  Novelty remains
subject to expert literature review because terminology for line fields,
cross fields, and projective tangent bundles varies substantially.
