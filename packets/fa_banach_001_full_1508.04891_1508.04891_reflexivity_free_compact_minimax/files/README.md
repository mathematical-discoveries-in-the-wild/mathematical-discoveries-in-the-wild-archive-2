# arXiv:1508.04891 — reflexivity is unnecessary

Status: `candidate_full_solution_likely_valid`

Remark 3 of Ricceri's *A minimax theorem in infinite-dimensional topological
vector spaces* asks whether reflexivity is necessary in Theorem 2 and
conjectures a counterexample in a Schur space.

This packet proves a stronger theorem: the identity in Theorem 2 holds on
every infinite-dimensional real Banach space. Consequently, there is no
counterexample in a Schur space.

The proof chooses an attained intermediate value `phi(a)=s<r`, takes a
subgradient `p` at `a`, and uses compactness of `T` on the infinite-dimensional
hyperplane `ker p` to obtain unit vectors `z_n` with `Tz_n=o(1/n)`. For
`x_n=y+nz_n`, any minimizing parameters `lambda_n` are analyzed according to
the scale of `lambda_n` and `n lambda_n`. Coercivity handles the escaping
scales; the subgradient inequality handles the bounded scale.

Files:

- `main.tex`: self-contained theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source page containing Theorem 2 and Remark 3.
- `verification.md`: proof and novelty audit.

Bounded searches through 2026-08-11 found no prior answer to Remark 3. The
candidate result remains subject to human mathematical review.
