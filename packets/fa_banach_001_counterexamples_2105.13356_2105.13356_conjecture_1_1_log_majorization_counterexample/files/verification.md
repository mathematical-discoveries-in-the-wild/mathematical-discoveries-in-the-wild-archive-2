# Verification report

Status: `candidate_counterexample_likely_valid_needs_human_review`

## Mathematical audit

1. The example uses `t=15/16` and the exact integer matrices displayed in the
   packet.
2. `A` is positive definite by inspection.  Sylvester's criterion applied to
   `B` gives leading principal minors
   `117567`, `5579090793`, `55894510422`, and `2308323855975`, all positive.
3. For `X=A^t(A#_tB)B^(1-t)`, determinant multiplicativity gives
   `det X=det A det B=det(AB)`.
4. Therefore the `k=3` log-majorization inequality is equivalent to
   `s_min(X)>=s_min(AB)`.
5. With `q=1179/5`, exact integer arithmetic shows that
   `25(AB)^T(AB)-1179^2 I` is positive definite.  Hence
   `s_min(AB)>q=235.8`.
6. The included rational-ball verifier encloses all four successive square
   roots used for the sixteenth powers.  Its final operator-norm ball for `X`
   has radius below `2.546e-42`.
7. A rational trial vector in that ball gives the exact certified upper bound
   `s_min(X)<235.715744`.
8. Thus `s_min(X)<s_min(AB)`, and the conjectured log-majorization fails.

## Exact certificate audit

The square-root enclosure uses the identity

`R(R-S^(1/2))+(R-S^(1/2))S^(1/2)=R^2-S`

and the Frobenius-norm bound

`||R-S^(1/2)||_F <= ||R^2-S||_F /
 (lambda_min(R)+sqrt(lambda_min(S)))`.

Every center and radius used after the initial numerical choice is a Python
`Fraction`.  Frobenius square roots are enclosed by integer square roots with
320 binary digits.  Matrix inverses are exact rational Gauss--Jordan inverses;
positive definiteness is checked by exact rational `LDL^T` pivots.  The final
two asserted inequalities are comparisons of exact rational numbers.

Running

```text
conda run --no-capture-output -n sandbox python \
  code/certify_counterexample.py
```

prints, in part,

```text
X ball radius <= 2.54531435395167742886893326151e-42
approximate s_min(X) = 235.715743188457775258697029297
approximate s_min(AB) = 235.93595791243642253277542207
approximate prefix-3 ratio = 1.00093423850694004245401405195
certified s_min(X) <= 235.715743188457775258697029297
threshold = 235.8
(AB)^T(AB)-threshold^2 I SPD: True
CERTIFIED: s_min(X) < threshold < s_min(AB)
```

## Discovery-search audit

The heuristic search sampled real and complex positive matrices in dimensions
2--5 with logarithmically distributed spectra and optimized the reduced real
`2 x 2` family.  The first strict violation appeared for real `4 x 4`
matrices at the third prefix product.  Simultaneous orthogonal conjugation,
independent positive rescaling, replacement of `t` by `15/16`, and rounding to
one decimal place preserved the gap; multiplying both rounded matrices by ten
produced the exact integer example.  The search is not part of the proof.

## Literature audit

- The four cheap run indexes contained no row for arXiv:2105.13356 or its exact
  Conjecture 1.1.
- Exact-expression, title, author, DOI, log-majorization, and weighted
  geometric-mean searches were performed through 2026-08-11.
- Gan and Kim, arXiv:2301.07934, Section 3, explicitly reproduce the exact
  inequality and call it still open.
- OpenAlex listed three works citing the published source: Gan--Kim (2023/24),
  Furuichi--Moradi--Conde--Sababheh (2023/24), and
  Audeh--Moradi--Sababheh (2026).  Their available source/abstracts concern
  other mean or singular-value inequalities and do not state this
  counterexample or decide the exact conjecture.
- No prior counterexample was found.  This is a bounded novelty audit, not a
  definitive priority claim.

## Rendering audit

The final packet is a four-page US-Letter PDF.  The final `latexmk` log has no
warnings, undefined references, overfull boxes, or underfull boxes.  All four
pages were rasterized at 150 dpi with Poppler and inspected individually; the
source crop, matrices, exact principal minors, equations, proof-ending symbol,
references, margins, and page breaks are clean and legible.  The final packet
and `tmp/main.pdf` are byte-identical, with SHA-256
`db30fc7a1f4646e28e222e62f5b567dba5b204281500c5933537fef7fd796dbb`.

