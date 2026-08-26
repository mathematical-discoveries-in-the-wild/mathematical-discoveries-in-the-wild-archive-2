# Verification Report

Candidate: arXiv:2203.09765, conjecture after Proposition 3.2.4.

## Claim checked

The claimed necessity is false: `I=L_1(G)*mu` can be metrically projective even when the unique `L_1` density of the chosen idempotent measure `mu` has norm greater than one.

## Verdict

candidate_full_negative_answer_likely_valid_human_review_recommended

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Source PDF page 99 (printed page 93) contains Proposition 3.2.4 and the exact conjecture. |
| Group-algebra setting | valid | For finite discrete `S_3`, `M(G)=L_1(G)=ell_1(G)` as measures/densities. |
| Norm-one idempotent | valid | `q=(delta_e+delta_(12))/2` is subgroup Haar measure, so `q*q=q` and `||q||_1=1`. |
| Peirce element | valid | `x=(1-q)*delta_(23)*q` satisfies `q*x=0`, `x*q=x`, and `x*x=0`. |
| New idempotent | valid | Expanding `(q+x)^2` gives `q+x=mu`. |
| Same left ideal | valid | `mu*q=mu` and `q*mu=q` give both inclusions `A*mu=A*q`. |
| Metric projectivity | valid | Source Proposition 2.1.13(i) applies to the common ideal `A*q` because `q` is a norm-one idempotent. |
| Norm obstruction | valid | The supports of `q` and `x` are disjoint; exact expansion gives `||q||=1`, `||x||=1`, `||mu||=2`. |
| Density uniqueness | valid | Any Haar density of `mu` is unique a.e. and has `L_1` norm equal to `||mu||_(TV)=2`. |
| General family | valid | The same Peirce construction works for a finite nonnormal subgroup; `x=0` would force the chosen element to normalize the subgroup. |

## Exact computation

`code/check_s3.py` uses rational coefficients and an explicit permutation multiplication law. It verifies:

    q*q=q, q*x=0, x*q=x, x*x=0,
    mu*mu=mu, mu*q=mu, q*mu=q,
    ||q||_1=1, ||x||_1=1, ||mu||_1=2.

It also checks the displayed four-term formula for `x` coefficient by coefficient.

## Adversarial audit

- The conjecture is about the particular presenting measure `mu`, not merely the existence of some norm-one idempotent generator. The example separates those notions.
- The proof does not assume that two right identities of a left ideal are equal; indeed `q` and `mu` are distinct right identities for the common left ideal.
- Haar normalization cannot change the obstruction because the `L_1` norm of the density is the total-variation norm of the measure.
- The noncommutativity is essential to this construction. The subgroup `<(12)>` is nonnormal in `S_3`, making `(1-q)Aq` nonzero.

## Deep upgrade attempts

1. The source's three parser signals were separated; the idempotent-measure conjecture was selected as the narrow algebraic target.
2. The source's metric-projectivity criterion for norm-one idempotent generators was combined with the observation that a left ideal can have multiple idempotent right identities.
3. The Peirce perturbation `q+x`, with `x in (1-q)Aq`, was derived abstractly.
4. A smallest concrete noncommutative group was sought; `S_3` with a nonnormal order-two subgroup supplies the required nonzero Peirce corner.
5. The full six coefficients were expanded and checked exactly.
6. The norm obstruction was strengthened from merely `>1` to the exact value `2` by disjoint support.
7. The construction was generalized to every discrete group with a finite nonnormal subgroup.
8. Density uniqueness, left-ideal orientation, source-proposition applicability, and later-literature status were independently audited.

## Novelty check

On 2026-08-11, the exact conjecture and core terms were checked in the run registry, solution, attempt, and proof-gap indexes. Bounded exact-phrase web/arXiv searches found the conjecture unchanged in the source/recent published text and found no later resolution or this counterexample. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official arXiv PDF and has 111 pages.
- `figures/source_conjecture_crop.png` is rendered from PDF page 99 and clearly shows the proposition and conjecture.
- The exact checker passes all identities.

Confidence: 97/100.

Recommended action: human review, especially of the source's categorical convention for metric projectivity; Proposition 2.1.13(i) appears to match it exactly.
