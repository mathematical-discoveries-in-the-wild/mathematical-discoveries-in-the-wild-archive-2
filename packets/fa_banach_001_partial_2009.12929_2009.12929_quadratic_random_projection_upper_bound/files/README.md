# arXiv:2009.12929 — quadratic random-polytope upper bound

This packet gives a substantial partial answer to Remark 4.5 on simultaneous
upper bounds for hyperplane projection constants of random symmetric
spherical polytopes.

The source converts a spherical epsilon-net into an inradius loss of order
epsilon. The exact spherical identity gives loss epsilon squared over two.
Combining this with an elementary high-probability covering-radius bound
proves

    sup_Y lambda(Y,X_N) <= 1 + C_(n,A) (log N/N)^(2/(n-1))

with probability at least 1 minus N to the power minus A, for every fixed
dimension and all sufficiently large N.

- source_paper.pdf: arXiv:2009.12929v3
- assets/source_question_crop.png: direct crop of PDF page 12
- solution_packet.pdf: compiled proof packet
- verification.md: integrity, mathematical, and visual checks

The result improves the source's upper endpoint but does not give a matching
lower bound. Human review remains pending.
