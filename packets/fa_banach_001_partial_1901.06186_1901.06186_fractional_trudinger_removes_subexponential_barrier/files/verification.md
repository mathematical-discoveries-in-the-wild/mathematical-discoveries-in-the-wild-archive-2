# Verification report

Status: `partial_likely_valid`.

## Proof audit

- From `phi(t)>=a t^p`, the Luxemburg definition directly gives
  `[u]_(W^{n/p,p}) <= a^(-1/p)||u||_(B^phi)`.
- The local Trudinger lemma is obtained by multiplying `v-v_(2B)` by a cutoff
  supported in `2B`.  Splitting pairs into `2B x 2B` and the support tail,
  fractional Poincare controls the multiplier and tail terms because `p>n`
  and `(n/p)p=n`.  Parini--Ruf Proposition 3.1 then applies after scaling.
- Restricting the extension to `B intersect Omega` gives the required local
  embedding with constants independent of the ball.
- The cutoff norm is exactly the bound in source Lemma 5.1; no new estimate is
  silently assumed there.
- Each cutoff is `1` on a set of measure `2^(-j-1)v` and `0` on a disjoint set
  of at least that measure.  Hence one of the two sets stays at distance at
  least `1/2` from any centering constant.
- Applying the local exponential estimate, inverting `phi`, and using
  `log(1+phi(t))=o(t^(p'))` yields a geometrically summable increment bound.
- The small-radius recentering argument is written with explicit constants;
  radii larger than `diam(Omega)/4` reduce to the small-radius estimate at
  radius `diam(Omega)/8`.
- The theorem is not claimed at the borderline or for arbitrary Young
  functions.
- For both displayed example families, the source condition is checked
  directly: `C_phi <= 1/(p-n)` for `t^p exp(c t^alpha)`, while termwise
  integration of the positive truncated-exponential series gives
  `C_(phi_gamma) <= 1/(q-n)`.

## Computational regression check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1901.06186_fractional_trudinger_removes_subexponential_barrier/code/verify_exponents.py
```

The script checks exact rational instances of the exponent conditions for the
two example families and verifies the geometric-series algebra for dimensions
2 through 20 and density ratios from `1e-2` through `1e-30`.  This is not a
proof; it guards against exponent and indexing mistakes.

Final output:

```text
power-times-exponential parameter checks: 1254
truncated-exponential parameter checks: 570
geometric recurrence checks: 551
all exponent and recurrence checks passed
```

## Evidence and rendering

- `source_paper.pdf` has 18 pages; the conjecture crop is from PDF page 3.
- `supporting_parini_ruf_1607.07681.pdf` has 16 pages; the supporting crop is
  Proposition 3.1 on PDF page 5.
- `solution_packet.pdf` has 4 letter-size pages.  It was rendered to PNG at
  130 dpi and every page was inspected; equations, source excerpts, margins,
  page breaks, and references are legible with no clipping.
- The final LaTeX log has no warnings, overfull/underfull boxes, undefined
  references, multiply-defined labels, or errors.

## SHA-256

```text
9d2a7ca120e8b516d2113f1a4757cade0fed102ab97c2d8bdb2bad2a61684901  solution_packet.pdf
c21f4019650456396ec11d524972d8072c2627ca2828fc65ce3cdd1eeea747de  source_paper.pdf
aac76ef464e4e17d645d50b9daadc79bb2f987d80533e54b2e1933a6bf2e7449  supporting_parini_ruf_1607.07681.pdf
943a159f0c97e91ef8c6e2f09e5e4471808cf459ba1a15ae390a0eaf679b0f5f  main.tex
05fb4ddaf097aa8032287fc8107cbea2baae8899937b50d596b08c8395c8caa2  figures/open_problem_crop.png
1b56bda993faf84f4804785d32a778373e9c14ab227c8ddd17b3416edeb248b8  figures/fractional_trudinger_crop.png
0852ec3b706c95f6b2eb437f8de211cde45386f534ca42407cd0353c6a1a6969  code/verify_exponents.py
```

## Reviewer focus

Audit the cutoff multiplier estimate in the local Trudinger lemma and the
direction of both inverse-Young-function inequalities.  Then check that the
source cutoff lemma is invoked with `t=b_j r`, `r=b_(j+1)r` and that all
constants are uniform in `j`, `x`, and the physical radius.
