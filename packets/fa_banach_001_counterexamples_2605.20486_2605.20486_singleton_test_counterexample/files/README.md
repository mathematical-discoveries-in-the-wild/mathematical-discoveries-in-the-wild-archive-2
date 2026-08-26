# arXiv:2605.20486 - singleton-test counterexample

Status: `candidate_counterexample_likely_valid`

This packet gives a full negative answer to Question 1 of Salas,
Tapia-García, and Venegas M., *The reach and limits of slope eikonal equations
in compact spaces* (arXiv:2605.20486v1).

The compact metric space is a Euclidean subset of `R^3` formed from a straight
limit arc and countably many polygonal arcs that share one root and accumulate
on the limit arc. Every intrinsic singleton-distance function has descent
slope one away from its target. However, for the closed countable set of all
branch endpoints, intrinsic distance has descent slope at least two at the
root. By the source paper's characterization, the space is not eikonal.

Files:

- `main.tex`: formal counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop.png`: printed source page 25 containing Question 1.
- `code/check_parameters.py`: independent arithmetic and limiting-ratio check.
- `verification.md`: proof audit, execution record, and review focus.

Novelty check: exact run-index and bounded primary arXiv searches on
2026-08-11 found only source v1 and no later answer or close counterexample.

