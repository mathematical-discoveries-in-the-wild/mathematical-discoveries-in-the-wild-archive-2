# Verification report

Status: `candidate_substantial_partial_result_likely_valid_needs_human_review`

## Mathematical audit

1. Write each closed plank as
   `P_i={y:a_i<=<u_i,y><=b_i}` with `||u_i||=1`.
2. If a point `x` of the closed unit ball is outside every plank, sphere
   coverage forces `||x||<1`.
3. For every plank choose the outer strict halfspace containing `x`. This
   yields signed normals `v_i in {u_i,-u_i}`, constants `c_i`, and an open
   sign cell `C={<v_i,y>>c_i for every i}` containing `x` and avoiding all
   planks.
4. If the normals have proper span, any nonzero common-kernel vector `v`
   gives the ray `x+tv` inside `C`.
5. If `N<=d` and the normals have full span, then `N=d` and the row system
   `<v_i,v>=1` has a unique solution. Again `x+tv` remains in `C` for every
   `t>=0`.
6. The ray norm begins below `1` and tends to infinity, so continuity gives a
   point of `C` on the unit sphere, contradicting coverage.
7. Therefore the planks cover the whole unit ball. Bang's plank theorem gives
   total Euclidean width at least the ball's minimal width, namely `2`.

The proof uses no limiting argument and no computation. Because every cell
inequality is strict and is constant or strictly increasing along the chosen
ray, closed-plank boundary points introduce no gap.

## Upgrade-attempt audit

- The first attempt established the `N<=d` result.
- A second, distinct pass observed that cardinality is unnecessary whenever
  the normal span is proper, giving the stronger second hypothesis.
- A third pass examined `N=d+1`. The complement sign cell can then be a
  bounded simplex because the selected signed normals may positively span
  `R^d`. Applying Bang to a ball with this cell removed, or summing simplex
  altitudes, does not compare cleanly with the original plank widths: the
  opposite plank boundaries meet different adjacent cells. This is the first
  genuine obstruction and leaves no credible short upgrade to the full
  conjecture.

## Literature audit

- The four cheap run indexes contained no row for arXiv:2211.10886 or the
  theorem proved here.
- The original conjecture source arXiv:2112.05382 records the `d=3` case and,
  for `d>=4`, only a reduction for at most three planks.
- Verreault's 2026 survey, arXiv:2203.05540v2 and DOI
  `10.1112/blms.70230`, still records the spherical-plank conjecture as open
  and the `S^3` at-most-three-plank case as known.
- Exact-phrase, boundary-covering, four-plank, cardinality, title, DOI, and
  citing-work searches through 2026-08-11 found no `N<=d` theorem or
  proper-normal-span extension.
- Novelty confidence is moderate. The result is an elementary polyhedral
  observation and could be folklore; no priority claim is made.

## Scope audit

The packet does not claim the full conjecture, does not address covers by
`N>=d+1` full-rank plank families, and does not decide either polynomial-plank
conjecture in the source. Any counterexample to the spherical-plank conjecture
must have at least `d+1` planks with normals spanning `R^d`.

## Rendering audit

The final packet is a three-page US-Letter PDF of 233871 bytes. The final
`latexmk` log has no warnings, undefined references, overfull boxes, or
underfull boxes. All three pages were rasterized at 150 dpi with Poppler and
inspected individually; the source crop, theorem statement, proof, equations,
proof-ending symbols, references, margins, and page breaks are clean and
legible. The final packet and `tmp/main.pdf` are byte-identical, with SHA-256
`e8060e28254cdf01f53478e7df353262e5bebc6a4f6b0f24a067042273f162bc`.
