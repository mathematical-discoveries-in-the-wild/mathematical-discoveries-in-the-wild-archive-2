# arXiv:2503.06217 — ZFC separable partition

Status: `candidate_counterexample` (full refutation of Conjecture 4.6), pending
expert review.

Source: Daniel L. Rodríguez-Vidanes and Juan Carlos Sampedro, *Isometric
classification of the L^p-spaces of infinite dimensional Lebesgue measure*,
arXiv:2503.06217 / Banach Journal of Mathematical Analysis 20 (2026), article
7, Conjecture 4.6 on printed page 19.

## Result

ZFC proves that the paper's infinite-dimensional Lebesgue measure space
admits a continuum-separable partition, which is stronger than a
continuum-separable envelope. Therefore the conjecture that some model of ZFC
has no such envelope is false.

Combining the partition with the source's Theorem 4.3 gives, without CH,

`L^p(mu) = ell^p(c, L^p[0,1])`

isometrically for every `1 <= p < infinity`.

## Mechanism

The source already constructs `c` finite measure-one rectangles with pairwise
null intersections. Extend them by Zorn's lemma to a maximal family of finite
positive measurable sets with pairwise null intersections. For a fixed
finite-measure set `E`, only countably many family members meet `E` in
positive measure. If their intersections did not exhaust the measure of `E`,
the measurable positive remainder could be added to the family, contradicting
maximality. This is exactly the source's separable-partition identity.

The family has cardinal at least `c` by construction and at most `c` because
the ambient Borel sigma-algebra is countably generated. Every member is
separable by source Lemma 2.3.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: current arXiv source PDF.
- `figures/open_problem_crop.png`: Conjecture 4.6 and its stated consequence.
- `verification.md`: proof and novelty audit.
- `evidence_sources/README.md`: exact source provenance.
- `code/crop_source.py`: reproducible source-page crop.

Associated attempt:
`attempts/2503.06217_maximal_disjoint_family_zfc_attempt.md`.
