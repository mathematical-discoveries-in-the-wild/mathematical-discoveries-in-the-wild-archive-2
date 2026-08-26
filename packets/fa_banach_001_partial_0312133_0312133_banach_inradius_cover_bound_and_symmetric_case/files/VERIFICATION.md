# Verification Report

Verdict: `partial_result_likely_valid_strengthened`.

Scope: exact result when all covering bodies are centrally symmetric in an
arbitrary real Banach space; `1/D` transfer under Hilbertian distortion `D`,
hence `1/sqrt(d)` for arbitrary covering bodies in a `d`-dimensional normed
space; and an independent elementary `2/(d+1)` bound. The unrestricted exact
Banach-space question is not claimed solved.

## Proof Audit

### 1. Symmetric-body plank lemma

Passed. If `x+tB` is contained in a centered symmetric body `K`, reflection
gives `-x+tB` inside `K`; convex averaging gives `tB` inside `K`. Hence the
inradius is realized, in the supremal sense, at the symmetry center. The
support-function identity

```text
r(K) = inf_{||f||=1} h_K(f)
```

holds for closed convex `K`, including unbounded bodies with extended support
values. Symmetry makes the two support values equal, producing a containing
plank of width arbitrarily close to `2r(K)`.

### 2. Hilbertian-distortion comparison

Passed. If `E subset B_X subset D E`, then an `E`-ball of radius `t`
contains an `X`-ball of radius `t/D`, and an `X`-ball of radius `t` contains
an `E`-ball of radius `t`. Thus

```text
r_E(C)/D <= r_X(C) <= r_E(C).
```

Applying Kadets's Hilbert theorem to the `E`-norm loses exactly one factor
`D`. John's theorem for the symmetric unit ball supplies `D <= sqrt(d)`.

### 3. Active-support balance

Passed. In finite dimensions, the dual unit sphere is compact and the support
function is continuous for compact `C`. If the active functionals at an
incenter did not have zero in their convex hull, strict separation would give
a direction improving all active slacks. A neighborhood/complement compactness
argument makes the improvement uniform over the whole dual sphere, contradicting
maximality of the inball.

### 4. Caratheodory coefficient calculation

Passed. From `0=sum lambda_j f_j`, with at most `d+1` active unit functionals,
choose `lambda_i >= 1/(d+1)`. For `x in C`,

```text
-f_i(x) <= rho (1-lambda_i)/lambda_i,
 f_i(x) <= rho.
```

The containing plank therefore has width exactly `rho/lambda_i`, at most
`(d+1)rho`.

### 5. Cover reduction

Passed. For `q<r(A)`, intersect each `A_n` with a contained closed `q`-ball
`U`. These intersections are compact in finite dimensions, retain a cover of
`U`, and have no larger inradius than `A_n`. Their containing planks cover
`U`, so Ball gives the claimed factor. The symmetric proof does not use this
intersection and therefore does not accidentally destroy symmetry.

### 6. Countable families

Passed with the standard countable form of Ball's theorem quoted by Kadets.
In finite dimensions it also follows directly by summably widening the closed
planks, obtaining an open cover of the compact ball, and taking a finite
subcover. If the original total width is infinite, the conclusion is trivial.

## Computational Stress Check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0312133_banach_inradius_cover_bound_and_symmetric_case/code/check_cube_triangulations.py
```

Observed:

- five-tetrahedron cube partition: total volume `1`, sum of l-infinity
  inradii `5/6`, ratio to cube inradius `5/3`;
- six-tetrahedron Freudenthal partition: total volume `1`, sum of inradii
  `1`, ratio to cube inradius `2`.

Neither bounded test contradicts the exact conjecture. The computation is not
part of the proof.

## Source and Render Audit

- Original PDF copied as `source_paper.pdf`.
- Page-one source statement visually rendered and cropped at full page width.
- Crop includes Kadets's complete sentence that the analogous general Banach
  question remains open.
- Final PDF compiled with all temporary artifacts under `tmp/`.
- Final PDF page render inspected for clipping, overlap, broken glyphs, and
  unreadable source imagery.

## Recommended Human Checks

1. Confirm the ellipsoid sandwich and inradius-comparison directions.
2. Confirm the extended-valued support identity for unbounded symmetric
   bodies in the exact hypotheses used.
3. Confirm the countable Ball theorem in arbitrary Banach spaces, or replace
   the citation with an explicit standard reference for the countable form.
4. Search classical relative-width/inradius literature for prior appearance
   of the distortion transfer and the `(d+1)` containing-plank lemma.
