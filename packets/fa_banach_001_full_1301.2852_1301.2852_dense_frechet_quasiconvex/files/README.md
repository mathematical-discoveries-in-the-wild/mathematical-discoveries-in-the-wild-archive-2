# Dense Fréchet points for densely continuous quasiconvex functions

Status: `candidate_full_solution_likely_valid_needs_human_review`

Source question: the open question in the Introduction of Patrick J. Rabier,
*Differentiability of quasiconvex functions on separable Banach spaces*,
arXiv:1301.2852 (source PDF page 5).

## Result

The answer is affirmative. Every real-valued, densely continuous,
quasiconvex function on a separable Banach space is continuous and
classically Gâteaux differentiable at the points of a dense subset.

The only case not already covered by the source is when

\[
m=\mathcal T\operatorname{-ess\,inf}_X f>-∞,
\qquad F'_m=\{f\le m\}
\]

is of second category. In that case, the packet proves the stronger statement
that points of Fréchet differentiability with derivative zero are dense in
`int(F'_m)`, and hence dense in `F'_m`.

The new ingredient is a uniform convex-hole lemma. If `C` is closed, convex,
and has empty interior, every ball of radius `R` contains a ball of radius
`R/8` whose points are more than `R/4` from `C`. Applying this successively to
closures of lower sublevels `{f<α_k}`, with `α_k` approaching `m` quadratically
faster than the hole radii shrink, produces a point `x` with

\[
f(y)-f(x)=o(\|y-x\|).
\]

Source Theorem 4.2 supplies dense Hadamard differentiability on
`X \ F'_m`; source Corollary 4.3 and Theorem 5.2 cover the other cases.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: the 28-page source arXiv PDF.
- `figures/open_problem_crop.png`: source page 5 with the exact question.
- `figures/near_counterexample_crop.png`: source page 25 explaining why its
  layered ℓ² construction had not settled classical Gâteaux differentiability.
- `VERIFICATION.md`: theorem-by-theorem proof audit, novelty bounds, and
  human-review focus.
- `code/check_nested_holes.py`: exact arithmetic audit of the geometric
  constants and convergence schedule.
- `code/render_source_evidence.py`: reproducible source-crop renderer.
- `code/render_solution_pdf.py`: reproducible RGB rendering of every final
  packet page for visual inspection.

## Reproduction

Render the source evidence and run the exact audit:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1301.2852_dense_frechet_quasiconvex/code/render_source_evidence.py

conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1301.2852_dense_frechet_quasiconvex/code/check_nested_holes.py
```

Compile from the packet directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
```

The final PDF is rendered to RGB page images and every page is visually
inspected before promotion.
