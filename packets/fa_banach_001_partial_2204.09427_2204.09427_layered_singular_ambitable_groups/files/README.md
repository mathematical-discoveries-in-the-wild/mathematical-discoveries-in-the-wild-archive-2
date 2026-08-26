# Layered singular-cardinal groups are ambitable

Status: `candidate_substantial_partial_likely_valid_human_review_needed`

Source: Friedrich Martin Schneider, *Concentration of invariant means and
dynamics of chain stabilizers in continuous geometries*, arXiv:2204.09427,
Section 5 (PDF pages 27--28).

Current-status support: Jan Pachl, *Another ambitable group*,
arXiv:2606.06000 (4 June 2026).

## Result

Let `kappa_0,kappa_1,...` be any strictly increasing sequence of infinite
cardinals, let `I_k` be nested sets of cardinality `kappa_k`, and put
`I=union_k I_k`. For every fixed nontrivial finite abelian group `A`, the
finite-support direct sum

```text
G = A^(I)
```

is nonprecompact and ambitable when it is given the ultrametric determined by
the first layer meeting the support. Thus every singular cardinal of
countable cofinality supports such examples, for every cofinal cardinal tower
and every finite nontrivial abelian coefficient group.

Pachl's 2026 construction is the special case `A=Z/2` and
`kappa_k=aleph_k`. Schneider's Lemma 5.3 then implies that the Samuel
compactification of each new example has continuum many pairwise disjoint
closed invariant nonempty subsets.

## Proof mechanism

Every continuous invariant pseudometric is dominated by a layer-step
ultrametric. Finite rational Lipschitz patterns are then placed in coherent,
pairwise disjoint translated blocks. At level `k+1`, the prescribed projection
fiber has size `kappa_(k+1)`, whereas all earlier patterns and all earlier
same-level stages forbid fewer than `kappa_(k+1)` points. The resulting code
is uniformly continuous because sufficiently close code points project to
the same lower-level block. One orbit therefore realizes all finite patterns
and is pointwise dense in every bounded Lipschitz ball.

## Limitation

The full question whether every topological group is precompact or ambitable
remains open. The proof needs a countable coherent tower of homomorphic
projections with strictly growing fibers. General nonprecompact groups need
not supply such a tower. Eight focused upgrades tested removal of strict
growth, transfinite towers, nonabelian coefficients, and a direct attack on
the weaker Samuel-separation problem; none justified the unrestricted claim.

## Files

- `solution_packet.pdf`: theorem, proof, corollary, upgrade audit, and review notes.
- `source_paper.pdf`: arXiv:2204.09427.
- `supporting_pachl_2606.06000.pdf`: June 2026 status and special example.
- `figures/`: source-question and current-status evidence crops.
- Attempt log: `runs/fa_banach_001/attempts/2204.09427_layered_singular_ambitable_groups.md`.

Human review should focus on the coherent translation recursion and the
finite-pattern density step. No computational dependency is used.
