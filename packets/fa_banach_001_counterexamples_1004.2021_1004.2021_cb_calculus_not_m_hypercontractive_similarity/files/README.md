# Completely bounded calculus without m-hypercontractive similarity

Source: G. Popescu, *Joint similarity to operators in noncommutative
varieties*, arXiv:1004.2021v2; Proc. London Math. Soc. 103 (2011),
331--370.

Status: candidate full counterexample, likely valid.

## Result

For every integer `m>=2`, take the one-variable radial domain associated
with `f=X` and no polynomial constraints.  Its universal model `W_m` is
multiplication by `z` on the weighted Bergman space with kernel
`(1-z wbar)^(-m)`.  The homomorphism

```text
p(W_m) -> p(S)
```

where `S` is the unilateral shift, is a complete isometry.  Nevertheless,
`S` is not similar to any operator in the order-`m` domain.  Indeed, such a
similarity would produce a bounded positive invertible `R` with

```text
R - 2 S R S* + S^2 R S*^2 >= 0.
```

The diagonal entries force `<R e_k,e_k>` to grow at least linearly, a
contradiction.  Also `S^k S*^k -> 0` strongly, so the source's accompanying
purity condition is met.

This gives a negative answer to the source's open converse for every
`m>=2`, with complete isometry in place of mere complete boundedness.

## Files

- `main.tex`: exact counterexample and full proof.
- `solution_packet.pdf`: rendered review packet.
- `code/verify_shift_obstruction.py`: exact coefficient, defect, recurrence,
  and purity checks.
- `verification.md`: proof, literature, build, checksum, and visual-QA
  record.

