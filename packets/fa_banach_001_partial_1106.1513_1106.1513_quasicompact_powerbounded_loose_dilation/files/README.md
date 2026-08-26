# Loose dilations for quasi-compact power-bounded Lp-operators

Status: `candidate_partial_result_likely_valid`

Source: Cédric Arhancet and Christian Le Merdy, *Dilation of Ritt operators
on Lp-spaces*, arXiv:1106.1513, final open problem in Section 5.

## Result

Every quasi-compact power-bounded operator on an `L^p`-space admits a loose
dilation whose dilating operator is an onto isometry. Consequently, the
source's implication from `p`-complete polynomial boundedness to loose
dilatability holds for all quasi-compact operators.

The proof splits off the finite-dimensional peripheral spectral subspace.
Power boundedness makes that part semisimple and similar to a diagonal
isometry. The complementary powers decay exponentially. They are dilated by
placing the input in coordinate zero of `ell^p(Z;L^p)` and summing output
coordinate `k` after applying `T^k`; Hölder's inequality makes the output map
bounded.

## Scope

The general source problem remains open here. For an arbitrary power-bounded
operator, the same construction applied to `rT` has constants that diverge as
`r -> 1`. A Hilbert-style completely bounded extension/factorization route
is unavailable in general `p`-operator spaces.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and complete proof.
- `VERIFICATION.md`: proof, literature, and rendering checks.
