# Verification and review checklist

## Source fidelity

- Cached arXiv source `1507.05114` was decompressed and compiled successfully.
- The source PDF has 14 pages.
- Problem 1 is on source PDF page 12.
- `figures/open_problem_crop.png` was cropped from the rendered source page,
  and contains the definition, exact question, and the following lower-bound
  uncertainty paragraph.

## Proof audit

### Universal lower bound

- The distance-coordinate map associated with `m` landmarks is continuous.
- If it resolves, it is injective.
- For `m<=d`, padding with zero coordinates gives a continuous injection
  `R^d -> R^d`.
- Invariance of domain makes its image open.
- For `m<d`, the image lies in a proper coordinate subspace.
- For `m=d`, the image lies in the nonnegative orthant and contains a point on
  a coordinate face (the image of a landmark). Both contradict openness.

### Facet obstruction

- The cone over the relative interior of a facet is open and nonempty.
- On that cone the norm equals its exposing functional.
- For a finite landmark set, sufficiently large translation puts both
  landmark-difference families inside this cone.
- The displacement between the two test points is a nonzero vector in the
  kernel of the exposing functional, so all landmark distances agree exactly.
- The corollaries for polyhedral norms and non-strict normed planes use only
  the existence of a facet.

### `ell_p` theorem

- Equality of distances at zero and at `e_i`, after taking `p`th powers and
  subtracting, isolates the scalar equation
  `|x_i-1|^p-|x_i|^p=|y_i-1|^p-|y_i|^p`.
- The derivative is
  `p(j_p(t-1)-j_p(t))`, with
  `j_p(t)=sign(t)|t|^(p-1)` strictly increasing for `p>1`.
- Hence the scalar function is strictly decreasing and every coordinate
  agrees.
- The universal lower bound gives exactness.

### Near-Hilbert theorem

- With `Phi=|.|_2^2+H`, the relative squared-distance map is
  `G(x)=1-2x+E(x)`, coordinatewise, where
  `E_i(x)=H(x-e_i)-H(x)`.
- The fundamental theorem of calculus and
  `Lip(grad H)<=eta` give `Lip(E_i)<=eta`.
- Therefore `Lip(E)<=sqrt(d) eta<2`.
- `G(x)=G(y)` implies
  `2|x-y|<=sqrt(d) eta |x-y|`, hence `x=y`.
- For the example `H=epsilon ||.||_4^2`, the gradient is globally Lipschitz:
  the Hessian is degree zero and bounded away from the origin, and the
  gradient extends Lipschitzly through zero. Small positive `epsilon` meets
  the hypothesis. The Euclidean component ensures strict convexity, while a
  direct parallelogram calculation shows the norm is non-Hilbert.

## Literature and novelty caution

- Cheap run indexes and targeted searches found no later primary-source answer
  to Problem 1.
- Search was complicated by the unrelated graph-theoretic and embedding uses
  of “metric dimension”.
- The lower bound uses a standard application of invariance of domain, and the
  other proofs are elementary. They may exist under different terminology.
- Treat all novelty claims as provisional until a specialist checks the 1957
  Kalisch--Straus literature and later work on determining sets in Minkowski
  spaces.

## Human review requested

1. Confirm the intended reading of the parenthetical “(strictly convex)” in
   Problem 1 and the decision to classify the packet as partial.
2. Check the open-cone formulation of the facet proof.
3. Check the `C^{1,1}` hypothesis and the explicit non-Hilbert example.
4. Search older terminology: determining sets, metric generators, and
   equidistant sets in finite-dimensional Banach spaces.
5. Do not cite the packet as resolving the universal strictly convex case.
