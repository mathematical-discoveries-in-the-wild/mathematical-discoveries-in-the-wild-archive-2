# A qualitative strong OSC does not force uniform prefractal constants

Status: candidate full counterexample to Conjecture 1 of arXiv:2003.10134
under Assumptions 1 and 3 as printed, likely valid pending expert review.

The paper conjectures that a polygonal self-similar face condition and a
qualitative strong open set condition with two fixed convex polygons force all
prefractal domains and their limit to share one interior and exterior Jones
`(epsilon,infinity)` constant.

The packet constructs polygonal truncations of an inward parabolic cusp.  Each
edge is the image of the original face under a contracting similitude.  The
same two nested thin rhombi work as open sets for every level, and their cell
images have disjoint interiors.  Nevertheless, at level `m` two interior
points on opposite sides of the notch are only `10/m^2` apart, while every
internal joining curve has length at least `2/m`.  Hence every admissible
uniformity constant satisfies

```text
epsilon_m <= 5/m -> 0.
```

The limit is the corresponding inward-cusp domain and is itself nonuniform.
Thus the qualitative OSC lacks the quantitative separation or bounded-
geometry hypothesis needed by the conjecture.

Files:

- `solution_packet.pdf`: complete review packet.
- `source_paper.pdf`: arXiv:2003.10134v4 / published-version source PDF.
- `figures/source_page35.png`: source page containing Assumption 3 and
  Conjecture 1.
- `figures/cusp_prefractals.png`: construction and path obstruction.
- `main.tex`: self-contained proof source.
- `verification.md`: proof audit, scope, and novelty-search record.
- `code/verify_geometry.py`: independent finite-level cell-geometry checks
  and figure generator.

Human review recommendation: confirm that the conjecture is read literally
with the level-dependent IFS families allowed in Subsection 6.1.  If the
authors intended a fixed finite generator library with uniform quantitative
separation, that extra assumption is not present in Assumptions 1 and 3 and
would exclude the counterexample mechanism.

