# The `Phi_1 \ Phi_2` negative-squares conjecture follows from Sasvari's classification

Status: **literature_implied_answer (full conjecture; candidate likely valid)**.

Golinskii, Malamud, and Oridoroga conjecture on page 3 of arXiv:1502.07179
that every `f in Phi_1 \ Phi_2` has `kappa_2^-(f)=+infinity`.

The conjecture follows from Theorem 3.2 of Zoltan Sasvari, *On bounded
functions with a finite number of negative squares*, Monatshefte fuer
Mathematik 99 (1985), 223--234, DOI `10.1007/BF01295156`. That theorem says
that a bounded continuous Hermitian function on an LCA group with exactly
`k` negative squares is the Fourier transform of a finite signed measure whose
negative part is concentrated at exactly `k` characters.

Applied to the radial function `g(x)=f(|x|)` on `R^2`, rotation invariance
forces the finite negative spectral support to be `{0}`. The restriction of
`g` to a line is positive definite because `f in Phi_1`; hence the projection
of the signed spectral measure onto that line is positive. But its atom at
zero is strictly negative: the positive spectral part gives zero mass to the
perpendicular line by rotation invariance, while the negative atom at the
origin survives projection. This contradiction proves the conjecture.

The implication is identified here rather than explicitly stated by Sasvari
(whose theorem predates the conjecture) or by the source authors. It is
therefore stored as a literature-implied answer, not as a newly discovered
full solution.

Artifacts:

- `solution_packet.pdf`: compact statement and complete implication proof.
- `source_paper.pdf`: arXiv:1502.07179; the conjecture is on PDF page 3.
- `supporting_primary.pdf`: Sasvari's 1985 article; Theorem 3.2 is on journal
  pages 229--231 (PDF pages 7--9).
- `supporting_restatement_1989.pdf`: Sasvari's 1989 Acta paper; its
  introduction restates the bounded classification on journal page 319.
- `verification.md`: independent dependency and scope audit.
- Attempt history:
  `runs/fa_banach_001/attempts/1502.07179_phi1_phi2_finite_negative_squares/`.

Ledger:
`runs/fa_banach_001/ledger/results/1502.07179_phi1_phi2_infinite_negative_squares_sasvari.json`.

