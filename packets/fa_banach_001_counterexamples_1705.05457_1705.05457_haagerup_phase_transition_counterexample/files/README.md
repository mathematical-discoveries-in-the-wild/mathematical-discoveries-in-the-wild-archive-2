# Counterexample: arXiv:1705.05457

This packet gives full negative answers to both Haagerup-function singularity
questions in the final item of arXiv:1705.05457.

For the radial positive-definite function `f_r(x)=r^|x|` on the free group
`F_k`, an exact adjacency identity expresses `delta_e` as a finite linear
combination of `f_r` and its left translates. Proposition 4.10 of the source
then gives `delta_e << f_r`. Hence `f_r` is neither singular to `A(F_k)` nor
singular to `B_lambda(F_k)` for any `0<r<1`.

Files:

- `solution_packet.pdf`: self-contained proof and source context.
- `source_paper.pdf`: archived arXiv:1705.05457v4 PDF.
- `source_question_crop.png`: real screenshot crop of source PDF page 42.
- `main.tex`: packet source.
- `code/verify_identity.py`: exact-rational finite-ball audit.
- `code/crop_source.py`: reproducible source-question crop.
- `VERIFICATION.md`: audit trail, visual QA, and hashes.

This is recorded as a new full counterexample, subject to expert review.
