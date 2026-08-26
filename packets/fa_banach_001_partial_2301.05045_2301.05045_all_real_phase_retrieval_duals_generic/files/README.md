# All real phase-retrieving duals are generic

Status: `candidate_partial_solution_likely_valid`

Source: Fahimeh Arabyani-Neyshaburi, Ali Akbar Arefijamaal, and Rajab Ali
Kamyabi-Gol, *Characterization of (weak) phase retrieval dual frames*,
arXiv:2301.05045, abstract and Theorem 2.3.

## Result

Let `Phi=(phi_i)_{i=1}^m` be any phase-retrieving frame for `R^n`, with
arbitrary finite redundancy. In the affine space `D_Phi` of all dual frames,
the phase-retrieving duals `PD_Phi` form:

- a relatively Zariski-open subset;
- a Euclidean-open dense subset;
- a full-Lebesgue-measure subset.

There is an explicit polynomial classification. For a candidate dual `G`, let
`R_I(G)` be the sum of squares of all `n x n` minors using columns indexed by
`I`, and set

`P(G) = product_I (R_I(G) + R_{I^c}(G))`.

Then, on `D_Phi`, `G` does phase retrieval exactly when `P(G) != 0`.

The density statement also has a strong one-dimensional form. If `G_0` is the
canonical dual and `G` is any dual, then

`G_t = (1-t)G + tG_0`

is a phase-retrieving dual for every real `t` except finitely many values.

## Proof mechanism

The real complement-property theorem converts phase retrieval into finitely
many spanning alternatives. Each spanning condition is detected by sums of
squared maximal minors, so failure is algebraic. The canonical dual belongs to
the affine dual space and still does phase retrieval because it is obtained by
an invertible self-adjoint change of variables. Hence the classification
polynomial is not identically zero on the affine dual space. Its zero set is
proper, nowhere dense, and null. Restriction to any line ending at the
canonical dual is a nonzero one-variable polynomial, which gives the finite
exceptional-set statement.

## Scope

This fully answers the source density/classification question for finite real
frames and removes the source Theorem 2.3 restriction `m=2n-1`. It is a
partial answer to the paper's broader question because the complex case is not
settled: the real complement property has no direct complex analogue of the
form used here.

## Novelty check

A bounded check on 2026-08-11 searched the run indexes, web/arXiv results for
the exact title, and official arXiv API queries for `phase retrieval dual
frames`, `alternate dual frames` plus `phase retrieval`, and `dual frames`
plus `open and dense` plus `phase retrieval`. Every exact query returned only
arXiv:2301.05045v1. No later paper or theorem stating the arbitrary-redundancy
real result or the radial finite-exception strengthening was found. Novelty is
plausible but not exhaustively certified.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and complete proof.
- `source_paper.pdf`: arXiv:2301.05045.
- `figures/open_problem_crop.png`: the abstract's classification/density
  questions and the authors' “some classes” scope.
- `figures/source_minimal_length_theorem_crop.png`: source Theorem 2.3,
  restricted to `m=2n-1`.
- `VERIFICATION.md`: mathematical and visual-QA report.

Human review should focus on the polynomial equivalence with the complement
property and on the canonical-dual phase-retrieval argument.

