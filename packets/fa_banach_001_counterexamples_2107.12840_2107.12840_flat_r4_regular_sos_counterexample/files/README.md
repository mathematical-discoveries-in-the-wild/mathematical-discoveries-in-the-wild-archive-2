# A flat elliptical counterexample in dimension four

Status: `candidate counterexample likely valid`.

This packet gives a smooth function `f : R^4 -> [0,infinity)` which is flat
at the origin, positive at every nonzero point, and is not a finite sum of
squares of regular functions.  Here “regular” has the meaning used by
Korobenko and Sawyer: `C^{2,delta}` for some `delta > 0`.

The source paper proves its counterexample theorem in dimensions at least
five.  Its obstruction, however, is a four-variable quartic.  The packet
removes the extra scale coordinate by gluing rescaled copies of `L+tau_n` in
disjoint four-dimensional balls accumulating at the origin.  A diagonal
choice of `tau_n` makes the source's compactness lower bound dominate every
loss introduced by rescaling.

The result is deliberately narrower than Remark 2.7 of the source: no
prescribed weak monotonicity condition is asserted.  Thus it settles the
unconstrained dimension-four existence gap, not the remaining
monotonicity-threshold problem.

Files:

- `main.tex` and `solution_packet.pdf`: complete construction and proof.
- `source_paper.pdf` and `source_paper.tex`: local source copies.
- `figures/source_page_5.png`: source definitions, dimension-five theorem,
  and dimension-boundary remark.
- `figures/source_page_32.png`: source hard-quartic compactness lemma.
- `code/verify_geometry_and_scaling.py`: exact geometry and scaling checks.
- `verification.md`: verification, provenance, and novelty-search record.

