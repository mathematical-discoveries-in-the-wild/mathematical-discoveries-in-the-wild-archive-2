# No uniform small-ball convexity radius in a punctured Banach space

Status: `full_counterexample`

Source target: Riku Klén, Antti Rasila, and Jarno Talponen,
*Quasihyperbolic Geometry in Euclidean and Banach Spaces*,
arXiv:1104.3745, PDF page 16.

The source asks whether the Euclidean critical-radius phenomenon for
quasihyperbolic balls in punctured spaces extends to Banach spaces. The answer
is **no**, already for the two-dimensional Banach space

```text
X = (R^2, ||.||_infinity),   Omega = X minus {0}.
```

For every sufficiently small `delta > 0`, the packet constructs a center
`c_delta`, two points `A_delta,B_delta`, and their midpoint `M_delta`. Explicit
paths show that `A_delta` and `B_delta` have quasihyperbolic distance

```text
(3/2) delta + (9/8) delta^2 + O(delta^3)
```

from the center, whereas a path-independent crossing estimate gives

```text
k(c_delta,M_delta)
  >= (3/2) delta + (81/64) delta^2 + O(delta^3).
```

The positive second-order gap is `9 delta^2 / 64 + O(delta^3)`. Choosing a
radius strictly between the endpoint distances and the midpoint distance gives
a nonconvex quasihyperbolic ball, and these radii tend to zero.

The decisive proof device is an exact one-dimensional envelope bound for a
positive function satisfying `|u'| <= u`, together with a folding argument
across the diagonal. Folding is legitimate because coordinate sorting and
coordinate swapping preserve the infinity norm and do not increase path
length. This controls arbitrary paths, not only the explicit bang-bang paths
used for the upper bounds.

The related Rasila--Talponen paper arXiv:1007.3197 explicitly says that the
analogous negative statement was only *presumed* for quasihyperbolic `k`-balls;
its proved counterexample concerns `j`-balls. A bounded exact-phrase, keyword,
and citation-neighborhood search through 11 August 2026 found no later answer
to this punctured-Banach-space question. The packet therefore records the
counterexample as an agent result, subject to normal expert verification and
novelty review.

Files:

- `solution_packet.pdf`: complete proof and provenance discussion.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:1104.3745.
- `supporting_paper_1007.3197.pdf`: the related partial-result paper.

