# Optimal tensor-power length in arXiv:1711.05624

Status: `candidate_full_solution_likely_valid`

This packet answers the first question in Remark 2.3 of Briët–Gopi,
arXiv:1711.05624v3: the scale `m = C_r n^(1-1/r)` in their hypergraph matrix
lemma is optimal up to constants.

## Result

Even for a hypergraph consisting of one `2r`-edge, any representation

`p_H(x) = n/(c_r n^m) <A x^{tensor m}, x^{tensor m}>`

with `||A||=O_r(1)` requires `m=Omega_r(n^(1-1/r))`.  The source proves the
matching upper bound.

The packet also gives a deeper upgrade for the more general common nonlinear
lift in the second sentence of Remark 2.3: representing all single `2r`-edge
characters simultaneously requires dimension `N=Omega_r(n^(2r-2))`.  This
does not settle whether `N=o(n^m)` is possible.

## Mechanism

- Fourier extraction identifies an edge coefficient with a parity-transition
  matrix pairing.
- The transition matrix's normalized trace norm is a Hellinger affinity.
- Marginalization to the edge and binomial factorial moments bound the affinity
  by `O_r((m/n)^r)`.
- The source normalization requires an edge coefficient of order `N/n`.
- For arbitrary common lifts, matrix-valued Parseval gives the polynomial
  dimension floor.

## Files

- `solution_packet.pdf`: proof and review packet.
- `source_paper.pdf`: arXiv:1711.05624v3.
- `figures/open_problem_crop.png`: Lemma 2.2 and Remark 2.3 on PDF page 7.
- `code/verify_parity_affinity.py`: small-instance spot checker.
- `verification_report.md`: proof, novelty, code, and render QA.

## Scope

The full claim concerns asymptotic optimality of the tensor-power parameter
`m`, not its leading constant.  The broader arbitrary-embedding question,
Theorem 1.1 improvement, LDC implications, and arithmetic-progression
conjectures remain open.

