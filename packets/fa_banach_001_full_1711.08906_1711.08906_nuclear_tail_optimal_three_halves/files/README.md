# Candidate Full Solution: the optimal universal nuclear-tail constant is 3/2

Status: `candidate full solution — likely valid; human review recommended`

Source: Jan Hamhalter and Ondřej F. K. Kalenda, *Measures of weak non-compactness in spaces of nuclear operators*, arXiv:1711.08906v1 / Math. Z. 292 (2019), 453–471.

Open question: Immediately after Theorem 2.1(c), on page 5, the authors ask whether the constant `2` in

`chi(A) <= tau(A) <= 2 chi(A)`

is optimal, where `tau(A)` is the infimum of the uniform nuclear-norm error after finite coordinate-corner compression.

Result: The factor `2` is not optimal. For every `p,q in (1,infinity)` and every bounded `A` in `N(ell^q(Lambda),ell^p(J))`,

`chi(A) <= tau(A) <= (3/2) chi(A)`.

Moreover, `3/2` is the best constant that works simultaneously for all admissible `p,q`.

Proof mechanism: If `P,Q` are coordinate projections, the sign changes `U=2P-I` and `V=2Q-I` are surjective isometries. The exact identity

`I - (T -> PTQ) = (3I - L_U - R_V - L_U R_V)/4`

gives norm at most `3/2` on the nuclear ideal. The Hausdorff noncompactness proof then improves by applying this complement norm to the error from a finite net. Sharpness uses trace duality, the `2 x 2` matrix

`[[1,-1],[-1,-1]]`,

whose `(infinity -> 1)` norm is `2` while deleting its `(1,1)` entry gives norm `3`, and a replicated-corner construction converting the finite-dimensional projection norm into a bounded infinite set with the same `tau/chi` ratio. Taking `p -> infinity` and `q -> 1` yields ratios approaching `3/2` within the allowed open range.

Scope: This determines the optimal constant uniformly over all `p,q`. It does not calculate the possibly smaller best constant for each fixed pair `(p,q)`, nor address the paper's other problems concerning `C(K)`, compact-operator spaces, C*-algebras, or general von Neumann preduals.

Novelty check: The lightweight run indexes were searched by arXiv id, exact title, `constant 2 optimal`, `three halves`, `corner`, and `nuclear`. Web/arXiv searches used the exact source sentence, title, authors, and nuclear-operator constant keywords. They returned the source paper but no later paper explicitly resolving this constant question or presenting the `3/2` sign-flip argument. Novelty is therefore plausible but not certified beyond this bounded search.

Files:

- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: page-5 source evidence.
- `code/check_corner_constant.py`: exact endpoint and algebraic sanity checks.
- `code/crop_source_page.py`: reproducible source crop.
- `VERIFICATION.md`: verifier report and limitations.

Human review focus: Check the dual orientation in the sharpness argument and the replicated-set computation of `chi`; both are written out explicitly in the packet.
