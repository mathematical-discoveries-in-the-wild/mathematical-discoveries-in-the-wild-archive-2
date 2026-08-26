# Counterexample to the simultaneous-rotation orbit lemma

Status: `candidate counterexample, likely valid pending expert review`

Source: Susanna Dann and Marisa Zymonopoulou, *Intersection Bodies with
Certain Symmetries* (published as *Sections of Convex Bodies with
Symmetries*), arXiv:1307.3206.

## Result

Lemma 1 of the source claims that for every vector in `R^(kappa*n)`, its
orbit under simultaneous block rotation by `SO(kappa)` is a
`(kappa-1)`-sphere whose linear span has dimension `kappa`.

This is false for `kappa >= 3`.  For the smallest counterexample, take
`kappa=3`, `n=2`, and identify the vector with the matrix

```text
X = [e_1 e_2] in M_(3,2)(R).
```

Its orbit consists of all ordered orthonormal pairs `(u,v)` in `R^3`.
Six such orbit points yield the six coordinate vectors of
`R^3 direct-sum R^3`, so the orbit spans all of `R^6`, not a 3-plane.

More generally, if `X` has rank `r` and `kappa >= 3`, then

```text
span{sigma X : sigma in SO(kappa)}
  = {Y : row(Y) is contained in row(X)}
```

and this space has dimension `kappa*r`.  The source's asserted dimension is
correct only in the rank-one case.

## Consequence and scope

The paper defines `H_x^perp` as this orbit span and subsequently treats it as
a fixed `kappa`-dimensional subspace.  The counterexample gives
`H_x^perp=R^6` and `H_x={0}`.  Thus the fixed-codimension hyperplane and
intersection-body construction is not defined as claimed for generic
directions when `kappa>=3`, and later arguments using that construction need
repair.

The paper's separate question about universal `L_{-p}` embeddings remains a
meaningful independent problem.  This packet does not claim to solve it; it
shows that the printed geometric setup and its supporting proof cannot be
used as stated.

## Files

- `main.tex`: self-contained counterexample and general correction.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:1307.3206v2.
- `figures/lemma1_crop.png`: source Lemma 1 and its proof on PDF page 4.
- `verify_counterexample.py`: exact symbolic check of the six rotations.
- `verification.md`: proof and novelty audit.

## Novelty check

The run indexes and bounded searches for the exact lemma, title, arXiv id,
corrections, and errata found no prior correction.  This is not exhaustive
bibliographic certification.

