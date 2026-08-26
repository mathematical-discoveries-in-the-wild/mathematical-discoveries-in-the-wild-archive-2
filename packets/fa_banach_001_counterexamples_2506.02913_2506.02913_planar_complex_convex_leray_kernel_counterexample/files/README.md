# 2506.02913 — planar complex-convex Leray-kernel counterexample

Status: `candidate full counterexample as written; likely valid; pending human review`

Source: Agniva Chatterjee, *Dual realizations of Bergman spaces on strongly
convex domains*, arXiv:2506.02913v2, Remark 7.3.

The printed question asks whether the positive operator `|B_D|` is bounded on
`L^p(D)` for every bounded smooth strongly complex-convex domain
`D subset C^n` containing the origin. It does not impose `n >= 2`.

This packet gives a negative answer in `n=1`. For

`D={r exp(i theta): r < 1+(13/20) cos(2 theta)}`,

the usual one-dimensional strong-complex-convexity condition is vacuous and
the domain is smooth, bounded, simply connected, radial, and star-shaped. The
packet exhibits exact interior points `(zeta_0,z_0)` at which `B_D=0` and
checks that the real Jacobian in `zeta` is nonzero. The implicit-function
theorem therefore produces an interior kernel zero for every `z` in an open
set. Since the positive kernel has exponent `n+1=2`, its area integral
diverges logarithmically there, even for the input `f=1`.

Important scope caveat: if “strongly C-convex” is intended only for several
complex variables, or if Remark 7.3 silently assumes `n>=2`, this packet does
not settle that strengthened version. It then records the necessary missing
dimension hypothesis and a complete planar obstruction.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: official arXiv v2 PDF.
- `figures/open_problem_crop.png`: Remark 7.3 on source page 27.
- `code/verify_counterexample.py`: exact symbolic verification and crop tool.
- `verification.md`: build, arithmetic, visual, and novelty audit.

Human review should first decide the source's dimension convention. On the
literal wording, this is a candidate full negative answer.
