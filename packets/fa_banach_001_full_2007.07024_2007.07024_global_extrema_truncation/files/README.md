# Full candidate: global-extrema truncation for arXiv:2007.07024

**Status:** candidate full solution; likely valid pending expert review.

This packet resolves the Section 5 conjectural high-energy extension in
arXiv:2007.07024. Under the source's general tail-convexity hypothesis, it
restores the complete conclusions of the corrected subcritical theorem:

- at least `cat(M)+1` constrained solutions;
- if all solutions are nondegenerate, at least `2P_1(M)-1` solutions.

The key observation is energy-free. At the global maximum and minimum of a
solution, the common Lagrange multiplier gives
`W'(max u) <= epsilon*lambda <= W'(min u)`. The prescribed mean lies between
the extrema. Fixed derivative barriers in the two convex tails therefore force
every critical point of a suitable subcritical truncation into the interval
where the truncation equals the original potential. Consequently *all* of the
subcritical theorem's low- and high-energy critical points transfer.

Files:

- `solution_packet.pdf`: expert-facing proof packet;
- `source_paper.pdf`: original paper compiled from its cached arXiv source;
- `corrigendum.pdf`: latest arXiv corrigendum PDF;
- `figures/open_problem_crop_1.png` and `open_problem_crop_2.png`: source pages
  28--29 containing the conjecture and Theorem 5.9;
- `verification_report.md`: proof and packet checks.

The bounded novelty search included the run's four cheap indexes, exact-phrase
web searches, the original/corrigendum, and the 2026 survey arXiv:2604.23920.
No later resolution was found through 2026-08-11; the survey still describes
the closed scalar theorem for subcritical potentials.

Human review should focus on the elementary maximum/minimum sign inequality
and on the standard construction of a `C^2` subcritical convex tail extension.

