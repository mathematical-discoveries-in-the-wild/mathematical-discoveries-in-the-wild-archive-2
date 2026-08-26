# Verifier report

## Computational scope

`code/verify_finite_phase_space_span.py` checks the finite analogue of the two
central proof lemmas for:

```text
Z/2, Z/3, Z/4, Z/5, Z/6,
Z/2 x Z/2, Z/2 x Z/3, and (Z/2)^3.
```

For each group it:

1. enumerates every subgroup `H`;
2. computes `H^perp` and every rectangle `H x H^perp`;
3. checks that these rectangles cover exactly
   `N={(g,chi):chi(g)=1}`;
4. constructs all local characters
   `1_H(u)1_Hperp(eta) eta(a) conjugate(alpha(u))`;
5. verifies that their complex matrix rank is exactly `|N|`.

All checks pass.  Exact output is in `code/verification_output.txt`.

## Mathematical audit

- For fixed `u`, the fiber of `N` is the annihilator of the cyclic closure of
  `u`; it has positive Haar measure iff that closure is compact.
- Tonelli can be applied because second-countable LCA groups are sigma-compact
  and their Haar measures are sigma-finite.
- If `C=closure(<u>)` and `D=closure(<chi>)` are compact, then for a fixed
  compact open `K0`, `K=K0 intersect D^perp` is compact open and
  `H=C+K` is compact open.  The condition `chi(u)=1` implies `H subset ker chi`.
- The restriction/evaluation identifications
  `dual(H)=Ghat/H^perp` and `dual(H^perp)=G/H` show that no local Fourier mode
  is omitted.
- Symmetrization of a complex linear approximation by self-adjoint pure
  projectors takes real parts of coefficients and does not increase the
  approximation error.

## Limitation

The finite calculations are consistency checks, not the general proof.  The
complete Haar-measure and Pontryagin-duality proof is in the PDF packet.
