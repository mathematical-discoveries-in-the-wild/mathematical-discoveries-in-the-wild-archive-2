# Concavity of the three-variable Rademacher moment for 2 < p < 3

Status: `partial_new_result_likely_valid` (three-variable case of the
Schechtman Rademacher p-concavity problem)

## Source problem

Haonan Zhang, *Some convexity and monotonicity results of trace functionals*,
arXiv:2108.05785, Section 4, points to Schechtman's open problem on whether the
Rademacher sequence in real `L_p` has p-concavity constant one. Jenkins and
Tkocz, arXiv:2207.09122, Section 3.2, confirm that the remaining range is
`2 < p < 3` and record the equivalent concavity of

```text
Phi_n(x) = E |sum x_k^(1/p) epsilon_k|^p.
```

## New partial theorem

For every `2 < p < 3`, `Phi_3` is concave on the positive orthant. By
Schechtman's equivalence, the constant-one Hanner-type inequality holds for
every three real `L_p` functions.

The Hessian is minus a weighted triangle Laplacian. Once the root
coefficients are ordered, at most one edge has negative weight. Positivity is
therefore equivalent to bounding that edge by the effective conductance of
the other two. In the triangle regime the sharp bound follows from the fact
that

```text
g(a,h) = a ((a+h)^q - a^q),  0 < q < 1,
```

is increasing in both variables.

## Scope and verification

The unrestricted number of variables remains open. Eight focused upgrade
attempts are documented in the packet. The symbolic proof is independent of
computation. `code/check_hessian.py` checks the closed formulas and searches
200,000 reproducible samples; it finds no contradiction beyond floating-point
roundoff.

Files include the source paper, the decisive Jenkins--Tkocz status/source
paper, the exact source crop, the LaTeX proof, verification code, and the
compiled review packet.

Ledger:
`runs/fa_banach_001/ledger/results/2108.05785_three_rademacher_concavity.json`.
