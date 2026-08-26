# Circle shape optimization for wave observability

Status: `candidate_partial_likely_valid`.

This packet solves the geometric shape problem completely on the circle:
`sup g_2^T = L` for every time, with maximizers classified by invariance under
the remainder rotation `T mod 2pi`. It also solves the deterministic wave
shape problem at every resonant time `T=2pi m`: `C_T=(T/2)g_1`, the supremum is
`TL/2`, and it is attained exactly at `L=1/2` by measurable sets selecting one
point from almost every antipodal pair.

Files:

- `solution_packet.pdf`: full theorem statements, proofs, novelty bounds, and
  upgrade obstruction.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv:1607.01535 PDF.
- `figures/open_problem_crop.png`: full-width crop of PDF page 22.
- `code/check_circle_formulas.py`: optional numerical sanity checks; not used
  in the proof.
- `verification.md`: review checklist and artifact hashes.

Scope limitation: arbitrary deterministic observation times and
higher-dimensional manifolds remain open. The packet records the two-scale
off-diagonal Gramian obstruction encountered in the upgrade attempt.
