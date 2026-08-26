# 1910.07273 — Borel parameters give countable Rosenthal index

Status: `candidate_partial_result_likely_valid_human_review_needed`.

Model: `GPT5.6`.

Source: Cabello Sánchez, Castillo, Marciszewski, Plebanek, and Salguero-Alarcón, *Sailing over three problems of Koszmider*, arXiv:1910.07273, Problem 7.10 on source PDF page 16.

## Result

Problem 7.10 asks:

1. whether `ri(L^theta)<omega_1` for every Borel `theta:(0,1)->2`; and
2. whether one can estimate the index effectively from the Borel class of `theta`.

The packet fully answers the first clause: for every Borel `theta`, the trace space `C_Q(L^theta)` is Borel, so `ri(L^theta)<omega_1`. The second, quantitative clause remains open.

## Proof mechanism

The source already proves `C_Q(L^theta)` analytic. The new argument proves it coanalytic.

- Rational-sequence convergence to either side of a split point has an explicit Borel description. Ordinary one-sided convergence governs all points except that, when `theta(y)=1`, the designated sparse sequence `S_y` is rerouted to the other side.
- A rational function fails to extend continuously exactly when the closure of its compactified graph has two values over one point or reaches an infinite endpoint.
- Because `L^theta` is Rosenthal, the graph-closure failure has a sequential witness. The Borel convergence relation makes the set of nonextendible traces analytic.
- Thus the trace space is both analytic and coanalytic, hence Borel by Souslin's theorem.

## Upgrade attempt

The one-sided Cauchy formulation was used to try to track an explicit Borel rank from the class of `theta`. The projection over the continuum of split points and the final analytic/coanalytic separation step lose that quantitative information. No class-sensitive ordinal bound is claimed.

## Verification and novelty

The verification report audits the split-point convergence formulas, Borel coding, graph criterion, Fréchet–Urysohn sequence witness, and the exact scope of the partial answer.

On 2026-08-11, bounded local-index and web/arXiv searches found the source and a later thesis restating it, but no later answer to Problem 7.10. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete partial-result proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 19-page arXiv PDF.
- `figures/open_problem_crop.png`: source PDF page 16 crop containing Problem 7.10.

## Human review recommendation

Review as a likely valid substantial partial result. The highest-value check is the equivalence between Stone-space convergence and formulas (1)–(2), especially at rational split points and along the exceptional sequences `S_y`.
