# Upgrade audit

The literature relation is a proper subcase, so five focused checks were made
for a possible promotion to the full source conjectures.

1. **Exact theorem matching.** Lerner's Conjectures 1.1 and 1.2 match
   Nieraeth's Conjectures 2.38 and 2.39 algebraically, but Lerner explicitly
   restricts to Banach function spaces on `R^n` and the cube maximal operator.

2. **Abstract local-median route.** A local rearrangement maximal operator can
   formally be written for another basis. The needed norm-growth/dual
   boundedness theorem, however, uses Euclidean cube decompositions and the
   sharp-function/Fefferman-Stein machinery. The source's `A_1`
   self-improvement axiom alone does not imply this theorem.

3. **Direct rescaling route for Conjecture 2.38.** Nieraeth's Theorem 2.36
   already supplies the known direction from `X_{r,s}` to `X^r`. Reversing it
   requires precisely a dual maximal-boundedness criterion. Lerner supplies
   that criterion for cubes, but no abstract analogue follows from the stated
   assumptions.

4. **`A_p`-regularity route for Conjecture 2.39.** Lerner's converse uses
   Euclidean `A_p`-regular lattices, reverse Hölder estimates for cube weights,
   and an `A_q`-regularity theorem. There is no corresponding `A_p` structure
   in the source's general measure-space/basis hypotheses.

5. **Quasi-Banach convexification route.** Lerner's first proof uses Banach
   Köthe duality, `X''=X`, and dual Fefferman-Stein estimates. Convexifying a
   quasi-Banach `X` does not preserve the exact rescaled identities needed to
   recover the full `r<1` statement. No safe reduction was found.

These failures identify real missing hypotheses rather than a clerical scope
gap. The remaining probability of obtaining the full abstract theorem from
the available ideas is minimal, so further attempts would repeat the same
missing duality mechanism.
