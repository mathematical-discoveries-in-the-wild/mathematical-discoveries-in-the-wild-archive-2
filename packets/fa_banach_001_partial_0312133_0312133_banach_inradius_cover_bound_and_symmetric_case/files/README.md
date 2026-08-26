# Banach Inradius Cover Bound and Symmetric-Body Case

Source paper: Vladimir Kadets, "Coverings by convex bodies and inscribed
balls", arXiv:math/0312133; *Proceedings of the American Mathematical
Society* 133 (2005), 1491-1495.

Status: candidate strengthened partial result, likely valid. The unrestricted
Banach-space question remains open. This packet proves three results:

1. the exact Kadets inequality in every real Banach space when all covering
   bodies are centrally symmetric (their centers may differ); and
2. the Hilbertian-distortion estimate `sum r(A_n) >= r(A)/D` whenever a
   Hilbert ellipsoid `E` satisfies `E subset B_X subset D E`, and consequently
   the universal estimate `sum r(A_n) >= r(A)/sqrt(d)` in dimension `d`; and
3. the independent elementary estimate
   `sum r(A_n) >= 2 r(A)/(d+1)` for arbitrary convex covers in every
   `d`-dimensional normed space.

## Main Result

Let `X` be a real Banach space and let a closed convex body `A` be covered by
a sequence of closed convex bodies `(A_n)`.

- If every `A_n` is centrally symmetric, then
  `sum_n r(A_n) >= r(A)`.
- If `dim X = d < infinity`, then, without symmetry,
  `sum_n r(A_n) >= r(A)/sqrt(d)`.
- The elementary containing-plank argument independently gives
  `sum_n r(A_n) >= 2 r(A)/(d+1)`.

The first statement is dimension-free and exact. The second is the strongest
universal quantitative bound in this packet; the third is retained as an
elementary certificate independent of ellipsoid comparison.

## Proof Mechanism

Ball's Banach-space plank theorem says that planks covering a norm ball of
radius `q` have total norm-width at least `2q`.

If `E subset B_X subset D E`, then every convex body satisfies
`r_E(C)/D <= r_X(C) <= r_E(C)`. Applying Kadets's exact theorem in the Hilbert
norm with unit ball `E` loses only the factor `D`. John's symmetric ellipsoid
theorem gives `D <= sqrt(d)` for every `d`-dimensional normed space.

For a centrally symmetric convex body `C`, symmetry moves every inscribed ball
to the symmetry center by averaging. Consequently, `C` can be placed in a
plank of width arbitrarily close to `2r(C)`. Replacing each covering body by
such a plank and applying Ball gives the exact inequality.

For an arbitrary compact convex set `C` in dimension `d`, an incenter has
active supporting functionals whose convex hull contains zero. Caratheodory's
theorem reduces this certificate to at most `d+1` functionals. One coefficient
is at least `1/(d+1)`, and its supporting direction yields a plank containing
`C` of width at most `(d+1)r(C)`. Intersect the original cover with an
inscribed ball of `A`, replace the intersections by these planks, and apply
Ball.

## Computational Stress Check

Before the proof route was found, an exact linear-programming search tested
two standard tetrahedral partitions of the `l_infinity^3` unit cube. The
five-tetrahedron partition has total relative inradius `5/6`, and the six-cell
Freudenthal partition has total relative inradius `1`, both above the cube
radius `1/2`. This is only a negative counterexample search, not evidence used
in the proof.

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0312133_banach_inradius_cover_bound_and_symmetric_case/code/check_cube_triangulations.py
```

## Files

- `main.tex`: self-contained proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:math/0312133.
- `figures/open_problem_crop.png`: full-width crop of the page-one question.
- `code/check_cube_triangulations.py`: bounded LP stress check.
- `VERIFICATION.md`: independent proof-obligation audit and render checks.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty and Scope

The 2026 published version of William Verreault's plank-theorem survey still
records the unrestricted general-Banach-space statement as open. Bounded
searches for the exact constants and the centrally symmetric covering-body
case found Kadets's Hilbert result, Ball's plank theorem, and the
Akopyan-Karasev partition results, but no statement matching either theorem in
this packet.

Novelty confidence is moderate, not high: both proofs are short syntheses of
classical support-function arguments with Ball's theorem and may already be
folklore. No priority claim is made.

## Human Review Recommendation

Review as a likely-valid strengthened partial result. The main checks are:

1. the directions of `r_E(C)/D <= r_X(C) <= r_E(C)`;
2. the active-support optimality condition at a finite-dimensional incenter;
3. the `rho/lambda_i <= (d+1)rho` containing-plank calculation;
4. the centered-inradius identity for an unbounded centrally symmetric body;
5. the countable-cover passage by summably enlarging planks.
