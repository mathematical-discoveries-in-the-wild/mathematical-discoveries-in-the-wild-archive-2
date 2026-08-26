# arXiv:1707.01889 — finite-fourth-moment Kolmogorov bound answered by arXiv:2607.28742

Status: already answered in later literature.

Remark 1.4(b)–(c) of the source asks for a Kolmogorov fourth-moment bound on a fixed Poisson chaos with the same square-root accuracy as its Wasserstein bound, assuming only a finite fourth moment.

Theorem 1.9 of Guangqu Zheng, *A Kolmogorov fourth-moment bound on Poisson chaos via a martingale core* (arXiv:2607.28742v1), proves for every variance-one `F` in a fixed Poisson chaos that

`d_K(F,N) <= 15.6 sqrt(E[F^4]-3)`.

The theorem explicitly removes the earlier assumptions `A` and `A^loc`. Its proof constructs regular fixed-chaos conditional expectations converging in `L^4` and passes the known regular bound to the limit.

Files:

- `solution_packet.pdf`: compact literature-status note.
- `source_paper.pdf`: official arXiv PDF for 1707.01889.
- `answer_paper.pdf`: official arXiv PDF for 2607.28742.
- `main.tex`: note source.
- `verification.md`: file and rendering checks.
