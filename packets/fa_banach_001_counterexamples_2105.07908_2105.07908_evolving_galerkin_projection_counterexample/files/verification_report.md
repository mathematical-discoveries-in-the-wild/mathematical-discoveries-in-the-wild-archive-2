# Verification Report

Candidate: arXiv:2105.07908, Remark 7.5 on uniform boundedness of transported Galerkin projections.

## Claim checked

The intended abstract question has a negative answer: compatibility and smooth transport do not imply uniform `X(t)`-boundedness of the `H(t)`-orthogonal projections onto the first `n` transported basis vectors.

## Verdict

`candidate_counterexample_likely_valid_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid with clerical note | Source PDF page 40, Remark 7.5. The printed domain `V_n(t)` makes the map the identity; the immediately following duality discussion requires the projection acting on `X(t)`. |
| Gelfand triple | valid | The weighted `ell_2(d)` space is separable, reflexive, and densely continuously embedded in ordinary `ell_2`; the pivot identifies with its dual inside `X*`. |
| Initial basis | valid | The standard vectors are orthogonal in both weighted and ordinary Hilbert products and form a Schauder basis of `X`; coordinate partial sums have norm one. |
| Shear bounded on `H` | valid | `K` maps each odd coordinate isometrically to the following even coordinate and kills even coordinates, so `||K||_H=1`. |
| Shear bounded on `X` | valid | The input odd coordinate has weight `k` while its even image has weight one, so `||Kx||_X <= ||x||_X`. |
| Invertibility | valid | `K^2=0`, hence `(I+aK)^{-1}=I-aK`; both families are uniformly bounded for `0<=a<=1/2`. |
| Compatibility and smoothness | valid | Spaces are fixed; `phi_0=I`; `phi_t` and its inverse are uniformly bounded on `X` and `H` and are `C^1` in operator norm. The transported inner products are polynomial in `t`. |
| Transported basis | valid | `w_j^t=phi_t e_j`; its pullback is constant, so its material derivative is zero exactly as required by the Galerkin construction. |
| Projection formula | valid | At odd cutoff `2k-1`, all previous blocks are complete and the current block contributes the line spanned by `e_{2k-1}+a e_{2k}`. Orthogonal projection of `e_{2k}` onto that line is `a(1+a^2)^{-1}(e_{2k-1}+a e_{2k})`. |
| Norm divergence | valid | The input has `X`-norm one; the output norm is `a(1+a^2)^{-1} sqrt(k^2+a^2)`, which diverges for every fixed `a>0`. |
| Reference-time contrast | valid | At `t=0`, `a=0`, transported and original bases coincide, and all coordinate projections have norm one. |
| Scope | valid | The result is abstract and does not claim failure for special PDE eigenbases or geometric transports. |

## Adversarial stress tests

- The weights are never below one, so `X -> H` is genuinely continuous; finite sequences are dense in both spaces.
- The alternating weights do not make `K` unbounded: `K` moves from the high-weight odd coordinate to the low-weight even coordinate, never in the reverse direction.
- Although the Hilbert adjoint of `K` behaves badly on `X`, the framework requires boundedness of `phi_t` and its inverse on `X` and `H`, not boundedness of the Hilbert adjoint on `X`; the dual evolution acts on `X*`.
- The bad vector `e_{2k}` belongs to `X`, so the lower bound is for the actual `X -> X` operator norm, not an extrapolation from `H`.
- Complete earlier blocks do not interfere with the calculation because they are `H`-orthogonal to the current coordinate block.
- The result does not exploit the typo literally. On `V_n(t)` the projection is the identity; the packet expressly answers the only reading relevant to the source's attempted duality estimate.

## Deep upgrade audit

A unitary evolution was rejected because it conjugates the reference projections and preserves uniform boundedness. A single finite-rank shear was upgraded to infinitely many independent nilpotent two-coordinate shears, producing divergence along every odd cutoff while keeping the evolution uniformly bounded and explicitly invertible. The example was then strengthened to fail for every `t>0`, not merely at one chosen time, by taking `a(t)=t/2`.

## Novelty check

On 2026-08-11, the exact arXiv id/title, Remark 7.5 wording, `P_n^t`, transported Galerkin bases, evolving Banach spaces, and uniform projection boundedness were checked against the run registry, solution, attempt, and proof-gap indexes and by bounded web/arXiv search. Results included the source and general projection/Galerkin literature, but no answer to this exact remark. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 46-page arXiv PDF.
- `figures/open_problem_crop.png` is rendered from source PDF page 40 and includes the full Remark 7.5.
- No numerical or computer-assisted claim enters the proof.

Confidence: 97/100.

Recommended action: specialist review by a functional analyst familiar with evolving Gelfand triples and Galerkin bases.
