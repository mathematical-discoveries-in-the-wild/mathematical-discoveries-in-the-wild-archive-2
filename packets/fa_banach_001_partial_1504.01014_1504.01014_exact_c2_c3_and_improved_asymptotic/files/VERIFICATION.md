# Verification report

Verdict: `candidate_substantial_partial_solution_likely_valid`

## Source audit

The local PDF is arXiv:1504.01014, *Discrete uncertainty principles and sparse
signal processing*, by Afonso S. Bandeira, Megan E. Lewis, and Dustin G. Mixon.
Problem 3 on PDF page 5 asks for the largest additive numerical-sparsity
constant `c(n)`.  The full-width crop contains the complete problem and the
source's bounds `c(n)<1+1/n` for `n>=4` and
`liminf c(n)>=1/540000`.

## Dimension-two audit

For the normalized `F_2`, direct multiplication gives
`y_0y_1=(x_0^2-x_1^2)/2`.  After ordering magnitudes `a>=b`, reverse triangle
and `ab>=b^2` give a pair-product sum at least `1/2`.  Thus the uncertainty sum
is at least 3.  A coordinate vector attains 3, and every 2-dimensional unitary
has the universal basis-vector upper bound 3.  Therefore `c(2)=3/2`.

## Dimension-three audit

The three phase-weighted identities in the packet were expanded directly with
`1+omega+omega^2=0`.  Each weighted sum is bounded by the sum `S(F_3x)` of the
three output pair-product magnitudes.  If `a>=b>=c` are the input magnitudes,
the appropriate identity gives `S(F_3x)>=a^2-bc`.  Adding
`S(x)=ab+ac+bc` yields `a(a+b+c)>=a^2+b^2+c^2=1`.  Hence the sum of numerical
sparsitites is at least 4, with equality at a coordinate vector.  The universal
upper bound is also 4, proving `c(3)=4/3`.

## Nullspace-width audit

After decreasing rearrangement into blocks of size `k`, each tail block has
2-norm at most the previous block's 1-norm divided by `sqrt(k)`.  Summing gives
both `sum_(j>=1)||z_(S_j)||_2<=||z||_1/sqrt(k)` and the same bound for the total
tail 2-norm.  RIP plus `Phi z=0` bounds the head by
`sqrt((1+delta)/(1-delta))` times this quantity.  Pythagoras gives exactly

```text
||z||_2^2 <= 2 ||z||_1^2 / ((1-delta)k).
```

No `delta<1/3` restriction is used; `delta<1` suffices.

## Parameter audit

For `delta=7/10` and `k=floor(n/5000)`, monotonicity of
`alpha log(e/alpha)` reduces the source theorem's condition to

```text
(256/2450) log(5000e) < (256/2450)(9.52) < 1.
```

The final nullspace lower bound is `(1-delta)k/2=3k/20`.  With
`z=(Ux,-x)`, its numerical sparsity is no larger than
`ns(x)+ns(Ux)`.  Dividing by `n` gives `liminf c(n)>=3/100000`.

## Upgrade-attempt audit

Eight focused routes are recorded in
`runs/fa_banach_001/attempts/1504.01014_optimal_numerical_sparsity_constants_attempt.md`:
universal upper bounds, exact dimensions two and three, dimension four,
phase-identity extension, direct RIP width, parameter optimization, and the
secondary deterministic-Fourier problem.  The all-dimensional exact problem
has no remaining credible route at the present budget.

## Novelty audit

Bounded local-index and web searches on 2026-08-11 found no explicit later
answer to Problem 3 and no exact match for `c(2),c(3)`.  Searches used the
source title/arXiv id/authors, the exact uncertainty expression, numerical
sparsity with optimal unitaries, and small-dimensional Fourier `l_1`
uncertainty.  Nearby papers use different functionals.  The deterministic
partial-Fourier search found later finite-vector-space results, not an answer
to the cyclic deterministic formulation.

## Human verifier focus

1. Expand the three `F_3` quadratic identities independently.
2. Check that relabeling magnitudes is compatible with selecting the
   corresponding weighted identity.
3. Recheck the decreasing-block tail inequality and Pythagorean constant.
4. Confirm the source's Theorem 8 allows every `delta<1`.
5. Recheck the elementary logarithmic bound for `delta=0.7`, `k=n/5000`.

## Build and render audit

The packet compiled to a four-page PDF without LaTeX warnings.  All four
pages were rendered to PNG at review resolution and visually inspected on
2026-08-11.  Equations, theorem boxes, the source crop, page breaks, and
references are legible; no clipping, overlap, missing glyphs, or malformed
math was observed.

SHA-256 checksums:

```text
a1d0e5690679f07c9d0c4620b35f7c54d8375fd59f53962eb22621408c8b628a  solution_packet.pdf
c12d6001379ecc179c13b4bd27f9ac84109e07b0e88e8deb8f93999a303a9f08  source_paper.pdf
1e0ddcac0c2690fb3374c74fccf580e56ca9462951ff48bd7b6961fd8bdc1cff  figures/open_problem_crop.png
```
