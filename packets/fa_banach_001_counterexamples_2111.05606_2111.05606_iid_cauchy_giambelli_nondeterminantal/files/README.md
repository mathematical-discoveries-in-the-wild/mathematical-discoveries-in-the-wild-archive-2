# An iid Cauchy counterexample to the Giambelli converse

Status: **candidate counterexample, likely valid; expert review requested**.

This packet gives a full negative answer to Conjecture 1 of Bufetov--Lazag,
*A determinantal point process governed by an integrable projection kernel is
Giambelli compatible* (arXiv:2111.05606). The conjecture appears on printed
page 5.

Fix the same `R > 0` as in the conjecture and let the point process on the real
line consist of exactly two independent points with Cauchy density

```text
R / (pi (x^2 + R^2)).
```

The points are distinct almost surely. Under `t = 1/(x+iR)`, Cauchy measure is
sent to uniform arclength on the circle with center `c=-i/(2R)` and radius
`1/(2R)`. The two-variable holomorphic mean-value property shows that the
expectation of every polynomial in the transformed points is its value at
`(c,c)`. Centering every Newton sum subtracts exactly the power sums of
`(c,c)`, so the expected centered specialization is the zero specialization.
All nonempty Schur expectations vanish, which proves Giambelli compatibility.
Because the configuration has only two points and all transformed variables
are bounded, the specialization is an `L^1`-specialization.

The process is not determinantal, even allowing a complex, nonsymmetric
kernel. Relative to Cauchy measure its correlation densities are `2`, `2`,
and `0` in orders one, two, and at least three. If a kernel represented these
densities, a conull choice of four points would give a `4 x 4` matrix whose
principal minors have precisely those values. Diagonal similarity and the
two- and three-minor equations force a small tournament normal form; its
four-by-four determinant is `-4`, contradicting the required zero four-point
correlation.

Packet contents:

- `solution_packet.pdf`: complete counterexample and proof;
- `main.tex`: reproducible LaTeX source;
- `source_paper.pdf`: the original arXiv paper;
- `figures/open_problem_crop.png`: full-width crop of Conjecture 1 on page 5;
- `code/verify_counterexample.py`: exact symbolic checks of the matrix
  obstruction and finite-degree checks of the centered mean-value mechanism;
- `VERIFICATION.md`: proof audit and verifier output;
- `novelty_search.md`: bounded literature-search record.

The code is a sanity check, not part of the proof. The principal human-review
points are the passage from Cauchy measure to the circle mean-value identity
and the reference-measure normalization in the non-determinantal argument.

