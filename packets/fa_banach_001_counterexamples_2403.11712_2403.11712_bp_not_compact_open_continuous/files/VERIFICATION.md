# Verification record

## Source

- The exact request was checked in local arXiv source and in the official
  12-page arXiv:2403.11712v2 PDF, printed page 4, Remark 3.2(2).
- The source asks for an example of a bp-continuous functional which is not
  `tau_c`-continuous on bounded sets for a Banach-space domain.

## Mathematical audit

- `K=[0,omega_1]` is compact and scattered, so finite Radon measures are
  atomic with countable support.
- A countable union of countable subsets of `[0,omega_1)` has countable
  supremum.  The corresponding final ordinal interval is clopen.
- This proves sequential weak-star continuity of endpoint mass.
- The point-mass net `delta_beta -> delta_omega_1` is weak-star convergent
  but endpoint mass is discontinuous along it.
- One-variable normal-family convergence proves
  `Df_n(0) -> Df(0)` weak-star under bounded pointwise convergence.
- A uniformly norm-bounded weak-star convergent net of linear functionals
  converges uniformly on norm-compact subsets, by a finite-net argument.
- Evaluation functions have supremum norm one, so discontinuity occurs on
  the unit ball requested by the source's bounded-set formulation.

## Novelty

- Searches covered the exact source sentence, arXiv id, bp versus
  compact-open continuity, and holomorphic functions combined with the
  Mazur property and `C([0,omega_1])`.
- No answer to the source request was located.
- The endpoint-mass weak-star example is classical; the packet makes no
  priority claim for that ingredient or for the resulting transfer.

## Build and visual QA

- `main.tex` compiled to a two-page A4 PDF with no final LaTeX warnings,
  undefined references, or overfull/underfull boxes.
- The complete packet was extracted to text and checked for all proof steps.
- Both rendered packet pages and the source page containing Remark 3.2(2)
  were visually inspected at high resolution.
- Packet SHA256:
  `b90751473b1340909b3b349d16e831a84dca8f5a6c32bdd73d8aad49093c71a6`.
- Source PDF SHA256:
  `1a8567181a8438f95b8f0e19aac4bc60fd66c52c355392049f3a0e6e12b51b43`.
