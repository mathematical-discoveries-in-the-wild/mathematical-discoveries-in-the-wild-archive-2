# Kernel criteria for quantum integration and a regular scalar-injective POVM

Status: `candidate_partial_likely_valid`

Source: Sarah Plosker and Christopher Ramsey, *An operator-valued Lyapunov
theorem*, arXiv:1801.03109, J. Math. Anal. Appl. 469 (2019), 117--125.

On source PDF page 7 the authors identify the injectivity of the quantum
integration map `E_nu` as a natural problem. The packet proves:

- `E_nu` is noninjective whenever the Radon--Nikodym density has a nontrivial
  kernel on a positive-measure set;
- `E_nu` is noninjective whenever the density is uniformly bounded below on
  any positive-measure set;
- consequently, any injective example must have an almost-everywhere
  injective density with dense nonclosed range;
- there is an explicit nonatomic circle POVM with a norm-continuous,
  uniformly coercive density for which scalar integration is injective, while
  full quantum integration is noninjective and the POVM range is nonconvex.

The last example shows that the source's `classically non-injective`
hypothesis is not automatic even under very regular Radon--Nikodym behavior.
The full question remains open in the isolated singular-density regime.

Novelty check: bounded searches of the run indexes, local arXiv corpus, and
the web/arXiv literature used the exact arXiv id/title and the phrases
`classically non-injective`, `POVM integration injective`, `operator-valued
Lyapunov`, and `Radon--Nikodym density`. They found the source and general
informationally complete POVM literature, but no later resolution or this
block-Fourier construction.

Human review should focus on the measurable kernel projection in Theorem 3.1,
the inverse-density calculation in Theorem 3.2, and the Fourier uniqueness
step in Theorem 4.1.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1801.03109.
- `figures/open_problem_crop.png`: source PDF page 7 evidence.
- `verification.md`: proof and rendering checks.
