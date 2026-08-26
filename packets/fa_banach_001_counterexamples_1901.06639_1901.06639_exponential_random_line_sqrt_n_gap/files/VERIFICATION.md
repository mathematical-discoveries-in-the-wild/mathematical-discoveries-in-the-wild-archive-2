# Verification report

Verdict: `candidate_full_counterexample_likely_valid`

## Source audit

The packet's `source_paper.pdf` is arXiv:1901.06639v2, *Random sections of
ellipsoids and the power of random information*, by Aicke Hinrichs, David
Krieg, Erich Novak, Joscha Prochno, and Mario Ullrich.  The full-width crop is
from PDF page 8 and contains the complete prose question plus Corollary 9.
The source asks whether `E[R_n(sigma)] asymp sigma_(n+1)` holds for
`sigma_j asymp a^j`, `0<a<1`.

## Kernel-line audit

The first `n+1` columns of the `n`-row Gaussian matrix have rank `n` almost
surely.  A vector on their null line, extended by zero, is annihilated by the
full infinite matrix.  Intersecting the ellipsoid with this one line can only
decrease its radius, so its line radius is a valid lower bound for `R_n`.

Right orthogonal invariance of an `n`-by-`(n+1)` iid Gaussian matrix makes the
unoriented null line Haar distributed.  Because the radius is sign invariant,
representing its unit direction as `g/||g||` is exact in distribution.

## Algebra audit

For `sigma_j>=c_0a^j`,

```text
L_n >= c_0 ||g|| / sqrt(sum_(j=1)^(n+1) a^(-2j)g_j^2)
    = c_0 a^(n+1)||g|| / sqrt(Q_n),
Q_n = sum_(r=0)^n a^(2r)g_(n+1-r)^2.
```

The factorization was checked term by term: multiplying the denominator by
`a^(n+1)` changes `a^(-2j)` into `a^(2(n+1-j))`.

## Probability and constant audit

`E[Q_n]<=1/(1-a^2)`, hence Markov gives
`P[Q_n<=4/(1-a^2)]>=3/4`.  For `d=n+1`, the standard bound
`P[chi_d^2<=d/2]<=exp(-d/16)` gives probability at least `3/4` for the norm
event when `d>=16 log 4`, hence for every integer `n>=22`.  The union bound
gives intersection probability at least `1/2`; independence is not assumed.

On the intersection the witness is at least

```text
c_0 a^(n+1) sqrt((n+1)(1-a^2)/8).
```

Multiplication by `1/2` yields the theorem's coefficient
`c_0 sqrt(1-a^2)/(4 sqrt(2))`.  Dividing by
`sigma_(n+1)<=C_0a^(n+1)` leaves a constant times `sqrt(n+1)`.

## Sharper-asymptotic audit

After reversing iid Gaussians, the normalized line witness is a ratio whose
numerator tends to one by the strong law and whose denominator tends to
`Q_infinity^(1/2)` by monotone convergence of the weighted square series.
The inverse square-root limit is integrable because it is bounded above by
`(h_0^2+a^2h_1^2)^(-1/2)`, locally integrable in two dimensions.  Fatou's
lemma is used only for a lower bound and requires no uniform integrability.

## Computational audit

`code/check_random_line_scaling.py` simulates the exact line formula.  It uses
no optimization and checks only that the normalized witness is stable across
increasing dimensions.  The command

```text
conda run --no-capture-output -n sandbox python \
  code/check_random_line_scaling.py --samples 10000 \
  --dimensions 10 25 50 100 200
```

returned mean normalized witnesses `1.29919`, `1.33080`, `1.33258`,
`1.31809`, and `1.32489`, respectively.  The computation is explicitly
non-probative.

## Novelty audit

Bounded searches on 2026-08-11 covered the four local indexes, exact source
metadata and wording, arXiv metadata queries for random ellipsoid sections and
exponential decay, and the 18 OpenAlex-indexed citing works for DOI
`10.1090/tran/8502`.  No explicit answer or the finite-coordinate random-line
argument was found.  arXiv:2109.14504 treats generalized `ell_p` ellipsoids
with emphasis on polynomial axes.  The later arXiv:2209.07266 survey describes
the exponential case only through the known polynomial-loss upper bound.

## Limitations

The proof disproves constant-factor equivalence but does not close the gap
between the lower scale `sqrt(n)a^n` and the source upper scale `n^2a^n` for
the full random radius.

## Human verifier focus

1. Confirm that the null line of the first `n+1` columns embeds into the full
   infinite-dimensional kernel.
2. Confirm the Haar law of that null line under right orthogonal invariance.
3. Recompute the coordinate reversal and the explicit constant.
4. Check that the source's `asymp` constants are independent of `n`, so the
   diverging square-root ratio is a complete negative answer.

## Build and render audit

The packet compiled with `latexmk` to a four-page PDF with no unresolved
references, LaTeX warnings, overfull boxes, or underfull boxes.  All four
pages were rendered at 150 dpi and visually inspected on 2026-08-11.  The
source crop is readable at normal review zoom; equations, page breaks, and
references are clean, with no clipping, overlap, missing glyphs, or malformed
math.  The source-page crop was also inspected separately at original
resolution.

SHA-256 checksums:

```text
78f323b7ea1245d2ff9f1c2dfdad426ee63c939f36e491a5859458b89a38f630  solution_packet.pdf
254569fad6625441d429505257b1bc5446b90f6ac06d016087a3fa5a576315aa  source_paper.pdf
0783eb41f72d19186039d60754296b50159702ae35b2c292c844960d7fb3f8ac  figures/open_problem_crop.png
```
