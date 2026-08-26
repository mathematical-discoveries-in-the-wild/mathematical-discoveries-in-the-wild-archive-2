# Positive-Entropy Case of Austin's Weak-Mixing Question

Status: `candidate partial result - likely valid`

Source: Tim Austin, *Non-convergence of some non-commuting double ergodic
averages*, arXiv:2407.08630; Proc. Amer. Math. Soc. 153 (2025), 1701-1707.

## Result

Austin asks whether every weakly mixing probability-preserving transformation
can occur, up to isomorphism, as the first transformation in a divergent
double-average example. This packet proves the positive-entropy case, in the
stronger form:

> Every ergodic probability-preserving automorphism of positive
> Kolmogorov-Sinai entropy is isomorphic to an automorphism `S` for which there
> are an automorphism `T` isomorphic to `S` and a bounded real function `f`
> such that
> 
> `1/N sum_{i=0}^{N-1} integral f(S^i x) f(T^i x) dmu(x)`
> 
> does not converge.

Consequently Austin's question has an affirmative answer for every weakly
mixing transformation of positive entropy. A subsequent lane-0 identification
found that the universal affirmative question is nevertheless false: the
weakly mixing Chacon transformation is universal for weak disjointness and so
forces convergence against every second system. See
`solutions/literature_implied_answers/2407.08630_chacon_universal_weak_disjointness_obstruction/`.
The present packet remains a valid occurrence theorem for the positive-entropy
class; it no longer represents a route to a universal affirmative answer.

## Mechanism

Austin's weak Pinsker theorem splits every positive-entropy ergodic system as
a direct product of a nontrivial Bernoulli shift and a remainder. On an
arbitrary nontrivial Bernoulli shift, conjugate the shift by a coordinate
permutation `p` whose fixed-point set in the nonnegative integers has no
asymptotic density. For a centered observable depending on coordinate zero,
the correlation at time `i` is exactly its variance when `p(i)=i` and zero
otherwise. The Cesaro averages therefore inherit the nonconvergence of the
fixed-point densities. Taking the product with the weak-Pinsker remainder and
transporting through the isomorphism completes the proof.

## Evidence and review status

- The source question appears on arXiv PDF page 6; the packet includes a real
  crop in `figures/open_problem_crop.png`.
- `VERIFICATION.md` audits the permutation construction, the conjugacy
  calculation, the correlation identity, and the entropy step.
- The later Chacon obstruction does not contradict this theorem; it shows only
  that the positive-entropy phenomenon cannot extend to every zero-entropy
  weakly mixing system.
- A bounded literature check through 9 August 2026 searched the run indexes,
  exact question wording, title/citation matches, and recent related arXiv
  papers on Gaussian, Poisson-suspension, simple-spectrum, and rank-one-base
  counterexamples. No paper stating this weak-Pinsker positive-entropy
  reduction was found. Novelty confidence is moderate, not definitive.

Human-review recommendation: verify the use of entropy additivity in the weak
Pinsker splitting and the convention in the coordinate-conjugacy computation.
The rest is elementary.
