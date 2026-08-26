# 1511.09045 — compactoid Mackey convergence classification

Status: `candidate_full_solution_human_review_needed`.

Model: `GPT5.6`.

Source: Federico Bambozzi, *Stein Domains in Banach Algebraic Geometry*, arXiv:1511.09045.

## Result

Remark 3.69 conjectures that, for every Frechet space, topological convergence of sequences agrees with Mackey convergence for both the von Neumann and compactoid bornologies, without the preceding nuclearity hypothesis.

This packet gives a sharp classification:

- over every nontrivially valued field, the conjecture is true for all metrizable locally convex spaces, hence for all Frechet spaces;
- over a trivially valued field, the literal unrestricted statement is false for `E=k^N`: the unit sequence is topologically null, while every von Neumann bounded set is zero and hence it is not Mackey null.

## Proof mechanism

For a topologically null sequence `x_n` over a nontrivially valued field, choose scalars `a_n` tending slowly to infinity so that `a_n x_n` remains topologically null. The set consisting of this rescaled null sequence and zero is compact. Its absolutely convex hull is compactoid and witnesses compactoid-Mackey convergence of `x_n`, since `a_n^(-1)->0`.

The reverse implications are direct: compactoid sets are bounded, and Mackey convergence with respect to a bounded set implies topological convergence.

## Verification and novelty

The verification report audits the diagonal rescaling, compactoid hull, scalar quantifiers in Mackey convergence, reverse implications, and the trivially valued counterexample.

A bounded local-index and external primary-source search on 2026-08-11 found no later resolution of Remark 3.69. Novelty remains subject to specialist review.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof audit.
- `source_paper.pdf`: official 54-page arXiv PDF.
- `figures/conjecture_crop.png`: source page 29 crop containing Lemma 3.68 and Remark 3.69.

## Human review recommendation

Review as a likely valid full solution. The proof is elementary but the conventions are specialized; reviewers should check the definitions of absolute convexity and Mackey convergence over the chosen valued field.
