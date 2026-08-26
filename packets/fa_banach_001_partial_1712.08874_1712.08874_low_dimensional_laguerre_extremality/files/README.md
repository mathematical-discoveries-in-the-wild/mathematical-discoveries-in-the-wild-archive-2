# Low-dimensional MSS Laguerre extremality

Status: `candidate_partial_result_likely_valid_needs_human_review`

Source target: Adam Marcus and Nikhil Srivastava, *The Solution of the
Kadison--Singer Problem*, arXiv:1712.08874.  The exact conjecture is stated in
Section 7.2 of Marcus--Spielman--Srivastava, *Interlacing Families II*.

## Result

For positive semidefinite (d\times d) matrices (A_i\) with

\[
\sum_iA_i=I_d,\qquad \operatorname{tr}A_i\leq\varepsilon,
\]

the MSS conjectured scalar packing globally maximizes the largest zero of the
mixed characteristic polynomial when (d=2\) or (d=3\), for all feasible
(m,\varepsilon\).

There is also an all-dimensional local result.  In the balanced case
(m\geq d\), \(\varepsilon=d/m\), the tuple (A_i=I_d/m\) is a strict local
maximizer along every nonzero affine feasible direction.  The exact quadratic
variation is a lower-degree associated Laguerre polynomial.

The general conjecture remains open.  Dimension four introduces a positive
((2,2)\) cross mixed-discriminant term; a direct coefficientwise extension of
the (d\leq3\) proof is false.

## Files

- `main.tex` / `solution_packet.pdf`: source statement, proofs, upgrade audit,
  and limitations.
- `source_paper.pdf`: the target lecture notes, arXiv:1712.08874.
- `supporting_mss_annals.pdf`: the primary paper containing the precise
  conjecture.
- `figures/lecture_extremality_crop.png`: target source's unproved assertion.
- `figures/precise_conjecture_crop.png`: exact formulation in the Annals paper.
- `code/check_mcp_extremality.py`: determinant evaluator, second-variation
  check, and randomized stress test.
- `VERIFICATION.md`: proof-obligation, computation, novelty, and scope audit.

## Reproduction

From this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
conda run --no-capture-output -n sandbox python code/check_mcp_extremality.py --trials 100
```

The final PDF was rendered to RGB images and every page was visually inspected.

