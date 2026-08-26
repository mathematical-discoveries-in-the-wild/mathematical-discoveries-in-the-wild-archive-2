# The endpoint $p=\infty$ multiplier regularity is completely determined

Status: `literature_implied_answer (endpoint subcase)`

Source question: Guillaume Dumas, *Regularity of matrix coefficients of a
compact symmetric pair of Lie groups*, arXiv:2305.09291, Remark 3.18 on PDF
page 28. The remark asks whether the rank-one regularity theorem for
$K$-bi-invariant $S_p$-multipliers is optimal.

Result recorded here: the endpoint $p=\infty$ is completely resolved. If
$d=\dim(G/K)$ and $a=(d-1)/2$, the optimal regularity of every
$K$-bi-invariant $S_\infty$-multiplier is

\[
C^{(\lfloor a\rfloor,a-\lfloor a\rfloor)}.
\]

This is an agent-identified implication of two known results.  Spronk's
Corollary 5.4 identifies invariant measurable Schur multipliers on an
amenable group with the Fourier--Stieltjes algebra $B(G)$. Compact groups
are amenable, so every $S_\infty$-multiplier here is a unitary matrix
coefficient.  Dumas's Theorem A gives the displayed regularity, and Dumas's
Corollary 3.17(5) supplies unitary coefficients that rule out every strictly
stronger regularity pair.  Conversely, every unitary coefficient is a
Herz--Schur multiplier by the standard Hilbert-space factorization of its
Toeplitz kernel.

When $a\notin\mathbb Z$, this is exactly the regularity of Dumas's operator
path $T$. When $a=m\in\mathbb Z$, it improves the path estimate
$C^{(m-1,1)}$ to the sharp multiplier statement $C^m$; hence no
$S_\infty$-multiplier can witness only the weaker endpoint regularity of
$T$.

The finite-`p` optimality question remains open.

Human-review recommendation: `likely valid`. The main point to verify is the
standard passage from Dumas's measurable Toeplitz Schur multiplier to
Spronk's invariant multiplier space; after that identification, the proof is
an immediate two-theorem implication.

Files:

- `solution_packet.pdf`: compact proof/status note.
- `source_paper.pdf`: arXiv:2305.09291.
- `supporting_paper_math0210304.pdf`: Nico Spronk, arXiv:math/0210304.
- `VERIFICATION.md`: source-location, proof-chain, and PDF-QA report.
- Ledger: `runs/fa_banach_001/ledger/results/2305.09291_p_infinity_multiplier_endpoint.json`.
