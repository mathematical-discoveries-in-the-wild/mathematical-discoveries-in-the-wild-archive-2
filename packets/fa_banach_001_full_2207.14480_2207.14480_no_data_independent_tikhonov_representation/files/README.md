# Full solution packet: no data-independent Tikhonov representation

## Source

- Daniel Obmann and Markus Haltmeier, *Convergence analysis of critical point
  regularization with non-convex regularizers*.
- arXiv: `2207.14480v2`; DOI: `10.1088/1361-6420/acdd8d`.
- Open conjecture: Section 4.3, pages 19--20 of the arXiv PDF.

## Classification

- Status: `full_solution_likely_valid`.
- Result type: full affirmative resolution of the source's set-valued
  non-equivalence conjecture.
- Scope: equality between the complete set of `alpha phi`-critical points and
  the complete set of minimizers of a standard Tikhonov functional with one
  data-independent modified regularizer.

## Result

Take `X=Y=R`, `K=I`, the original regularizer `R=0`, and a constant tolerance
`phi=epsilon>0`. For every fixed `alpha>0`, the `alpha phi`-critical set for
datum `y` is the interval

```text
[y-sqrt(2 alpha epsilon), y+sqrt(2 alpha epsilon)].
```

No proper extended-real function `S` can make these intervals equal to

```text
argmin_x ( |x-y|^2/2 + alpha S(x) )
```

for all data `y`; in fact, equality already fails for the two data values
`0` and `sqrt(2 alpha epsilon)`. Thus the source method is not, in general,
standard Tikhonov regularization with a data-independent modified penalty.

## Proof idea

The source's relative-subgradient definition says that `x` is critical exactly
when its objective value is at most `inf(T+alpha phi)`. In the scalar example
this produces the moving interval above. Let `rho=sqrt(2 alpha epsilon)`.
Both `0` and `rho` lie in the critical intervals for data `0` and `rho`.
If a single penalty `S` represented both intervals as minimizer sets, equality
of the two objective values for datum `0` would force
`S(0)-S(rho)=epsilon`, whereas datum `rho` would force
`S(rho)-S(0)=epsilon`. Their sum gives `0=2 epsilon`.

## Scope limitation

This settles the conjecture under the set-valued interpretation used in
Section 4.3: all relative-critical points are to agree with all Tikhonov
minimizers. It does not say that every algorithmically selected single-valued
branch is non-Tikhonov; for example, selecting the center of each interval is
represented by the zero penalty.

## Files

- `main.tex`: self-contained expert-facing proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of the arXiv paper.
- `figures/open_problem_crop_page19.png` and
  `figures/open_problem_crop_page20.png`: the complete two-page source
  conjecture.
- `code/verify_two_data_obstruction.py`: exact algebraic sanity check.

## Novelty check

The run's registry, solution, attempt, and proof-gap indexes had no entry for
this paper or conjecture. Exact-concept queries of the official arXiv API on
August 11, 2026 found the source paper, the authors' 2023 convergence-rates
follow-up (`2302.08830`), and one unrelated paper on relative
subdifferentials. The follow-up contains no equivalence result, and no arXiv
paper settling this conjecture was found within those exact-query bounds.

