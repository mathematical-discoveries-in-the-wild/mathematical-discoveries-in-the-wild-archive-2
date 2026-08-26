# arXiv:2303.03871 — finite-projection subcases for even cluster counts

Status: `candidate_substantial_partial_likely_valid`

Question 1 asks whether the bounded sequences with a finite positive even
number of accumulation points form a lineable set. This packet gives an exact
finite-geometry reduction for every three-dimensional candidate subspace and
proves four unconditional forbidden classes for its joint cluster set.

A hypothetical three-dimensional subspace of `L(2N) union {0}` must have a
joint cluster set `P` that:

- affinely spans `R^3`;
- has at least six points;
- is not centrally symmetric; and
- meets an even number of affine lines parallel to every direction determined
  by `P`.

The packet does **not** settle lineability. A later preprint claiming the full
negative answer, arXiv:2511.08760, is officially withdrawn; the packet isolates
the coincident collision-hyperplane issue in its first-version argument.

Files:

- `main.tex`: self-contained partial-result packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local compilation of the official ingested arXiv source.
- `figures/open_problem_page.png`: full-page source evidence for Question 1.
- `code/check_small_projection_parity.py`: exhaustive finite stress test,
  explicitly non-probative.
- `VERIFICATION.md`: proof, computation, literature, and rendering audit.
