# Algorithmic stable-rank extraction was already answered

Status: `literature_already_answered`.

## Resolution

Cohen--Nelson--Woodruff, arXiv:1507.02268v3, Theorem 5, give a deterministic
polynomial-time diagonal sampler with `O(k/epsilon^2)` nonzeros for every
matrix of operator norm at most one and Frobenius norm squared at most `k`.

Apply it to `B=A^*/||A||` and set `D=S^2`.  This gives exactly

`||A D A^* - A A^*|| <= epsilon ||A||^2`

with `O(srank(A)/epsilon^2)` nonzeros, resolving the algorithmic question in
the diagonal formulation stated after Theorem 1.1 of arXiv:1605.03861.

The answering v3 predates the source by about ten weeks.  The mapping does
not claim that all selected weights can be made equal.

## Files

- `solution_packet.pdf`: exact theorem-to-question reduction.
- `source_paper.pdf`: arXiv:1605.03861.
- `answer_paper.pdf`: arXiv:1507.02268v3.
- `main.tex`: packet source.
- `VERIFICATION.md`: provenance and render QA.
