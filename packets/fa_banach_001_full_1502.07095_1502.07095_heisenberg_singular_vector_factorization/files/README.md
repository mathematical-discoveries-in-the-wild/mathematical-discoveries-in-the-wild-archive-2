# Heisenberg singular-vector factorization

Status: `candidate_full_likely_valid`.

This packet proves conjecture (3.140) of Křižka--Somberg,
arXiv:1502.07095.  If

```text
lambda_1 + lambda_2 + n = a - 1,
```

then the scalar singular vector factors exactly as

```text
product_{j=0}^{a-1} (sum_i f_i g_i + (j-lambda_2)c) v_lambda.
```

The proof converts the source's Fourier-side polynomial
`T^lambda_{a,a}(q^a)` back through symmetrization.  An exact exponential
normal-ordering identity reduces the conjecture to a one-line binomial
coefficient extraction.

The human-facing artifact is `solution_packet.pdf`.  The folder also contains
the source paper, the exact source-question crop, and an exact symbolic verifier.
