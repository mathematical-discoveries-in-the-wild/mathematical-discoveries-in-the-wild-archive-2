# 1401.2653 — compact affine actions reduce to the linear-isometric case

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: Natalia Jonard-Pérez, *Equivariant absolute extensor property on
hyperspaces of convex sets*, arXiv:1401.2653v2.

## Result

Question 6.2 asks whether `CB(L)` is a `G-AE` whenever a compact group `G`
acts continuously and affinely on a Banach space `L` and the induced action
on `CB(L)` is continuous. The answer is affirmative.

## Proof mechanism

Haar-average any orbit to obtain a fixed point `c`. Translation by `c`
conjugates the affine action to a continuous linear action `rho`. The norm

`||x||_G = sup_{g in G} ||rho(g)x||`

is complete, equivalent to the original norm, and `G`-invariant. The two
Hausdorff metrics on `CB(L)` are bi-Lipschitz equivalent, so the assumed
continuity of the induced action survives. The translated hyperspace is
therefore in the exact setting of Theorem 5.1 of the source, which proves it
is a `G-AE`.

## Files

- `main.tex`: complete self-contained reduction and proof.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial hypothesis audit.
- `source_paper.pdf`: arXiv v2 source PDF.
- `figures/open_question_crop.png`: source Question 6.2 and preceding remark.
- `figures/source_theorem_5_1_crop.png`: the source theorem used in the proof.

## Novelty and review

A bounded local-index and external search on 2026-08-12 found no later paper
stating this reduction or answering Question 6.2. Novelty remains subject to
specialist review. The recommended audit points are the Bochner-integral
barycenter for possibly nonmetrizable compact `G`, the invariant norm, the
Hausdorff bi-Lipschitz comparison, and the applicability of source Theorem
5.1 after conjugation.
