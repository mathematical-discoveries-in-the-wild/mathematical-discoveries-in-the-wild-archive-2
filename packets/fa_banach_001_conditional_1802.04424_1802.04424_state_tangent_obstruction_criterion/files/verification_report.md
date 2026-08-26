# Verification Report

Candidate: arXiv:1802.04424, conjecture following Lemma 4.4.

## Claim checked

The conjecture for a bi-approximately unital Lp-operator algebra is equivalent to nonnegativity on the support idempotent of every unboundedly rescaled weak-star tangent functional at the zero state restriction.

## Verdict

conditional_reduction_likely_valid_human_review_recommended

The packet deliberately does **not** claim a full solution.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Official published page 433 states the converse conjecture. |
| State convexity | valid | Source Remark 2.26 and Corollary 4.25(1). |
| State closure | valid | Source Lemma 2.25(5): the weak-star closure of `S(A)` is the restriction compactum from `S(A^1)`. |
| Polar identity | valid | Real bipolar duality gives `c_(A*) = weak-star closure(cone S(A))`. |
| Cone decomposition | valid | Compactify scalar coefficients in `[0,infinity]`; finite limits give rays through state restrictions, while the infinite limit gives a zero-state tangent. |
| Finite-ray sign | valid | Bicontractivity makes `e` real positive in `(A^1)**`; state restrictions are therefore nonnegative on `e`. |
| Tangent criterion | valid | The decomposition and bipolarity reduce the conjecture exactly to the sign on the tangent part. |
| Approximate-identity extraction | valid | Finite multiplication-error maps, convex weak-to-norm closure, and source Lemma 2.22 give a real-positive cai once `e` is in the weak-star closure of `r_A`. |
| Unbounded escape construction | valid | `0` is in the weak-star closure of `S(A)`; choosing states smaller than `n^-2` on each finite test set makes `n omega_(F,n) -> 0` while norms grow like `n`. |
| Nonzero escape construction | valid | Convexity permits mixing a prescribed state with the fast-zero net. |

## Critical correction to the abandoned full proof

The earlier candidate proof asserted that a weak-star convergent net is norm bounded by uniform boundedness. This is false for arbitrary nets. A convergent net is only eventually bounded on each fixed test vector, and the tail may depend on that vector. The explicit state-net construction in the packet demonstrates the failure inside the exact state space under study.

Consequently, the identity

    closure(R_+ S(A)) = R_+ closure(S(A))

was not established and must not be used. The conditional packet replaces it with the correct finite-ray/tangent decomposition.

## Deep upgrade attempts

1. Exact-source and later-literature checks isolated the still-open real-positive-cai clause from neighboring scaledness questions already answered in the published remarks.
2. Direct local reflexivity reached only `||1-2a|| <= 1+epsilon`; exact correction is a proximinality/Kaplansky-density issue.
3. Counterexample templates using compact operators, continuous-field suspensions, and block sums failed because bicontractivity removes their fixed complement-norm obstruction.
4. Real polar duality reduced the problem to the sign of the dual cone on the support idempotent.
5. An adversarial net audit invalidated the apparent uniform-boundedness closure argument.
6. Hahn-Banach smoothness and codimension-one u-ideal geometry identify canonical norm-preserving extensions but do not prove positivity of that extension.
7. Multiplication by the central accretive support cannot be assumed positivity-preserving; the source's commuting-idempotent example blocks that route.
8. Compactification of the scalar coefficients yielded the exact finite-ray versus zero-tangent dichotomy and the stated conditional criterion.

## Novelty check

On 2026-08-11, the exact conjecture and its end-of-paper version were checked against the run registry, solution, attempt, and proof-gap indexes. Bounded exact-phrase web/arXiv searches through 2026 located no later resolution or the tangent-cone formulation. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official Pacific Journal of Mathematics article and has 62 PDF pages.
- `figures/open_problem_crop.png` is rendered from article page 433 and contains Lemma 4.4 plus the exact converse conjecture.
- The reduction is exact and has no numerical component.

Confidence: 88/100.

Recommended action: specialist review, with particular attention to the real-polar closure identity and the scalar-subnet dichotomy.
