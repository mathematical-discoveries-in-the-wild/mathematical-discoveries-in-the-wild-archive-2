# Half-quadratic threshold for star-shaped Minkowski volume monotonicity

Source: Matthieu Fradelizi, Zsolt Lángi, and Artem Zvavitch, *Volume of the
Minkowski sums of star-shaped sets*, arXiv:1910.06146v2.

Status: candidate substantial partial result; complete proof in `main.tex` and
`solution_packet.pdf`.

For a compact star-shaped set `S` in `R^d`, the source proves

```text
vol(S[k+1]/(k+1)) >= vol(S[k]/k)
```

when `k >= (d-1)(d-2)`. This packet proves the same conclusion, with the same
equality characterization, whenever

```text
k >= d-1  and  (k-d+2)(k+1)^(d-1) > k^d.
```

In particular, it is enough that

```text
k >= binom(d,2)-1.
```

Thus the sufficient threshold drops from asymptotic size `d^2` to `d^2/2`.
The exact coefficient criterion improves the clean bound slightly further; its
first valid values in dimensions `4,5,6,7` are `5,8,13,19`, compared with the
published `6,12,20,30`.

The proof retains the exact coefficient in inequality (10) of the source. All
of the source's cubical-layer transport argument before its final scalar
estimate is valid for `k >= d-1`. A second-order Taylor bound proves the new
closed-form threshold.

Files:

- `solution_packet.pdf` — expert-facing proof packet.
- `main.tex` — self-contained LaTeX source.
- `source_paper.pdf` — exact source paper.
- `figures/open_problem_crop.png` — full-width rendering of source page 2,
  containing Conjecture 1, the star-shaped definition, and Theorem 1.
- `verification.md` — proof audit, search bounds, and review focus.
- `code/verify_thresholds.py` — exact-integer scalar sanity checks.

Limitation: this does not settle the remaining star-shaped cases below the
exact coefficient cutoff, and therefore does not fully resolve the BMW
conjecture or even its star-shaped restriction.
