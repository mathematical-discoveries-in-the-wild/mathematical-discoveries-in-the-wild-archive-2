# Verification Report

Candidate: arXiv:1909.10190v2, Question 6, lower range `0<d<1/2`.

## Claim checked

For each `0<d<1/2`, the measure space

```text
([0,1], A_{H^d}, H^d)
```

is semilocalizable under CH and is not semilocalizable under the relatively
consistent inequality `non(N_L1)<cov(N_L1)`. Hence its semilocalizability is
independent of ZFC in the same relative-consistency sense used in the source.

## Verdict

Likely valid strong partial resolution. Confidence: 93/100.

The argument answers all of Q6 below the critical exponent. Its only external
mathematical inputs are De Pauw's abstract vertical-horizontal theorem and
the source's CH semilocalizability theorem. Both are invoked with their exact
hypotheses. The upper range is explicitly excluded.

## Step-by-step audit

| Step | Status | Verification |
| --- | --- | --- |
| Choice of ratio | valid | `r=2^(-1/d)` satisfies `2r^d=1`, so the two-branch strongly separated attractor has dimension `d` and finite positive `H^d` measure. For `d<1/2`, `r<1/4`. |
| Four-map separation | valid | The intervals `P_a([0,1])`, `P_a(x)=rx+a(1-r)/3`, have adjacent gap `(1-4r)/3>0`. |
| Coding bijection | valid | Strong separation makes addresses unique. Pairing `(i_n,j_n)` with `2i_n+j_n` is bijective at every level and hence gives a bijection `C_d x C_d -> K_d`. |
| Bi-Lipschitz estimates | valid | At the first differing level `n`, product distance lies in `[(1-2r)r^(n-1),sqrt(2)r^(n-1)]`, while image distance lies in `[((1-4r)/3)r^(n-1),r^(n-1)]`. Combining gives uniform two-sided bounds. |
| Leaf size | valid | Each vertical or horizontal image leaf is bi-Lipschitz to `C_d`, so it has finite positive `H^d` measure. |
| Leaf intersections | valid | `V_s intersect H_t={Phi(s,t)}`; the singleton is locally null because `d>0`. |
| Local-null reduction | valid | If `V_s intersect Z` is locally null, testing it against the finite-measure measurable set `V_s` gives ordinary `H^d`-nullity. |
| Incidence projection | valid | On a leaf, the opposite-coordinate map is a coordinate projection after `Phi^(-1)`, hence Lipschitz. It sends a null leaf section onto the incidence parameter set, whose `H^d` outer measure is zero. The symmetric condition is identical. |
| Abstract theorem | valid | The parameter Cantor sets are Polish; normalized `H^d` restrictions are diffuse Borel probabilities; compact leaves are measurable; all three incidence hypotheses of source Theorem 8.3 hold. |
| Subspace Hausdorff measure | valid | Hausdorff outer measure on a metric subspace agrees with the ambient Hausdorff outer measure for its subsets, by intersecting covers with the subspace. |
| Caratheodory trace | valid | Ambient measurability implies trace measurability. Conversely, split an arbitrary ambient test set first by measurable `K`, then split its `K` part by the subspace-measurable set. This proves ambient Caratheodory measurability. |
| Local-null trace | valid | For subspace-to-ambient, test against `F intersect K` for every ambient finite-measure `F`; the reverse direction is immediate. |
| Principal ideal | valid | A class below `[K]` differs by a locally null set from its representative intersected with `K`. Thus the subspace quotient is exactly the principal ideal below `[K]`. |
| Completeness inheritance | valid | In a complete Boolean algebra, the ambient supremum of elements all below `b` is still below `b`; every principal ideal is therefore complete. |
| CH side | valid | `H^d` is a Borel-regular outer measure on the Polish interval, so the source's CH almost-decomposition result applies and implies semilocalizability. |
| Scope at `d=1/2` | valid | The candidate theorem is strict below `1/2`; the source's Theorem 9.8 supplies the endpoint. |
| Upper-half limitation | valid | `4r>1` when `d>1/2`, and `dim_H(C_d x C_d)=2d>1`, precluding a bi-Lipschitz embedding in the line. The packet does not turn this route obstruction into a negative claim. |

## Adversarial checks

- `H^d(K_d)` is infinite because `dim_H K_d=2d>d`; the proof never treats
  `K_d` as a finite-measure test set. Only the individual leaves need finite
  measure, and they have it.
- The incidence parameter sets need not be Borel. De Pauw's theorem uses the
  outer measures of the parameter probabilities, and Lipschitz null-image
  control is sufficient.
- A generic continuous coding of a Cantor product into an interval would not
  preserve Hausdorff null sets. The strict separation and common contraction
  ratio provide the required bi-Lipschitz control.
- The subspace sigma-algebra cannot merely be asserted to be a trace for an
  arbitrary outer measure. Here the packet supplies the full Caratheodory
  proof using measurability of the Borel set `K_d`.
- Semilocalizability is defined using the local-null ideal, not the ordinary
  null ideal. The proof traces the local ideal explicitly.
- Nonlocalizability does not always pass from a subspace to a superspace. It
  does here because the subspace quotient is a principal ideal and principal
  ideals inherit order completeness.

No contradiction, hidden numerical dependency, or unproved geometric claim
was found.

## Literature audit

The source paper, its publication metadata, run indexes, exact Q6 wording,
exact-title searches, and the adjacent arXiv:2105.11331 were checked. No later
paper explicitly answering Q6 was located. This is a bounded novelty check,
not proof of novelty.

## Remaining verifier focus

1. Compare the trace/local-null ideal lemma with De Pauw's categorical
   conventions for restricting measurable spaces with negligibles.
2. Confirm that the published 2024 version has no post-arXiv modification of
   Q6 relevant to the claimed scope.
3. Search set-theoretic measure-theory literature not indexed by the exact
   terminology `semilocalizable` for an equivalent pre-existing result.

## Human review recommendation

Send to a geometric measure theorist familiar with Boolean measure algebras
and Cichon's diagram. The construction itself is elementary; review effort
should concentrate on the imported vertical-horizontal theorem and the
principal-ideal transfer.
