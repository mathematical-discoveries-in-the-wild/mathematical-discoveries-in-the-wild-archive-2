# Verification report

Verification date: 11 August 2026.

## Exact mathematical certificate

Command:

```text
conda run --no-capture-output -n sandbox python -u \
  runs/fa_banach_001/solutions/full/0902.2731_nonconvex_thy_angle/verify_certificate.py
```

The command exited with status 0. Its decisive output was:

```text
C degrees=(96, 84)/(96, 84) terms=4074/4123
R gcd degree=(64, 57)
R degrees=(128, 112)/(128, 112) terms=7289/7289
primitive contents numerator=1057606992923406500991852890973798400000000000000000000000000000000
primitive contents denominator=1057606992923406500991852890973798400000000000000000000000000000000
CERTIFIED: all 13,545 numerator Bernstein coefficients are positive
numerator minimum=12531744508246953 at (0, 0)
CERTIFIED: all 14,577 denominator Bernstein coefficients are positive
denominator minimum=1285453186679270785/28 at (1, 1)
```

The omitted maximum coefficients are also exact and positive. The verifier:

1. reconstructs the unit-direction rational parametrization from the gauge;
2. evaluates both polarization terms using the exact Cartesian formula for
   `q^2`;
3. differentiates the rational Thy cosine and cancels its exact polynomial
   gcd;
4. strips only the manifestly positive factor `(1+z^2)^4`;
5. converts both remaining primitive polynomials to the tensor Bernstein
   basis using Python `Fraction`, with no floating-point arithmetic; and
6. asserts their degrees, term counts, coefficient counts, and exact least
   coefficients.

The equal primitive contents show that the positive prefactor in the
normalized derivative identity is exactly one. Strict positivity of every
Bernstein coefficient proves strict positivity of both polynomials on
`[0,1]^2`, hence strict angular monotonicity on the first half-circle.
Antipodality and reflection give the second half-circle.

## Independent hand checks

- `9/10 <= 1 + cos(4 theta)/10 <= 11/10`, proving positive definiteness.
- At `h=pi/8`, the two unit vectors `(cos h, +/- sin h)` have midpoint
  `(cos h,0)` of gauge `(11/10) cos h > 1`, proving failure of the triangle
  inequality.
- At separation `0` the normalized polarization is `1`; at separation `pi`
  it is `-1`.
- For `epsilon=pi-delta`, the identity
  `C_alpha(pi-epsilon)=-C_{-alpha}(epsilon)` transfers the negative derivative
  from `(0,pi/2]` to `[pi/2,pi)` without changing the base direction inside
  the differentiated expression.
- An affine line not through the origin traverses one open semicircle in
  strict order, so composing its direction parameter with the strictly
  decreasing polarization cosine and then with `arccos` gives (An 11).

## Source integrity

- `source_paper.pdf`: 21 pages, SHA-256
  `6317f5e5eaa6e0954e51ae1a48fb73bba0fc092b7f38fcf5f4b0931ee5a95321`.
- `figures/problem_crop.png`: SHA-256
  `4ec92bd828c901a57cc2df69cd1339b0f48b8d38af94ee4a0ff153c128427db2`.

## PDF checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex`
  exited with status 0 and resolved all cross-references.
- The final log has no overfull boxes, underfull boxes, undefined references,
  compilation warnings, or errors. (The only grep match is the package name
  `infwarerr` in a package-information line.)
- The final packet has 5 letter-sized pages.
- All five pages were rendered at 150 dpi with Poppler and inspected at
  original resolution. The source crop is legible; equations, status box,
  table, captions, page numbers, and references are unclipped and
  non-overlapping. A first render exposed literal `qquad`/`quad` text from
  missing TeX backslashes; these were corrected before the final render.
- Final `solution_packet.pdf` SHA-256:
  `cbfb368f4b2a03f5fa168a057a7fc52b585578d085799400897e00097d43922d`.
