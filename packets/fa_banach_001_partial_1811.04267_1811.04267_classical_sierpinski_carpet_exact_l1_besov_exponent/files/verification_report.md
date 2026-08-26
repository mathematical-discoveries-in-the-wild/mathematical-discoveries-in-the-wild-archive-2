# Verification report

Status checked: `candidate_partial_result_likely_valid` (full theorem for the
classical carpet; partial relative to the broad source wording).

## Mathematical checks

- The source question was verified on p. 25 of arXiv:1811.04267.
- The heat/metric conversion is `lambda = alpha d_W`.
- Murugan–Shimizu Theorem 1.4 was checked: for every `p>1`, the critical
  metric smoothness is `s_p=d_w(p)/p` with
  `d_w(p)=log(8 rho(p))/log(3)`.
- Their capacity scaling theorem includes `p=1`, so the endpoint scaling
  constant is meaningful even though their Sobolev identification is stated
  for `p>1`.
- At `p=1`, discrete coarea proves capacity equals min-cut.
- The lower cut bound uses `2^n` disjoint rows with transverse ternary address
  in `{0,2}^n`.
- The middle wall between columns `(3^n-3)/2` and `(3^n-1)/2` has exactly
  `2^n` face edges. Rotations and a bounded coarse dual separator give the
  uniform annular upper bound.
- Corner adjacency changes capacities only by a universal factor because each
  corner edge has a two-edge face-adjacency route with bounded congestion.
- Hölder comparison was checked in both directions and yields
  `1/2 <= rho(p) <= 8^(p-1)/2^p`.
- Bounded truncation preserves a nonconstant representative for some level
  and converts `KS^{lambda,1}` to `B_{p,infinity}^{lambda/p}`.
- The 2022 lower bound evaluates to
  `d_H-d_tH+1=log(4)/log(3)` for the classical carpet.
- The unbounded transfer uses only local restriction and the explicit
  side-interface contribution `(3/8)^n=r^(d_H-1)`.

## Computational sanity check

`code/capacity_probe.py` was run with NetworkX. For a representative annulus,
the minimum cuts doubled from refinement 1 to refinement 2 in both the
face-adjacency and face-plus-corner graphs. This is not used as proof.

## Literature and novelty bounds

The exact arXiv id and core symbols/formulas were searched in the run indexes
and on the web through 11 August 2026. The search found the original paper,
the 2022 lower-bound/conjecture paper, the 2025 `p>1` critical theorem,
pre-fractal isoperimetry, and a January 2026 paper that still treats the
carpet Hölder endpoint as conjecturally non-sharp. No exact statement of the
classical equality or this `p downarrow 1` proof was found. This is bounded,
not exhaustive.

## Artifact checks

- `source_paper.pdf` is the original arXiv PDF.
- The open-question crop was rendered from source page 25 and visually checked.
- Supporting PDFs are local copies of the decisive lower-bound and `p>1`
  theorem sources.
- `solution_packet.pdf` compiles in four pages with no unresolved references,
  box warnings, or LaTeX warnings.
- Extracted text was checked for the theorem, endpoint limit, scope, review
  recommendation, and references.
- All four final pages were rendered to PNG and visually inspected; equations,
  the source crop, page breaks, and bibliography are legible and unclipped.
- The final finite check returned cuts `[8, 16]` for face adjacency and
  `[17, 34]` for face-plus-corner adjacency at refinements one and two.

Highest-value human check: the uniform coarse-dual/nested-wall construction
in Lemma 1. Every later step follows by explicit inequalities.
