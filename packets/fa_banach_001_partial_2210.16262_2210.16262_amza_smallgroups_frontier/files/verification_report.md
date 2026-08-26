# Verification report

Status: `candidate_partial_computational_likely_valid`

## Mathematical and completeness checks

- Source Questions 6.2--6.4 were checked on arXiv PDF page 16.
- The implemented formula is the source character-table formula for `AMZA`.
- Abelian quotient/derived cases are safe to skip because `AMZA=1` there and
  every amenability constant is at least 1.
- For solvable groups, Hall conjugacy makes one Hall subgroup per prime subset
  exhaustive for the normal-Hall question; nonsolvable groups use all normal
  subgroups.
- `ass(G)` is precisely the nonnegative diagonal part of the full double sum,
  hence `ass(G) <= AMZA(G)` and is a safe equality-case filter.
- SmallGroups coverage was checked by the program for every tested order.
- Every group of order 256 is nilpotent, so omitting that order from the
  nonnilpotent `7/4` scan is safe.

## Computational checks

- Runtime: GAP 4.15.1; SmallGrp 1.5.4.
- Known/source benchmark values reproduced exactly:
  `7/3, 7/4, 511/72, 83/32, 497/32, 1727/128`.
- Normal Hall scan: 7,747 relevant nonabelian quotient cases; no violation.
- Sharp-value scan: 6,892 nonnilpotent groups, 186 full `AMZA` evaluations
  after the exact minorant filter; no equality.
- Derived scan: 976 nonabelian derived subgroups; no violation.
- Order 256 independently completed: 56,092 groups enumerated, 410 relevant
  derived cases, no violation.
- All comparisons were made before decimal conversion.

## Scope and novelty checks

- This proves only the finite range `|G| <= 383`.
- Exact-phrase web searches and cheap run-index searches found the source but
  no later claimed answer to Questions 6.2--6.4.
- The literature check was bounded, so novelty confidence is moderate.
- Human reproduction and expert review are required.

## Rendering checks

- Compiled with two LaTeX passes; all references and citations are resolved.
- The final log contains no overfull boxes, underfull boxes, undefined
  references, or warnings.
- All three rendered pages were inspected at original resolution.
- No clipping, overlap, malformed mathematics, illegible text, or bad page
  break was found.
