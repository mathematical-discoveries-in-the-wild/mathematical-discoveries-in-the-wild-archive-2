# Verification Report

Candidate: arXiv:2601.01681, Question 5.12, finite-tree subcase

## Claim Checked

For every nondegenerate finite topological tree `K`, the natural action of the
full compact-open group `Aut(K)` of homeomorphic median automorphisms is Tame1
and is not Tame2.

## Verdict

likely valid

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Finite skeleton | valid | Endpoints and branch points are finite and topologically invariant; suppressing valence-two subdivision points leaves finitely many closed edges. |
| Automorphisms preserve median | valid | A homeomorphism of a tree preserves unique arcs, hence preserves the triple-arc median. |
| Ellis elements fix one skeleton permutation | valid | Restrictions of approximating automorphisms to the finite skeleton take values in a finite set; pointwise convergence makes them eventually constant on all skeleton vertices. |
| Edge restriction embedding | valid | Once the skeleton permutation is fixed, normalized edge restrictions are monotone interval maps. Restriction to all edges is continuous and injective; compact-to-Hausdorff gives an embedding. |
| First countability | valid/external | Uses the established first countability of the Helly compactum of monotone interval maps. Finite products and subspaces are first countable. The skeleton-permutation pieces are clopen, avoiding the false general assertion that an arbitrary finite union of closed first-countable subspaces must be first countable. |
| Failure of Tame2 | valid/external | Edge-supported increasing homeomorphisms extend by the identity and give a subsystem whose Ellis semigroup is the known non-hereditarily-separable interval Ellis semigroup. |
| Scope | valid | This is a partial answer for geometric realizations of finite trees, not a classification of all finite-rank compact median algebras. |

## Counterexample Search

Small cases checked conceptually: the interval (one edge), a triod (one branch
vertex), and arbitrary finite subdivisions. Valence-two subdivision points do
not affect the essential skeleton, and the proof specializes correctly.

Result: none found.

## External Dependencies

- Megrelishvili, arXiv:2601.01681, Example 5.13: the interval homeomorphism
  Ellis semigroup is first countable and not hereditarily separable.
- Glasner--Megrelishvili (2022): the tame hierarchy/Helly-space facts cited by
  the source.

## Gaps

- Novelty was checked only by bounded index and web/arXiv phrase searches.
- A continuum theorist should confirm that `Aut(K)` is understood exactly as
  all homeomorphic median automorphisms; for trees this equals `Homeo(K)` by
  preservation of unique arcs.

## Confidence

Score: 91/100

Reason: the proof is topological and finite-skeleton based, with its two
nontrivial dynamical inputs already stated in the source. The only material
uncertainty is literature novelty, not the internal implication.

## Human Review Recommendation

send to human
