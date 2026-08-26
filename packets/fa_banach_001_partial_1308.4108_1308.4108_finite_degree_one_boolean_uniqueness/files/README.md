# Finite degree-one Boolean uniqueness

Status: `substantial partial result (likely valid)`

Source: Hamed Hatami, Pooya Hatami, and James Hirst, *Limits of Boolean
Functions on F_p^n*, arXiv:1308.4108, concluding remarks, PDF page 12.

## Result

The source asks how two limit objects with identical affine-system densities
must be related. This packet gives a complete common-factor classification for
all `{0,1}`-valued limit objects depending on finitely many degree-one
coordinates.

Represent such an object by `f:F_p^r->{0,1}` and quotient by its translation
period subgroup. The resulting aperiodic finite function is its minimal affine
core. Two such cylinders have all the same affine densities if and only if
their minimal cores are affinely isomorphic. Equivalently, both factor through
one common finite affine Boolean function by surjective affine maps.

The proof reconstructs the full law of every Boolean affine-restriction array
from subset densities. On the full `m`-dimensional affine system, that array is
`f o A` for a uniformly random affine map `A:F_p^m->F_p^r`. Translation
periods detect the core dimension; the positive-probability invertible stratum
then recovers the affine orbit.

## Scope

The theorem works for every prime `p` and allows redundant selected
coordinates. It does not resolve fractional-valued cylinders,
higher-degree/nonclassical coordinates, or arbitrary measurable limit
objects. Two additional upgrade attempts isolate product-Bernoulli mixture
identifiability and inverse-limit coherence as the respective obstructions.

## Files

- `main.tex`, `solution_packet.pdf`: theorem, proof, upgrade attempts, and
  literature scope.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_problem_crop.png`: readable full-width source crop.
- `verification_report.md`: proof and rendering audit.
- `novelty.md`: bounded primary-source search record.
