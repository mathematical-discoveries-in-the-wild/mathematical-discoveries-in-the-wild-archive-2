# Literature resolution: right Bregman Klee sets without full domain

**Status:** `literature_already_answered`.

## Original question

In Remark 7.3 on PDF page 15 of arXiv:0802.2322, Bauschke, Wang, Ye,
and Yuan ask whether their singleton theorem for right Bregman Klee sets
remains true after dropping the assumption `dom f = R^J`.

The retained setting is finite dimensional: `f` is Legendre,
`U = int dom f`, and `C` is a nonempty compact subset of `U`. The right
Klee assumption says that every `x in U` has a unique right Bregman farthest
point in `C`.

## Explicit later answer

ArXiv:0908.2013, by Bauschke, Macklem, Sewell, and Wang, identifies the
question from `[7, Remark 7.3]` in its introduction and says it will settle it
entirely. Its Theorem 3.2 on PDF page 10 proves:

> If `C` is compact and right-Bregman Klee, then `C` is a singleton.

No full-domain hypothesis on `f` appears. This is therefore a direct and
complete affirmative answer to Remark 7.3.

## Proof mechanism in the later paper

For the convex right farthest-distance function
`F_C(x) = sup_{c in C} D_f(x,c)`, Theorem 3.1 first produces a minimizer
`x_0` inside `U`, including when `dom f` has a boundary. The
Ioffe--Tikhomirov subdifferential formula and uniqueness of the active
farthest point then give

`0 = grad f(x_0) - grad f(Q_C(x_0))`.

Injectivity of the Legendre gradient yields `x_0 = Q_C(x_0)`. Since this
point is farthest from itself with zero Bregman distance, nonnegativity and
strict convexity force every member of `C` to equal `x_0`.

## Files

- `source_paper.pdf`: arXiv:0802.2322.
- `supporting_paper_0908.2013.pdf`: the explicit later answer.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered and visually verified status packet.

