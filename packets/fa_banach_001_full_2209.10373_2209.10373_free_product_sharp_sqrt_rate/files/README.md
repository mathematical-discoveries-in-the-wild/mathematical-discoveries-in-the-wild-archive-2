# Candidate full result: the sharp rate for `(1-x)(1-y)` is `n^{-1/2}`

Status: `candidate_full_solution_likely_valid`

Source: Palak Arora, Meric Augat, Michael T. Jury, and Meredith Sargent,
*An Optimal Approximation Problem for Free Polynomials*, arXiv:2209.10373,
Section 3.1, PDF page 14.

## Result

For the free polynomial

```text
f(x,y) = (1-x)(1-y),
```

let

```text
c_n = min_{deg p <= n} ||p(x,y)f(x,y)-1||_2^2.
```

The packet proves an exact scalar recursion for `c_n` and the asymptotic

```text
sqrt(n) c_n -> 1.
```

In particular, the exponent `p=1/2` asked about in the source is sharp.  The
result also identifies the leading constant.

## Proof idea

Right multiplication by `(1-x)(1-y)` is a four-term operator on the binary
word tree.  Hilbert-space duality converts the least-squares error into the
reciprocal of a minimum-energy problem subject to the local constraint

```text
h_w - h_wx - h_wy + h_wxy = 0.
```

The constrained energy can be eliminated recursively down the tree.  Two
scalar state variables `e_n` and `kappa_n` suffice, and the exact answer is
`c_n=1/e_n`.  A moving-fixed-point argument then shows
`e_n ~ sqrt(n)` with leading constant one.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2209.10373.
- `figures/open_problem_crop.png`: source-page crop containing the question.
- `code/verify_recurrence.py`: exact-arithmetic comparison with the primal
  Gram-matrix least-squares problem, plus a long-run asymptotic check.
- `verification.md`: proof and computation audit.

## Scope and novelty

This fully answers the source paper's explicit sharpness question for the
single example `(1-x)(1-y)`.  It does not settle the source's broader question
about a decay exponent uniform over all free polynomials.

A bounded run-index, exact-phrase, arXiv/web, author, journal, and citation
search on 9 August 2026 found the source paper and later classical/commutative
OPA work citing it, but no later solution of this free example.  Novelty is
therefore plausible but remains subject to specialist review.

## Human review focus

Check the orientation of the right-multiplication adjoint, the two-state tree
decomposition defining `E_m` and `F_m`, and the scalar trapping argument used
to pass from the exact recurrence to the leading constant.  The included
exact-arithmetic verifier independently matches the recurrence to the primal
least-squares errors for the first several degrees.
