# Verification report

Status: candidate full solution, suitable for expert review.

## Source identification

- Exact target: arXiv:2003.05382, PDF page 9, Problem 2.17.
- The crop in `figures/problem_2_17_crop.png` was regenerated from
  `source_paper.pdf` by `code/make_crop.py` and visually checked against the
  source page.
- The supporting Boolean projection identity is Lemma 3.1 of
  arXiv:1711.06227; its PDF is included.
- Exact-phrase and core-keyword searches in the local source corpus and on
  arXiv found continued use of Boolean max-convolution only for positive
  variables.  A 2025 paper treats monotone, rather than Boolean,
  selfadjoint maxima.  No later primary source answering Problem 2.17 was
  found.

## Mathematical audit

1. The Boolean product model preserves each marginal vector-state law.
2. Alternating vacuum moments factor because
   `V_i^* V_j = |xi_i><xi_j|` for distinct indices.
3. The direct-sum zero eigenspace is excluded from lower spectral projections
   for negative thresholds and included for nonnegative thresholds.
4. Below zero, the two relevant ambient subspaces intersect only in the
   vacuum line, proving the endpoint test.
5. At and above zero, complements of the lower spectral projections are
   Boolean-independent projections, so the Vargas--Voiculescu projection
   formula gives `FG/(F+G-FG)`.
6. Both scalar branches are associative; the boundary at zero preserves
   monotonicity and right continuity.
7. The finite-fold formula is also obtained directly from the atom at zero of
   the sum of the finite family of complementary projections.
8. Centering is performed only after the spectral maximum is formed, so the
   translated-input unit obstruction does not arise.
9. Applying `chi(u)=exp(1-u^{-1})` reduces all three displayed limits to the
   elementary classical limits `(1-c/n)^n -> exp(-c)`.

## Executable checks

Command:

```sh
conda run --no-capture-output -n sandbox python code/verify_formulas.py
```

Result:

```text
all Boolean-maximum formula checks passed
```

The script checks the semigroup identity on a grid, all three limit formulas,
and two finite-dimensional canonical Boolean products.  The matrix examples
include mixed-sign and purely negative marginal spectra.  Their spectral
projection intersections agree with the piecewise theorem at every tested
threshold.

## PDF build and visual QA

`latexmk -pdf -interaction=nonstopmode -halt-on-error` completed in a fresh
temporary output directory.  The final log contains no overfull/underfull box,
undefined-reference, or package warnings.  The resulting PDF has five pages.
All five pages were rendered to PNG with Poppler at 130 DPI and visually
inspected: equations and references are legible, no content is clipped or
overlapping, and the final page terminates cleanly.

This constitutes a proof because the operator construction is explicit, the
spectral projections are calculated at every real threshold, and the three
limit laws follow from exact finite-`n` CDF identities.  The numerical checks
are corroborative and are not used in place of any proof step.

