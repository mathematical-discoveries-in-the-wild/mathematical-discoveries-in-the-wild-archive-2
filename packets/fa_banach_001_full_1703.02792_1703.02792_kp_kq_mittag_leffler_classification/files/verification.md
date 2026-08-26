# Verification record

Status: `candidate_full_solution_likely_valid`

## Source and target

- Source: arXiv:1703.02792v2, Anand–Chavan, *On sum of two subnormal kernels*.
- Exact target: Question 3.10(ii), printed page 12.
- Cheap registry/solution/attempt/proof-gap indexes: no hit for this arXiv id.
- Bounded primary-source searches through 2026-08-11 found no later answer to
  the operator question. They did locate the independent Mittag–Leffler phase
  diagram of Hanneken–Achar–Vaught and arXiv:2312.07444, which reproduces its
  numerical boundary.

## Eight-pass proof and upgrade audit

1. Reduced subnormality, using the source criterion, to the Hausdorff moment
   sequence `a_k=1/((k+1)^m+(k+1)^M)`.
2. Identified the continuous interpolation
   `f(s)=s^(-m)/(1+s^r)` and its inverse Laplace density
   `h(t)=t^(M-1) E_{r,M}(-t^r)`.
3. Closed the discrete-versus-continuous gap: two bounded analytic functions
   on the right half-plane agreeing at every positive integer coincide,
   because those zeros violate the half-plane Blaschke condition.
4. Used uniqueness of finite Laplace-transform measures after shifting by one
   to prove that the Hausdorff property is equivalent, not merely implied by,
   nonnegativity of `h`.
5. Tested the initially plausible linear threshold `m>=r-1`. High-precision
   evaluation and the published phase table refute its sharpness; at `r=1.5`
   the true threshold is approximately `0.29365`, not `0.5`.
6. Identified the exact transition-strip criterion with the established
   zero-free boundary `M>=phi(r)` for `1<r<=2`; fractional integration proves
   that positivity is upper-closed in `M`.
7. Proved the `r>2` impossibility by contour residues: the poles
   `exp(+-i*pi/r)` dominate and create an exponentially amplified cosine, so
   the inverse density changes sign infinitely often.
8. Audited endpoints and prior results: `r<=1` follows from Schneider's sharp
   complete-monotonicity theorem; `r=2`, `phi(2)=3`, gives exactly the source's
   `m>=1` theorem; `r=0` has an elementary gamma density.

## Computational check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1703.02792_kp_kq_mittag_leffler_classification/code/check_classification.py
```

The script evaluates the defining Mittag–Leffler series at 80-digit
precision. It checks representative signs below and above the tabulated
phase boundary, the exact `r=2, m=1` identity, and an `r>2` sign change. The
proof is analytic and does not depend on finite numerical sampling.

Observed output on 2026-08-11:

```text
r=1.5 below/above: -0.026665697005852 0.004425693069404
r=1.8 below/above: -0.047508554431677 0.059862890680815
r=2 below threshold: -0.21187692971713
r=2.2 oscillatory sample: -10.374693146749
all classification sanity checks passed
```

`latexmk` compiled the five-page packet without undefined references,
overfull boxes, or final-pass LaTeX warnings. All five final pages were
rendered at 150 dpi and inspected; the source evidence was corrected to
printed page 12, and the final packet has no clipping, overlap, broken glyphs,
or illegible content.

## Human-review focus

- Check boundedness of `f(z+1)` and use of the half-plane Blaschke zero
  condition in the interpolation lemma.
- Check that `e^{-t}h(t)dt` is a finite signed measure for every exponent gap,
  including `r>2`, and hence falls under Laplace-transform uniqueness.
- Check that the Hanneken–Achar–Vaught phase boundary includes its endpoint as
  nonnegative and matches the `phi` convention used in the theorem.
- Check the contour asymptotic and phase of the dominant residue for `r>2`.

The packet does not answer Question 3.10(i) or the multivariable Question 3.11.
