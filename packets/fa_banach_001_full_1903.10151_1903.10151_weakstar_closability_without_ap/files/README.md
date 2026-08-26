# Weak-* closability of the Fourier gradient without AP

Status: `candidate full solution (likely valid; human review requested)`.

## Source problem

Cédric Arhancet and Christoph Kriegler, *Riesz transforms, Hodge-Dirac
operators and functional calculus for multipliers I*, arXiv:1903.10151v9.
Proposition 3.12 (PDF pages 53--54) proves weak-* closability of the
Fourier-gradient operator under the assumption that the discrete group `G`
has the approximation property (AP). Remark 3.13 (PDF page 54) asks whether
AP is really necessary.

## Result

AP is not necessary. For every discrete group `G`, every cocycle appearing in
the source construction, and every `-1 <= q < 1`, the operator

\[
\partial_{\psi,q}:\mathcal P_G\subseteq \mathrm{VN}(G)
\longrightarrow \Gamma_q(H)\rtimes_\alpha G
\]

is weak-* closable. The proof works for nets, hence also for the sequential
form used in the source footnote.

## Idea

The source proof uses AP to approximate an alleged weak-* limit by
finite-support Fourier multipliers. This is unnecessary. Apply the normal
crossed-product Fourier coefficient map

\[
C_s(z)=E_\Gamma\bigl(z(1\rtimes\lambda_s)^*\bigr).
\]

If `x_i -> 0` weak-* and `partial(x_i) -> y` weak-*, then for every `s`

\[
C_s(y)=\lim_i \widehat x_i(s)s_q(b_\psi(s))=0.
\]

All Fourier coefficients of `y` vanish. Their uniqueness, equivalently the
orthogonal decomposition of the crossed-product `L^2` space, gives `y=0`.

## Review notes

- The proof uses only normality of the canonical expectation, the explicit
  formula for the gradient on Fourier polynomials, and uniqueness of Fourier
  coefficients.
- The range `q < 1` is retained exactly from Proposition 3.12; at `q=1` the
  Gaussian field operators need not be bounded elements of the target von
  Neumann algebra.
- This resolves only Remark 3.13, not the paper's endpoint Lipschitz-algebra
  equalities or commutator-norm question.
- A bounded search on 11 August 2026 covered the run indexes, the exact remark
  sentence and label, the paper title/arXiv id, `weak* closable`, `Gamma_q`,
  crossed-product gradients, citing-paper results, and the 2022 Springer book
  record. No later answer to Remark 3.13 was found. This supports, but does not
  establish, novelty.

Human-review recommendation: verify the convention for the coefficient map
`C_s` and the standard `L^2` Fourier decomposition; after those two checks the
argument is immediate.

## Files

- `main.tex`, `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: arXiv:1903.10151v9.
- `figures/open_problem_context_page53.png` and
  `figures/open_problem_remark_page54.png`: rendered source evidence.
- `proof.md`: standalone formal proof.
- `verification.md`: proof audit and novelty-search bounds.
- Ledger: `runs/fa_banach_001/ledger/results/1903.10151_weakstar_closability_without_ap.json`.
