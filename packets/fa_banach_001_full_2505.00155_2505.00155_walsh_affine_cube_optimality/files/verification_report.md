# Verification Report

Candidate: arXiv:2505.00155, deterministic Walsh affine-cube lower bound for endpoint Orlicz subsystem selection.

## Claim checked

For every fixed `alpha > 0` and all sufficiently large `N = 2^d`, the full character system of `F_2^d` has the property that every subset of at least

`N / (e (log N)^(alpha+1))`

characters has `L^2 log^alpha L` synthesis norm at least

`c(alpha) (log log N)^(alpha/2)`.

Combined with Burstein's upper theorem, this resolves the stated optimality question up to constants depending on `alpha`.

## Verdict

`full_solution_likely_valid; expert review requested`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Bounded orthogonal system | valid | The `N` functions `chi_xi(x)=(-1)^(xi dot x)` on uniform `F_2^d` are orthonormal and have `L-infinity` norm one. |
| Cube-count recursion | valid | Splitting an `(s+1)`-cube into opposite faces gives `C_(s+1)=E_h (E_x g_h)^2 >= C_s^2`; hence `C_r >= delta^(2^r)`. |
| Degenerate-direction bound | valid | A first linear dependence at position `j` gives at most `2^(j-1) N^(r-1)` direction tuples. Summation gives fewer than `(2^r-1)N^(r-1)`. |
| Existence of a genuine flat | valid | Total contained ordered cubes are at least `delta^(2^r) N^(r+1)`. If `delta^(2^r)N>2^r`, this exceeds every degenerate cube tuple, so an independent-direction cube exists. |
| Choice of flat size | valid | With `rho=alpha+1`, `delta >= e^-1(log N)^-rho`, and `m=2^r <= log N/(8 rho log log N)`, one has `log(delta^m N/m) >= log N - m(1+rho log log N)-log m > 0` for large `N`. |
| Lower comparability of `m` | valid | Taking the largest power of two below the displayed scale gives `m > log N/(16 rho log log N)` and therefore `log m >= (1/2)log log N` eventually. |
| Exact character sum | valid | For an affine flat `V=xi_0+H`, the normalized sum equals `sqrt(m)` in absolute value on `H-perp` and zero outside; `H-perp` has probability `1/m`. |
| Luxemburg lower bound | valid | At scale `b_alpha(log m)^(alpha/2)`, the modular is `lambda^-2 log^alpha(sqrt(m)/lambda)` and exceeds one for small fixed `b_alpha` and large `m`. |
| Coefficient normalization | valid | Coefficients `m^-1/2` on `V` have `ell^2` norm one, and extending them by zero to the ambient selected set is allowed. |
| Match to source quantifiers | valid | A single bounded ONS is constructed for each `N=2^d`, and every selected subset at the source threshold is bad. This is exactly the worst-case obstruction needed to show the universal upper factor cannot improve. |

## Adversarial checks and overclaim control

- The proof does not assume that arbitrary integer Fourier subsets contain intervals or progressions. The binary affine-flat lemma is proved for every dense subset of `F_2^d`.
- Degenerate cubes are not silently identified with affine subspaces. They are explicitly counted and removed.
- The flat dimension `r` grows, but the cube inequality and dependent-tuple count are uniform in `r`; the only condition is the displayed numerical inequality.
- The source threshold contains natural logarithms. Replacing `d` by `log N / log 2` changes only constants, and the proof works directly with `log N`.
- The result is along `N=2^d`, an infinite sequence. This suffices to exclude any uniform `o((log log n)^(alpha/2))` improvement.
- The theorem claims asymptotic order, not a sharp numerical constant or a statement for every integer dimension.

## Novelty check

On 2026-08-11, the exact arXiv id/title and endpoint-Orlicz terms were searched in the run registry, solution, attempt, and proof-gap indexes. External searches used the exact title and combinations of `bounded orthogonal systems`, `Orlicz`, `Walsh`, `affine subspace`, `Gowers norm`, and `log log`. They returned the source and background/adjacent papers, but no later paper claiming to answer Remark 2.11 and no matching theorem with the deterministic all-subsets conclusion. This is a bounded search, not a guarantee of novelty.

## Artifact verification

- `source_paper.pdf` is the 17-page arXiv v2 source.
- `figures/open_problem_crop.png` is a genuine full-width render of page 13 and includes Theorem 2.10, equation (2.13), and the complete Remark 2.11 sentence stating that optimality remains open.
- The packet cites the source paper and proves every additional ingredient in line.

Confidence: 96/100.

Recommended action: immediate expert review by an analyst familiar with bounded orthogonal systems and Orlicz norms. The most important audit is the cube-count/degenerate-cube comparison, followed by the exact matching of optimality quantifiers.
