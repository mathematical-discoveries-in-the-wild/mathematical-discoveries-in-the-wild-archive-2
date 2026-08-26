# Ordinary-norm multiplier distance for finite Pick spaces

Status: `candidate_substantial_partial_likely_valid`

Remark 4.3 of arXiv:2011.06578 asks whether the paper's RKHS/multiplier
comparison survives when ordinary algebra norms replace cb norms.

This packet proves the full qualitative replacement for finite sets.  For a
fixed finite `X` and any equal-cardinality sequence `Y_k`, ordinary algebra
distortion tending to one is equivalent to:

- automorphism-invariant geometric convergence;
- RKHS Banach--Mazur convergence; and
- completely bounded multiplier convergence.

It also proves the existence of a local ordinary-to-cb/geometric modulus.
The result is classified conservatively as substantial partial because it
does not recover the source's explicit power-type numerical inequalities.

Files:

- `solution_packet.pdf` -- expert-facing theorem and proof
- `source_paper.pdf` -- arXiv:2011.06578v3
- `main.tex` -- packet source
- `figures/open_question.png` -- source Remark 4.3
- `verification.md` -- mathematical and artifact audit

Attempt:
`runs/fa_banach_001/attempts/2011.06578_operator_norm_multiplier_distance_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/2011.06578_operator_norm_qualitative_equivalence.json`
