# Verification report

## Result classification

Candidate full solution, likely valid; novelty cautious. The packet proves the
specific `g=2` wild-disc conjecture stated in Section 5.3 of the current
manuscript associated with arXiv:2212.00748.

## Source audit

- `source_paper.pdf` is the authors' 37-page manuscript created January 24,
  2024, downloaded from Igor Klep's publication page.
- PDF page 17 says that the existence of non-free matrix extreme points for
  `g=2` is still open, says the authors “strongly strongly conjecture” such
  points for the wild disc, gives the wild-disc LMI, gives
  `I-X^2-Y^2 >= 0`, and identifies the expected `8 x 8` regime.
- `figures/open_problem_page17.png` is a readable 180-dpi rendering of that
  page and was visually inspected.
- Cheap run indexes and bounded web/arXiv searches through 13 August 2026 for
  the identifier and the combinations “wild disc”, “matrix extreme”, and
  “non-free matrix extreme” found the source paper and a 2024 survey, but no
  later exact two-variable example. Specialist novelty review is still
  recommended.

## Mathematical audit

1. The Schur complement of the two identity diagonal blocks gives membership
   exactly when `I-X^2-Y^2 >= 0`.
2. The rational data satisfy `P=I-X^2-Z^T Z`. The checker proves the rational
   center `Q` has square residual below `1.265e-15`.
3. On upper-triangular coordinates, a rational approximate inverse for
   `H -> QH+HQ` has exact residual below `1.827e-9`; the inferred inverse norm
   is below 1192.
4. The contraction constant is below `5.748e-8`, so a symmetric exact root
   `Y^2=P` exists within `3.014e-12` entrywise of `Q`.
5. Exact multiplication gives `ZK=0`; a `3 x 3` minor of the numerator of `Z`
   is `-42`, hence `rank(Z)=3`, `dim ker(Z^T Z)=5`, and the displayed
   `(K,-XK,-YK)` columns span `ker L_A(X,Y)`.
6. Direct block multiplication of the source paper's matrix-extreme equation
   gives exactly the three systems used in the packet. The trace equation also
   matches Theorem 2.6(3).
7. A fixed 108-row minor at `Q` has an exact rational inverse-residual bound
   below `2.075e-6` and inverse infinity-norm bound below 3146.
8. The row-sum perturbation from `Q` to `Y` is at most
   `(2176/21)||Y-Q||_max`. The final Neumann product is below `9.824e-7`, so
   the actual minor is invertible and the point is matrix extreme.
9. The Arveson system has `3*5=15` scalar equations and `2*8=16` unknowns.
   It therefore has a nonzero solution. By the source paper's Proposition 2.4
   and Corollary 2.5, the matrix extreme point is not free extreme.

## Computational audit

Executed from the packet directory:

```sh
conda run --no-capture-output -n sandbox python -m py_compile \
  code/verify_wild_disc_certificate.py
conda run --no-capture-output -n sandbox python \
  code/verify_wild_disc_certificate.py
```

The run printed `EXACT CERTIFICATE: PASS`. Floating point only proposes the
two rational approximate inverses. All accepted residuals, inverse bounds,
contraction bounds, and rank-stability bounds are recomputed with Python
integers and `Fraction` arithmetic. The packet checker matches the attempt
copy byte-for-byte.

## PDF and rendering audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final log contains no undefined references, overfull boxes, underfull
  boxes, or LaTeX warnings.
- Ghostscript text extraction contains the theorem, exact data, certificate,
  non-free conclusion, review status, and references.
- `solution_packet.pdf` has five letter-size pages.
- All five pages were rendered at 150 dpi and visually inspected. Equations,
  large integer matrices, margins, page transitions, references, and page
  numbers are legible, with no clipping or overlap.

## Review recommendation

Prioritize an independent run of the checker, then review the source-Theorem
2.6 translation and the perturbation factor `2176/21`. Subject to those checks
and a specialist novelty search, this should be accepted as a full affirmative
solution of the two-variable wild-disc conjecture.
