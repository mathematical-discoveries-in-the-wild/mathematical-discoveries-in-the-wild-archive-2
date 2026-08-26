# Verification report

Status checked: candidate substantial partial result, likely valid.

## Mathematical audit

1. The maximum identity is quoted from the source paper and applies at every
   finite spatial argument. The necessity proof does not assume separate
   continuity: it derives the northeast limit from output continuity, uses
   the given left continuity for the southwest limit, and then applies a
   monotone rectangular squeeze to arbitrary approaches.
2. Boundary continuity was audited separately. If either coordinate tends
   to zero, `T(u,v) <= min(u,v)` applies. At a coordinate equal to one, only
   a left approach is possible in that coordinate, which is covered by left
   continuity and the same squeeze.
3. In the ordinal-sum witness, every pair with `r+s<3` was split into the
   cases: both spatial points in `[1,2]`; one below 1; or one above 2. The
   first case lies below the nilpotent threshold and gives `a`; every other
   case gives at most `a`. Thus the supremum at 3 is exactly `a`.
4. For `x>3`, choosing equal points just above `3/2` makes the normalized
   component coordinates sum to more than one and yields values approaching
   `a+(b-a)/2`. This proves a genuine right jump, including endpoint cases
   `a=0` and `b=1`.
5. The additive-generator transport is an exact change of variables, not an
   approximation: `L(r,s)<x` is equivalent to
   `phi(r)+phi(s)<phi(x)`.

## Source and visual checks

- The source crop is taken from the official arXiv PDF, printed page 15, and
  includes Theorem 4.6 and the complete open Remark 4.7.
- The final packet was compiled from `main.tex`, all pages were rasterized,
  and every rendered page was visually inspected for clipping, overflow,
  missing glyphs, and unreadable source evidence.

## Novelty audit

Cheap run indexes and bounded literature searches through 2026-08-17 used
the arXiv id, exact title, exact open-remark wording, and core combinations
of t-norm continuity, maximum t-conorm, continuous d.d.f.s, and tensor
products. They found the final journal publication but no later proof or
counterexample addressing Remark 4.7. The source already records the
pointwise maximum formula; the exact continuity corollary and the explicit
ordinal-sum obstruction were not located. Novelty remains a candidate claim
until specialist review.

## Human review priorities

- Confirm the standard ordinal-sum convention used in Theorem 2, especially
  that outside a common component the t-norm equals the minimum.
- Check that the source's topology at infinity agrees with the continuity
  argument in Theorem 1.
- Re-run a specialist literature search for results after the 2026 journal
  publication.
