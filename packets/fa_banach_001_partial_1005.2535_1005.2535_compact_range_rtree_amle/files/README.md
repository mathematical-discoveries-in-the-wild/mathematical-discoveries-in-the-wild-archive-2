# Compact-domain AMLEs with arbitrary complete R-tree targets

Status: `candidate partial result - likely valid`

Model: `GPT5.6`

Source: Assaf Naor and Scott Sheffield, *Absolutely minimal Lipschitz
extension of tree-valued mappings*, arXiv:1005.2535, later published in
*Mathematische Annalen* 354 (2012), 1049-1078.

## Result

Let `X` be a compact length space, let `Y` be a nonempty closed subset, let
`T` be an arbitrary complete R-tree, and let `f:Y->T` be Lipschitz. Then `f`
has an absolutely minimal Lipschitz extension `u:X->T`. Moreover, `u` can be
chosen to take values in the closed convex hull of `f(Y)` and to satisfy

```text
Lip_X(u) = Lip_Y(f).
```

The target need not be bounded, compact, locally finite, or the realization
of a finite graph. This settles the target-tree part of the source conjecture
for compact domains. It does not remove the source's local-compactness
hypothesis for arbitrary domains, and it does not establish uniqueness for
general R-tree targets.

## Proof mechanism

The closed convex hull of a compact subset of a complete R-tree is compact.
Approximate this hull from inside by increasing finite subtrees and project the
boundary data onto them. Naor-Sheffield gives an AMLE for every projected
problem. The extensions are equi-Lipschitz and take values in one compact
tree, so Arzela-Ascoli gives a uniformly convergent subsequence. Each finite
tree solution satisfies comparison with distance functions for every point of
the full compact hull: distance to a point outside the finite subtree differs
by a constant from distance to its gate projection. Comparison is closed under
uniform convergence and implies the AMLE property. A final nearest-point
projection argument transfers absolute minimality from the compact hull to
the ambient R-tree.

## Files

- `main.tex`: complete theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `verification.md`: independent proof audit and scope checks.
- `source_paper.pdf`: the original source paper.
- `figures/open_problem_crop.png`: genuine crop of the source conjecture.

## Novelty status

The run indexes and bounded searches on 9 August 2026 used the arXiv id,
exact paper title, `R-tree AMLE`, `compact R-tree absolutely minimal
Lipschitz extension`, and close variants. They found the source and general
AMLE references, but no exact compact-domain arbitrary-R-tree theorem. This is
evidence rather than a guarantee of novelty; human literature review remains
necessary.

## Human-review recommendation

Check the compact-convex-hull lemma, the gate identity used to upgrade
finite-subtree comparison to full-hull comparison, and the fact that the
comparison-implies-AMLE direction in the source does not require the target
to be a finite metric tree.
