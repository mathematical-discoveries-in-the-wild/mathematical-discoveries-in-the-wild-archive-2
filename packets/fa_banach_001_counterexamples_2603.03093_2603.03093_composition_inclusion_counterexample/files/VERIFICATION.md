# Verification Report

Verdict: `counterexample_likely_valid`.

Scope: Problem 3.11 is answered negatively as stated. The packet additionally
proves the requested boundedness for every non-extreme symbol `b`, and proves
contractivity for arbitrary `b` when `psi(0)=0`. It does not characterize all
extreme symbols for which the inclusion holds, and it does not fully answer
Problems 3.10 or 3.12.

## Proof Audit

### 1. Counterexample hypotheses

Passed. `b(z)=z` belongs to the closed unit ball of `H^infinity`, and
`psi_a(z)=(a-z)/(1-conjugate(a)z)` is an analytic disk automorphism for every
`0<|a|<1`.

### 2. Rank-one kernel calculation

Passed. For `b(z)=z`,

```text
K_b(z,w) = (1-conjugate(w)z)/(1-conjugate(w)z) = 1,
```

so `H(b)=span{1}`. The disk-automorphism identity gives

```text
K_psi(z,w)
 = (1-|a|^2)/((1-conjugate(a)z)(1-a conjugate(w)))
 = h_a(z) conjugate(h_a(w)).
```

Thus `H(psi)=span{h_a}`. Since `a` is nonzero, `h_a` is nonconstant and the
constant one is not in that one-dimensional space. But `C_psi 1=1`.

### 3. Zero-at-zero positive theorem

Passed. The standard RKHS adjoint calculation says that `C_psi` is a
contraction exactly when

```text
K_(b composed with psi)(z,w) - K_b(psi(z),psi(w))
```

is positive. The first kernel factors as `K_b(psi(z),psi(w)) K_psi(z,w)`.
If `psi(0)=0`, Schwarz's lemma gives `psi(z)=zq(z)` with `q` Schur, and

```text
K_psi(z,w)-1 = z conjugate(w) K_q(z,w),
```

a positive kernel. The Schur product theorem completes the check.

### 4. Non-extreme positive theorem

Passed. Normalize `alpha=psi(0)` with the involutive automorphism `phi_alpha`
and put `u=phi_alpha composed with psi`. Then `u(0)=0`. The automorphism kernel
identity makes weighted composition

```text
f -> h_alpha (f composed with phi_alpha)
```

unitary from `H(b)` to `H(b composed with phi_alpha)`. For non-extreme `b`,
the transformed symbol is non-extreme and its forward shift is bounded.
Multiplication by `1/h_alpha`, a constant multiple of
`1-conjugate(alpha)z`, is therefore bounded. Hence unweighted composition by
`phi_alpha` is bounded, and composition with the contractive `C_u` proves the
claim.

### 5. Literature and source audit

Passed within bounded scope. Cheap run indexes and exact/nearby web searches
found no duplicate answer. The related arXiv papers returned by search concern
composition on a fixed non-inner rational `H(b)` or maps from `H(b)` to Hardy
space, not the operator from `H(b)` to `H(b composed with psi)`.

The source paper was rebuilt from the locally cached arXiv v1 TeX and BibTeX.
PDF page 13 was rendered at 180 dpi, and the full-width crop contains Problem
3.11 in full with its surrounding generality.

### 6. Render audit

Passed. The final four-page packet compiled with resolved references and no
overfull boxes or duplicate anchors. Every page was rendered and inspected at
high resolution. The theorem, kernel identities, source crop, and bibliography
have no clipping, overlap, broken glyphs, or unreadably scaled text.

## Recommended Human Checks

1. Recheck the direction of the RKHS kernel domination criterion.
2. Confirm that non-extremality is preserved under precomposition by a disk
   automorphism.
3. Confirm the standard equivalence used from the source paper: the forward
   shift is bounded on `H(b)` when `b` is non-extreme.
