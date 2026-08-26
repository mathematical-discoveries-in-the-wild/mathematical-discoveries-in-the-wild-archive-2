# John-ellipsoid polynomial bounds for the basis constants

**Status:** candidate full answer to the source's exponential-improvement
question, likely valid, pending human review.  The theorem proves a complete
dimension-polynomial bound for all the source constants and the exact value
for ellipsoidal norms; it does not determine the exact worst-case constants
for dimensions above two.

Source: Stefan Gerdjikov and Nikolai Nikolov, *Some inequalities for norms in
\(\mathbb R^n\) and \(\mathbb C^n\)*, arXiv:2303.03210, Section 6 (PDF
pp. 17--18).

Main result: over both \(\mathbb R\) and \(\mathbb C\), and for every angle
parameter \(0\le\rho\le1\),

\[
  \sqrt n\le c_n^\rho\le n.
\]

The upper bound is constructive modulo the classical John-ellipsoid
optimization: diagonalize the John ellipsoid in the fixed inner product and
use its eigenbasis.  This replaces the paper's greedy \(2^n-1\) constant by
\(n\).  For every ellipsoidal norm, the optimal constant is exactly
\(\sqrt n\).

Files:

- `solution_packet.pdf`: proof packet for review.
- `main.tex`: packet source.
- `source_paper.pdf`: original target paper.
- `figures/open_problem_page17.png` and `open_problem_page18.png`: the complete
  two-page source question.
- `code/check_bounds.py`: deterministic algebraic and randomized sanity
  checks; it is not part of the proof.
- attempt history:
  `runs/fa_banach_001/attempts/2303.03210_john_ellipsoid_upgrade_attempts.md`.

Human review should focus on the phase-averaged complex John argument and on
the scope label: the polynomial-growth question is answered, whereas exact
values beyond the cited planar cases remain open.
