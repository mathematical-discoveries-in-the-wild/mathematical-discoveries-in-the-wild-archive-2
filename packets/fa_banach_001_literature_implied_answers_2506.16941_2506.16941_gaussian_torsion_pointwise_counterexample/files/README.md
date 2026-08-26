# Gaussian interval counterexample to weighted torsion concavity

Source: Dario Cordero-Erausquin and Alexandros Eskenazis, *Concavity
principles for weighted marginals*, arXiv:2506.16941, Question 18.

Question 18 has a negative answer. This packet gives a direct exact
one-dimensional witness: for the standard Gaussian and the centered interval
`(-R,R)`, the map `R -> sqrt(u_R(0))` is strictly convex on `(0,infinity)`.
Consequently the intervals of radii 1 and 3 violate the proposed joint
concavity at the midpoint and at `x=0`.

The question was already answered negatively at the torsional-rigidity level
by F. Marín Sola and F. Salerno, arXiv:2603.19164. The elementary pointwise
argument here is a sharper direct witness, but the packet is classified as a
literature-implied answer rather than a novelty claim.

Verification command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/literature_implied_answers/2506.16941_gaussian_torsion_pointwise_counterexample/code/verify_gaussian_intervals.py

The other open questions in arXiv:2506.16941, especially hereditary convexity
and negative-exponent weighted marginals, are not resolved here.

