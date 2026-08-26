# Verification record

## Source and literature checks

- Source question verified in arXiv:1510.04560v2, Remark 4.4(b), PDF page 14.
- Supporting estimate verified in arXiv:2205.13843v2, Lemma 4.1(iii), PDF
  page 10: `max_i ||T^k P_{M_i^perp}|| = O(k^-1/2)`.
- Reich--Zalas bibliographic identity cross-checked against the arXiv record
  and DOI `10.1007/s11075-023-01533-w`.
- Bounded exact-phrase/title/identifier searches found no explicit statement
  of the fractional-range implication.  Classification is therefore
  `literature_implied_answer (full)`, not `literature_already_answered`.

## Proof audit

For `0 < alpha < 1/2`:

1. The coefficients `c_n` of `(1-z)^(-alpha)` satisfy
   `c_n = O(n^(alpha-1))`.
2. Reich--Zalas gives `||T^n Q_i|| = O(n^-1/2)`, so
   `sum c_n ||T^n Q_i|| < infinity`.
3. The coefficients `d_m` of `(1-z)^alpha` satisfy
   `sum |d_m| < infinity`; since `T` is a contraction, the corresponding
   operator series converges absolutely.
4. The product double series is absolutely convergent because
   `||T^(m+n) Q_i|| <= ||T^n Q_i||`.
5. Its scalar convolution is exactly 1, hence
   `(I-T)^alpha B_i = Q_i`.
6. Summing these factorizations over finitely many `i` proves the algebraic
   sum inclusion.

The real-to-complex transfer is harmless: regard a complex Hilbert space as
a real one.  Orthogonal projections, products, norms, and the estimate are
unchanged; the binomial functional calculus is then applied to the original
complex-linear contraction.

## PDF audit

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  completed successfully.
- The final PDF has 5 pages and no unresolved-reference, overfull-box, or
  underfull-box warnings.
- All 5 pages were rendered at 135 dpi and visually inspected.  Text,
  equations, embedded source pages, captions, and bibliography are legible;
  nothing is clipped or overlapping.

## Exact coefficient verifier

Command:

```text
conda run --no-capture-output -n sandbox python code/verify_binomial_convolution.py
```

Result: exact rational convolution coefficients through degree 40 passed for
`alpha = 1/7, 1/3, 2/5, 49/100`.  This checks the Cauchy-product identity used
in the proof; the analytic convergence justification remains the proof given
in `main.tex`.
