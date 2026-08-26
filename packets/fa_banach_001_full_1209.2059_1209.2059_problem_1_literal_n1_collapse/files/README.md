# Literal full answer to Problem 1 in arXiv:1209.2059

Status: candidate full answer to the printed statement; formulation caveat.

Gilles Pisier's *Quantum Expanders and Geometry of Operator Spaces*
(arXiv:1209.2059), Section 3, Problem 1, asks what follows if a
finite-dimensional operator space `E` satisfies

`k_E(N,C) <= 1 for all N`.

Taken literally, the hypothesis includes `N=1`. The definition of `k_E`
then supplies a single linear functional `f:E -> M_1 = C` satisfying

`|f(x)| <= ||x|| <= C |f(x)|` for every `x in E`.

Thus `f` is injective and `dim(E) <= 1`. Every nonzero one-dimensional
operator space is completely isometric to `C`, so its exactness constant is
`1`.

The surrounding discussion says that exact spaces have `k_E(N,c)=1` for all
sufficiently large `N`. It is therefore likely that Problem 1 intended an
eventual-`N` hypothesis. This packet does not answer that stronger intended
version.

Files:

- `main.tex` and `solution_packet.pdf`: full statement, proof, and scope caveat.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: source page 25, including the complete
  printed Problem 1.
- `verification.md`: proof and rendering checks.

Human-review recommendation: verify that the printed universal quantifier was
not subject to an implicit convention excluding small `N`; if the intended
question was eventual in `N`, retain this packet as a formulation correction,
not as a solution of the intended problem.

