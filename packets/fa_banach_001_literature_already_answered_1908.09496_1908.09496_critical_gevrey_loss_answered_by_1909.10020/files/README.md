# Critical Gevrey derivative loss: exact later answer

Status: `literature_already_answered (Open Problem 2 only)`

Original source: Marina Ghisi and Massimo Gobbino, *Residual pathologies*,
arXiv:1908.09496, Open Problem 2 on PDF page 24.

Answer source: Marina Ghisi and Massimo Gobbino, *Critical counterexamples for
linear wave equations with time-dependent propagation speed*,
arXiv:1909.10020, Theorem 3.2 on PDF page 11 and its proof on PDF pages 23–24.

## Identification

Open Problem 2 asks whether, at the critical Gevrey order
`s=(1-alpha)^(-1)` and finite radius `r0`, there are an alpha-Hölder
propagation speed, an initial velocity, and a finite time `t0` such that the
solution with zero initial displacement undergoes severe derivative loss for
every `t>t0`.

Theorem 3.2 of arXiv:1909.10020 gives exactly this in a stronger residual
form.  It allows the nondissipative case `delta=0`, takes
`s=S=(1-alpha)^(-1)` and arbitrary `r0>0`, gives an explicit `t0`, and proves
loss beyond the critical Gevrey-hyperdistribution scale for all `t>t0`.
The proof on PDF page 23 explicitly chooses `u(0)=0` and constructs the
initial velocity `u'(0)=sum_i a_i e_i`, so there is no mismatch in the
initial-data formulation.

The later authors explicitly describe the critical cases as having been left
open, state that Theorem 3.2 resolves the first one, cite arXiv:1908.09496,
and say their results complete the strictly hyperbolic Hölder picture.  This
is therefore an explicit literature answer, not a new theorem of this run.

## Remaining scope

The other two questions in *Residual pathologies* are not answered by this
identification:

- Open Problem 1 asks for Kohn's approximate-differentiability counterexample
  with `f'` approximately differentiable at every point.
- Open Problem 3 asks for transport derivative loss in every open subset of
  the spatial support.

Exact-phrase and author/title searches through 11 August 2026 did not locate
a later answer to either remaining problem.

## Files

- `source_paper.pdf`: arXiv:1908.09496.
- `supporting_paper_1909.10020.pdf`: the answer paper.
- `main.tex`, `solution_packet.pdf`: compact status note.

