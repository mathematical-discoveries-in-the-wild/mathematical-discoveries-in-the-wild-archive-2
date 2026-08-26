# Verification report

## Mathematical audit

- The marginal maps have no fixed points, so every joint coupling row has
  exactly the stated parameterization by `s_xy in [0,1]`.
- The mixed-difference matrix has no zero entries.  Its sign pattern is exactly
  the displayed policy, proving uniqueness of the pointwise minimizer.
- Finite discrete-state generators are bounded Feller generators, and the cost
  belongs to every generator domain.
- The competitor changes only `s_22` and preserves both marginal generators.
- Uniformization uses rate two, which dominates every joint exit rate.
- The six-state recurrence proves the entire infinite sequence of cost-iterate
  differences, not merely a numerical approximation.
- The resulting exact gap is positive because `exp(2)>5`.

## Independent executable checks

`code/verify_counterexample.py` uses only integer arithmetic for the structural
claims.  It:

- recomputes the nine mixed differences;
- enumerates all 512 extreme coupling policies and checks pointwise domination;
- checks 25 uniformized iterates, including the stable exact recurrence;
- reports the positive decimal value only as a convenience.

Recommended status: `full_counterexample_likely_valid`; human review requested.

## Packet verification

- Final PDF: 3 A4 pages, 255590 bytes.
- Final PDF SHA-256:
  `fca33e42ff4f957d2c0cdfa25214b55b8d2060a6091c5414755b0b98f906d62b`.
- Source-paper PDF SHA-256:
  `c46b46fce6fc08c5552c56e70ce5c70864837c0bf25570d6d45b66521fa8daf9`.
- All three rendered packet pages were visually inspected at original
  resolution.  No clipping, overlap, overflow, or unreadable formulas were
  found.

