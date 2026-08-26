# 2606.06675 - completely bounded multipliers form a dual Banach algebra

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: Mahmood Alaghmandan, Olof Giselsson, Ebrahim Samei, and Lyudmila Turowska, *Multipliers of Beurling-Fourier algebras*, arXiv:2606.06675v1.

## Result

The source proves that for every locally compact group `G` and weight inverse `omega`,

`M_cb A(G,omega) = (A(G,omega) hat_tensor_A C_r^*(G))^*`

completely isometrically. It says the authors believe this multiplier algebra is a dual Banach algebra, proving that only for amenable `G`.

This packet proves the statement for every locally compact group and every weight inverse covered by the source theorem. Multiplication is separately completely weak-star continuous for the source predual.

## Proof mechanism

Fix a completely bounded multiplier `psi`. On the balanced predual define

`S_psi [a tensor x] = [(psi a) tensor x]`.

This is well defined because the balanced relation

`ab tensor x - a tensor b.x`

is sent to

`(psi a)b tensor x - (psi a) tensor b.x`,

which is another balanced relation. Under the source pairing,

`S_psi^*(phi) = phi psi`.

Thus multiplication by every fixed multiplier has a preadjoint and is weak-star continuous. No amenability assumption is needed.

## Verification and novelty

The proof is abstract but self-contained after the source's Theorem 7.12. The verifier report checks functoriality, invariance of the balanced subspace, the adjoint pairing, and both source quantifiers.

A bounded local-index and external search on 2026-08-11 found only arXiv v1 and no later answer or matching general theorem. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: the 34-page arXiv v1 paper.
- `figures/open_problem_crop.png`: full-width page-27 source passage containing the conjecture and Theorem 7.12.

## Human review recommendation

Review as a likely valid full solution. Focus on the right-module convention in the balanced tensor product, the fact that a completely bounded multiplier is a completely bounded module map, and the exact source pairing used to identify multiplication with `S_psi^*`.
