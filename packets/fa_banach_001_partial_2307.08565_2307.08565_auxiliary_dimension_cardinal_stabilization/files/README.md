# Auxiliary-dimension cardinal stabilization

Status: `candidate_substantial_partial_likely_valid`

Source: Raj Dahya, *Interpolation and non-dilatable families of C0-semigroups*, arXiv:2307.08565 (2023; revised 2024), Problem 2.8 on PDF page 12.

This packet proves that the universal auxiliary-dimension invariant in Problem 2.8 depends on the index set `I` only through

`min(|I|, |B(H)|)`.

Consequently it stabilizes once `|I| >= |B(H)|`. If `delta=dim H`, then

`|B(H)| = 2^max(delta,aleph_0)`,

and the source estimate improves to

`aleph_0 <= kappa_H(I) <= max(aleph_0,min(|I|,2^max(delta,aleph_0)))`.

In particular, whenever `|I|>|B(H)|`, the paper's auxiliary space of dimension `|I|` is provably nonoptimal. For separable nonzero `H`, the threshold is the continuum. The exact stabilized value, and the exact value for uncountable `I` below the threshold, remain open.

## Files

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Problem 2.8 and the authors' optimality question.
- `code/crop_source.py`: reproducible crop script.
- `tmp/`: rendering and LaTeX intermediates.

## Verification and review recommendation

The proof is purely set-theoretic/cardinal and uses the source paper's simultaneous interpolation theorem. Human review should focus on the two reindexing inequalities proving exact stabilization and on whether “smallest dimension” is interpreted uniformly over all families, as in Problem 2.8. A bounded index and web/arXiv search through 2026-08-17 found no later resolution or exact match; novelty confidence is provisional.

