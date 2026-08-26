# Critical-exponent frame-potential conjecture: literature-implied negative answer

Status: `literature_implied_answer (full negative answer)`.

## Source question

Kasso A. Okoudjou, *Preconditioning techniques in frame theory and
probabilistic frames*, arXiv:1504.02023, Section 3.2, PDF page 29, records the
conjecture that for `N >= 3`,

\[
q_N=\frac{\log(N(N+1)/2)}{\log N}
\quad\Longrightarrow\quad
\operatorname{FP}_{q_N,N+1}(\Phi)\ge N+3
\]

for every collection of `N+1` unit vectors in `R^N`, with equality only for
an orthonormal basis plus one repeated vector or an equiangular FUNTF.

## Identification and answer

Zhiqiang Xu and Zili Xu, *The minimizers of the p-frame potential*,
arXiv:1907.10861, Definition (6) and Theorem 1.2 (PDF pages 3--4), introduce
the lifted ETF `L_2^N` and completely classify all minimizers for `N+1` unit
vectors and `0<p<2`.

The configuration `L_2^N` is a planar Mercedes triple together with `N-2`
orthogonal unit vectors perpendicular to its plane.  In the source paper's
diagonal-including convention,

\[
\operatorname{FP}_{q_N,N+1}(L_2^N)
=N+1+6\,2^{-q_N}.
\]

For every `N >= 3`, one has `q_N>log_2 3`, and therefore
`6*2^{-q_N}<2`.  Hence

\[
\operatorname{FP}_{q_N,N+1}(L_2^N)<N+3.
\]

Thus the source conjecture is false in every dimension in which it was posed.
The supporting paper proves the much stronger complete phase diagram, but it
does not explicitly single out the 2015 critical-exponent sentence; the
relation is an agent-identified implication.  This is not a new
counterexample.

## Files

- `solution_packet.pdf`: compact status and identification note.
- `source_paper.pdf`: arXiv:1504.02023.
- `supporting_paper_1907.10861.pdf`: decisive later paper.
- Ledger: `runs/fa_banach_001/ledger/results/1504.02023_p0_frame_conjecture_answered_by_1907.10861.json`.

