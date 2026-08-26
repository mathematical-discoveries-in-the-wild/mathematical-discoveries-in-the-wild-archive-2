# Amplification questions in arXiv:2308.05671 answered by arXiv:2502.08595

Status: `literature_already_answered`

This is a literature-status record, not a new theorem proved by this run.

## Source questions

Rémi Boutonnet, Daniel Drimbe, Adrian Ioana, and Sorin Popa,
*Non-isomorphism of \(A^{*n}\), \(2\le n\le\infty\), for a non-separable
abelian von Neumann algebra \(A\)*, arXiv:2308.05671, Section 4.3.

The source asks to identify \((A^{*n})^t\) for arbitrary \(t>0\).  It proves
the formula only for \(t=1/k\) when \(A\) is homogeneous.  For the infinite
free power it proves \(\mathbb Q\subseteq\mathcal F(A^{*\infty})\) and states
the expectation \(\mathcal F(A^{*\infty})=\mathbb R_+^*\).

## Explicit later answer

Ken Dykema and Junchen Zhao, *Free products and rescalings involving
non-separable abelian von Neumann algebras*, arXiv:2502.08595; *Journal of
Functional Analysis* 290 (2026), article 111264,
doi:10.1016/j.jfa.2025.111264.

The abstract explicitly states that its results answer two questions in
Section 4.3 of the source paper.  Theorem 2.8 proves that every diffuse
abelian tracial von Neumann algebra is self-symmetric.  Definition 3.3
constructs an interpolation \(\mathcal F_{s,r}(A)\) with
\(\mathcal F_{n,0}(A)\cong A^{*n}\) for integers \(n\ge2\), and Theorem 3.5
proves, for all \(t>0\),
\[
 (\mathcal F_{s,r}(A))^t
 \cong
 \mathcal F_{s/t,\,(s+r-1)/t^2-s/t+1}(A).
\]
Therefore
\[
 (A^{*n})^t
 \cong
 \mathcal F_{n/t,\,(n-1)/t^2-n/t+1}(A)
 \qquad(n\ge2,\ t>0),
\]
which is the requested arbitrary-scale identification.  Theorem 4.5 proves
\(\mathcal F(A^{*\infty})=\mathbb R_+^*\), settling the second question.

## Scope

This resolves the amplification subsection for diffuse abelian \(A\), hence
in particular for the non-separable abelian algebras in the source theorem.
It does not resolve the source paper's separate questions about freely
complemented maximal amenable MASAs, \(\operatorname{Out}(A^{*n})\), or
finite-index subfactors.

## Files

- `source_paper.pdf`: arXiv:2308.05671.
- `supporting_paper_2502.08595.pdf`: the answering paper.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger:
`runs/fa_banach_001/ledger/results/2308.05671_amplifications_answered_by_2502.08595.json`.
