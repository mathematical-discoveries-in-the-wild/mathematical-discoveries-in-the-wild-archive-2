# Finite-union closure for weak-mixing linear non-recurrence

Status: `candidate_partial_result_likely_valid`

Source: Sophie Grivaux, *Non-recurrence sets for weakly mixing linear
dynamical systems*, arXiv:1202.3114.

## Result

Finite unions of non-recurrence sets for weakly mixing linear Gaussian
systems are again non-recurrence sets for such a system. The proof uses the
finite Hilbert direct sum, product Gaussian measure, and the Cartesian product
of the positive-measure witness sets.

Consequently, if a strictly increasing sequence satisfies
`n_(k+r)/n_k -> infinity` for some fixed `r`, then `{n_k}` is non-recurrent
for a weakly mixing linear Gaussian system. Splitting indices modulo `r`
gives `r` superlacunary streams, and finite-union closure recombines them.
This strictly extends the source's adjacent-ratio hypothesis.

## Scope

The arbitrary lacunary, shifted-rigidity, and old Bohr-recurrence questions
remain open here. Countable products lose positive witness measure, and
ordinary rigidity does not provide the summable rate needed for exact
trimming.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem, corollary, and complete proofs.
- `VERIFICATION.md`: proof, literature, upgrade, and rendering checks.
