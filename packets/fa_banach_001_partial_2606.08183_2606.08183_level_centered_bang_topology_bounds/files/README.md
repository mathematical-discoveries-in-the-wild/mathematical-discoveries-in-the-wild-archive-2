# Level-centered Bang degrees and sublevel-set topology

**Status:** substantial partial result and sharp obstruction, likely valid;
pending human review.

**Source:** Armin Rainer, *Effective quasianalytic Remez inequalities on tame
sets*, arXiv:2606.08183 (2026), prompt after Corollary 1.18 on PDF page 9.

## Result

The global Bang degree appearing in the paper's Remez inequality cannot bound
the affine-section component constants of a sublevel set, even with fixed
dimension, fixed convex domain, fixed analytic weight, and a fixed derivative
majorant.  On `K=[0,2pi]x[0,1]`,

```text
f_N(x,y)=1+exp(-N) sin(Nx)
```

is `(mu,2)`-smooth for the fixed analytic weight `mu_j=j`, and its global Bang
degree is uniformly bounded, while `{|f_N|<=1}` and every horizontal line
section have `N+1` connected components.

The correct one-dimensional repair is level-centered.  For a quasianalytic
function `g` on an interval, the number of components of `{|g|<=t}` is at most
the sum of the source's associated Bang degrees for `g-t` and `g+t`, plus one.
For a convex planar domain this gives an explicit uniform `B_1(K_t)` whenever
the nonzero line restrictions of `f-t` and `f+t` have a uniform positive norm.

## Scope and files

The packet does not define or solve a general effective topology theory for
arbitrary Denjoy--Carleman presentations.  The source itself leaves
“Denjoy--Carleman complexity” undefined, and higher-dimensional component
bounds need multivariate critical-system or effective-stratification data not
contained in a scalar Bang degree.

- `main.tex` and `solution_packet.pdf`: obstruction, positive theorem, and
  planar corollary.
- `source_paper.pdf`: local compilation of the cached arXiv source.
- `figures/open_problem_crop.png`: metric-entropy prompt on source PDF page 9.
- `runs/fa_banach_001/attempts/2606.08183_sublevel_topology_bang_degree_attempts.md`:
  five focused routes and the higher-dimensional obstruction.

The proof has no computational dependency.  Recommended human-review focus:
the uniform derivative estimate for the oscillatory family, the `N+1`
component count including the endpoint component, and the convention for line
restrictions identically equal to a boundary level.

