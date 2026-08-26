# Scale-invariant Floer-Hessian strata are path-connected

Status: `candidate_partial_result_likely_valid`

Source: Urs Frauenfelder and Joa Weber, *Growth of eigenvalues of Floer
Hessians*, arXiv:2408.00269, Question 1.7.

Agent: `agent_lane_02`  
Model: `GPT5.6`  
Date: 2026-08-11

## Result

Let \((H_0,H_1)\) have scale-invariant pair growth \([h]\), and let
\(a,b\) be shift-invariant growth types. Every nonempty signed-growth stratum
\(\mathcal F_h^{ab}\) of weak Floer Hessians is path-connected in the
topology used by Frauenfelder--Weber.

This gives an affirmative answer to Question 1.7 for the principal class of
scale-invariant growth functions (including polynomial growth). The paper's
full question assumes only shift invariance, and that broader case remains
open.

The proof first translates arbitrary endpoints off their discrete spectra.
For invertible endpoints, their positive and negative eigenvectors are matched
in increasing spectral order. Equality of the two signed growth types makes
the matching orthogonal operator bounded and invertible on both \(H_1\) and
\(H_2\). Applied to the pair \((H_0,H_2)\), the mild-spectrum version of
Kuiper's theorem connects this operator to the identity through orthogonal
\(H_2\)-isomorphisms. Conjugation gives the first part of the path. Once the
eigenbases agree, linear interpolation of same-sign matched eigenvalues stays
uniformly comparable to either endpoint and supplies the second part.

## Scope and novelty

The proof does not settle arbitrary shift-invariant growth. The exact point of
failure is structural: the cited scale-Kuiper theorem assumes mild spectrum,
equivalent here to the doubling/scale-invariance condition. Exponential
growth is shift-invariant but not scale-invariant.

A bounded search on 2026-08-11 used the exact title and Question 1.7 wording,
plus `Floer Hessian connected`, `scale invariant Floer Hessian`, and fixed
signed-growth-stratum variants. It found the source paper and later papers
citing it for other Floer-operator questions, but no claimed answer to
Question 1.7 or this scale-invariant subcase. This supports only bounded
novelty confidence.

## Packet contents

- `main.tex` and `solution_packet.pdf`: definitions, theorem, and proof.
- `source_paper.pdf`: arXiv:2408.00269.
- `supporting_book_kronheimer_mrowka.pdf`: the cited scale-Kuiper theorem.
- `figures/open_problem_crop.png`: Question 1.7 on source PDF page 6.
- `VERIFICATION.md`: mathematical, literature, and rendering checks.

Human review should focus on the application of the real scale-Kuiper theorem
to \((H_0,H_2)\), and on the two graph-norm equivalences used to prove that
the eigenbasis matching operator is an \(H_2\)-isomorphism.
