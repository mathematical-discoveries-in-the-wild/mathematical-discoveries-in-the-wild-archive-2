# Verification notes

## Formal argument

For a unit vector `v`, the absolute row sum of row `i` of `vv*` is `|v_i| ||v||_1`. Hence the induced infinity norm is `||v||_infinity ||v||_1`.

Writing `m=||v||_infinity`,

`1 = sum |v_i|^2 <= m sum |v_i|`.

The defect is `sum |v_i|(m-|v_i|)`, a sum of nonnegative terms. Equality—and therefore contractivity—holds exactly when every coordinate modulus is zero or `m`. Unit normalization gives `m=1/sqrt(k)` on a support of size `k`.

## Source-coordinate list

For `v=(sin(xi)cos(phi), sin(xi)sin(phi), cos(xi))` on `[0,pi)^2`, support sizes one, two, and three yield exactly:

- `{0} x [0,pi)`;
- `{pi/2} x {0,pi/4,pi/2,3pi/4}`;
- `{pi/4,3pi/4} x {0,pi/2}`;
- `{atan(sqrt(2)), pi-atan(sqrt(2))} x {pi/4,3pi/4}`.

This union matches all families already identified in the source and proves exhaustiveness.

## Computational checks

`code/verify_classification.py`:

- verifies the norm formula against direct absolute row sums on 20,000 seeded random vectors in dimensions 2 through 8;
- verifies contractivity at all non-continuum representatives in the displayed list and at sampled points of the degenerate `xi=0` family;
- verifies strict norm increase under small generic perturbations of nondegenerate representatives.

## Source and novelty

- The exact setup and final question were checked on printed pages 18–19 of the official arXiv PDF and against the parsed TeX source.
- Cheap run indexes contained no result for arXiv:0903.3580.
- Bounded exact-title, exact-question, and rank-one contractive-projection searches found no later primary source answering this parameter question.

## Visual QA

The final packet was compiled, rendered page by page, and inspected for clipping, overflow, missing figures, and legibility.
