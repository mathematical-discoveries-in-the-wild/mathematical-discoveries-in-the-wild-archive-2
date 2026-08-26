# Finite-tree automorphism actions are Tame1 but not Tame2

Status: candidate partial result, likely valid, awaiting human review

Source: Michael Megrelishvili, *Tameness of actions on finite rank median
algebras*, arXiv:2601.01681, Question 5.12 on PDF page 15.

## Claimed contribution

Let `K` be the geometric realization of a nondegenerate finite simplicial tree,
with its canonical rank-one median, and let `G=Aut(K)` be the compact-open
group of all homeomorphic median automorphisms. Then `(G,K)` is Tame1 but not
Tame2.

This gives a complete answer to Question 5.12 for a natural branched rank-one
class. It extends the interval example in the source and contrasts with the
source's Wazewski-dendrite example, whose full automorphism action is not
Tame1.

## Proof mechanism

The endpoints and branch points form a finite invariant skeleton. Every
automorphism permutes this skeleton and its finitely many complementary open
edges. For a fixed skeleton permutation, restrictions to the edges lie in a
finite product of classical Helly compacta of monotone interval maps. Each
corresponding component of the enveloping semigroup is therefore first
countable. The components are clopen and finite in number, so the whole
enveloping semigroup is first countable.

On the other hand, reparametrizations supported on one closed edge form a copy
of the order-preserving homeomorphism group of `[0,1]`. Its enveloping
semigroup embeds in the full enveloping semigroup and is not hereditarily
separable. Thus the action is not Tame2.

## Files

- `main.tex`: self-contained partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2601.01681.
- `figures/open_problem_crop.png`: real crop of Question 5.12 and its immediate
  context from source PDF page 15.
- `verification.md`: adversarial proof check.

## Novelty check

On 2026-08-09, the run's registry, solution, attempt, and proof-gap indexes were
searched for arXiv:2601.01681 and finite-rank median/tameness keywords, with no
hit. A bounded web/arXiv search used combinations of `finite tree`,
`automorphism`, `Tame1`, `dendrite`, and `enveloping semigroup`. It found the
source paper and Codenotti's 2025 non-Tame1 dendrite examples, but no prior
finite-tree classification. Novelty confidence is moderate rather than
definitive because this is a bounded phrase search.

## Human review recommendation

Send to a specialist in tame dynamics/continuum theory. The main points to
check are the clopen finite decomposition of the Ellis semigroup by essential
skeleton permutations and the embedding of the interval subsystem.
