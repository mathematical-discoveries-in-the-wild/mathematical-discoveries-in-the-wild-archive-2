# Literature-implied answer: Conjecture 5.1 of arXiv:1309.3596

Status: literature-implied full answer, likely valid, pending human review.

Lucia and Puls conjecture that the Dirichlet problem is solvable on the
`p`-harmonic boundary of every space in their standing complete doubling PI
class, without a global `(p,p)`-Sobolev inequality. Their exhaustion produces
the candidate `p`-harmonic function but leaves open whether the error is in
the `BD^p`-closure of compactly supported continuous functions.

Theorem 1.1 of Shanmugalingam, arXiv:2311.17356, states that every bounded
sequence in the homogeneous Newton--Sobolev space has a strongly convergent
tail-convex-combination subsequence. Applying it to the exhaustion errors,
pinning the quotient constants by local-uniform convergence, and using a
compact-support gluing lemma yields the required Royden decomposition. Tietze,
Stone--Weierstrass, a common diagonal exhaustion, and comparison then give the
arbitrary continuous boundary-data assertion.

The supporting paper does not cite or mention the source conjecture. This is
therefore an agent-identified literature implication, not an explicit
literature answer and not a claim that the supporting theorem is new.

Human review should prioritize:

- the bounded `Lip_c` density and gluing step in Lemma 1;
- identification of the homogeneous limit modulo constants;
- the simultaneous diagonal extraction and comparison argument for arbitrary
  continuous boundary data.

The packet does not claim uniqueness of the nonlinear Royden decomposition;
uniqueness is not part of Conjecture 5.1's requested existence statements.

Files:

- `main.tex` / `solution_packet.pdf`: proof packet;
- `source_paper.pdf`: arXiv:1309.3596;
- `supporting_paper_2311.17356.pdf`: homogeneous compactness theorem;
- `VERIFIER_REPORT.md`: independent logical audit;
- `figures/open_problem_crop.png`: Conjecture 5.1 and its proposed route;
- `figures/supporting_theorem_crop.png`: supporting Theorem 1.1.
