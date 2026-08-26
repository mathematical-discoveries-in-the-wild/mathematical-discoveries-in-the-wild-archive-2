# Counterexample: a singularizing channel with divergent Cesaro averages

status: candidate_counterexample_likely_valid

source: Sviatoslav V. Dzhenzher, *Singularizing preserving countable
additivity quantum channels on quantum measurable cardinals*,
arXiv:2605.24923 (2026).

target: the conclusion asks whether the strong Cesaro-convergence results for
normal-state channels have analogues for singularizing random-unitary
channels, and points to quasi-compactness as a possible route.

packet: `runs/fa_banach_001/solutions/counterexamples/2605.24923_singularizing_channel_non_mean_ergodic/`

ledger: `runs/fa_banach_001/ledger/results/2605.24923_singularizing_channel_non_mean_ergodic.json`

## Result

The universal analogue is false. Whenever a cardinal `kappa` carries an
atomless countably additive probability measure on all its subsets (the source
paper's measurable-cardinal setting), there is a countable-additivity
preserving, singularizing random-unitary channel `Q` such that

`||(1/N) sum_{n=1}^N Q^n rho_0 - (1/(2N)) sum_{n=1}^{2N} Q^n rho_0|| >= 1`

for every `N`. Thus the Cesaro averages fail to converge in strong operator
topology. The same channel is not quasi-compact.

## Construction

On `H = ell_2(kappa) tensor ell_2(Z)`, let `S_j` be translation in the first
factor and `U` the bilateral shift in the second. Average conjugation by
`S_j tensor U` against the atomless countably additive measure.

The first-coordinate averaging makes every output state singular. Meanwhile,
the `n`-th iterate places the second coordinate exactly at `e_n`. These orbit
states live on mutually orthogonal projections. A diagonal observable equal
to `+1` on coordinates `1,...,N` and `-1` on `N+1,...,2N` separates the two
Cesaro means by exactly `1`.

## Verification

- The singularizing argument was checked separately for normal and singular
  input states using the Yosida--Hewitt decomposition.
- Every relevant vector matrix coefficient is supported on a countable set of
  translations, hence has measure zero.
- `code/check_cesaro_gap.py` verifies the exact finite-coordinate weight
  calculation for `N=1,...,100`; this is a sanity check, not the proof.
- A bounded web/arXiv and run-index search on 2026-08-09 found the source paper
  but no prior counterexample to its singularizing Cesaro direction.
- Human review should focus on the convention that SOT for channels means
  pointwise norm convergence on the ambient dual Banach space and on the
  standard quasi-compact-orbit implication.

## Scope

This disproves a universal singularizing mean-ergodic analogue and supplies an
explicit non-quasi-compact singularizing channel. It does not rule out Cesaro
convergence or quasi-compactness under additional tightness, compactness, or
mixing hypotheses.
