# Candidate Partial Result: Quantitative Norm Converse for Co-commutative Quantum Groups

Status: `partial_result_likely_valid`

Model: GPT5.6

Source: Adam Skalski and Ami Viselter, *Convolution semigroups on locally
compact quantum groups and noncommutative Dirichlet forms*, arXiv:1709.04873,
Question 2.20 on PDF page 31.

## Claimed contribution

Let `H` be any locally compact group and let `G=H-hat` be its co-commutative
locally compact quantum group. For every state `mu` on `C^*(H)`, with counit
`epsilon`,

`||mu-epsilon|| <= 2 sqrt(||R_mu-id||_{B(VN(H))}).`

Hence operator-norm convergence `R_{mu_i}->id` forces
`mu_i->epsilon` in norm. This proves the source question for all
co-commutative quantum groups, not only the co-amenable ones. In particular,
it adds genuinely non-co-amenable examples by taking `H` nonamenable.

This is a partial result only. It does not settle Question 2.20 for arbitrary
locally compact quantum groups.

## Proof mechanism

The multiplier identity `R_mu(lambda_s)=mu(u_s)lambda_s` turns the operator
norm error `delta` into a uniform bound `|mu(u_s)-1|<=delta`. In the GNS
representation of `mu`, take the minimum-norm point of the closed convex hull
of the orbit of the cyclic vector. It is invariant and equals the orthogonal
projection onto invariant vectors. The uniform coefficient bound gives
`||Pxi||^2>=1-delta`. Normalizing `Pxi` produces a vector that realizes the
counit in the same representation, and the exact distance formula for vector
states yields the square-root estimate.

## Verification

- The argument applies to arbitrary locally compact `H`; it uses no invariant
  mean and no amenability assumption.
- The minimum-norm orbit-hull vector is invariant by uniqueness, and equals
  `Pxi` because it has the same inner products with all invariant vectors as
  `xi`.
- For errors at least `1`, the asserted estimate is the trivial fact that two
  states have distance at most `2`; the substantive argument handles errors
  below `1`.
- No computational evidence and no unproved lemma are used.

Verifier verdict: likely valid. The main review points are the right
convolution formula on the canonical group unitaries and the final vector-state
norm calculation; both are written out in `main.tex`.

## Novelty and search bounds

On 2026-08-11, the run's lightweight indexes were searched for the exact
arXiv id, the exact question, and combinations of `right convolution`,
`counit`, `operator norm`, `co-amenable`, and `co-commutative`. The locally
parsed arXiv corpus was searched for later citations to arXiv:1709.04873.
Bounded official-arXiv searches used the exact id, title, and question terms.
No later paper explicitly answering Question 2.20, and no statement of this
quantitative co-commutative subcase, was found. Novelty confidence is moderate
rather than high because the argument is elementary once one specializes to
group duals.

## Files

- `main.tex`: complete candidate partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: real crop of Question 2.20 from source PDF
  page 31.
- `../../../attempts/1709.04873_convolution_norm_converse_attack.md`: full and
  partial attack log.

Human review recommendation: verify the two identifications above and, if
accepted, retain this as a substantial partial answer covering the complete
co-commutative class. Do not describe it as resolving the general locally
compact quantum-group question.

