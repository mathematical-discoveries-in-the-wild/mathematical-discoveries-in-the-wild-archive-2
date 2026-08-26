# arXiv:1708.09635 — nilpotents for the explicit lacunary weight

Status: candidate full result, likely valid.

## Source question

For White's explicit weight
`omega(n)=exp(|n|_{S_0})` on `Z`, with
`S_0={2^{i^2}:i>=0}`, does the radical of
`l1(Z,omega)**` contain nilpotent elements of arbitrarily high index?

## Result

Yes.  For every integer `m>=2`, the packet constructs a weak-star cluster
point `Phi_m` of normalized point masses whose nilpotency index is exactly
`m`.  More strongly, the principal left ideal `A** Box Phi_m` has
nilpotency index exactly `m`, hence lies in the Jacobson radical.

The construction uses sparse digits in the mixed-radix chain
`q_i=2^{i^2}`, `R_i=q_{i+1}/q_i`.  A digit is chosen just above
`R_i/(2m)`.  Fewer than `m` copies remain strictly balanced, so their word
lengths add.  Exactly `m` copies carry at every shared digit and save at
least one unit of word length per digit.  The resulting uniform exponential
decay is strong enough to annihilate products of `m` arbitrary left
multiples in the first Arens product.

## Files

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: local copy of arXiv:1708.09635.
- `figures/open_problem_crop.png`: source question on page 2.
- `code/verify_mixed_radix.py`: independent finite MILP and local-inequality
  checks.
- `code/verification_output.txt`: saved verifier output.
- `VERIFIER_REPORT.md`: proof and artifact verification summary.

## Novelty status

Exact phrase/title searches, the run indexes, the author's publication list,
and the 2026 sequel arXiv:2602.02764 were checked through 2026-08-17.  No
prior resolution of this exact question was found.  Novelty is plausible,
not certified.

## Human review recommendation

Prioritize (1) the strict-balanced mixed-radix lemma, especially the local
normalization inequality; and (2) the claim that the uniform finite-stage
norm estimate survives every nested limit defining a product of arbitrary
left multiples.  Both points are proved explicitly in the packet.
