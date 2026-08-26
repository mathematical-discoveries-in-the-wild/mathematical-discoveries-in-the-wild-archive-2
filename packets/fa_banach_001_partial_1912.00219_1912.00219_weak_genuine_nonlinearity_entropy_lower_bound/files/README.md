# Entropy lower bound for weakly genuinely nonlinear scalar laws

Status: `candidate_partial_likely_valid`.

The open problem in arXiv:1912.00219 asks for sharp epsilon-entropy estimates
for fixed-time solution sets of one-dimensional scalar conservation laws with
general weakly genuinely nonlinear `C^2` flux.

This packet proves two lower bounds:

- universally, `H_epsilon >= c/epsilon` for every such flux;
- if a sign-definite state window of width comparable to `epsilon` has
  curvature at most `K_epsilon`, then
  `H_epsilon >= c/(epsilon K_epsilon)` (with the displayed dependence on
  `L` and `T` in the packet).

The proof encodes a binary code by many noninteracting small pulses inside a
locally convex or concave state window. Pulse spreading is at most
`T K_epsilon delta`, so flatter windows allow more independent bits. Weak
genuine nonlinearity always supplies one fixed curved window, proving the
universal lower bound.

The result is partial: a general weakly genuinely nonlinear flux can have
curvature-sign components shorter than the epsilon amplitude scale, which
prevents this packing from matching the source paper's generalized-variation
upper bound.

Files:

- `main.tex`: proof and upgrade audit.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: arXiv:1912.00219.
- `supporting_paper_1806.07758.pdf`: prior special-class lower bounds.
- `figures/open_question_crop.png`: exact source question.

Build from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```
