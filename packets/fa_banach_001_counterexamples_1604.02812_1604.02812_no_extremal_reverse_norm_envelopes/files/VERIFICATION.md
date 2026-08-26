# Verification record

## Source and literature

- The two existence questions were verified in arXiv:1604.02812, PDF page
  11, immediately after Corollary 3.5.
- The source proves only special cases after asking the general questions.
- Targeted searches by identifier, title, exact extremal-norm phrases, and
  core keywords found no explicit later full answer or matching
  counterexample.

## Proof audit

1. `||.||_1` is an L-norm as the dual of the operator M-norm.
2. `omega_*` is an L-norm as the dual of the numerical-radius M-norm.
3. Positive scaling preserves the L property, so both norms in the maximum
   defining `p` are L-norms.
4. The exact values `omega_*(E)=1`, `omega_*(J)=2`, and
   `omega_*(E+J)=3` have matching upper and lower bounds in `main.tex`.
5. The two projection compressions satisfy the coefficient constraint and
   yield `5/2 > 9/4`, so `p` is definitively not an L-norm.
6. A greatest L-minorant would have to dominate both component L-norms and
   therefore equal their non-L maximum.
7. Finite-dimensional duality reverses all norm inequalities and takes
   L-norms to M-norms, so the companion nonexistence result follows exactly.

## Computational verifier

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_counterexample.py
```

Result: PASS.  It checked the projection constraint and compressions, the
three trace norms, the numerical-radius witness values, all three dual
pairings, and the strict `5/2 > 9/4` violation.  The matching analytic upper
bounds for the dual numerical-radius values are proved in `main.tex`.

## PDF audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final packet has 4 pages and no unresolved-reference, overfull-box, or
  underfull-box warnings.
- All 4 pages were rendered at 145 dpi and visually inspected.  The source
  page, equations, table, proofs, and references are legible, with no clipping
  or overlap.
