# Literature resolution for arXiv:1611.02223, equation (7.2)

**Classification:** literature already answered; high confidence.

Lindberg asks in equation (7.2) whether the `L^{p'}` norm is equivalent to
the supremum of pairing against Jacobians with normalized `L^{np}` gradient.
Tuomas Hytönen's arXiv:1804.11167 answers this affirmatively in every
dimension `n>=2` and for every `1<p<infinity`.

The exact specialization is Theorem 3.1.4 with
`r_1=...=r_n=np`, hence `r=p`. The proof of Theorem 3.2.1 on PDF pages
29--30 writes out the resulting norming inequality, and Remark 3.2.3(2)
explicitly cites Lindberg's published page 739 and explains that Hytönen's
argument proves the more general all-dimensional result.

This resolves only the norm-equivalence/weak-factorization subproblem. It
does not prove that every datum is one Jacobian and does not settle the
continuous-right-inverse conjecture.

Files:

- `solution_packet.pdf`: review-ready literature-resolution packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: Lindberg, arXiv:1611.02223.
- `supporting_paper_1804.11167.pdf`: Hytönen, arXiv:1804.11167v4.
- `tmp/`: extracted text, source/supporting evidence renders, build files,
  and final-packet page renders used for visual verification.
