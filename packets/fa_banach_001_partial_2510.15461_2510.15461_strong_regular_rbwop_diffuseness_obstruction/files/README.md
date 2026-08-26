# Diffuseness and Weak-Interior Obstructions for Strong Regularity with r-BWOP

Source paper: G. Lopez-Perez, E. Martinez Vano, and A. Rueda Zoca,
"Big weak open radius versus big slice diameter," arXiv:2510.15461;
Mediterranean Journal of Mathematics 23 (2026), article 141.

Status: likely valid partial result. The source question remains open: this
packet does not construct a strongly regular r-BWOP space and does not prove
that no such space exists.

## Result

Let `X` have the r-BWOP. For nonempty relatively weakly open subsets
`U_1,...,U_n` of `B_X`, positive weights `lambda_i` summing to one, and

```text
C = sum_i lambda_i U_i,
```

one has

```text
diam(C) >= max_i lambda_i.
```

Consequently, if `diam(C) < epsilon`, then every coefficient is smaller than
`epsilon` and `n > 1/epsilon`. If `diam(C) < 1`, the norm closure of `C` has
empty relative weak interior in `B_X`.

Using the standard localization of strong regularity, any hypothetical
strongly regular r-BWOP space must realize arbitrarily small local
strong-regularity witnesses inside every weak opening using more than
`1/epsilon` weak openings, each with coefficient below `epsilon`; every such
witness of diameter below one has weakly nowhere-dense norm closure.

There is also a broad no-go theorem:

```text
No strongly regular r-BWOP space has property (overline P1).
```

In particular, no isometric predual of an `ell_1(Gamma)` space can be both
strongly regular and r-BWOP.

## Why This Matters

The direct full contradiction fails because a small convex combination of
slices need not contain a relatively weakly open subset. The theorem identifies
exactly how a positive example would have to exploit that gap: its witnesses
must become arbitrarily diffuse and must have no weak interior even after norm
closure. It also rules out the substantial class where convex combinations of
slices locally contain weak openings up to closure.

## Files

- `main.tex`: complete proof packet source.
- `solution_packet.pdf`: rendered and visually checked packet.
- `source_paper.pdf`: local copy of arXiv:2510.15461.
- `figures/open_problem_crop.png`: full-width crop of Remark 3.3(3), PDF page 14.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Human Review Recommendation

Review as a structural partial result, not as a solution of the existence
question. The main checks are the scaled-copy diameter estimate, the use of
the classical localization lemma for strong regularity, and the application
of property `(overline P1)` to a small convex combination of slices.

