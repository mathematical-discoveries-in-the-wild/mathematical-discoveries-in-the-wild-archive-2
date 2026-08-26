# Verification report

Status: `candidate_full_solution_likely_valid_human_review_needed`

## Claim checked

Question 1.15 of arXiv:2304.00621 is fully answered at the level requested:
the maximal initial half-open range is `[p,Q_n(p))`, and the paper's literal
supremum is `Q_n(p)` for `p >= |beta|/beta_n` and infinity below that
threshold because the symbol space eventually collapses to constants.

## Adversarial step check

| Step | Status | Notes |
| --- | --- | --- |
| Vertical boundary of `Omega(n)` | valid | The three line segments give the displayed piecewise `Q_n(p)`; the formulas agree at both junctions. |
| Sufficiency below `Q_n(p)` | external, verified | This is exactly Theorem 1.10 of arXiv:2304.00621: interior of `Omega(n)` plus the diagonal. |
| Sharp single-scale sequence | external, verified | Section 4.2 of arXiv:1704.07810 states failure outside `Omega(n)` with inputs in an arbitrarily small origin neighborhood and dual witnesses near the positive curve arc. |
| Separator membership | valid | For `b(x)=eta(x_n)`, bounded Lipschitz regularity in `x_n` gives anisotropic Holder order every `alpha <= beta_n`; source Lemma 3.8 converts this to `BMO^{beta,alpha}`. |
| Commutator identity on supports | valid | `bf_k=0` and `bg_k=g_k`, hence `<[b,H]f_k,g_k>=<Hf_k,g_k>` exactly. |
| Failure outside `Omega(n)` | valid | The transferred pairings diverge while the proposed estimate and normalized `L^p`, `L^{q'}` norms would bound them uniformly. |
| Triviality for `alpha > beta_n` | valid | Each coordinate-line Holder exponent is `alpha/beta_j>1`; subdivision forces all coordinate increments to vanish. |
| Threshold algebra | valid | Solving `|beta|(1/p-1/q)=beta_n` yields `q_triv=p|beta|/(|beta|-p beta_n)`. |
| Nonempty failure gap | valid | On `Omega(n)`, `x-y <= 2/[n(n+1)]`; strict exponent ordering gives `2|beta|/[n(n+1)] < beta_n`, so `q_triv>Q_n(p)`. |
| Endpoint treatment | valid | Neither source proves the non-diagonal boundary. The packet makes no endpoint claim; the requested interval is half-open and `p_max` is a supremum. |

## Counterexample and edge-case audit

- For `n=2`, the middle branch collapses at `p=3/2`, yielding the familiar
  endpoints `p/(2-p)` and `2p`.
- For `p=|beta|/beta_n`, every finite `q` has `alpha<beta_n`, so the finite
  branch of the dichotomy is correct.
- At `q=q_triv`, `alpha=beta_n`; the smooth one-coordinate separator still
  belongs to the symbol space, so this endpoint lies in the failure gap.
- The sign pattern of the negative branch is irrelevant: the supporting
  sharpness construction and separator use only `t in [1/2,1]`.
- No computational evidence is used as proof.

## Literature audit

Cheap run indexes and bounded exact-phrase/core-keyword searches through
2026-08-13 found no answer to Question 1.15. The later arXiv:2403.08338 concerns
the missing planar lower bound at `p=q`; it does not determine the fractional
upper range. The decisive prior input is explicitly cited as Cladek--Ou's
sharp single-scale obstruction, not presented as new.

## Verdict

Likely valid, send to a human expert. Review should concentrate on the support
localization imported from Cladek--Ou Section 4.2 and on the interpretation of
the source's literal supremum versus its claimed maximal interval.
