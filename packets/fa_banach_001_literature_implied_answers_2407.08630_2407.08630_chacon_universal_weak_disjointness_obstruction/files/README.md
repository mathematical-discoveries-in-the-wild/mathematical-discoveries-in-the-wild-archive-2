# Chacon Universality Gives a Full Negative Answer to Austin's Question

Status: `literature_implied_answer (full negative resolution)`

Source: Tim Austin, *Non-convergence of some non-commuting double ergodic
averages*, arXiv:2407.08630v3; Proc. Amer. Math. Soc. 153 (2025),
1701--1707.

Supporting source: Emmanuel Lesigne, Benoit Rittaud, and Thierry de La Rue,
*Weak disjointness of measure preserving dynamical systems*, Ergodic Theory
Dynam. Systems 23 (2003), 1173--1198, DOI
10.1017/S0143385702001505; HAL: hal-00017086.

## Result

Austin asks whether every weakly mixing probability-preserving transformation
can occur as the first transformation `S` in a divergent double-average
example. The answer is no.

The classical Chacon transformation `C` is weakly mixing, but Proposition 4.2
of Lesigne--Rittaud--de La Rue proves that it is *universal*: it is weakly
disjoint from every probability-preserving dynamical system. Consequently, for
every transformation `T` on the same probability space and all bounded
measurable `f,g`,

```text
B_N(x) = 1/N sum_{n=0}^{N-1} f(C^n x) g(T^n x)
```

converges almost everywhere and in every finite `L^p`. In particular,

```text
1/N sum_{n=0}^{N-1} integral f(C^n x) g(T^n x) dmu(x)
```

always converges. Thus no system isomorphic to Chacon's transformation can
appear as `S` in any of the nonconvergent senses discussed by Austin.

## The Diagonal Argument

Weak disjointness is deliberately stronger than ordinary almost-everywhere
convergence on a product space. For each pair `f,g`, it supplies full-measure
sets `A` in the first space and `B` in the second space such that the averages
converge for *every* pair `(x,y)` in the rectangle `A x B`.

When both transformations act on the same probability space, `A intersect B`
still has full measure. Substituting `y=x` gives convergence of `B_N(x)` almost
everywhere on the diagonal. Boundedness gives convergence in finite `L^p` by
dominated convergence, and integrating gives convergence of Austin's scalar
averages.

## Why This Is Literature-Implied

The supporting theorem predates Austin's paper by two decades and therefore
does not explicitly claim to answer Austin's concluding question. The answer
requires the short diagonal identification above. This packet is accordingly
filed as a literature-implied answer rather than a new counterexample or an
explicit later literature answer.

The full negative conclusion supersedes the need to extend the separate
positive-entropy construction as a route to Austin's universal question. That
construction remains a valid theorem showing that every positive-entropy
ergodic system does occur in a divergent example; the Chacon obstruction shows
that the zero-entropy weakly mixing remainder cannot be settled uniformly in
the affirmative.

## Evidence and Verification

- Austin's question appears on arXiv PDF page 6; see
  `figures/open_problem_crop.png`.
- Definition 1 of the supporting paper appears on article page 2 (local PDF
  page 3); see `figures/weak_disjointness_definition_crop.png`.
- The supporting paper calls Chacon weakly mixing and states Proposition 4.2,
  "The Chacon dynamical system is universal," on article page 12 (local PDF
  page 13); see `figures/chacon_universal_crop.png`.
- `VERIFICATION.md` audits the quantifiers, the same-space diagonal step,
  dominated convergence, isomorphism invariance, and the literature status.

## Novelty Check

A bounded check through 9 August 2026 searched the run indexes; exact title,
arXiv-id, and question-wording matches; citation/title searches combining
Austin's paper with Chacon transformation, universality, and weak
disjointness; and recent related counterexample papers by Huang--Shao--Ye and
Ryzhikov. No later source was found explicitly pointing out this corollary.
The mathematical input itself is published literature, so novelty confidence
is intentionally low and the packet is provenance-only.

## Human Review Recommendation

Verify the natural universal reading of Austin's word "any." Under that
reading the counterexample is decisive. If a different convergence mode was
intended, note that the argument proves almost-everywhere and finite-`L^p`
convergence of the bounded function averages, as well as convergence of their
integrals.

