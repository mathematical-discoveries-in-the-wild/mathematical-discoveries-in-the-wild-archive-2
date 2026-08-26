# A no-go theorem for the literal unbounded-operator extension

Result type: partial

Status: candidate sharp obstruction, likely valid pending expert review.

Source paper:

- Jichao Zhang and Shangquan Bu, “Maximal regularity for fractional
  difference equations with finite delay on UMD spaces,” arXiv:2406.15417
  (2024).
- Open-direction location: Introduction, source PDF page 3.
- Local source: source_paper.pdf.
- Evidence crop: figures/open_problem_crop.png.

## Claimed contribution

The source's literal all-data classical formulation cannot be extended to any
genuinely unbounded closed operator. An impulse at time zero forces
u(3)=f(0), while the equation at time three requires u(3) in D(A).
Solvability for every finitely supported X-valued forcing therefore gives
D(A)=X, and the closed graph theorem makes A bounded.

Two upgrades make the obstruction sharp:

- the source's alpha-resolvent sequence is itself rigid, because its first
  recurrence step contains A I=A; a bounded-operator-valued sequence
  satisfying Definition 3.1 forces A bounded;
- an explicit far-left diagonal unbounded self-adjoint operator on ell2
  satisfies both frequency-domain R-boundedness conditions from the source,
  yet admits no classical solution for an impulse outside its domain.

Thus a meaningful unbounded theory must change at least one of the solution
class, forcing space, resolvent-family definition, or time discretization.

## Files

- main.tex: full proof packet source.
- solution_packet.pdf: rendered proof packet.
- source_paper.pdf: original arXiv paper.
- figures/open_problem_crop.png: full-width crop of the open-direction
  statement.
- verification.md: proof audit and review focus.
- tmp/: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the run's cheap indexes were searched by arXiv id, title,
and the terms “unbounded operator”, “fractional difference”, and “maximal
regularity”. Targeted web searches for the exact title plus “unbounded
operator”, the quoted open-direction phrase, and close finite-delay terms found
the source and related bounded-operator papers but no later resolution of this
obstruction. The search was bounded, so novelty confidence is moderate.

## Scope and human review focus

This packet is not claimed to solve every possible unbounded fractional
difference model; the source statement is too broad for that. It completely
rules out the literal classical/all-data extension of the paper's explicit
scheme and shows why the existing frequency criterion and resolvent sequence
cannot simply be retained. Review should focus on the time-zero computation
and on whether “classical solution” is interpreted, as usual, to require
u(n) in D(A) whenever A u(n) occurs.
