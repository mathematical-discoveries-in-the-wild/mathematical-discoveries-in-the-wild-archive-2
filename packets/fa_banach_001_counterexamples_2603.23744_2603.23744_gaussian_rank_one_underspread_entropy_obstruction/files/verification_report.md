# Verification report

## Mathematical audit

- Recomputed the normalized Gaussian, rank-one kernel, Weyl symbol, and
  symplectic Fourier transform under the source paper's `2 pi` convention.
- Checked the exact real-line covering number
  `N(epsilon) = ceil(c/epsilon)` by orthogonal projection of arbitrary Hilbert
  covering centers onto the rank-one range.
- Recomputed the `2d`-dimensional radial integral and its coefficient
  `1 / (2^d d! (d+1))`.
- Checked that scaling `c` makes the spreading `L1` norm arbitrarily small
  without changing the asymptotic mismatch.
- Separately proved the operator-norm bound for an `L1` spreading
  representation.
- Audited, but did not claim, the stricter compact-spreading-support variant.
  The packet explicitly excludes that scope.

## Executable check

Command:

```text
python code/verify_gaussian_obstruction.py
```

Result:

```text
PASS: Gaussian Weyl/log-integral formulas and entropy separation verified (45 radial integrations)
```

The standard-library script uses Simpson integration in 45 combinations of
dimension, scale, and level; checks arbitrary spreading-norm smallness in
dimensions 1 through 8; and checks monotone ratio decay.  This is a numerical
sanity check only.  The packet proves the identities exactly.

## Build and visual QA

Build commands:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
cp tmp/main.pdf solution_packet.pdf
pdftoppm -png -r 150 solution_packet.pdf tmp/rendered/page
```

- `solution_packet.pdf` has 4 letter-size pages.
- The final LaTeX log has no unresolved references, warnings, underfull boxes,
  or overfull boxes.
- Every rendered page was inspected at original resolution on 2026-08-11.
- Page 1: title, status, source direction, full evidence paragraph, and first
  displayed formula are readable and unclipped.
- Page 2: definitions, proof intuition, theorem, Gaussian kernel computation,
  and spreading formula are readable and unclipped.
- Page 3: exact entropy/integral computation, boundedness proposition, and
  start of verification section are readable and unclipped.
- Page 4: limitations, novelty statement, human-review recommendation, and
  bibliography are readable and unclipped.

## SHA-256

```text
ddc005c61abcc7cf76049031ed65c5051dd03614f84114db87c8ab05297fb3e5  solution_packet.pdf
000437cb623be1661c4aeb4fd967a4839f28556284ce36702c86f8161f146db7  source_paper.pdf
c51cc126759d5d77f5e82668348d1f3186721930f41ebf6832177319528c70ba  figures/future_direction_crop.png
```

## Verdict

`candidate_counterexample_likely_valid` at the exact integrable-spreading
scope stated in the packet.  The main human-review risk is terminological
scope, not the Gaussian or entropy calculation.

