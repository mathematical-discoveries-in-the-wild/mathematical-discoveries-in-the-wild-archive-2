# Strict failure of reversed double semi-polarity

Status: `candidate_counterexample_likely_valid`

Source: Ákos G. Horváth, Zsolt Lángi, and Margarita Spirova,
*Semi-inner products and the concept of semi-polarity*, arXiv:1308.0974;
Results in Mathematics 71 (2017), 127–144.

Source location: Section 6, Question 2, page 14 of the arXiv PDF.

## Result

The source asks whether every convex body `M` containing the origin in its
interior satisfies

```text
M=(M^circ)_circ,
```

where the first operation is the right semi-polar and the second is the left
semi-polar.  The answer is **no**, already in the smooth, strictly convex
space `ell_4^2`.

Let `B_2` be the Euclidean unit disk, `e_1,e_2` the coordinate vectors, and

```text
M=conv((1/10)B_2 union {e_1,e_2}),
y=(1/sqrt(2),1/sqrt(2)).
```

The functional `z_1+z_2` is at most one on `M`, but equals `sqrt(2)` at `y`,
so `y` is not in `M`.  If `x` is in `M^circ`, testing at `e_1,e_2` gives
`x_1,x_2<=1`.  The `ell_4` semi-inner product satisfies

```text
[x,y]_4=(x_1+x_2)/2<=1,
```

so `y` belongs to `(M^circ)_circ`.  Thus the inclusion is strict.

The packet also proves the general identity

```text
(M^circ)_circ = F^{-1}(conv F(M)),
```

where `F(y)=[.,y]` is the norm-duality map.  Hence equality for a given body
is equivalent to convexity of `F(M)`.

## Packet contents

- `main.tex`: self-contained structural theorem and explicit counterexample.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_question_page14.png`: readable source-question crop.
- `verification.md`: adversarial proof and render audit.

Human review recommendation: **review as a full negative answer**.  The key
convention check is that the source's superscript semi-polar is applied first
and its subscript semi-polar second.
