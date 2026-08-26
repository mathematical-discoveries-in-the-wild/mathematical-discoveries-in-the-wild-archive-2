# Closed cones are exactly the conic Fitzpatrick fixed points

Status: `partial_result_likely_valid`.

Source: Y. García Ramos, J. E. Martínez-Legaz, and S. Simons, *New results on q-positivity*, arXiv:1111.6094, Positivity 16 (2012), 543--563, DOI 10.1007/s11117-012-0191-7.

The source formulates the generalized Fitzpatrick problem of characterizing sets `A` for which `G_{Phi_A}=A`. In its positive-definite Hilbert-space model it proves the identity for closed convex sets and, separately, verifies one nonconvex example: the union of the coordinate axes in `R^2`.

## Result

Let `H` be a real Hilbert space with `q(x)=||x||^2/2`, and let `A` be a nonempty cone, with no convexity assumption. Then

```text
A = G_{Phi_A}  if and only if  A is norm closed.
```

Thus every nonempty closed cone is a generalized Fitzpatrick fixed point. This gives a complete classification inside the conic subclass and strictly extends the source's coordinate-axes example.

The proof is self-contained. For a closed cone, distance is homogeneous: `d_A(lambda x)=lambda d_A(x)` for `lambda>0`. The fixed-point criterion can be written as

```text
sup_b { d_A(b)^2 - ||b-x||^2 } = d_A(x)^2.
```

For `x` outside `A`, evaluate the supremum at `b=lambda x` with `lambda>1` close to one; homogeneity makes the left side strictly larger than `d_A(x)^2`. Conversely, closure is necessary because every point of `closure(A)` automatically belongs to `G_{Phi_A}`.

## Scope and novelty

This is a solved subcase of the generalized `q`-positive fixed-point problem, not a solution of Fitzpatrick's full monotone-operator problem on `X x X*`. The source's nonconvex axes example is a closed cone, but the source does not state the general conic theorem.

A bounded novelty search through 2026-08-09 checked the run indexes, exact source title/citations, and exact combinations of `closed cone`, `G_{Phi_A}`, `Fitzpatrick function`, `fixed point`, and `q-positive` on arXiv and publisher/author pages. No prior statement of this theorem was found. Because the proof is short and grows directly from the source's example, novelty confidence is moderate and should be checked by a specialist.

Human-review recommendation: verify the intrinsic-conjugate calculation, the nonclosed-cone necessity argument, and the bounded novelty search.

Packet PDF: `solution_packet.pdf`.
