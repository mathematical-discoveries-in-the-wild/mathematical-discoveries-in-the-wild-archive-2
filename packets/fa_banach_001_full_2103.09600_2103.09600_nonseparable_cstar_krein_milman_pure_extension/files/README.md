# Full candidate: nonseparable C*-Krein--Milman theorem

status: `candidate_full_solution_likely_valid`

source: B. V. Rajarama Bhat and M. Kumar, *C*-extreme maps and nests*,
arXiv:2103.09600; J. Funct. Anal. 282 (2022), Paper 109397.

packet: `runs/fa_banach_001/solutions/full/2103.09600_nonseparable_cstar_krein_milman_pure_extension/`

ledger: `runs/fa_banach_001/ledger/results/2103.09600_nonseparable_cstar_krein_milman_pure_extension.json`

## Result

For every unital C*-algebra `A` and every separable Hilbert space `H`, the generalized
state space `UCP(A,B(H))` is the BW-closure of the C*-convex hull of its C*-extreme
points. This removes the source's separability/type-I restriction and answers its
full-generality question affirmatively.

## Mechanism

A finite BW test set lies in a separable subalgebra `B`. The source theorem applies on
`B`. Its proof uses special C*-extreme building blocks obtained from a pure UCP map
and a pure one-dimensional compression. Arveson's pure-extension argument lifts the
pure map to `A`; the same compression remains pure, so the source's direct-sum/nest
criterion makes the lifted block C*-extreme. Keeping the original operator
coefficients gives an approximation on `A` with the same restriction to `B`.

## Files

- `solution_packet.pdf`: theorem, proof, verification, and novelty notes.
- `source_paper.pdf`: arXiv:2103.09600.
- `figures/open_problem_crop.png`: source page 19 containing the open question.
- `verification.md`: logical and artifact checks.
