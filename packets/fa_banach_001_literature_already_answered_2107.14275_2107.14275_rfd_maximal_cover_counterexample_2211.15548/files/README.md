# RFD maximal C*-cover question: exact literature counterexample

Status: **literature_already_answered (full negative answer)**.

Thompson, arXiv:2107.14275, Question 1 asks whether
`C*_{max}(A)` must be residually finite dimensional whenever the operator
algebra `A` is RFD.

Michael Hartz, arXiv:2211.15548, Theorem 1.3 and Corollary 1.4, answers no.
He constructs the unital, completely isometrically 2-subhomogeneous algebra

`B = { [[f,0],[h,conj(g)]] : f,g in A(D), h in C(T) }`

inside `M_2(C(T))`. The algebra `B` is RFD, but its maximal C*-algebra is
not RFD.

Files:

- `solution_packet.pdf`: exact question, construction, and deduction
- `source_paper.pdf`: arXiv:2107.14275
- `supporting_paper_hartz_2211.15548.pdf`: Hartz's primary paper
- `figures/open_question_crop.png`: Thompson's Question 1
- `figures/hartz_algebra_crop.png`, `hartz_theorem_crop.png`, and
  `hartz_counterexample_crop.png`: Hartz's construction and conclusion
- `verification.md`: compilation, rendering, QA, and checksums

