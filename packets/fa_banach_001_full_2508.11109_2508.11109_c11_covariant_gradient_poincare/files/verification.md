# Verification report

Status: `candidate_full_result_likely_valid_needs_human_review`

## Mathematical audit

### 1. Gauss-map measure argument

- A compact connected embedded `C^{1,1}` hypersurface is the boundary of its
  bounded complementary component and has a Lipschitz outward normal `nu`.
- For each `omega in S^d`, a maximizer of `x dot omega` is a support point
  whose outward normal is `omega`; hence `nu` is onto.
- The Lipschitz area formula gives
  `int_Gamma J_Gamma nu = int_{S^d} N(nu,omega) >= H^d(S^d)`.
- At a.e. differentiability point, `J_Gamma nu=|det B|`. Thus the set where
  the shape operator is invertible has positive measure.

This replaces the source proof's use of continuity of `B` and a nonempty open
elliptic set.

### 2. Regularity of a weakly parallel field

For a tangential field with `nabla_Gamma v=0`, weak differentiation of
`v dot nu=0` gives in each chart

```text
partial_i v = -(v dot partial_i nu) nu = A_i v,
```

with `A_i in L^infinity`. Sobolev embedding followed by this equation
iterates the exponent until `v` is bounded; the equation then gives
`v in W^{1,infinity}`. It also gives `partial_i |v|^2=0`, so connectedness
makes `|v|` constant.

### 3. Weak curvature compatibility

In a `C^{1,1}` chart, the metric is `W^{1,infinity}`, Christoffel matrices
are `L^infinity`, and the coordinate vector `V` is `W^{1,infinity}`. The
parallel system `partial_i V+Gamma_i V=0` may therefore be commuted in
distributions. The curvature distribution kills `V`.

For a `W^{2,infinity}` immersion, direct expansion of the coordinate
curvature formula is legitimate: distributional third derivatives cancel by
commutation of mixed partials, leaving the `L^infinity` Gauss tensor
`h*h-h*h`. Thus the compatibility is an a.e. algebraic identity. At a point
where `B e_i=kappa_i e_i` and every `kappa_i` is nonzero, it reads

```text
0 = kappa_i kappa_j (v_j e_i-v_i e_j),  i!=j.
```

Because `d>=2`, every component vanishes. The positive-measure elliptic set
and constant length then imply `v=0` globally.

### 4. Poincare estimate

The identity

```text
nabla_M v = nabla_Gamma v - nu v^T B
```

with `B in L^infinity` gives the estimate with an extra `L^p` term. If the
extra term could not be removed, a normalized violating sequence would
converge strongly in `L^p` by Rellich compactness. Its weak `W^{1,p}` limit
would be parallel and hence zero, contradicting the extra-term estimate.

### 5. Sharp assumption check

- `d>=2` is necessary: the unit tangent of a closed curve is a nonzero
  parallel field.
- Embeddedness and compactness are used to make the Gauss map onto.
- Codimension one identifies its Jacobian with `|det B|`.
- Connectedness turns zero weak gradient of `|v|` into one global constant.

No computation or unproved numerical assertion enters the result.

## Upgrade-attempt audit

Seven materially distinct passes are recorded in
`attempts/2508.11109_c11_covariant_gradient_injectivity.md`:

1. exact transplantation of the source proof and identification of its
   continuity obstruction;
2. the Lipschitz Gauss-map area-formula replacement;
3. finite Sobolev bootstrapping of weakly parallel fields;
4. the low-regularity curvature commutator and Gauss identity;
5. the compactness proof of the quantitative estimate;
6. downstream weak Bochner/Stokes regularity audit;
7. bounded novelty and failure-mode audit.

The strongest route closes the exact question fully; no further partial-to-
full upgrade is needed.

## Literature audit

- The four cheap run indexes had no row for arXiv:2508.11109 or this
  `C^{1,1}` covariant-gradient theorem.
- The current arXiv record is v3, dated 2026-03-04, and says v3 is a metadata
  update with no content change. The open sentence remains in the source.
- Bounded exact-id, exact-phrase, covariant-gradient, weak-parallel-field,
  weak-Gauss-equation, and Lipschitz-Gauss-map searches through 2026-08-11
  found no resolution of the exact question.
- The ingredients are classical and the observation could be implicit in
  low-regularity submanifold geometry. The packet makes no priority claim.

## Scope audit

The packet proves injectivity and the full `W^{1,p}` Poincare estimate, and
derives weak `L^2` Bochner--Laplace well-posedness. It explains why the
source's weak all-`p` Bochner proof propagates. It does not claim new
higher-order estimates and does not repackage every downstream Stokes,
Oseen, or Navier--Stokes theorem.

## Rendering audit

- Final PDF: four US-Letter pages, 354055 bytes.
- `latexmk` completed after all cross-reference passes.
- The final log contains no warnings, undefined references, overfull boxes,
  or underfull boxes.
- All four pages were rasterized at 130 dpi and visually inspected. The
  status box, source crop, theorem, displayed equations, page transitions,
  proof-ending symbols, references, and margins are clean and legible.
- `solution_packet.pdf` and `tmp/main.pdf` are byte-identical.
- Final SHA-256:
  `d66ce6fc82c9cd98345ced42efdf44e3d5a8b74e003378323568252e1fabaca6`.

## Human-review focus

Independently check the distributional product convention in the commuted
parallel system and the coordinate derivation of the weak Gauss identity.
Then check the support-point orientation in the Gauss-map surjectivity proof.
Those are the only nonroutine low-regularity steps.
