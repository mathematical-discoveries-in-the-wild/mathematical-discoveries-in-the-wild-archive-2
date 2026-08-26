# Verification report

## Claims checked

1. The normalized `H^2` Gaussian in the source convention violates
   Corollary 2.3 when its constant is the value printed in Remark 2.2.
2. The normalized `H^1` Gaussian in Suguro's convention violates the same
   inequality with the proposed exact value `2/(Q*pi*e)`.

## Counterexample 1: printed source constant

For `n=2`, `m=1`, `Q=6`, take `a=1`, `b=8/5` in

```text
f_(a,b) = (a/pi)^(n/2) (b/pi)^(1/4)
          exp(-a*(|x|^2+|y|^2)/2-b*z^2/2).
```

Squaring gives a product probability density.  Applying the source fields

```text
X_i = partial_xi + (y_i/2) partial_z,
Y_i = partial_yi - (x_i/2) partial_z
```

gives

```text
Ent(f^2) = -(5/2)log(pi)+(1/2)log(8/5)-5/2,
E(f)     = 12/5.
```

Therefore

```text
J(f) = exp(Ent(f^2)/3)/E(f)
     = (5/12)(8/5)^(1/6)(pi*e)^(-5/6).
```

Direct substitution into the source's printed `1/Q` formula yields

```text
C_print(2,1) = 2^(-5/2) pi^(-11/12).
```

The exact ratio is

```text
J(f)/C_print = (10/3) 5^(-1/6) pi^(1/12) e^(-5/6) > 1.
```

The proof packet gives a rounding-free elementary proof using
`5^(-1/6)>3/4`, `pi^(1/12)>1`, and `e^(-5/6)>2/5`.

## Source correction check

The locally archived arXiv:2410.15566v1 page reproduces the printed exponent
`1/Q`.  Yang's cited arXiv:2301.03332v4, Theorem 1.2, has exponent `2/Q`.
After translating Yang's dimensions `(m,n)` to the source's `(2n,m)`, the
correct constant is

```text
C_tilde(n,m)=4^(2m/Q)/(2n(Q-2) pi^((2n+m)/Q))
             * [Gamma(2n+m)/Gamma((2n+m)/2)]^(2/Q).
```

For `m=1`, the duplication formula reduces it to
`(n!)^(1/(n+1))/(pi*n^2)`.  Thus the explicit failure targets the printed
constant, not the corollary after correction.

## Counterexample 2: Suguro's exact candidate

In the convention

```text
X = partial_x + 2y partial_s,
Y = partial_y - 2x partial_s,
Q = 4,
```

the proposed witness is

```text
g = pi^(-1/2)(1/(6*pi))^(1/4)
    exp(-(x^2+y^2)/2-s^2/12).
```

Its square is normalized and direct integration gives

```text
Ent(g^2) = -(3/2)log(pi)-(1/2)log(6)-3/2,
E(g)     = 4/3,
J(g)     = exp(Ent(g^2)/2)/E(g)
         = (3/4)(6*pi^3*e^3)^(-1/4).
```

The exact ratio to `2/(Q*pi*e)=1/(2*pi*e)` is

```text
(3/2)(pi*e/6)^(1/4) > 1,
```

because `pi>3` and `e>2`.

## Reproduction

Run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_constants.py
```

The script uses only Python's standard library.  It asserts both strict
counterexample inequalities, checks the gamma-form simplification for
dimensions `1,...,20`, and prints all relevant values and ratios.

The evidence crops can be regenerated after rendering the relevant source
pages at 180 dpi into `tmp/source_render/`:

```bash
conda run --no-capture-output -n sandbox python code/make_evidence_crops.py
```

## Novelty and scope audit

The cheap run indexes and a bounded primary-source web search through
2026-08-09 found no erratum, correction, or prior Gaussian counterexample.
This is bounded evidence only.  The full result is the pair of explicit
counterexamples.  The exact value of `alpha_n` remains open, as does Suguro's
separate asymptotic suggestion.

## Human review focus

Recommended checks are the exact source transcription, Yang notation map,
and the logical scope of Suguro's disjunctive proposal.  The analytic
calculations themselves reduce to the displayed Gaussian moments and exact
one-line inequalities.
