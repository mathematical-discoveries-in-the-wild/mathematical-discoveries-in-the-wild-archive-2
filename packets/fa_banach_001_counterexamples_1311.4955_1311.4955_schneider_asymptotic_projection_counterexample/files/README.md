# Negative answer to Problem 4.2 of arXiv:1311.4955

Source: Christos Saroglou, *On the equivalence between two problems of
asymmetry on convex bodies*, arXiv:1311.4955v2 (2014).

Status: candidate full counterexample, likely valid.

## Result

Let `S_n` be the supremum of

```text
P(K) = |Pi K| / |K|^(n-1)
```

over centrally symmetric convex bodies in `R^n`.  Problem 4.2 asks whether
`(S_n/2^n)^(1/n)` tends to one.  It does not.  The normalized sequence has
a limit, but

```text
lim (S_n/2^n)^(1/n) >= (9/8)^(1/3) > 1.
```

The key facts are exact multiplicativity of `P` under Cartesian products
and the elementary identity `P(B_1^3)=9`, whereas the three-cube has value
8.  Cartesian powers amplify this fixed three-dimensional gap
exponentially.

## Files

- `main.tex`: complete proof and source/context discussion.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: official source arXiv PDF.
- `figures/problem_4_2_crop.png`: source Problem 4.2.
- `figures/source_page_9.png`: full source PDF page 9.
- `code/verify_projection_product.py`: exact determinant and ratio audit.
- `VERIFICATION.md`: mathematical, source, build, and visual checks.

## Scope

This fully answers Problem 4.2 negatively.  It does not determine the exact
Schneider maximum in any dimension and does not settle the distinct polar
projection-body Problem 4.5.

## Human review recommendation

Accept as a candidate full counterexample.  Check the Cartesian-product
formula for projection bodies and the four zonotope determinants giving
`|Pi B_1^3|=16`.

