# Attempt log

1. **Question isolation.** Extracted the two explicit questions. Problem 1 is
   topological/geometric convergence of the full Steiner sequence; Problem 2
   asks for convergence of perimeters.
2. **Lyapunov search.** Checked diameter, symmetric-difference distance, and
   perimeter. The useful exact quantity is the radius of the smallest
   origin-centered containing ball, which cannot increase under a centered
   Steiner symmetrization.
3. **Subsequence upgrade.** A ball-convergent subsequence forces the monotone
   centered circumradii of the entire sequence to converge to the ball radius.
4. **Deep upgrade: quantitative shell lemma.** Proved that any ball-volume
   compact set contained in `B_R` is within Hausdorff distance at most
   `max(R-r, 2(R^n-r^n)^(1/n))` of `B_r` once `R` is close to `r`. This handles
   possible holes and nonconvexity without regularity assumptions.
5. **Representative audit.** Verified that the argument is valid for the
   source's actual compact representatives, including null-set sensitivity of
   Hausdorff distance.
6. **Problem 2 upgrade attempt.** Combined Hausdorff convergence, volume
   preservation, perimeter monotonicity, BV compactness, and lower
   semicontinuity. These yield only
   `P(ball) <= lim P(E_i)`; Hausdorff convergence cannot provide the reverse
   inequality because fine corrugations may carry excess perimeter. No credible
   general upper-bound mechanism was found, so Problem 2 is left open.
7. **Novelty screening.** Checked exact-phrase and later-symmetrization
   searches. General convergence and nonconvergence results were found, but no
   explicit solution of this precise implication.

Outcome: candidate full affirmative proof of Problem 1; Problem 2 remains open.
