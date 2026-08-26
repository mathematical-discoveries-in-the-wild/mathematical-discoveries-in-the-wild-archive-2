# Verification Report

Candidate: arXiv:2308.09799, Conjecture 1.1.

## Claim checked

The universal pairwise-orthogonal family asserted in Conjecture 1.1 does not
exist for the left action of `S_3` on itself. More generally, the asserted
property is equivalent to multiplicity-freeness of the quasi-regular
representation on `L^2(G/K)`.

## Verdict

likely valid

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | Conjecture 1.1 on PDF page 1 has exactly the universal-subcollection formulation used in the packet. |
| Hypotheses | valid | `S_3` and its discrete six-point space are compact; left translation is continuous and transitive. |
| Minimal-space lemma | valid | Any member of a subcollection whose direct-sum closure is a minimal space lies inside that minimal space and therefore equals it. |
| Standard representation | valid | The displayed transposition matrices have no common invariant line, so the two-dimensional representation is irreducible. |
| Coefficient embeddings | valid | They intertwine the standard and left regular actions; Schur orthogonality makes each embedding injective. |
| Orthogonality obstruction | valid | `M_a` is orthogonal to `M_b`; `M_(a+b)` is their diagonal and has nonzero inner product with `M_a`. Distinctness follows from the orthogonal direct sum. |
| General necessity | valid | Multiplicity at least two always supplies a coordinate and a nonorthogonal diagonal minimal copy. |
| General sufficiency | valid | In the multiplicity-free case, character projections preserve a closed invariant `Y`, and compact-group finite-spectrum approximants converge uniformly inside `Y`. |
| Symbolic check | valid | The exact checker verifies all six left translations, rank, commutant, and Gram identities. |

## Counterexample search

The construction is finite-dimensional and entirely explicit. The diagonal
copy is not merely a nonorthogonal vector: it is a distinct closed minimal
invariant subspace. The conjecture does not allow the family to depend on the
subspace being represented, so the contradiction cannot be avoided by
choosing a different orthogonal decomposition for the diagonal.

## External dependencies

- The source paper supplies the exact conjecture and definitions.
- Standard Peter-Weyl decomposition, Schur orthogonality, and Frobenius
  reciprocity are used for the characterization. The finite `S_3`
  counterexample itself is also constructed explicitly and checked exactly.

## Gaps

No mathematical gap found. The only substantial external input in the
general equivalence is standard compact-group harmonic analysis. Even if the
general sufficiency direction were omitted, the explicit finite
counterexample would still completely disprove the conjecture.

## Confidence

Score: 97/100.

The residual risk is bibliographic rather than mathematical: the obstruction
may be folklore or already noticed informally, although no exact later answer
was found in the bounded search.

## Human review recommendation

Approve as a candidate counterexample after checking the source wording and
the one-line implication that every minimal invariant subspace must itself be
listed. The explicit `S_3` construction is the decisive proof; the exact
multiplicity-free characterization is a useful strengthening.
