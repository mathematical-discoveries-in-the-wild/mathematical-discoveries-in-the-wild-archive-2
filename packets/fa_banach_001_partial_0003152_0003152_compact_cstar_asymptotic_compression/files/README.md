# Asymptotically exact cutdowns for compact C*-algebras

Status: `candidate_partial_result_likely_valid`

Source: Hermann Pfitzner, *Perturbation of l1-copies and measure convergence
in preduals of von Neumann algebras*, arXiv:math/0003152, second question in
Section 6.

## Result

For every compact (dual/annihilator) C*-algebra
`A = direct-sum^{c0} K(H_i)`, the second source question has an affirmative
answer. A bounded sequence in `A*` spanning `ell_1` almost isometrically has
a subsequence `(phi_mn)` and pairwise orthogonal finite-rank projections
`a_n,b_n in A` such that

`||phi_mn - b_n phi_mn a_n|| -> 0`.

The proof applies the source's orthogonal-functional theorem to the predual
`A*` of `A**`, then uses finite singular-value truncations of the resulting
orthogonal trace-class families. Their left and right finite-rank supports
belong to `A` and inherit pairwise orthogonality.

## Scope

The general C*-algebra question remains open here, as does the source's first
question about avoiding subsequences. For arbitrary `A`, the orthogonal
supports live in `A**`; producing asymptotically exact pairwise orthogonal
inner cutdowns in `A` is the unresolved separation step.

The 2016 Peralta--Pfitzner extension (arXiv:1405.5414) still gives a
subsequence and a fixed-accuracy non-normal conclusion. A bounded exact-
phrase and citation search located no statement of the scoped theorem above.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and proof.
- `VERIFICATION.md`: mathematical, literature, and rendering checks.
