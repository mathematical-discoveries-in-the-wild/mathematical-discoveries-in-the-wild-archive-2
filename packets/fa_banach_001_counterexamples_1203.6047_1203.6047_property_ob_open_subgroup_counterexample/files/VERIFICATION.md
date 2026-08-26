# Verification Report

Verdict: `counterexample_likely_valid`

Verifier model: `GPT5.6`

Date: 2026-08-11

## Claim audited

The Polish group `G = Z^N semidirect S_infinity`, with the product and
pointwise-convergence topologies, has property (OB), while its open subgroup
`H = Z^N semidirect Stab(0)` does not.

## Audit

1. **Topology.** `Z^N` and `S_infinity` are Polish. Coordinate permutation is
   a continuous action: a condition on finitely many output coordinates is
   controlled by fixing finitely many indices and restricting finitely many
   input coordinates. Hence the semidirect product is Polish.

2. **Neighbourhood basis.** For finite `A`, the set `U_A` of pairs whose base
   component vanishes on `A` and whose permutation component fixes `A`
   pointwise is a subgroup. The permutation condition preserves vanishing on
   `A`. Enlarging the finitely many coordinates occurring in a basic product
   neighbourhood shows that some `U_A` lies in every identity neighbourhood.

3. **Finite double cosets.** For `P_A = Stab(A)` pointwise, the double coset
   `P_A p P_A` is determined by the partial injection
   `a -> p(a)` on those `a in A` for which `p(a) in A`. Conversely, if two
   permutations induce the same partial injection, a left multiplier in
   `P_A` makes them agree on `A`, after which their quotient is a right
   multiplier in `P_A`. There are finitely many partial injections of a finite
   set, so a finite representative set `E` exists.

4. **Base factorization.** Let `tau` swap `A` with a disjoint equally sized
   block. Split `a` into the part `x` vanishing on `A` and the part supported
   on `A`. Moving the latter to the disjoint block gives `y` vanishing on `A`
   and

   ```text
   (a,1) = (x,1)(0,tau)(y,1)(0,tau).
   ```

   This follows directly from the semidirect-product law and `tau^2=1`.

5. **Global bounded width.** Writing `p = u e v` with `u,v in P_A` and
   `e in E`, every `(a,p)` lies in

   ```text
   U_A tau U_A tau U_A E U_A.
   ```

   With `F={1,tau} union E`, this is contained in `(F U_A)^4`. For nonempty
   symmetric open `V`, choose `U_A` inside `V^2`; after adjoining `1` to `F`,
   `(F V^2)^4` is contained in `(F' V)^8`. This matches exactly the
   bounded-width criterion cited from Rosendal's Theorem 1.11.

6. **Failure in the open subgroup.** `H` is open because `Stab(0)` is open.
   Under the law `(a,p)(b,q)=(a+p.b,pq)`, the zeroth coordinate of `p.b` is
   `b_0` whenever `p` fixes `0`. Hence `(a,p) -> a_0` is a continuous
   surjective homomorphism `H -> Z`. Its absolute value is an unbounded
   continuous length function, so Rosendal's equivalent criterion shows that
   `H` fails property (OB).

## Remaining review risk

No mathematical gap was found. The main non-proof risk is novelty: the bounded
search did not find a prior answer, but it was not a complete citation search.

