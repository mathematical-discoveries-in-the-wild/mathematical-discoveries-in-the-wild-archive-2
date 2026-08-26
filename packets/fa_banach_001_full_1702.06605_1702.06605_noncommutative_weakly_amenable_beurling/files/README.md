# A nontrivial weakly amenable Beurling algebra on a noncommutative group

Status: `candidate_full_solution_likely_valid` (independent proof; human review requested).

Source: Varvara Shepelska and Yong Zhang, *Non-weakly amenable
Beurling algebras*, arXiv:1702.06605, introduction, printed page 3 (PDF
page 3). The source says that no nontrivial weakly amenable Beurling algebra
which is noncommutative was known.

## Result

For every `0 < alpha < 1/2`, let

```text
G = Z x S_3,
Omega(n,sigma) = (1+|n|)^alpha.
```

Then `G` is noncommutative, `Omega` is an unbounded symmetric polynomial
weight, and `l1(G,Omega)` is weakly amenable. Thus this is a full explicit
example of the type requested by the source.

The proof establishes a reusable tensor theorem: if `A` is a unital
commutative weakly amenable Banach algebra and `B` is a unital amenable Banach
algebra, then `A projective-tensor B` is weakly amenable. Apply it to
`A=l1(Z,omega_alpha)` and `B=l1(S_3)`. Amenability of the latter follows from
the explicit finite-group diagonal.

## Literature and novelty caveat

A bounded search on 2026-08-09 covered the four cheap run indexes, the local
arXiv corpus, exact phrases from the source challenge, tensor-product/weak-
amenability searches, and later arXiv papers. No independent verified source
for this finite-factor construction was found.

Mehdipour--Rejali, arXiv:2209.08346 (2022), Corollary 4.3, states a much
broader pullback conclusion which would imply noncommutative examples.
However, the proof of its Proposition 4.1(i) assumes without justification
that every non-inner quasi-additive function upstairs lies in the image of the
pullback map. The preceding discussion establishes only injectivity and
preservation of inner functions, not this surjectivity. The preprint therefore
does not currently provide a verified duplicate of the result packaged here.
Novelty remains subject to expert literature review.

## Files

- `solution_packet.pdf`: complete theorem and proof.
- `source_paper.pdf`: original arXiv source.
- `figures/open_problem_crop.png`: real crop of the source challenge.
- `main.tex`: packet source.

## Human-review focus

Check the standard amenability restriction step for a derivation on
`A projective-tensor B`, and the lemma that a unital commutative weakly
amenable algebra has no derivations into any symmetric unital module. The
packet proves that lemma directly, so there is no unproved dependency.

