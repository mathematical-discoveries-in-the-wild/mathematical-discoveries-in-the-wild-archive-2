# Verification record

Date: 2026-08-11

Status: candidate full solution, likely valid, subject to human review.

## Mathematical audit

- A finite-valued lower-semicontinuous convex functional on a Banach space is
  norm-continuous and has a continuous subgradient at every point.
- A nonzero vector in `T(E)` gives a continuous coercive one-variable path, so
  every level strictly above `phi(0)` is attained on `T(E)`.
- The kernel of one continuous functional is infinite-dimensional, including
  the case where the functional is zero.
- A compact operator cannot be bounded below on an infinite-dimensional
  Banach space. Hence unit `z_n` can be chosen in that hyperplane with
  `||Tz_n|| <= n^-2`.
- `Tx_n -> a` ensures eventual feasibility `x_n in X`.
- The parameter objective is lower semicontinuous on compact `I`, so a
  minimizer exists. A finite-valued lower-semicontinuous function on compact
  `I` is bounded below.
- If a limiting parameter is nonzero, the residual norm diverges. If the
  parameter tends to zero but `|n lambda_n|` diverges, the residual norm again
  diverges.
- When `n lambda_n` is bounded, the subgradient annihilates `z_n`; its value
  on the residual error tends to zero because `n||Tz_n|| -> 0` and
  `lambda_n -> 0`.
- Lower semicontinuity of `psi` at zero and the subgradient inequality give
  the required liminf. Letting the intermediate level increase to `r` closes
  the equality.

## Novelty audit

- Exact searches of the run registry and all cheap indexes: no hit.
- Exact and close searches of the locally parsed arXiv corpus: the source plus
  later reference-list citations only.
- OpenAlex work `W2270788042` reported two citing works on 2026-08-11.
- Primary-text inspection of arXiv:2002.01413 and arXiv:1810.08957 found no
  answer or discussion of the reflexivity/Schur conjecture.
- The arXiv source record was checked at version 3, dated 2015-09-08.

This is a bounded novelty check, not a claim of exhaustive bibliographic
priority.

## Artifact audit

- The archived arXiv TeX source was compiled to a clean five-page source PDF.
- Printed source page 4, containing Theorem 2 and Remark 3, was extracted,
  tightly cropped, and embedded as the source-evidence image.
- The packet compiled twice with no undefined references, overfull boxes, or
  LaTeX warnings in the final log.
- The final packet has four pages. Every page and the source crop were rendered
  at high resolution and visually inspected; text, equations, references, and
  the evidence page are legible with no clipping or overlap.

## Human-review focus

Review the supporting-hyperplane choice, the compact approximate-kernel lemma
on `ker p`, and the subsequence trichotomy for minimizing parameters. These are
the only substantive logical joints; no numerical computation is used.
