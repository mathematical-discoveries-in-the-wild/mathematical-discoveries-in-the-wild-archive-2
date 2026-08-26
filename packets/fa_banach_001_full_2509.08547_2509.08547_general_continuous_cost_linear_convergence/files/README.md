# Linear Convergence for General Continuous QOT Costs

Result type: `full`

Status: candidate full solution, likely valid pending expert review.

Source paper:

- Alberto González-Sanz, Marcel Nutz, and Andrés Riveros Valdevenito,
  “Linear Convergence of Gradient Descent for Quadratically Regularized
  Optimal Transport,” arXiv:2509.08547v3 (2026).
- Open extension: Remark 2.5, page 7.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The packet proves the extension proposed in Remark 2.5: dual gradient descent
for quadratically regularized optimal transport converges linearly in `L^2`
for every continuous transport cost, under the source paper's original compact
support and connectedness assumptions. In fact, the proof does not require
the source's additional condition that the marginals avoid boundaries of
convex sets.

The result preserves the source step-size range `0 < eta < epsilon` and gives
eventual geometric contraction of the normalized potentials.

## New mechanism

The source attempts to prove convergence of the exact secant operators to a
single linearization and therefore needs all zero-level sections to be
negligible. The packet avoids that limit.

Let `xi_* = f_* + g_* - c`. The optimality equations imply that the strictly
active set

```text
E = {(x,y): xi_*(x,y) > epsilon/2}
```

has uniformly positive sections in both coordinates. The weighted bipartite
energy

```text
integral_E (f(x)+g(y))^2 dP(x)dQ(y)
```

has a spectral gap on the normalized quotient space. The exact secant weights
belong to `[0,1]` and become identically one on `E` after burn-in. Every exact
error operator therefore inherits the same lower spectral bound, while its
upper spectral bound is at most `2`. This yields a uniform strict contraction.

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop containing Theorem 2.3 and
  Remark 2.5.
- `code/verify_weighted_core.py`: finite-dimensional checks of the weighted
  spectral domination argument; these are not part of the proof.
- `VERIFICATION.md`: proof audit and reviewer focus.
- `tmp/`: LaTeX intermediates and visual-QA renders.

## Later-literature comparison and novelty check

A bounded search on 2026-08-09 covered the run's cheap indexes, the exact
source title and arXiv id, and combinations of “quadratically regularized
optimal transport,” “general continuous cost,” “strictly active,” “secant
weights,” “spectral gap,” and “linear convergence.”

The close later result is González-Sanz--Nutz--Riveros Valdevenito,
“Polyak--Łojasiewicz Inequality for Quadratically Regularized Optimal
Transport,” arXiv:2605.27175 (2026). It proves arbitrary uniformly continuous
costs but assumes that one marginal has a density bounded above and away from
zero on a convex or Lipschitz support. The present packet retains the much
weaker compact-support/connectedness framework and uses a different,
non-quantitative active-core spectral gap. No source found in the bounded
search states this stronger extension. Novelty confidence is moderate pending
specialist review.

## Human review focus

Please check:

- the general-cost uniform preconvergence argument inherited from the source;
- the local-a.e.-constancy argument proving that the active-core energy has
  trivial kernel on the normalized space;
- the Fredholm step upgrading trivial kernel to a positive spectral gap;
- the exact secant representation and the domination `w_n >= 1_E` after
  burn-in;
- the comparison with the stronger marginal assumptions in arXiv:2605.27175.

