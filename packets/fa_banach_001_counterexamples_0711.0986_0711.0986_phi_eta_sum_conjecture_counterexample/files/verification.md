# Verification notes

## Exact source target

Page 2 of arXiv:0711.0986 defines `bar_eta_{ij}`, recalls
`bar_eta_{ij}<=2 phi_{j-i}`, displays the aggregate conjecture, and states that
it remains open. The packet uses the standard finite-sequence coefficient

```text
phi_r = max_t sup |P(B|A)-P(B)|,
```

where `A` ranges over positive-probability events in the past through time
`t`, and `B` over events from time `t+r` onward.

## Eta-matrix audit

The alphabet is `{+1,-1}^L`. In coordinate `k`, the only dependent pair is
`(Z_k,Y_k)` at times `k` and `k+L`. All other entries are independent fair
signs. Therefore:

- at time `i<=L`, changing the `i`th coordinate changes only the law of
  `Y_i`;
- its total variation change is exactly `c` while the tail still contains
  time `i+L`;
- after that time the change is zero; and
- for `i>L`, the current symbol has no dependent future variable.

Thus `bar_eta_{ij}=c` exactly on `i<=L`, `i<j<=i+L`, and is zero otherwise.
With `c=1/L`, the maximal row sum is exactly one.

## Phi lower-bound audit

At cut `t=L`, the past event `Z_r=...=Z_L=+1` has positive probability.
The corresponding future contains `m=L-r+1` independent signs of bias `c`.
Marginally those signs are independent and fair. Hence `phi_r` is at least
the total variation between the biased and unbiased product measures.

For the likelihood ratio `Lambda=product(1+c epsilon_i)`, orthogonality gives

```text
E(Lambda-1-cS)^2 = (1+c^2)^m-1-mc^2.
```

The fourth-moment identity `E S^4=3m^2-2m`, combined with Holder, gives the
self-contained bound `E|S|>=sqrt(m/3)`. These facts yield the lower estimate
used in the manuscript without asymptotics or a central limit theorem.

## Constants

For `L=1024`, `c=1/L`:

```text
max_i sum_j bar_eta_ij = 1,
conjectured right side = 2,
analytic lower bound on the left side = 2.9333313745...,
exact binomial lower value = 4.2591246806....
```

Only the analytic value is needed for the proof.

## Full-support audit

Since `0<c<1`, every `(Z_k,Y_k)` sign pair has positive probability. Together
with the independent fillers, this gives positive mass to every point of the
finite product alphabet. No conditional probability on a null atom is used.

## Literature bounds

A bounded search on 2026-08-11 covered the run registry, the exact title,
`eta-mixing`, `phi-mixing`, the displayed comparison, and the phrase `the
latter remains open`. It found the arXiv/published source and bibliographic
copies, but no later primary paper stating a proof or counterexample. A
broader primary-source query timed out and no full citation-graph sweep was
performed, so novelty confidence is moderate rather than definitive.

## Human-review recommendation

Review should prioritize:

1. agreement of the finite-sequence `phi_r` convention with the source's
   cited convention;
2. the assertion that the full vector-valued sequence has exactly the stated
   eta matrix; and
3. the likelihood-ratio remainder estimate and final factor `1/2`.

## Packet build validation

- `check_counterexample.py` passed all assertions and evaluated all 1024
  product total variations.
- `latexmk` completed with no warnings, undefined references, or overfull or
  underfull boxes in the final log.
- The final PDF has 5 letter-sized pages and SHA-256
  `de34b500e07cea9df32987220f4e1952be1ff65ab2a80f9b74ad4b3a7181e221`.
- Every final page was rendered at 150 dpi and visually inspected on
  2026-08-11; no clipping, overlap, illegible display, or broken evidence
  image was found.
