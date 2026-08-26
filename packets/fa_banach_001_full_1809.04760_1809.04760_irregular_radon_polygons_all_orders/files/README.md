# Irregular polygonal Radon planes with every admissible number of vertices

Status: `full_solution_likely_valid`.

Source: K. Mandal, D. Sain, and K. Paul, *A complete characterization of
Radon planes whose unit spheres are regular polygons*, arXiv:1809.04760v2
(the PDF title is *A complete characterization of polygonal Radon planes*).
The open question is on page 11, after the conclusion.

## Open question

For every natural number `n`, does there exist a Radon plane whose unit sphere
is an irregular polygon with `4n+2` vertices? If so, give a general construction.

## Full answer

Yes, for every `n >= 1`. Put `m=4n+2`, let `P_m` be a Euclidean regular
`m`-gon centered at the origin, and choose any `lambda>0` with `lambda != 1`.
Apply the anisotropic linear map

```text
T_lambda(x,y) = (lambda*x,y).
```

Use `T_lambda(P_m)` as the unit ball. The source paper proves that the norm
with unit ball `P_m` is Radon. The map `T_lambda` is a linear isometry from
that normed plane onto the newly defined one, so it preserves
Birkhoff--James orthogonality and hence preserves the Radon property.
Invertibility preserves all `m` vertices.

The image polygon is not Euclidean regular. If its original vertices are
`v_k=(cos(2*pi*k/m),sin(2*pi*k/m))`, then the image of edge `k` has length

```text
2*sin(pi/m)*sqrt(lambda^2*sin^2((2k+1)*pi/m)
                 + cos^2((2k+1)*pi/m)).
```

For `k=n` this is `2*lambda*sin(pi/m)`, while for `k=0` it is

```text
2*sin(pi/m)*sqrt(lambda^2*sin^2(pi/m)+cos^2(pi/m)).
```

Equality of these two lengths would force
`(1-lambda^2)*cos^2(pi/m)=0`, impossible because `m>=6` and
`lambda != 1`. Thus the unit sphere is an irregular polygon with exactly
`4n+2` vertices. Taking `lambda=2` gives a deterministic one-line algorithm.

## Verification and novelty

The proof is exact and uses no numerical premise. The included checker tests
the displayed edge-length formula for `n=1,...,100` at `lambda=2`; this is
only a regression check, not part of the proof.

A bounded search through 2026-08-11 checked all lightweight run indexes,
exact-title and exact-question searches, arXiv searches for polygonal Radon
planes, and combinations of `irregular`, `4n+2`, `affine image`, and
`affinely regular`. No later paper explicitly answering this exact all-orders
question was found. The literature does recognize affine-regular hexagonal
Radon unit spheres, and affine invariance is elementary, so novelty confidence
is deliberately **moderate-to-low** even though the answer to the source's
stated question is complete.

Human-review recommendation: verify that the source's word `irregular` is used
in its stated Euclidean sense (failure of equal edge lengths/equal angles),
and confirm the bounded literature search before any novelty claim.

Packet PDF: `solution_packet.pdf`.

