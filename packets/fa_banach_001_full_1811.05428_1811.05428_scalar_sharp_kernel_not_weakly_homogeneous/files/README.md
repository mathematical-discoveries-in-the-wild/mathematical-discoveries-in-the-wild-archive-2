# Scalar sharp kernel with a non-weakly-homogeneous multiplier

Status: `candidate_full_solution` (affirmative), pending expert review.

Source: Soumitra Ghara, *The orbit of a bounded operator under the Möbius
group modulo similarity equivalence*, arXiv:1811.05428 / Israel Journal of
Mathematics 238 (2020), Section 3, PDF page 8.

## Result

The packet answers the source's residual scalar-kernel question. Let

`g(z) = 1/(1-z)` and `H = H^2 direct-sum Cg`,

with the orthogonal direct-sum norm. Its scalar kernel is

`K(z,w) = 1/(1-z conjugate(w)) + 1/((1-z)(1-conjugate(w)))`.

Multiplication by `z` is bounded because `zg=g-1`. The kernel is sharp: for
every `w` in the disk, the eigenspace of `M_z^*` at `conjugate(w)` is exactly
the span of `K(.,w)`.

Nevertheless,

`point-spectrum(M_z^*) = disk union {1}`.

A nontrivial disk rotation moves the exceptional boundary eigenvalue from
`1` to another point of the unit circle. Since similarity of operators
implies similarity of their adjoints and preserves point spectrum, `M_z` is
not similar to all its rotations and is not weakly homogeneous.

## Novelty status

The four run indexes, the local arXiv corpus, exact-phrase web/arXiv searches,
the source's citation neighborhood, and searches for the specific
`H^2 direct-sum C/(1-z)` construction found no prior answer. The search did
find the author's thesis restating the question. Novelty therefore remains a
bounded-search assessment, not a guarantee.

## Files

- `solution_packet.pdf`: rendered theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: source paper containing the open question.
- `figures/open_problem_crop.png`: source-page evidence.
- `code/crop_source.py`: reproducible crop script.
- `verification.md`: proof and rendering audit.
- `tmp/`: build intermediates and rendered QA pages.

Ledger:
`runs/fa_banach_001/ledger/results/1811.05428_scalar_sharp_kernel_not_weakly_homogeneous.json`

