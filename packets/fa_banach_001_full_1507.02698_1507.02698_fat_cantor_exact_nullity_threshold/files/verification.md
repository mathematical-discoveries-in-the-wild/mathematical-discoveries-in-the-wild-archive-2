# Verification notes

## Exact target

The source's conclusion asks:

1. whether there are positive-measure empty-interior sets with
   `0<s_E(p)<n/p`; and
2. for the nullity threshold of the fat Cantor sets in Example 4.7.

The theorem answers both and includes all Cartesian powers used in the
source's notation.

## Critical arithmetic

Set

```text
s_0 = (1/p)(1 + log(2)/log(alpha)),
a_0 = 1-p s_0 = -log(2)/log(alpha).
```

Because `0<alpha<1/2`, one has `0<a_0<1`, `0<s_0<1/p`, and

```text
alpha^a_0 = 1/2,       2 alpha^a_0 = 1.
```

Thus the normalized capacity of the level gap is uniformly positive exactly
at `s=s_0`. For `s<s_0`, `q=2 alpha^(1-sp)<1`, so the descendant-gap series
converges.

## Localized Swiss-cheese audit

At global level `k>J`, a fixed level-`J` basic interval contains exactly
`2^(k-J-1)` gaps of length `g_k=beta alpha^(k-1)`. If `a=1-sp`,

```text
S_J = sum_{k>J} 2^(k-J-1) (g_k/2)^a
    <= C 2^(-J) (2 alpha^a)^J.
```

Writing `L=1-beta/(1-2alpha)>0`, the level-`J` interval has length
`l_J>=L 2^(-J)`. A comparison ball of radius `l_J/4` therefore has
`r^a>=c 2^(-aJ)`, and

```text
S_J/r^a <= C (2 alpha)^(aJ) -> 0.
```

This validates the strict source criterion for every beta once `J` is large.

## Capacity-density audit

For `x` in the Cantor set, a ball of radius `delta_j=2l_{j-1}` contains the
level-`j` parent gap, a ball of radius `g_j/2`. At `s=s_0`, monotonicity and
the source lower ball-capacity estimate give

```text
cap_{s_0,p}(B_delta_j(x) \ G)/delta_j
    >= c [2 alpha^(1-p s_0)]^(j-1) = c.
```

For `x` outside the closed set, sufficiently small balls lie in the
complement and the normalized capacity diverges. The source's equivalence
therefore proves threshold nullity.

## Slicing audit

For a split `R^n=R x R^(n-1)`, the multiplier

```text
m_s(xi,eta)=((1+|xi|^2)/(1+|xi|^2+|eta|^2))^(s/2)
```

satisfies the Marcinkiewicz multiplier bounds for every `s>=0`. Hence

```text
H^{s,p}(R^n) -> L^p(R^(n-1); H^{s,p}(R)).
```

Almost every slice of a function supported by `G^n` is supported by `G`, so
one-dimensional nullity forces the original function to vanish. The reverse
inequality uses the source's tensor-product proposition with a small positive
regularity margin.

## Stress tests

- Classical Smith--Volterra--Cantor set: `alpha=beta=1/4` gives
  `s_0=1/(2p)`, in particular `s_0=1/4` for `p=2`, matching the source lower
  bound.
- As `alpha` tends to `0`, `s_0` tends to `1/p`, consistent with increasingly
  tiny gaps.
- As `alpha` tends to `1/2` from below, `s_0` tends to `0`, consistent with
  gaps whose total scale approaches the thin-Cantor boundary.
- Beta affects constants and measure but cancels from the threshold exponent.

## Literature bounds

A bounded search on 2026-08-11 covered the run registry, the exact paper
title, `nullity threshold`, the quoted fat-Cantor question, and the quoted
intermediate-threshold question. It found the source paper and bibliographic
copies but no later primary paper stating this exact formula or construction.
Novelty remains subject to specialist review.

## Recommendation

Human review should prioritize:

1. the exact formulation of the source set-of-uniqueness equivalence used in
   the upper bound;
2. the passage from a level basic interval to a Swiss-cheese subset in the
   lower bound; and
3. the Marcinkiewicz conditions for the directional lifting multiplier.

## Packet build validation

- `check_threshold.py` passed four representative parameter regimes and the
  exact critical-factor identity.
- `latexmk` completed with no warnings, undefined references, or overfull or
  underfull boxes in the final log.
- The final PDF has 5 letter-sized pages and SHA-256
  `6c85035d564539f1d59ec7d54c5961f8a0bb5a1832e25dc1de84e334878fbf2b`.
- Every final page was rendered at 150 dpi and visually inspected on
  2026-08-11; no clipping, overlap, illegible mathematics, or broken source
  figure was found.
