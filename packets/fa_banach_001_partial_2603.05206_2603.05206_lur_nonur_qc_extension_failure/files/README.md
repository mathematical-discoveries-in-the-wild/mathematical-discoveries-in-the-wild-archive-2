# An LUR non-UR ball without the quasiconvex extension property

Status: `candidate_partial_likely_valid`.

Source: C. A. De Bernardi and L. Veselý, *Extending quasiconvex
functions from uniformly convex sets*, arXiv:2603.05206 (2026).

## Result

There is an explicit separable Banach space `X` whose closed unit ball is
locally uniformly rotund (LUR) but not uniformly rotund (UR), and a
Lipschitz quasiconvex function `f:B_X -> R` which admits no uniformly
continuous quasiconvex extension to `X`.

Take

```text
E_n = ell_{p_n}^2,       p_n = 2^(3(n+1)),
X   = (direct sum E_n)_ell2.
```

The source paper's planar nonrotund construction gives one bounded
Lipschitz quasiconvex witness `q` on the square, with a nested fan of
half-plane sublevels and levels tending to one.  Define

```text
f((x_n)) = sup_n q(x_n),       (x_n) in B_X.
```

The coordinate planes isolate the planar witnesses.  A hypothetical
uniformly continuous quasiconvex extension is forced, in the `n`th plane,
to jump by an amount tending to one between two points at distance `2^-n`.
This contradicts uniform continuity.

This is a substantial partial answer, not a solution of the full question.
It proves that LUR alone does not imply the extension property and gives a
concrete LUR/non-UR counterexample body.  It does not prove that every LUR
non-UR body fails the property.

## Files

- `solution_packet.pdf`: human-review packet with the complete proof.
- `main.tex`: packet source.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: page-2 statement of the open problem.
- `code/verify_geometry.py`: reproducible checks of the explicit numerical
  choices (supporting evidence, not a substitute for the proof).
- `novelty.md`: bounded duplicate and literature search.
- `verification.md`: proof, computation, build, and rendering checks.

Human review should focus on the extraction of the normalized planar fan
from the proof of Theorem 3.2 in the source paper and on the half-plane
continuation step.  Both are stated explicitly in the packet.

