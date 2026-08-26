# Multiplicative Brownian eigenvalue convergence answered by arXiv:2511.10535

Status: `literature_already_answered`

## Source question

Ching-Wei Ho and Ping Zhong, *Brown Measures of Free Circular and
Multiplicative Brownian Motions with Self-Adjoint and Unitary Initial
Conditions*, arXiv:1908.08150, later JEMS 25 (2023), 2163--2227.

On arXiv PDF page 7 the source says it is open, even from the identity, to
prove that the empirical eigenvalue distribution of the Brownian motion
`G_N(t)` on `GL(N,C)` converges to the Brown measure of the free
multiplicative Brownian motion `b_t`.  On PDF page 50 it states the unitary
initial-condition version: if the empirical eigenvalue law of an independent
unitary `U_N` tends to the spectral law of `u`, prove that the empirical
eigenvalue law of `U_N G_N(t)` tends to the Brown measure of `u b_t`.

## Explicit later answer

Tatiana I. Brailovskaya, Nicholas A. Cook, Todd Kemp, and Felix Parraud,
*Eigenvalues of Brownian Motions on GL(N,C)*, arXiv:2511.10535v2 (2026),
answers both questions.

Theorem 1.2 on PDF page 9 proves almost-sure weak convergence of the empirical
eigenvalue law of `B_0 B(t)` whenever the independent initial matrix `B_0`
converges almost surely in star-distribution to `b_0`.  It adds that for normal
`B_0` this hypothesis is precisely weak convergence of its empirical
eigenvalue law.  Definition 1.7 on PDF page 15 identifies the limiting measure
as the Brown measure of `b_0 b(t)`.  Taking `B_0=U_N` gives the source's full
unitary-initial question; taking `U_N=I` gives its identity case.

The identification is explicit, not a new result of this run.  On PDF page 17
the supporting paper cites Ho--Zhong as reference [68], says that Ho--Zhong
extended the Brown-measure computation to unitary initial conditions, and
describes its own Theorem 1.2 as solving the missing convergence problem.
The later result is stronger than requested because it allows nonnormal
initial matrices with a star-distribution limit.

Files:

- `source_paper.pdf`: arXiv:1908.08150.
- `supporting_paper_2511.10535.pdf`: decisive later paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger:

- `runs/fa_banach_001/ledger/results/1908.08150_brown_measure_convergence_answered_by_2511.10535.json`
