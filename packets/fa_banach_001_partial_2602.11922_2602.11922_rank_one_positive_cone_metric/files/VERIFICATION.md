# Verification Report

Status: `candidate_partial_result_likely_valid`.

## Mathematical checks

- Recomputed `PQP = |<u,v>|^2 P` and hence
  `Tr(aP kappa_p bQ) = sqrt(ab)|<u,v>|^(2/p)`.
- Checked the derivative reduction
  `G(y) = y^(alpha-1)(1-y)/(1-y^alpha)` and the numerator
  `h(y) = alpha-1-alpha*y+y^alpha` for `G'(y)`.
- Verified `h(1)=0` and `h'(y)=alpha(y^(alpha-1)-1) <= 0`, so `h(y) >= 0`
  on `[0,1]` and the concavity direction is correct.
- Checked both branches in the triangle proof for `f o theta`: when the sum of
  the two base angles is at most `pi/2`, subadditivity applies; otherwise
  `f >= identity` dominates the diameter `pi/2`.
- Proved the metric-cone lemma self-contained by a three-vector spherical
  realization and the Euclidean triangle inequality.
- Checked the zero-radius quotient agrees exactly with the zero matrix.
- Checked separate homogeneity gives the exact density/radius decomposition
  `2d_p(A,B)^2 = a+b-2sqrt(ab)F_p(rho,sigma)`.
- Checked the converse cone argument: a strict angular triangle failure yields
  an explicit original-distance failure after choosing the middle trace so its
  Euclidean cone point lies on the chord between the endpoints.
- Expanded the three-state Gram determinant and verified its nonnegativity is
  equivalent to all angular triangle inequalities for angles in `[0,pi/2]`.

## Computational sanity check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2602.11922_rank_one_positive_cone_metric/code/check_rank_one_metric.py
```

The script compares direct matrix functional calculus with the closed trace
formula and samples 2,000 complex rank-one triples at each of
`p = 0.5, 1.0, 1.5, 1.9, 2.0`.  This is a numerical sanity check, not a proof.
It reported a maximum trace-formula error of `9.770e-15` and a maximum sampled
triangle defect `d(A,C)-d(A,B)-d(B,C)` of `-5.324e-02`.

## Literature boundary

The local indexes, the source paper, Komálovics--Molnár (2024), and the full
rank-one section of Vuong's April 2026 follow-up were checked.  Those sources
state the theorem for the normalized projector set.  No explicit statement for
arbitrary `aP` was found.  The full matrix-cone problem remains open.

## Render audit

The packet compiled in two LaTeX passes with no undefined references,
underfull boxes, or overfull boxes.  All six pages were rendered to PNG at
150 dpi and inspected at original resolution.  The source-question crop is
complete and readable; no clipping, overlap, broken glyphs, or margin defects
were found.

## Human-review focus

Confirm the literature-scope distinction between normalized projectors and the
non-normalized rank-one positive cone, and recheck the one-variable concavity
calculation.  The rest of the proof is elementary metric-cone geometry.
