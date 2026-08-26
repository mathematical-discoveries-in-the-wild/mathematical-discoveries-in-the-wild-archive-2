# Verification Report

Candidate: arXiv:2109.14504, threshold conjecture for random sections of polynomial ell_p-ellipsoids.

## Claim checked

For `1 < p <= infinity`, `q=p*`, and nonincreasing positive semiaxes with `sum sigma_j^q = infinity`, every fixed codimension has, in a sufficiently large ambient dimension, a Gaussian section of radius at least `sigma_1/2^(1/p)` with arbitrarily high probability. Hence the source's random-radius decay is zero. This closes both polynomial cases explicitly left open by the source.

## Verdict

`candidate_full_solution_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Source PDF page 9 states the threshold conjecture, lists precisely two unresolved regimes, and proposes the stronger `sigma not in ell_{p*}` zero-decay statement. |
| Uniform Gaussian block lemma | valid | A fixed net plus binomial Chernoff gives many coordinates of size at least one. The Gaussian `2 -> 2` operator bound transfers this to every sphere point while losing at most a fixed fraction. This proves a uniform positive empirical `q`-moment for every `q>0`. |
| Probability over dyadic blocks | valid | Block failure is at most `2 exp(-c 2^k)`, so the sum over all blocks after a sufficiently large starting block is arbitrarily small. No independence between block events is required. |
| Weighted lower bound | valid | On block `[2^k+1,2^(k+1)]`, monotonicity gives weight at least `sigma_{2^(k+1)}^q` on every coordinate, hence contribution at least `c_q^q 2^k sigma_{2^(k+1)}^q`. |
| Condensation | valid | Cauchy condensation applies to the nonincreasing nonnegative sequence `sigma_j^q`; the shifted condensed series diverges exactly when its original series does. |
| Tail body support function | valid | Holder duality gives `h_K(v)=||(sigma_j <g_j,v>)_{j>=2}||_q`, including `p=infinity, q=1`. |
| Inradius inference | valid | For compact symmetric convex bodies, `h_K(v)>=R` for all unit `v` is equivalent to `K` containing the Euclidean ball of radius `R`. |
| First-column absorption | valid | The tail body depends only on columns `2,...,m`; on the event `||g_1||<=B`, an inradius at least `sigma_1 B` puts `-sigma_1 g_1` in the tail image. |
| Ellipsoid normalization | valid | The constructed coefficient vector has first coordinate one and tail p-norm at most one, so total p-norm is at most `2^(1/p)`; for `p=infinity` it is at most one. The resulting kernel point has Euclidean norm at least its first coordinate. |
| Decay quantifiers | valid | A positive decay exponent requires one high-probability upper bound for every `m>n`. For large `n`, the packet chooses an `m` whose fixed lower event has probability `3/4`, contradicting the claimed upper event of probability greater than `1/2`. |
| Polynomial specialization | valid | `sum j^(-lambda p*)` diverges exactly for `lambda <= 1/p*`, covering both missing regimes verbatim. |

## Stress tests and rejected overclaims

- The theorem does not claim one fixed ambient dimension works for all codimensions; the source's uniform definition does not require that.
- The required `m` can be enormous at the critical line. This affects algorithmic usefulness but not the decay definition.
- No pointwise convergence in direction is promoted to uniform convergence without proof; the net/operator-norm lemma supplies uniformity.
- The proof does not use the false implication that an average quadratic lower bound directly controls lower moments below two.
- The general theorem is not stated for `p=1`, where the dual exponent is infinity and the support-function summation mechanism changes.
- The packet establishes the source's zero-decay branch. The positive-decay branch is cited only as already proved in the source.

## Novelty check

On 2026-08-11, the exact arXiv id/title and the terms `random sections`, `ell_p ellipsoids`, `threshold conjecture`, `Gelfand numbers`, `polynomial semiaxes`, and `divergent ell_{p*}` were checked in the run registry, solution, attempt, and proof-gap indexes. An external search of arXiv and exact-title records found the original paper and its 2023 publication record, but no later primary-source resolution. This is a bounded search, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 24-page arXiv v1 PDF.
- `figures/open_problem_crop.png` is rendered from source PDF page 9 and contains the exact conjecture and unresolved cases.
- The proof packet is self-contained apart from standard Gaussian concentration/operator-norm estimates, whose needed consequences are stated and integrated into the proof.
- No numerical computation is used as mathematical evidence.

Confidence: 94/100.

Recommended action: high-priority review by an asymptotic geometric analyst. The central conceptual check is that divergent dual mass indeed forces the Gaussian tail image to contain arbitrarily large Euclidean balls uniformly over directions; the packet supplies the full dyadic proof.
