# NERF erasure-rate monotonicity: already answered

Status: `literature_already_answered`.

Fickus and Mixon ask on source-PDF page 14, Section 4, whether every
`(p,C)`-numerically erasure-robust frame is also a `(p',C)`-NERF whenever
`0 <= p' < p` (with the relevant surviving-set cardinalities integral).

Yang Liu explicitly identifies this question and answers it affirmatively in
Lemma 1 of *Comparison on the Robustness Against Erasure Rates of Numerically
Erasure-Robust Frames*, International Journal of Applied Mathematics 33 (2020),
585-590, DOI 10.12732/ijam.v33i4.3.

The packet includes a short independent audit of the theorem. For a larger
surviving set `S`, sum the frame operators of all its smaller surviving
subsets. Their sum is a scalar multiple of the frame operator of `S`, and the
positive-semidefinite cone with condition number at most `C^2` is closed under
addition. Hence `Cond(F_S) <= C`.

Files:

- `solution_packet.pdf`: compact literature-status and verification note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: Fickus-Mixon open-question source.
- `supporting_paper_liu_2020.pdf`: Liu's explicit answer.

Scope: this resolves only the erasure-rate monotonicity question. The source's
separate questions about NERFs above the one-half erasure barrier are not
addressed.
