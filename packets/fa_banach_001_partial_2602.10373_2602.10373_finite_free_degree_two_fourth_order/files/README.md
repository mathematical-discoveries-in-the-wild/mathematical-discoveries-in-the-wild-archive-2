# Degree-two case of the finite-free fourth-order comparison

Status: `candidate_partial_likely_valid`.

Source: Otte Heinävaara, *Convolution comparison measures*,
arXiv:2602.10373, Conjecture 5.2 on page 16.

## Result

Conjecture 5.2 is true for every pair of monic real-rooted quadratic
polynomials. If `mu_p` and `mu_q` put equal mass on the two roots of `p` and
`q`, then for every `f in C^4(R)` with `f^(4)>=0`,

```text
(1/2) sum_{x:(p boxplus_2 q)(x)=0} f(x)
    <= integral f d(mu_p boxplus mu_q).
```

The proof also gives a standalone extremal lemma: among compactly supported
symmetric laws with a fixed second moment, the symmetric two-point law is
minimal for every test with nonnegative fourth derivative.

## Proof mechanism

Write the roots as `m +/- alpha` and `n +/- beta`. The finite convolution has
roots

```text
m+n +/- sqrt(alpha^2+beta^2).
```

After centering, the free convolution is a symmetric random variable `Z` with
the same second moment. For `t>=0`,

```text
v -> (sqrt(v)-t)_+^3
```

is convex. Jensen applied to `Z^2` compares the cubic stop-loss transforms.
Symmetry handles negative `t`, and Taylor's integral remainder converts the
kernel comparison into the desired inequality for every `f`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original source paper.
- `figures/conjecture_5_2_crop.png`: exact source-page crop.
- `supporting_mss_finite_free_convolution.pdf`: supporting definition paper.
- `code/verify_degree_two.py`: symbolic verification of the two algebraic
  identities used in the proof.
- `verification.md`: reproducibility and QA record.

## Scope

The general-degree conjecture remains open here. A serious upgrade attempt
found that the constant-square Jensen mechanism is special to degree two; it
already ceases to apply to symmetric cubics. Exact moment and random-matrix
searches found no counterexample in higher degrees.

Human review should focus on the fourth-order extremal lemma and the passage
from cubic stop-loss kernels to arbitrary `C^4` tests.

