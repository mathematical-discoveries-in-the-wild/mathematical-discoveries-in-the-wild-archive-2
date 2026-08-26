# Exact higher-order jet functional on the real line

Status: candidate_partial_likely_valid

Source: Matthew J. Hirn and Erwan Y. Le Gruyer, *A general theorem of
existence of quasi absolutely minimal Lipschitz extensions*, arXiv:1211.5700,
Section 2.4.5 (PDF page 10).

## Result

For every `m >= 1` and scalar `m`-fields on an arbitrary subset of the real
line, define the pair cost as the least Lipschitz seminorm of `F^(m)` among
`C^{m,1}` functions interpolating the two endpoint jets. The packet proves:

- an explicit finite-dimensional dual formula for this cost via `m+1`
  moment constraints on `F^(m+1)`;
- exact interpolation of arbitrary data on `R`, with no multiplicative loss;
- equality between the supremum of the pair costs and the least global
  `Lip(F^(m))`;
- properties `(P0)` through `(P5)` from the source paper; and
- applicability of the source's quasi-AMLE theorem to scalar higher-order
  fields on `R`.

## Scope

This is a complete one-dimensional, all-orders subcase. It does not settle
the question on `R^d` for `d >= 2`. The proof relies on the total order of
the line: after extending jets to the closure, each complementary interval
can be filled independently by an exact two-point minimizer. There is no
analogous independent-gap decomposition in higher dimensions.

A bounded arXiv search using the source id and the core terms `m-fields
Gamma^m`, exact `C^{m,1}` extension, one-dimensional Whitney jets, minimal
Lipschitz highest derivative, and Hermite `L^infinity` interpolation found
nearby Whitney extension results but no exact match. Novelty confidence is
moderate, not definitive.

## Packet contents

- `main.tex`, `solution_packet.pdf`: statement, explicit formula, complete
  proof, source-axiom verification, scope, and search bounds.
- `source_paper.pdf`: arXiv:1211.5700v3.
- `figures/open_problem_crop.png`: the source statement on PDF page 10.
- `verification_report.md`: mathematical and artifact checks.

Human review should concentrate on the arbitrary-closed-set pasting lemma and
the continuity argument for `(P4)`. The result is deliberately classified as
a candidate partial result until reviewed.
