# Intrinsic equals extrinsic for reinforced Triebel--Lizorkin spaces on a cube

**Status:** candidate full solution of Conjecture 4.22 in arXiv:1302.3751,
subject to human review.

For the full parameter range in the source,

```text
1 <= p < infinity, 0 < q < infinity, s > sigma_{p,q},
```

the packet proves

```text
F_{p,q}^{s,rinf}(Q) = F_{p,q}^{s,rinf}(Q)^*
```

with equivalent quasi-norms. More strongly, it constructs a bounded linear
right inverse to restriction that preserves every critical reinforced face
condition simultaneously.

## Proof intuition

A fixed-parameter common Seeley--Hestenes extension can be chosen as a
finite sum of coordinate reflections and dilations. Tensoring it over the
cube gives, on every exterior collar cell,

```text
D^alpha E_Q f(x) = sum_A c_{A,alpha} (D^alpha f)(T_A x).
```

If `Gamma` is any open face, then every affine image satisfies

```text
dist(T_A x, Gamma) <= C dist(x, Gamma).
```

Normal distances are scaled by one of finitely many slopes. Tangential
coordinates outside the open face are reflected into `(0,1)`, so their
distance contribution disappears. A change of variables therefore bounds
the two-sided weighted norm of the extension by the intrinsic one-sided
norm. The same finite operator works for all faces and all critical orders.

## Consequence

For the unit square,

```text
W_2^{1,rinf}(Q)^*
= {f in W^{1,2}(Q): integral_Q |f|^2/dist(x,Gamma_0)^2 < infinity}
= F_{2,2}^{1,rinf}(Q).
```

Hence the intrinsic Sobolev space has the oscillating `u`-Riesz basis sought
in the source for every integer `u>1`.

## External input and verification

The sole decisive external input is the finite common-extension case of
Lu and Yao, arXiv:2211.15567v2, Theorem 23 and equations (29)--(30. The
supporting PDF is included. Their theorem gives the bounded finite reflection
operator on the ordinary Triebel--Lizorkin space; the simultaneous preservation
of all reinforced open-face weights is proved in this packet.

No computation is needed. The main human-review points are the localization
of the half-space reflection operator to the product cube and the
open-face distance comparison. Both are expanded in the PDF.

## Novelty and scope

Targeted searches through 2026-08-09 found no paper stating the conjectured
equality. The source thesis and related reinforced-space paper still expose
the issue, while Lu--Yao do not discuss reinforced face weights. Novelty is
plausible, not certified.

The proof treats the axis-parallel cube and the full stated parameter range.
It does not claim the analogous result for arbitrary polyhedra.

Files:

- `solution_packet.pdf`: compiled candidate proof.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_2211.15567.pdf`: decisive extension theorem.
- `figures/open_problem_crop.png`: Conjecture 4.22 and proposed extension route.
- `main.tex`: packet source.

Ledger:
`runs/fa_banach_001/ledger/results/1302.3751_intrinsic_extrinsic_reinforced_cube_equality.json`.
