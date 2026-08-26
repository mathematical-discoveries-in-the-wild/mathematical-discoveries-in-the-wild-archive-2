# Verification report

## Mathematical checks

- The radial function has the strict lower bound `R(theta)>=7/20`, so the
  boundary is smooth and the Minkowski gauge is smooth away from the origin.
- The domain is radial and simply connected. In complex dimension one its
  complex tangent space is `{0}` at every boundary point, so positive
  definiteness on nonzero complex tangent vectors is vacuous.
- `code/verify_counterexample.py` uses SymPy exact rational arithmetic. It
  checks the displayed coordinates of `z_0`, `B_D(zeta_0,z_0)=0`, the exact
  value `m_D(z_0)^2<1`, both displayed first derivatives, and the positive
  real Jacobian determinant.
- The last step is qualitative and standard: a transverse zero persists by
  the real implicit-function theorem, and bounded first derivatives give
  `|B_D(zeta,z)| <= C|zeta-zeta(z)|`. The area integral of the inverse square
  diverges.

## Source and novelty checks

- Source: official arXiv:2506.02913v2 PDF, last revised 11 June 2026.
- The question is on source PDF page 27, Remark 7.3.
- Searched on 11 August 2026: the four lightweight run indexes; exact arXiv
  id and title; the exact question wording; and combinations of `strongly
  C-convex`, `B_D`, `Leray kernel`, and `L^p bounded`.
- Results found the source, general Cauchy--Leray work, and source summaries,
  but no later answer to Remark 7.3 and no matching radial counterexample.
- Novelty is therefore plausible only within this bounded search.

## Scope check

The packet deliberately does not claim a counterexample for `n>=2`. Its full
status relies on the literal quantifier `D subset C^n` in the source question
and the standard vacuous dimension-one complex-tangent condition. If the
authors intended several complex variables only, reclassify this as a planar
dimensional caveat/partial result.

## Build and visual checks

- `latexmk` completed after two passes with no remaining warnings, undefined
  references, overfull boxes, or underfull boxes.
- The four-page packet was rendered at 150 dpi. Every page was visually
  inspected: the status box, source crop, equations, page breaks, proof-ending
  symbol, scope warning, and bibliography are legible and unclipped.
- `solution_packet.pdf` SHA-256:
  `53040892008676074a7179e1b2a8a1cfa188e196bb2cb9e9fe01fa0d89044cea`.
- `source_paper.pdf` SHA-256:
  `f6447c788ea124a43d03f4fcf056a0d2aa51b1c3fa7713bece9e84d7deb56d6c`.
- `figures/open_problem_crop.png` SHA-256:
  `788d5c717ea4812a243e0dc8f3d84bf44094c66ffd494fe66d00f2b16c522585`.
