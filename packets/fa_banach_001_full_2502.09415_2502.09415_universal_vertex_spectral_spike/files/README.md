# Universal vertices explain the spectral spike in arXiv:2502.09415

Status: `candidate_full_solution_likely_valid` to the source's qualitative
simulation conjecture, with an explicit scope caveat about total bin mass.

## Result

Let `D_N=d floor(N/2)` be the diameter of the discrete torus and let
`H_N={i: W_i >= D_N^alpha}`.  Every vertex in `H_N` is universal.  Therefore
the unscaled adjacency matrix has eigenvalue `-1` on the zero-sum coordinate
subspace supported by `H_N`; after the paper's scaling, the exact eigenvalue
is `-1/sqrt(c_N)` with multiplicity at least `(|H_N|-1)_+`.

Moreover,

`|H_N| ~ Bin(N^d, D_N^(-alpha(tau-1)))`.

When `alpha(tau-1)<d`, this gives a sharply counted finite-size atom of mass
asymptotic to `D_N^(-alpha(tau-1))`.  At `alpha=0`, the graph is complete and
the atom has multiplicity `N^d-1`.  A positive-profile Gaussianized matrix has
simple spectrum almost surely, so it has no analogous forced atom.

For the source's `N=5000, d=1, alpha=0.1, tau=4` plot, the theorem predicts
about 477 forced eigenvalues (9.54% of the ESD) at `-0.019844...`, exactly in
the central bin.

## Files

- `solution_packet.pdf`: self-contained theorem and proof packet.
- `source_paper.pdf`: arXiv:2502.09415v2.
- `figures/open_problem_crop.png`: exact conjecture on source PDF page 9.
- `figures/source_simulation.png`: source Figure 1 right panel.
- `code/verify_spike.py`: seeded algebraic and numerical checks.
- `VERIFICATION.md`: proof, novelty, computation, and render QA.

## Scope

The theorem isolates and sharply counts the exact universal-vertex
eigenspace.  It proves that high-connectivity saturation necessarily creates
the observed kind of spike.  It does not claim that every eigenvalue in a
finite-width histogram bin is contributed by universal vertices; that would
require a local spectral law.  The forced mass vanishes for every fixed
`alpha>0`, consistently with the paper's absolutely continuous limiting ESD.
