# Macaev liftability is equivalent to logarithmic local linearization

Status: `partial_result_likely_valid`

Source problem: F. Cabello Sanchez and R. Garcia, *The Twisted Hilbert
Space Ideals*, arXiv:2112.03852, page 5:

> Is every operator in the Macaev ideal liftable?

## Result

For `m >= 1`, let `Lambda(m)` be the worst distance from a normalized
quasilinear map `Phi: ell_2^m -> ell_2` to the linear maps:

`Lambda(m) = sup_(Q(Phi)<=1) inf_L ||Phi-L||`.

Then the source question has a positive answer if and only if

`Lambda(m) = O(log(m+1))`.

The forward direction is constructive. The logarithmic estimate gives
`O(log m)` liftings of rank-`m` projections. Abel summation of the spectral
resolution of a positive compact operator then converges exactly under the
Macaev condition `sum_m s_m/m < infinity`.

The converse is a counterexample assembly. If `Lambda(m)/log(m+1)` is
unbounded, choose normalized finite-dimensional quasilinear blocks whose
linearization distances grow faster than `k^4 log(m_k+1)`. Their Hilbertian
direct sum defines a twisted Hilbert extension. On the quotient take the
block-scalar compact operator

`D = direct_sum_k [1/(k^2 log(m_k+1))] I_(m_k)`.

The operator belongs to the Macaev ideal, but the block lifting obstruction is
at least `k^2`, so it is not liftable.

Thus failure of the logarithmic local estimate does not merely obstruct the
standard proof route: it forces a negative answer to the original problem.

## Finite-range upgrade

Kalton's logarithmic linearization theorem gives the sharp two-parameter
estimate

`Lambda_cont(m,r) <= C(1 + log(m+r))`

for continuous quasilinear maps `ell_2^m -> ell_2^r`. This follows by padding
the smaller Hilbert space to dimension `max(m,r)` and applying his Theorem 2.2.
Combining it with the Abel argument proves Macaev liftability through every
continuous twist whose restrictions to the nested singular subspaces have
polynomial finite-range profile:

`dim span Phi(E_m) <= (m+1)^a` for some fixed `a`.

The estimate is logarithmically sharp when the two dimensions are comparable.

## Scope

This is an exact finite-dimensional reformulation, not a decision of the
remaining target-dimension-free logarithmic estimate. Kalton's theorem controls
`log(m+r)`, while the universal problem needs `log(m)` for unrestricted,
possibly infinite-dimensional, Hilbert target. A Maurey-projection dualization
does not eliminate this gap without assuming the splitting estimate one is
trying to prove. The cited Schatten-class proof does not settle
that estimate: its essential splitting constant is obtained by an ultraproduct
contradiction and has no quantitative dependence on the exponent.

## Files

- `main.tex`: complete equivalence theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:2112.03852.
- `supporting_paper_kalton_2002.pdf`: logarithmic equal-dimensional
  linearization theorem used for the finite-range upgrade.
- `figures/open_problem_crop.png`: source question on page 5.
- `VERIFICATION.md`: proof audit and scope check.

Human review should focus on the completed dense block-sum twisted extension
in the counterexample direction and on the Macaev block calculation.
