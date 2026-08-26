# Higher Baire-class completeness program

Status: `candidate_partial_result_likely_valid`

Source: S. Gabriyelyan, A. V. Osipov, and E. Reznichenko,
*Completeness and reflexivity type properties of B1(X)*,
arXiv:2601.00733v2, Problem 3.10 on PDF page 11.

## Result

The packet gives three linked results.

1. If `E` is any pointwise vector subspace of `R^X` containing `C(X)`, then
   `E` is quasi-complete if and only if `E=R^X`. Consequently, for every
   nonzero countable `alpha`, all complete/quasi-complete,
   (semi-)reflexive, and (semi-)Montel properties of `B_alpha(X)` are
   equivalent to `B_alpha(X)=R^X`. The same holds for `B(X)`.

2. For arbitrary Tychonoff `X`, `B_alpha(X)` is sequentially complete if and
   only if `B_alpha(X)=B_{alpha+1}(X)`.

3. For metrizable `X`, the complete intrinsic program is:

   - the strong properties hold iff every subset of `X` is
     `Sigma^0_{alpha+1}`;
   - local completeness, sequential completeness, and
     `B_alpha=B_{alpha+1}` hold iff
     `Sigma^0_{alpha+1}(X)=Pi^0_{alpha+1}(X)`.

For `B(X)`, sequential and local completeness always hold. All stronger
properties are equivalent to `B(X)=R^X`, equivalently every characteristic
function is Baire; for metrizable `X`, equivalently every subset is Borel.

## Scope

This is a substantial partial answer to Problem 3.10, not a full arbitrary-
Tychonoff solution. The intrinsic local-completeness characterization for a
fixed higher Baire class on nonmetrizable domains remains open. Eight focused
upgrade routes are recorded in the packet and attempt note; the surviving
obstruction is the failure of a general Lebesgue--Hausdorff converse without
additional domain hypotheses.

A bounded search found the source paper and general Baire-classification
literature but no prior statement of the abstract quasi-completion theorem or
the metrizable higher-rank characterization. Novelty confidence is bounded.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem statements and proofs.
- `source_paper.pdf`: arXiv:2601.00733v2.
- `figures/open_problem_crop.png`: Problem 3.10 on PDF page 11.
- `VERIFICATION.md`: proof and rendering audit.

Human review should focus on the bounded-box completeness argument, the
barrelled weak-space transfer, and transfinite Borel indexing.
