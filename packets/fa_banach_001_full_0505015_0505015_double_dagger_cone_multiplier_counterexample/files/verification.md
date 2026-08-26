# Verification report

Status: candidate_full_likely_valid

## Exact target

Baladi--Tsujii ask on PDF page 19 whether their double-dagger norm is
equivalent to the anisotropic Sobolev norm.  They already prove the latter
equivalent to the dagger norm, so the missing inequality is

    ||P(D)u||_t+||Q(D)u||_t <= C||(P(D)+Q(D))u||_t.

## Proof audit

1. The circular upper and lower cones are closed, have nonempty interiors,
   and intersect only at zero.
2. A smooth angular cutoff can be zero exactly on the upper cap, one on the
   lower cap, and strictly between zero and one elsewhere.
3. With p=s/2 and q=-s/2, the quotient
   m_R=P(R xi)/(P(R xi)+Q(R xi)) converges away from zero to the
   characteristic function of the complement of the upper cone.
4. Norm equivalence on C_c^\infty(K) rescales to the same estimate for
   P(RD),Q(RD) on functions supported in a ball of radius cR.
5. On a fixed frequency annulus, derivatives of the inverse sum symbol have
   at most R^{s(|alpha|+1)} growth.
6. Taking s small and s<beta<1 permits truncation of the inverse test at
   spatial radius R^beta with o(1) graph-norm error.  The truncated test is
   admissible in the expanding ball.
7. This produces a uniform local L^t multiplier estimate for the limiting
   cone characteristic.
8. Affine de Leeuw restriction at xi_3=1 yields a local multiplier estimate
   for the characteristic function of the exterior of a disk in R^2.
9. Fefferman's ball-multiplier theorem contradicts this for every t!=2.
10. At t=2, Plancherel gives
    ||P u||_2+||Q u||_2 <= sqrt(2)||(P+Q)u||_2, so the Hilbert endpoint is
    genuinely different.

## Source and novelty audit

The exact question crop is rendered from the official arXiv PDF.  Exact
phrases, run indexes, the parsed corpus, the published Numdam record, and
bounded primary-source searches through 11 August 2026 found no later answer
or this cone/ball-multiplier counterexample.

## Artifact audit

Compile main.tex with references resolved, inspect the log for overfull
boxes, render every page, and visually inspect all pages before promotion.

## Reviewer focus

The only non-elementary inputs are the local affine form of de Leeuw's
restriction theorem and Fefferman's local ball-multiplier obstruction.
Check the graph-norm cutoff estimate in the support-localization lemma and
the quantifier that K is arbitrary with nonempty interior.

