# Parameter monotonicity and threshold for Nguyen's entire function

Status: `candidate_full_likely_valid`.

For

```text
F_a(z) = sum_{k>=0} z^k / product_{j=1}^k (a^j+1),  a>1,
```

the open conjecture in arXiv:1912.10035 has a positive answer:

```text
F_{a1} in LP and a2>a1  =>  F_{a2} in LP.
```

The proof normalizes the sign-detecting interval with
`H_a(y)=F_a(-(a+1)y)`.  For every parameter that can belong to the
Laguerre--Polya class and every relevant `y`, the terms of `dH_a/d a` can be
paired to prove strict negativity.  A negative sign witness therefore stays
admissible and becomes strictly more negative as `a` increases.

Combining this with Theorem 1 of the source paper proves that there is a
single membership threshold `a0`.  Exact rational section certificates give

```text
3.9642 < a0 < 3.9643.
```

This also disproves the paper's printed sufficient bound `a >= 3.91719`.
The denominator-clearing step in its Lemma 5 contains `a^5+1` where the
correct factor is `a^6+1`.

Run the exact bracket certificate with:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1912.10035_parameter_monotonicity_threshold/code/exact_certificate.py
```

The certificate uses only exact Python `Fraction` arithmetic.  The main
monotonicity proof is analytic.  The human-facing packet is
`solution_packet.pdf`.
