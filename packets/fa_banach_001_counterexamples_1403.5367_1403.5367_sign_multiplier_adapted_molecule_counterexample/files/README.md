# The sign multiplier destroys the adapted one-molecule condition

Result type: `counterexample`

Status: candidate full negative answer to the concrete uncertainty in Remark
7.3, likely valid pending expert review.

Source paper:

- Pascal Auscher and Sebastian Stahlhut, “A priori estimates for boundary
  value elliptic problems via first order systems,” Part I of *Functional
  Calculus for First Order Systems of Dirac Type and Boundary Value Problems*,
  Mémoires de la Société Mathématique de France (N.S.) 144 (2016),
  arXiv:1403.5367.
- Open-question location: Remark 7.3, source PDF page 45.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The answer to Remark 7.3 is negative, already for the scalar constant-
coefficient derivative.  Take `D=-i d/dx`, `B=I`, and let the bounded
holomorphic calculus symbol be the sign function on the two components of a
bisector.  If `a=Du` is a compactly supported adapted `H_D^1` atom and
`integral u != 0`, then

`m=sgn(D)a`

is not an `(H_D^1,epsilon,1)`-molecule for any `epsilon>0` and any associated
interval.

Indeed, the unique `L^2` function `v` satisfying `Dv=m` is `sgn(D)u`, a
constant multiple of the Hilbert transform of `u`.  Its nonzero-mean term
gives `v(x)=c/x+O(x^-2)`.  Hence its `L^2` norm on a dyadic annulus of radius
`R` is bounded below by `R^-1/2`, whereas the adapted molecule condition
requires `O(R^-1/2-epsilon)`.

## Files

- `main.tex`: self-contained counterexample and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Remark 7.3.
- `verification.md`: proof audit and review focus.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Novelty check

On August 11, 2026, the run indexes were searched by arXiv id, exact title,
Remark 7.3 terminology, and the adapted-molecule phrase.  Exact-phrase web
searches found copies of the source memoir but no later answer; searches for
the sign/Hilbert-transform mechanism likewise found no matching resolution.
Novelty confidence is moderate pending specialist citation review.

## Scope and human review focus

This completely answers the specific uncertainty in Remark 7.3 and shows that
the source's extra annular factor reflects a real low-frequency obstruction.
It does not resolve the broader endpoint functional-calculus, abstract atomic-
decomposition, or perturbation questions elsewhere in the memoir.

Review should focus on matching the source's normalization of
`(H_D^1,epsilon,1)` molecules and on the admissibility of the piecewise-
constant sign function in the bisectorial `H^infinity` calculus.
