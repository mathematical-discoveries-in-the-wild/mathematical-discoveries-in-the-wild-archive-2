# Literature-implied answer: all massive integer-spin field strengths

status: literature_implied_answer (full conjectured scope)

source: Joseph C. Várilly and José M. Gracia-Bondía, *Stora's fine notion of
divergent amplitudes*, arXiv:1605.00237.

supporting theorem: Jens Mund and Erichardson T. de Oliveira,
*String-localized free vector and tensor potentials for massive particles
with any spin: I. Bosons*, arXiv:1609.01667, Lemma 14.

packet: `runs/fa_banach_001/solutions/literature_implied_answers/1605.00237_all_spin_massive_field_strength_extension/`

ledger: `runs/fa_banach_001/ledger/results/1605.00237_all_spin_massive_field_strength_extension.json`

## Identification

The source conjectures on PDF page 9 that its fine ultraviolet extension
result for massive spins 1 and 2 extends to all massive field strengths.
Lemma 14 of arXiv:1609.01667 proves on PDF page 28 that, for every massive
integer spin `s`, the point-local field-strength two-point function has a
homogeneous polynomial numerator of degree `2s`.

This is the missing input for the source paper's own NST criterion.  Acting
with such a degree-`2s` numerator on the scalar propagator gives a leading
term `H_{2s}(x)/(x^2-i0)^(2s+1)` with harmonic numerator.  The criterion's
strict inequality becomes `2s > 2s-2`; the source's massive
associate-homogeneity construction then extends the remaining mass terms.
Consequently the later lemma implies the conjecture for every positive
integer spin.

## Provenance and scope

The supporting authors cite the source paper in their discussion of massive
associate homogeneity, but they do not explicitly say that Lemma 14 resolves
the conjecture.  The connection is agent-identified, hence this packet is in
`literature_implied_answers/` rather than `literature_already_answered/`.

The identification covers the complete family named in the conjecture.  It
does not address interacting composite fields or higher time-ordered
products.

## Files

- `main.tex`: compact status and implication note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1605.00237.
- `supporting_paper_1609.01667.pdf`: decisive later theorem.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

