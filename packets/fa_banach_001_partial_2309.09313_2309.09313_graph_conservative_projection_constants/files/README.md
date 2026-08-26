# Exact conservative-field projection constants on graph families

Status: **candidate partial result, likely valid**.

This packet addresses the Section 4.5 question in arXiv:2309.09313 asking
for the smallest norm of an extension of the integral operator from
conservative vector fields to all vector fields on a finite weighted graph.
Equivalently, it computes relative projection constants of the conservative
(cut/gradient) space inside the full `ell_infinity` edge space.

The general graph problem remains open. The packet proves exact constants
for:

- every weighted cycle;
- every weighted cactus;
- every unweighted complete graph;
- every unweighted complete bipartite graph; and
- every cut-vertex block sum of those graph families.

Files:

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: compiled deliverable.
- `figures/source_question.png`: exact source-question screenshot.
- `code/verify_projection_constants.py`: rational and independent LP checks.
- `verification_report.md`: verification transcript and scope.
- `novelty_search.md`: bounded literature-search record.
- `source_paper.pdf`: source paper used for the screenshot.

Reproduce the computation from the repository root with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2309.09313_graph_conservative_projection_constants/code/verify_projection_constants.py
```
