# Verification report

Status: `candidate_counterexample_likely_valid`

## Direct verifier

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1109.0313_finite_monoid_weak_exactness_counterexample/code/verify_counterexample.py
```

Output:

```text
verified associative unital monoid, injective coproduct, derivation, non-innerness
table ((0, 0, 2), (0, 1, 2), (0, 2, 2))
inner_pattern (1, 0, 1) derivation_pattern (1, 0, 0)
```

The script checks the 27 associativity identities, a two-sided identity,
surjectivity of the multiplication map, multiplicativity of both module
characters, all nine basis derivation identities, and non-innerness.

## Exhaustive discovery search

Commands:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1109.0313_finite_monoid_weak_exactness_counterexample/code/search_finite_semigroups.py \
  --n 2 --all-hits

conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1109.0313_finite_monoid_weak_exactness_counterexample/code/search_finite_semigroups.py \
  --n 3 --all-hits
```

Summary output:

```text
SUMMARY n=2 tables=16 semigroups=8 module_cases=14 hits=0
SUMMARY n=3 tables=19683 semigroups=113 module_cases=341 hits=27
```

For the promoted unital table with support `{1}`, the exact rational
calculation returns `H1_dim=1`, `Der_dim=2`, and `Inn_dim=1`. The search was
used to discover and sanity-check the example. The packet proves the required
nonzero cohomology directly and does not rely on exhaustive enumeration.

## Proof audit

- The table is associative by the final-factor split `u in {0,2}` versus
  `u=1`.
- The coproduct is an injective normal unital coassociative star
  homomorphism; injectivity follows by evaluating at `(1,t)`.
- The coordinate line `E=C 1_{1}` is stable under both `A` actions and under
  pointwise multiplication by `M`.
- Finite dimensionality implies weak-star operator closedness.
- The derivation identity reduces to three cases according to the right
  factor `t`.
- The inner-derivation line and the displayed derivation have incompatible
  value vectors.

## Render audit

The packet was compiled with `latexmk` into a five-page PDF. All five final
pages were rendered at 144 dpi and visually inspected. The source screenshot
is readable at normal review zoom, the question is not clipped, equations and
the multiplication table are legible, and there are no overlapping or missing
elements.
