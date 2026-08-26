# Verification record

## Target match

- Source: arXiv:2003.10134v4, page 35, Assumption 3 and Conjecture 1.
- Target: whether the Fractal Self-Similar Face condition and the stated
  qualitative Strong Open Set Condition force `Omega_m` and `Omega` to be
  uniformly exterior and interior `(epsilon,infinity)`-domains with one
  `epsilon` independent of `m`.
- Result: no under the assumptions as printed.  The constructed family even
  converges to a genuine inward-cusp domain.

## Proof audit

1. `K_0=[(-100,0),(100,0)]`.  For `h=3/2,2`, let `O_h` be the open rhombus
   with long diagonal `K_0` and other vertices `(0,plus/minus h)`.  Then
   `O_{3/2}` is strictly contained in `O_2`, and the three boundary
   intersections in Assumption 3 all equal the two endpoints of `K_0`.
2. At level `m`, put `a=1/m` and sample the two parabolas
   `x=plus/minus t^2`, `y=-1+t`, `a<=t<=1`, at mesh `m^-4`; join their lower
   endpoints by a horizontal cap.  Add the two baseline edges to obtain a
   simple polygonal arc from the endpoints of `K_0`.
3. Map `K_0` by a similitude onto each oriented edge.  Every edge has length
   below `200`, so every map is contractive.  The images of both fixed
   rhombi remain in the corresponding rhombus.  Their open interiors are
   pairwise disjoint: consecutive cells meet only at the common endpoint;
   same-arm nonconsecutive cells are separated in the vertical coordinate;
   opposite-arm cells are separated by at least `2/m^2` while their
   transverse widths are `O(m^-4)`; and the cap cases follow from its fixed
   aperture.  Thus both `O_{3/2}` and `O_2` satisfy the OSC for every `m`.
4. Each polygonal arc has exactly the original two endpoints as its
   zero-dimensional boundary, so Assumption 1 holds.
5. The polygonal domains converge in Hausdorff-boundary and characteristic-
   function senses to the rectangle with the inward parabolic notch removed.
6. At height `-1+2/m`, the points `(-5/m^2,-1+2/m)` and
   `(5/m^2,-1+2/m)` lie inside the domain.  Every internal path between them
   crosses the line `x=0` below the cap, hence has length at least `2/m`.
   Their distance is `10/m^2`, forcing `epsilon_m<=5/m` from condition (i)
   in the paper's Definition 2.
7. The identical argument with arbitrary `t>0` proves that the limit cusp
   domain is not uniform.

## Mechanical check

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify_geometry.py \
  --figure figures/cusp_prefractals.png
```

Expected final line:

```text
VERIFIED: contraction, two fixed OSC rhombi, and epsilon_m <= 5/m
```

The script checks the exact construction at levels 2 through 5 using a
separating-axis test for the open rhombus cells, checks containment for both
fixed open sets, checks all contraction ratios, and recomputes the quantitative
uniformity obstruction.  These finite checks supplement rather than replace
the uniform coordinate proof in `main.tex`.

## Scope and interpretation

The counterexample uses the level-dependent finite IFS families permitted by
the notation `(psi_{i,m})_{1<=i<=N_m}` in Subsection 6.1.  It also adapts to
the successive-composition convention used in Appendix B: apply the level
`m` cusp generator inside each parent cell.  Similarity invariance preserves
the `5/m` obstruction in a copied cell.

If “self-similar” was intended to require a fixed finite generator library,
uniform lower bounds on contraction ratios, or quantitative separation of
nonadjacent cells, those are meaningful repair hypotheses but are not stated
in Assumptions 1 and 3.  The result is therefore a counterexample to the
literal conjecture, not a claim against stronger stationary/quasiarc versions.

## Novelty check

The run's four lightweight indexes had no hit for arXiv:2003.10134 or this
conjecture.  Crossref identifies the published source as DOI
`10.1007/s00526-021-02159-3`.  An OpenAlex citation audit on 2026-08-11 found
eleven citing works through that date; their titles and available abstracts
concern PDE well-posedness, Mosco convergence, optimization, or self-similar
measures, and none states a proof or counterexample for Conjecture 1.  Exact
title and conjecture-phrase web searches likewise located no later primary
resolution.

