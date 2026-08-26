# Verification record

## Claim and source

- Source: Sahiba Arora and Jochen Glück, *An operator theoretic approach to
  uniform (anti-)maximum principles*, arXiv:2104.12205.
- Exact signal: the question after Proposition 4.7, PDF page 15.
- Claim: both order restrictions in Theorem 4.5 are necessary in the stated
  generality; an example with `m1=m2=3` defeats propagation to the opposite
  side of the initial real resolvent point.

## Mathematical audit

1. Poisson convolution `K` on the circle is positive, self-adjoint, injective,
   has dense range, fixes only constants, and maps `L2` into `L-infinity`.
2. The three-phase operator `Q(f0,f1,f2)=(f1,f2,Kf0)` is positive, injective,
   has dense range, and satisfies `Q^3=diag(K,K,K)`; the adjoint cube has the
   same form.
3. For `A=I-Q^{-1}`, bounded-shift power-domain invariance gives
   `dom(A^3)=ran(Q^3)` and `dom((A')^3)=ran((Q')^3)`.  Hence the source's two
   domination inclusions hold for `m1=m2=3` with `u=1` and integration
   functional `phi`.
4. The fixed spaces of `Q` and `Q'` are both the global constants, so `0` is
   the required geometrically simple eigenvalue of `A` and an eigenvalue of
   `A'`, with the required positive eigenvector and eigenfunctional.
5. `R(1,A)=Q>=0`, so the assumed lower rank-one estimate holds.
6. For `delta>0`, factorization yields the displayed exact resolvent formula.
   On positive data `(0,0,1_B)`, its first component is
   `-delta (I+delta^3 K)^{-1}1_B`.  The inverse is identity minus a bounded-
   kernel convolution operator, so this component stays bounded away from
   zero on arbitrarily small arcs while the rank-one comparison is only
   proportional to the arc measure.  No lower rank-one bound is possible.
7. Replacing `A` by `-A` converts the failure into the upper-bound failure
   asked about in Theorem 4.5(b).

## Computational verifier

Command:

`conda run --no-capture-output -n sandbox python code/verify_counterexample.py`

The verifier used cyclic grids of sizes 12, 24, 48, 96, and 192.  The exact
cube identities had zero numerical error, the resolvent formula had maximum
error below `9e-16`, and the least rank-one lower-comparison constants were
approximately `17.473, 35.473, 71.473, 143.473, 287.473`.  Their ratios to
grid size converge to `1.5`, confirming the predicted linear divergence.
Final status: `PASS`.

This finite computation supports but does not replace the small-set proof.

The final five-page PDF compiled without warnings, was rendered at 144 dpi,
and every page was visually inspected.  SHA-256:
`acd3040fc179e4b5303b8ffca603ede42a85dda23c0c8f09a95913dff40e0742`.

## Novelty audit

On 2026-08-17 the four lightweight run indexes were searched by arXiv id,
title, and core operator/resolvent terms.  Bounded web searches used the exact
source sentence, theorem terminology, exact title, author names, and variants
of one-sided rank-one resolvent domination.  They found the source paper and
related later papers on eventual domination and individual maximum principles,
but no explicit resolution of this question or the construction here.  This
is a bounded novelty check, not an exhaustive priority claim.

## Human-review recommendation

Check chiefly the power-domain identity for `A=I-Q^{-1}` and the conversion of
the small-arc estimate into failure of the operator order.  The remaining
block algebra and sign-flip argument are direct.
