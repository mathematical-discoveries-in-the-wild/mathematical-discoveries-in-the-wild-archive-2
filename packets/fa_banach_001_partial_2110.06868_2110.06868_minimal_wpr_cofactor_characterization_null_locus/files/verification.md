# Verification report

Verdict: **likely valid candidate partial result**.

## Exact checker

Command, run from this packet directory:

```sh
conda run --no-capture-output -n sandbox python code/verify_cofactor_theorem.py
```

Observed output:

```text
published n=3 example: full spark and all cofactor equations verified
published n=4 example: explicit equal-magnitude non-WPR pair verified
n=2: explicit witness gives nonzero hypersurface polynomial F=1
n=3: explicit witness gives nonzero hypersurface polynomial F=1
n=4: explicit witness gives nonzero hypersurface polynomial F=1
n=5: explicit witness gives nonzero hypersurface polynomial F=1
n=6: explicit witness gives nonzero hypersurface polynomial F=1
n=7: explicit witness gives nonzero hypersurface polynomial F=1
n=8: explicit witness gives nonzero hypersurface polynomial F=1
all exact checks passed
```

The code uses integer Bareiss determinants. It checks examples and the explicit
nonzero-polynomial witness; it does not prove the all-dimensional theorem.

## Exhaustive sign-frame subsearch

Command:

```sh
conda run --no-capture-output -n sandbox python code/search_sign_frames_n5.py
```

Observed output:

```text
projective row sets checked: 12870
full-spark row sets: 0
minimal-WPR solutions: 0
```

This is a complete exact enumeration of eight projective `{+1,-1}` rows in
`R^5`, normalized to have first coordinate `+1`. It rules out only that finite
ansatz and does not settle general real existence.

## Manual proof audit

- Necessity: normalized complementary kernel vectors yield an equal-magnitude
  ambiguity. Weak sign agreement makes every coordinate difference of squares
  have the same sign; their sum is zero, so every difference vanishes.
- Sufficiency: full spark reduces nontrivial ambiguities to balanced row
  partitions. Equal square profiles give `v=D u`, after which every nonzero
  product `x_j y_j` has the common sign of `b^2-a^2`.
- Algebraic nullity: a single fixed-partition cofactor equation is a polynomial.
  On the two shifted coordinate blocks it evaluates to `1`, so it is nonzero.
- Published `R^4` example: direct multiplication gives
  `|Phi x|=|Phi y|=(2,0,2,2,0,2)` for the pair in the packet, while the common
  coordinate products have opposite signs.

## Non-proof evidence kept out of the theorem

Unconstrained and one-split-conditioned floating-point optimizations in
dimensions four and five repeatedly approached the cofactor equations by
losing a coordinate or a minor. Those runs motivated further checks but are
not a certificate and are not used in any claimed conclusion.
