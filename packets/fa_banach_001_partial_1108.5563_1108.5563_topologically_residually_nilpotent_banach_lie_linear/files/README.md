# Residually nilpotent Banach--Lie algebras are linear

**Status:** candidate substantial partial result, likely valid; human review
requested.

The source recalls Wojtynski's still-open question asking whether every
quasinilpotent Banach--Lie algebra admits a faithful continuous representation
on a Banach space. It proves the nilpotent case.

This packet proves a broader positive theorem: every Banach--Lie algebra
separated by continuous homomorphisms into nilpotent Banach--Lie algebras has a
faithful bounded representation. In particular, this holds whenever the
intersection of the closed lower-central series is zero.

The key quantitative observation is that the source's polynomial
representation of a nilpotent quotient strictly lowers homogeneous degree.
Weighting degree `m` by `R^m` makes its operator norm arbitrarily small. The
quotient representations can therefore be placed on one `ell_2` direct sum
with a uniform bound, while separation by the quotients preserves
faithfulness.

The theorem applies to genuinely nonnilpotent quasinilpotent algebras; an
explicit weighted-shift semidirect product is included. It does not show that
all quasinilpotent Banach--Lie algebras are topologically residually nilpotent,
so the full source problem remains open.

Files:

- `solution_packet.pdf`: review-ready partial-result packet.
- `main.tex`: complete LaTeX source.
- `source_paper.pdf`: original source paper.
- `figures/open_question_crop.png`: source PDF crop containing the question.
- `code/crop_open_question.py`: reproducible crop script.
- `tmp/`: LaTeX intermediates and rendered-page verification files.

Novelty confidence is moderate after bounded index, primary-source, and exact
phrase searches; the short argument may be folklore. Expert review should
focus on the degree-lowering renorming and the diagonal direct sum.
