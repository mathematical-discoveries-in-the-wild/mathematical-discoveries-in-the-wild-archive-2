# Counterexample packet: integrable spreading does not imply log-integral entropy

## Source and target

- Thomas Allard and Helmut Bölcskei, *Entropy and Minimax Risk of
  Hypoelliptic Pseudodifferential Operators*, arXiv:2603.23744 (2026).
- Printed future direction: page 6, immediately before Corollary 2.  It asks
  for a rigorous underspread-operator analogue of Theorem 1 and anticipates
  entropy formulae of the same phase-space log-integral form.
- The official TeX source's commented development (lines 1078--1098) proposes
  finite spreading-function `L1` norm as the relevant class and an inversion
  route through eigenvalue asymptotics.

## Classification

- Status: `candidate_counterexample_likely_valid`.
- Result: full counterexample to the natural **integrable-spreading**
  formulation, even with arbitrarily small spreading norm.
- Scope boundary: not a counterexample to every stricter definition requiring
  compact spreading support of prescribed area, and not a contradiction of
  the source paper's proved hypoelliptic theorem.

## Result

For every dimension `d >= 1` and every `delta > 0`, there is a positive
self-adjoint rank-one Weyl operator `T` with strictly positive Schwartz Weyl
symbol `a` and Schwartz spreading function `eta` satisfying
`||eta||_1 < delta`, but

`H_T(epsilon) / integral log_+(a(z)/epsilon) dz -> 0`.

Explicitly, for the normalized Gaussian
`g(t) = 2^(d/4) exp(-pi |t|^2)` and `T_c = c |g><g|`,

- `a_c(z) = c 2^d exp(-2 pi |z|^2)`;
- `eta_c(zeta) = c exp(-pi |zeta|^2/2)` and `||eta_c||_1 = c 2^d`;
- `H_Tc(epsilon) = log ceil(c/epsilon)` on the real Hilbert space;
- the proposed phase-space integral equals
  `log(c 2^d/epsilon)^(d+1) / (2^d d! (d+1))`.

The two sides differ by a full power of `log(1/epsilon)`.

## Proof idea

The obstruction is spectral rank.  Integrable (indeed Gaussian) spreading
does not force the Weyl symbol's phase-space distribution to count spectral
degrees of freedom.  The rank-one projector has only one entropy axis, while
its positive Gaussian symbol occupies a ball whose radius grows like
`sqrt(log(1/epsilon))`; integrating the logarithmic height over that ball
produces power `d+1` instead of power `1`.

There is a second structural warning: an `L1` spreading representation is a
norm-convergent integral of unitary time-frequency shifts, so the represented
operator is bounded.  It cannot itself have eigenvalues tending to infinity,
as contemplated in the commented inversion route.

## Verification and upgrade attempts

- `code/verify_gaussian_obstruction.py` numerically re-integrates 45 radial
  cases, checks arbitrary spreading-norm smallness, and checks entropy-ratio
  decay.  The proof itself is exact and symbolic.
- Six focused routes were audited in the attempt log: precise formulation,
  Weyl normalization, arbitrary norm smallness, exact entropy comparison,
  boundedness of the proposed inversion class, and a strict compact-support
  upgrade.
- The compact-support upgrade was not claimed: the Gaussian spreading
  function is not compactly supported, and the tractable rank-one positive
  realization does not survive that replacement.

## Novelty status

Bounded searches on 2026-08-11 used the exact future-work phrase, target title
and authors, and combinations of `metric entropy`, `underspread`, `log
integral`, `rank one`, and `Wigner`.  They found approximate-diagonalization
and scaled Szegő-asymptotic literature, but no exact Gaussian rank-one entropy
counterexample or later answer to this 2026 direction.  Novelty confidence is
bounded rather than exhaustive.

## Human review

Prioritize (1) acceptance of finite `L1` spreading as the precise formulation
being refuted, (2) the Weyl/spreading normalization, and (3) the explicit scope
exclusion for compact-support or scaled-family versions.  The entropy and
radial integral calculations are elementary and exact.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: compiled and visually inspected packet.
- `source_paper.pdf`: locally compiled original arXiv source.
- `figures/future_direction_crop.png`: source-page evidence.
- `code/verify_gaussian_obstruction.py`: numerical sanity checker.
- `verification_report.md`: build, code, hash, and visual-QA record.

