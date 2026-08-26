# 2505.00155 - Walsh affine cubes prove endpoint optimality

Status: `full_solution_likely_valid`; `human_review_needed`.

Model: `GPT5.6`.

Source: Will Burstein, *Lambda_p Style Bounds in Orlicz Spaces Close to L^2*, arXiv:2505.00155v2.

## Result

The source asks whether the factor

`(log log n)^(alpha/2)`

in its best-subsystem `L^2 log^alpha L` synthesis bound is optimal when the selected subsystem has at least

`n / (e log^(alpha+1) n)`

elements. This packet proves that it is optimal in worst-case asymptotic order.

For every sufficiently large `N = 2^d`, take all `N` characters of `F_2^d`. Every subset `I` at the source cardinality satisfies

`N_Phi(I) >= c(alpha) (log log N)^(alpha/2)`.

Together with the source upper theorem, this gives matching upper and lower orders.

## Proof mechanism

An elementary cube count shows that a subset `A` of `F_2^d` with density `delta` contains a nondegenerate affine `r`-flat whenever

`delta^(2^r) 2^d > 2^r`.

At density `1 / (e (log N)^(alpha+1))`, one may choose

`2^r ~_alpha log N / log log N`.

If `V` is that affine frequency flat, the normalized sum of its characters has absolute value exactly `sqrt(|V|)` on the annihilator of the direction space, a set of probability exactly `1/|V|`, and is zero elsewhere. Its Luxemburg norm is therefore at least

`c(alpha) (log |V|)^(alpha/2) ~ c(alpha) (log log N)^(alpha/2)`.

Because every admissible subset contains such a flat, the proof has the deterministic quantifier missing from the source's Bernoulli lower bound and from the earlier lane-19 exchangeable-selector partial result.

## Verification and novelty

The proof is self-contained after the source statement. The verifier report checks the cube-count recursion, the count of dependent direction tuples, the density-to-flat scale, the exact character-sum identity, and the Luxemburg modular calculation.

A bounded run-index and external search on 2026-08-11 found the source paper and background/adjacent work but no later paper claiming to resolve Remark 2.11 and no matching deterministic Walsh-affine-cube lower theorem. Novelty remains subject to expert literature review.

## Files

- `main.tex`: complete full-result proof packet.
- `solution_packet.pdf`: rendered packet.
- `verification_report.md`: adversarial step-by-step verification.
- `source_paper.pdf`: arXiv v2 source paper.
- `figures/open_problem_crop.png`: page-13 source evidence containing Theorem 2.10 and Remark 2.11.

## Human review recommendation

Review as a likely valid full solution. Focus on the normalized cube count versus the number of degenerate direction tuples, the choice `2^r ~ log N / log log N`, and the match between the source's optimality quantifiers and the all-subsets conclusion for the constructed Walsh system.
