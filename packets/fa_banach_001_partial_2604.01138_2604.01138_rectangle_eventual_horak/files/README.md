# Eventual strict inequality in Horak's rectangle conjecture

Status: `candidate_partial_result_likely_valid_needs_human_review`

Source question: Remark 3.4 of Vladimir Bobkov, *Non-Ljusternik--Schnirelman
eigenvalues of the pure p-Laplacian exist*, arXiv:2604.01138 (source PDF page
11), which records Horak's conjectured one-crossing behavior for the second
variational eigenvalue on rectangles.

## Result

Let `R_a=(0,a)x(0,1)` with `1<a<2`, and let `lambda_bar(p;R_a)` be the
vertical antisymmetric branch, equivalently the first Dirichlet p-Laplacian
eigenvalue of `(0,a/2)x(0,1)`. Define

\[
r_a=\frac{a+1-\sqrt{2a}}2,
\qquad
\rho_a=\frac{a}{4r_a}<1.
\]

The packet proves

\[
\lambda_2(p;R_a)<\lambda_{\rm bar}(p;R_a)
\quad\hbox{whenever}\quad
\frac{(p+1)(p+2)}{2(p-1)}\rho_a^p<1.
\]

Thus the strict inequality holds for all sufficiently large `p`. Since
equality holds at `p=2` and both branches are continuous, the equality set
has a finite last point `p_last(a)`, and strict inequality holds for every
`p>p_last(a)`.

This proves the entire post-last-contact half of the conjecture for each
fixed `1<a<2`. It does **not** prove that equality holds throughout
`[2,p_last(a)]`, and its geometric gap vanishes at `a=2`, so it does not
settle the source's anticipated `p*(a)=infinity` regime for `a>=2`.

The proof uses two tangent opposite-corner disks of radius `r_a`, their
distance-to-boundary cones as a genus-two test family, and sharp
one-dimensional Poincare on the vertical half-rectangle.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: the 13-page source arXiv PDF.
- `figures/open_problem_crop.png`: source page 11 with the exact conjecture.
- `VERIFICATION.md`: source, proof, computation, novelty, and limitation audit.
- `code/check_rectangle_threshold.py`: geometry and finite-p threshold audit.
- `code/render_source_evidence.py`: reproducible source-crop renderer.
- `code/render_solution_pdf.py`: reproducible RGB rendering of every final
  packet page for visual inspection.

## Reproduction

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2604.01138_rectangle_eventual_horak/code/render_source_evidence.py

conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2604.01138_rectangle_eventual_horak/code/check_rectangle_threshold.py
```

Compile from the packet directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
```

The final PDF is rendered to RGB page images and every page is visually
inspected before promotion.
