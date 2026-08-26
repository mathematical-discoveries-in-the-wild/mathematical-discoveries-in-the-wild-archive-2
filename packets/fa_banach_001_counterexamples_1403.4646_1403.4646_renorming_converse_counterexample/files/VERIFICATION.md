# Verification report

Verified: 2026-08-12 (Europe/Madrid)

## Mathematical checks

- For an arbitrary norm `q`, directly computed the two limsup functions from
  the periodic value sets `{-u,u}` and `{-u,0,u}`.
- Checked the midpoint inequality
  `2 q(z) <= q(z-u)+q(z+u)`, which makes the added `q(z)` term redundant.
- Checked the common radius: `q(u)` is attained at zero, and
  `2 q(u) <= q(z-u)+q(z+u)` is the matching lower bound.
- Checked the common center formula as the intersection of the two radius
  `q(u)` balls centered at `u` and `-u`.
- Every tail of each periodic sequence contains its full finite value set.
  The pseudodistance therefore equals the Hausdorff distance between the two
  sets, which is exactly `||u||` in the original norm.
- Independently checked the convex-hull upgrade using convexity of the norm:
  the supremum of distance over a finite set equals the supremum over its
  convex hull.

## PDF checks

- `latexmk` completed with no unresolved references, warnings, overfull boxes,
  or underfull boxes in the final log.
- `solution_packet.pdf` has 3 A4 pages.
- Rendered and inspected all three pages at 140 dpi. The conjecture crop,
  formulas, proofs, page breaks, and bibliography are legible and unclipped.
- `source_paper.pdf` is the official 13-page arXiv PDF; Conjecture 3.3 appears
  on printed page 8.

SHA-256:

```text
2c917286ed1c6ba72d18b9f4dcfa292f93796bfff9744cbc89a52df5fdb27c53  solution_packet.pdf
994e0a8f54a07ac560f53a2aa785a2ff6e9f833b6deab9ee0065c11a34b9ffad  source_paper.pdf
```

