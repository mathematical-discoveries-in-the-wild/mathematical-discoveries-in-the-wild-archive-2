# A finite-dimensional nonclosed zero set for a sum of maximally monotone operators

Bauschke, Bo\c{t}, Hare, and Moursi (arXiv:1110.4877), Remark 3.12,
ask whether two maximally monotone operators on a finite-dimensional Hilbert
space can have a nonclosed primal solution set
`zer(A+B)` when their domains meet.

This packet gives an affirmative answer already on `R^2`.  On
`D=(0,infinity) x (-infinity,0]`, set

```text
F(x,y) = (y/x^2, 1/x),
A(x,y) = F(x,y) + N_{R x (-infinity,0]}(x,y),
```

with `A` empty outside `D`, and take
`B=N_{R x {0}}`.  The symmetric part of the Jacobian of `F` is
`diag(-2y/x^3,0)`, so `A` is monotone.  A complete case split proves
`ran(Id+A)=R^2`; Minty's theorem makes `A` maximally monotone.  Finally,

```text
zer(A+B) = (0,infinity) x {0},
```

which is convex and nonclosed.

Files:

- `main.tex` — self-contained proof packet;
- `solution_packet.pdf` — compiled review packet;
- `verification.md` — proof, novelty, and QA audit;
- `code/check_counterexample.py` — monotonicity and Minty-range stress test;
- `source_paper.pdf` — original arXiv PDF;
- `figures/open_problem_crop.png` — source page containing Remark 3.12.

Status: `full_solution_likely_valid`.  Human review should focus on the
surjectivity case split for `Id+A`; it is the only nonstandard maximality step.
