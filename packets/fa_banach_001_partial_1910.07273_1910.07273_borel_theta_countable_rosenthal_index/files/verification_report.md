# Verification Report

Candidate: arXiv:1910.07273, Problem 7.10 on the Rosenthal index of `L^theta`.

## Claim checked

For every Borel `theta:(0,1)->2`, `C_Q(L^theta)` is Borel in `R^Q`, and therefore `ri(L^theta)<omega_1`. This answers the first clause of Problem 7.10; no effective bound in terms of the Borel class is claimed.

## Verdict

`candidate_partial_result_likely_valid_human_review_needed`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Exact source target | valid | Source PDF page 16, Problem 7.10, first asks countability of the index and then an effective estimate. |
| Source input | valid | Source Lemma 7.8 proves that Borel `theta` makes `L^theta` Rosenthal and `C_Q(L^theta)` analytic. |
| Borel exceptional relation | valid | The chosen map `y -> S_y` is continuous on the irrationals and arbitrary only on the countable rational set, so `{(y,q):q in S_y}` is Borel. |
| Free-sequence condition | valid | Eventual avoidance of every finite subset of `Q` is a countable Borel condition and is exactly convergence away from isolated rational points. |
| Upper split-point formula | valid | At `y^+`, the generator `R_y^theta` must eventually contain the sequence. This forces left approach, excluding `S_y` precisely when `theta(y)=1`. |
| Lower split-point formula | valid | At `y^-`, `R_y^theta` must eventually exclude the sequence. Right approach always works; left approach works exactly along `S_y` when `theta(y)=1`. |
| Other generators | valid | If `x!=y`, real convergence gives a positive gap. Only finitely many terms of `S_x` lie on the wrong side of a midpoint, and freeness removes them eventually. |
| Endpoint and isolated cases | valid | At `0^-` and `1^+`, real endpoint convergence plus freeness is sufficient; convergence to an isolated rational is eventual constancy. |
| Convergence relation is Borel | valid | The explicit formulas use only real convergence, freeness, eventual quantifiers, Borel `theta`, and the Borel exceptional relation. |
| Graph-fiber criterion | valid | Singleton interior fibers make the compact graph projection a homeomorphism; conversely a continuous extension has exactly such a graph closure. Endpoint fibers represent unbounded escape. |
| Sequential witnesses | valid | A product of a Rosenthal compactum with a compact metric space is Rosenthal, hence Fréchet–Urysohn by Bourgain–Fremlin–Talagrand. Every bad graph-closure point is therefore witnessed by a sequence from the graph. |
| Coanalyticity | valid | Nonextendibility is the projection of the Borel relation coding two unequal limits over one point or an endpoint limit. Thus it is analytic and the trace space is coanalytic. |
| Borel conclusion | valid | Source analyticity plus new coanalyticity gives Borelness by Souslin's theorem, exactly implying countable Rosenthal index for dense `Q`. |
| Scope | valid partial | The proof gives no ordinal bound from the Borel class of `theta`; the second clause remains open. |

## Adversarial stress tests

- Repeating one rational infinitely often is explicitly excluded for convergence to the remainder; without freeness the displayed formulas would be false at rational split points.
- The deleted set `S_x` for a generator with `x!=y` causes no hidden oscillation: a midpoint separates `x` and `y`, and monotone convergence of `S_x` leaves only finitely many exceptional points on the far side.
- The graph criterion uses the compactification `psi(t)=t/(1+|t|)` so failure caused by unbounded values is not lost.
- A unique interior value in every graph fiber automatically gives a continuous, not merely set-theoretic, extension because a continuous compact-to-Hausdorff bijection is a homeomorphism.
- The Fréchet argument is applied to the product compactum, not only to `L^theta`; product Rosenthality is supplied by a direct Baire-one representation.
- The proof relies on the source's analyticity result and does not circularly infer it from Rosenthality alone.

## Deep upgrade attempt

The split-point formulas also yield one-sided Cauchy conditions indexed by `y`. Tracking their raw Borel complexity does not currently give an ordinal estimate because failure is projected over uncountably many split points. Likewise, the analytic/coanalytic separation theorem is qualitative. A bound relative to a particular effective Borel code may be possible, but it is not proved and the packet does not claim the second clause.

## Novelty check

On 2026-08-11, the exact arXiv id/title and Problem 7.10 text, plus close variants involving `ri(L^theta)`, Borel `theta`, split interval, and twisted sums, were checked against the run registry, solution, attempt, and proof-gap indexes and by bounded web/arXiv search. Results included the source paper and a later thesis reproducing the construction, but no claimed answer. This is a bounded check, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the official 19-page arXiv PDF.
- `figures/open_problem_crop.png` is rendered from source PDF page 16 and includes the complete two-clause problem.
- No numerical or computer-assisted claim enters the proof.

Confidence: 92/100.

Recommended action: specialist review by a descriptive-set theorist familiar with Rosenthal compacta and Stone compactifications.
