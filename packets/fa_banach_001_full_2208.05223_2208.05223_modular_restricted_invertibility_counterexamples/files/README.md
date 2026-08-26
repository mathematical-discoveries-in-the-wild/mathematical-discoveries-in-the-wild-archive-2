# Modular restricted-invertibility counterexamples

Source: arXiv:2208.05223, K. Mahesh Krishna.

## Main result

Conjectures 1.2 and 1.3 are false. Over the single fixed separable
commutative C*-algebra of convergent sequences, construct in every
dimension a matrix-valued sequence with these properties:

- every column has module norm one;
- the determinant is identically zero, as explicitly allowed;
- the module operator norm is exactly `sqrt(2)`;
- every pair of columns coincides at one designated coordinate.

Thus no subset of two or more columns has any positive uniform lower
bound, while the conjecture demands a subset of size at least `c d / 2`.
Because the entries commute, the same matrices are Manin matrices and also
refute the noncommutative conjecture. The construction works over
`ell_infinity` as well, so it persists for a commutative W*-algebra.

## Secondary printed-statement observation

Conjecture 2.6 repeats `1-epsilon` in its upper bound. Literally, it demands
an exact scaled isometry. A dimension argument using
`0,e_j,i e_j` disproves that printed statement over the scalar algebra.
This does not address the evidently intended `1+epsilon` upper bound.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: compiled packet
- `verification_report.md`: proof and artifact audit
- `source_paper.pdf`: official arXiv PDF
- `figures/restricted_invertibility_conjectures.png`: exact Conjectures 1.2/1.3
- `figures/printed_jl_conjecture.png`: exact printed Conjecture 2.6

Status: candidate full negative answers, likely valid; human review recommended.
