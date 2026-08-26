# Verification report

Verdict: `candidate_full_likely_valid`

## Version audit

The deterministic source scan used an older parsed source. The official arXiv
page was checked before promotion: arXiv:2507.17122 is now v5, revised 18 July
2026. Version 5 already adds norming-functional Birkhoff--James rectification
and replaces the older fourth question with Problem 5.11 about other types of
orthogonality. The packet uses the current v5 PDF and current Problems
5.8--5.12; it does not claim the source's Birkhoff--James result.

## Exact proof audit

1. The half-sum/half-difference maps are inverse linear maps.
2. Unit endpoints are equivalent exactly to normalized isosceles
   orthogonality; zero half-sums are allowed and encode antipodal endpoints.
3. Suprema, infima, parameter families, and arbitrary predicates transfer by
   reindexing along a genuine bijection; no continuity is needed.
4. Unit-ball transfer is surjective using two radii in `[0,1]`, including
   zero vectors by radius zero.
5. The matrix family has denominator `||A||_F^2`; for
   `A=[[tau,upsilon],[upsilon,-tau]]`, this is exactly
   `2(tau^2+upsilon^2)`, the source normalization.
6. Rectifiability is precisely surjectivity of `(x,y,beta)->(x,beta x+y)`.
   If surjectivity fails, the indicator of a missing point proves the
   necessity of the criterion.
7. Sphere rectification treats antipodal pairs as a separate boundary because
   their half-sum is zero.
8. For Pythagorean rectification, `q(t)=||z-tx||^2` is continuous and convex;
   its equal-length forward differences are nondecreasing. Secant-slope
   comparison and `q(t)/t^2 -> ||x||^2` give limits `-infinity` and
   `+infinity`, so the desired level `||x||^2` is attained.
9. Substituting `y=z-beta x` gives exactly
   `||x-y||^2=||x||^2+||y||^2` with the correct shift `beta+1`.
10. Operator transfer is direct because bounded linearity gives
    `T(u+v)=Tu+Tv` and `T(u-v)=Tu-Tv`; constraints pull back unchanged.

No computation, external lemma, or unproved dependency is used.

## Source and evidence audit

- `source_paper.pdf` is the official current arXiv v5 PDF (26 pages).
- Problems 5.8--5.12 are on printed/PDF page 22.
- `figures/open_problems_crop.png` is a 1530-by-1050 full-width readable crop
  containing all five complete problem statements and their immediate
  context.

## Novelty audit

The cheap run indexes were searched for `2507.17122`, the exact title,
isosceles orthogonality, geometric constants, matrix parameters,
rectification, and operator versions. No overlapping packet was found.

Bounded arXiv/web searches through 2026-08-17 used:

- the exact title and current problem phrases;
- `L'_YJ` with matrix, multiple-parameter, and operator terminology;
- half-sum/half-difference and unit-sphere isosceles formulations;
- universal transfer and other-orthogonality rectification phrases;
- close papers arXiv:2111.08392, 2504.00826, 2509.23319, 2602.13974,
  2606.01064, and 2606.01068.

These sources give particular geometric constants and orthogonal versions,
but no universal finite-point transfer theorem, arbitrary coefficient-matrix
family, necessary-and-sufficient rectifiability criterion, or Pythagorean
rectification result was found. Novelty is plausible, not certified.

## Interpretation limitation

The problems do not define “equivalently expressed,” “kinds,” or what counts
as a satisfactory operator characterization. The packet formalizes these as
exact domain reparameterizations with auxiliary scalar variables. Under that
literal reading the result is complete. Under any unstated requirement of
formula simplicity or naturality, it should instead be read as a complete
structural baseline and a substantial partial answer.

## Render audit

`latexmk` completed without undefined references, overfull/underfull boxes, or
LaTeX warnings. The resulting `solution_packet.pdf` has six pages. All pages
were rendered at 130 dpi to `tmp/qa-page-01.png` through
`tmp/qa-page-06.png` and visually inspected: the source crop, formulas,
theorem statements, proofs, page numbers, and bibliography are readable and
unclipped.

## Human-review recommendation

Review the interpretation boundary first. Mathematically, check the antipodal
boundary, the indicator-function necessity argument, and the two secant-slope
limits in the Pythagorean lemma. If those pass and a specialist search finds
no prior formulation, promote as a full structural answer.
