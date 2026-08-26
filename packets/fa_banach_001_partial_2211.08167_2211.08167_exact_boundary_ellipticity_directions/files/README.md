# Exact boundary-ellipticity directions for arXiv:2211.08167

Status: `candidate_partial_result_likely_valid`

Source: Franz Gmeineder, Bogdan Raiţă, and Jean Van Schaftingen,
*Boundary ellipticity and limiting L¹-estimates on halfspaces*,
arXiv:2211.08167v1.

## Result

For the explicit first-order operator in Example 6.5, the paper states
boundary ellipticity only for normals in `span{e_3,...,e_n}`.  The exact
set is substantially larger:

```text
A is boundary elliptic in direction ν
    iff ν is not in span{e_1,e_2}.
```

Indeed, the complete nonzero complex characteristic variety is

```text
C* (1,i,0,...,0)  union  C* (1,-i,0,...,0).
```

This characterization is preserved by every composition `B A` in the
example when `B` is complex-elliptic.  Combining it with the source's
sharp halfspace theorems gives an if-and-only-if characterization of all
halfspace normals for which the limiting trace and Sobolev estimates hold
for this entire arbitrary-order family.

The result solves an explicit family adjacent to the paper's proposed
future study of the admissible normal set.  It does not solve the stated
general-domain trace program.

## Novelty caveat

The current v1 source and local run indexes contain only the smaller
sufficient set.  Exact web searches for this operator and for later work
on its admissible normals found no separate characterization or erratum.
Novelty is provisional pending specialist review.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: LaTeX source.
- `verification.md`: algebra, source, novelty, and rendering checks.
- `source_paper.pdf`: official arXiv PDF.
- `source_material/source_2211.08167.tex`: inspected source TeX.
- `code/verify_characteristic_cone.py`: exact symbolic/sample checks.
- `figures/future_work_and_example_crop.png`: real crop of source page 20.
