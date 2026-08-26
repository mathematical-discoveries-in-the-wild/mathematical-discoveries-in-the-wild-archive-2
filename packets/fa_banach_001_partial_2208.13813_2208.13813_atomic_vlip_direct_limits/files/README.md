# Atomic direct limits in VL_IP

This packet gives a substantial partial answer to the direct-limit existence
question on page 25 of arXiv:2208.13813.

It proves that every direct system in the category of real vector lattices and
interval-preserving linear maps has a direct limit whenever every object is
lattice-isomorphic to `c00(A)` for some set `A`.  This includes all
finite-dimensional Archimedean vector lattices.  The proof identifies
interval-preserving maps out of `c00(A)` as precisely the linear maps sending
each coordinate atom to an atom or zero, then equips the ordinary vector-space
colimit with the coordinate order on its surviving atomic rays.

Status: `candidate_partial_likely_valid`, pending human review.

Files:

- `main.tex`: complete theorem and proof.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: readable crop of the source question.
- `VERIFICATION.md`: proof, build, visual-QA, and hash record.
