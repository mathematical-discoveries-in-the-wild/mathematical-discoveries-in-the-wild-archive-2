# Contractive centered Lp decay forces Poincaré without symmetry

Status: `candidate_full_likely_valid`

Source: Patrick Cattiaux, Arnaud Guillin, and Cyril Roberto, *Poincaré
inequality and the Lp convergence of semi-groups*, arXiv:1003.0784,
Section 4, PDF page 12.

## Result

The source leaves open the converse in its nonsymmetric extension: if, for
some `p>2`, centered `L^p` convergence holds with the crucial prefactor
`K_p=1`, must the Poincaré inequality follow? The authors obtain exponential
`L^2` decay with an unspecified prefactor but cannot force `K_2=1`.

This packet proves the converse. For an invariant Markov diffusion semigroup,
not assumed symmetric, if

`N_p(P_t f) <= exp(-lambda*t) N_p(f)`

for one `p>2`, then

`Var_mu(g) <= (p-1)/lambda * integral Gamma(g,g) dmu`.

Consequently centered `L^2` convergence holds with prefactor one and rate at
least `lambda/(p-1)`.

The key is to shift before taking the fractional power. For each smooth `g`,
choose `c_epsilon` so that a smooth approximation to
`sign(g-c)|g-c|^(2/p)` has mean zero. Its `p`-th power tends to
`|g-c|^2`, while the weighted carré-du-champ multiplier is bounded by one.
This repairs both obstacles explicitly identified by the source: lack of
`C^2` regularity and failure of the naive fractional power to preserve mean
zero.

## Evidence and verification

- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop of source PDF page 12.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `code/check_fractional_regularizer.py`: 1,159,968 scalar regression checks
  of the regularizer inequalities.
- `VERIFICATION.md`: proof audit and command/results log.

Cheap run indexes and bounded web/arXiv searches on 2026-08-17 used the exact
source sentence and the phrases `K_p=1 Poincare nonsymmetric semigroup`,
`centered Lp exponential convergence Poincare`, and the source's weighted
carré-du-champ formula. They found the 2010 arXiv/published versions and later
related centered Sobolev work, but no resolution of this exact converse.
Novelty confidence is moderate-high pending expert review.

Human review should focus on the passage from semigroup decay to the
infinitesimal weighted inequality and on the standard core/closure step after
the smooth regularization.
