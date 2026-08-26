# Continuous-embedding Fraïssé theory: an exact separatedness dichotomy

**Status:** candidate partial result, likely valid.

**Source:** Jamal K. Kawach and Jordi López-Abad, *Fraïssé and Ramsey
properties of Fréchet spaces*, arXiv:2103.11049, Problem 5.3 (PDF p. 25).

The packet proves a sharp answer to the existence clause of Problem 5.3.  For a
finite-dimensional multi-seminormed space `X`, let `N_X` be the intersection of
the kernels of its seminorms.  A linear map `T:X->Y` is continuous exactly when
`T(N_X) subset N_Y`.  Consequently:

- every linear map from a separated finite-dimensional source is continuous;
- no non-separated finite-dimensional space embeds continuously and injectively
  into a Hausdorff Fréchet space;
- the separated finite-dimensional subcategory is therefore the maximal domain
  for a Hausdorff continuous-embedding theory;
- on that subcategory continuity changes no morphisms, and the source paper's
  pushout and Fraïssé-limit proofs apply with the same stability modulus
  `2 delta`.

This gives a positive continuous-morphism Fraïssé theory for the separated
finite-length and fixed-length classes, plus a matching impossibility theorem
for retaining non-separated truncations.  The broader request to classify
particular subclasses and identify all resulting limits remains open.

## Contents

- `solution_packet.pdf`: expert-facing statement and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Problem 5.3 on source PDF p. 25.
- `tmp/`: build and rendering intermediates.

## Verification

The proof was checked at the level of each target seminorm: after
`T(N_X) subset N_Y`, every `q_j o T` descends to the finite-dimensional quotient
`X/N_X` and is therefore bounded by the quotient norm.  The converse uses the
identity `N_X = closure({0})`.  The category transfer uses Proposition 2.3 of
the source: its amalgam is separated and its structure maps are linear, hence
automatically continuous when their finite-dimensional sources are separated.
No computation is used.

## Novelty check

On 2026-08-11, the run registry and solution/attempt/proof-gap indexes were
searched for arXiv:2103.11049 and the core terms.  Exact-phrase and keyword web
searches for Problem 5.3, continuous multi-seminormed embeddings, and Fréchet
Fraïssé theory returned the source paper and general background, but no later
answer.  Novelty confidence is moderate; the continuity lemma itself is
elementary and may be folklore, while its sharp application to the source
problem was not located.

## Human-review recommendation

Check the categorical transfer paragraph against the precise preferred
definition of a “continuous Fraïssé class,” especially whether the ambient
hereditary property is formulated only with continuous morphisms.  The linear
topological dichotomy is elementary and exact; classification as a partial
rather than full answer is deliberately conservative because Problem 5.3 is
open-ended.
