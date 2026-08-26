# Linear dependence on the number of simultaneous Riesz selectors

Status: `candidate_full_solution_likely_valid_needs_human_review`

Source problem: the unnumbered Problem after Corollary 4.8 in Marcin Bownik,
*Selector form of Weaver's conjecture, Feichtinger's conjecture, and frame
sparsification*, arXiv:2405.18235.

## Result

For (m) unit-norm Bessel sequences with common Bessel bound (B>1), and
(0<\varepsilon<1), selector blocks of size

\[
\left\lceil\frac{16mB^2}{\varepsilon^2}\right\rceil
\]

suffice to obtain one selector that has Riesz bounds
(1-\varepsilon,1+\varepsilon) in all (m) Hilbert spaces. This follows by
one application of the source paper's simultaneous Bessel-selector theorem to
the normalized families together with all their Naimark complements.

The linear dependence on (m) is sharp. For every fixed
(B>1+\varepsilon), two blocks of any size (r\le m) admit (m) unit-norm
Bessel families of bound at most (B) for which no selector works. Cyclically
shifted orthonormal bases give the construction. In particular, for (B=2)
and fixed (0<\varepsilon<1), the optimal block size is
(\Theta(m)).

Therefore the source's (O(m^2B/\varepsilon^2)) bound is not asymptotically
optimal as (m\to\infty); the correct exponent of (m) is one in the
fixed-parameter regime.

## Files

- `main.tex` / `solution_packet.pdf`: self-contained proof and lower-bound
  construction.
- `source_paper.pdf`: the source arXiv PDF.
- `figures/source_problem_crop.png`: source page 26 with Corollary 4.8 and the
  open problem.
- `VERIFICATION.md`: proof-obligation, novelty, and scope audit.
- `code/check_linear_selector.py`: exact scalar-inequality and cyclic-coverage
  checks.

## Reproduction

Run the exact checks:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2405.18235_linear_m_riesz_selector/code/check_linear_selector.py
```

Compile from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The final PDF was rendered to RGB PNG images and every page was visually
inspected.

