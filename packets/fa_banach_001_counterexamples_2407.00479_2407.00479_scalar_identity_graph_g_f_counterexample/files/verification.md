# Verification record

Status: all analytic, computational, source-evidence, build, and visual
checks completed; candidate remains counterexample_likely_valid pending
independent expert review.

## Analytic audit

- In E=R, B=B*=R^2, L(u,v)=(v,u), and both quadratic pairings are ordinary
  coordinate products.
- For every lambda>0, the graph M_lambda is closed and monotone.
- Its quasidensity expression is a single nonnegative square with zero
  minimum, so it is CMQd and hence maximally monotone under the source
  theorem.
- Direct completed squares give the formulas for P_M and G_M.
- The F_M objective has the null direction (u,v)=(t,-lambda*t). Off
  y=lambda*z, the resulting affine function is unbounded below; on that
  line the entire objective is a nonnegative square with zero minimum.
- The source explicitly defines F_M with a leading negative infimum and
  codomain ]-infinity,infinity], so F_M=+infinity is admissible.

## Source evidence

figures/open_problem_crop.png is rendered directly from official arXiv PDF
page 20 by code/make_source_crop.py; it is not a retyped image.

## Computational check

Command:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/2407.00479_scalar_identity_graph_G_F_counterexample/code/verify_counterexample.py

Result: PASS on all exact symbolic checks. The checker verifies the
quasidensity square, completed squares for P_M and G_M, both branches of
the F_M computation, the null-direction drift, and the concrete witness
G_M(0,1)=1/4.

## Remaining reviewer focus

1. Confirm the source convention for F_M, including the leading minus sign
   and the order b*-Lb.
2. Confirm that the stated extended codomain permits +infinity.
3. Repeat the bounded novelty search independently.

## Render QA

Compiled with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
    cp tmp/main.pdf solution_packet.pdf
    pdftoppm -png -r 150 solution_packet.pdf tmp/final_render/page

Final PDF: 3 letter-sized pages, 233,766 bytes. The final LaTeX log has no
undefined references, overfull boxes, underfull boxes, or warnings. All
three rendered pages were inspected individually at 150 dpi on 2026-08-11.
The source crop is legible and complete; every formula, page break,
reference, and margin is clean.

SHA-256:

    solution_packet.pdf  9badc481b2e8078d89654e0396e1927c1aa5ca1b0d9e51529b0fc71f37c3e86e
    source_paper.pdf     28442bb1a8c0985e8d33ab385a7b2bf10686f0ec5a770b059afd970cff427f7f
    open_problem_crop    1c837538c8669cfcba977113f5666cb73c822c3a2fd7d79817736cea08923b2e
