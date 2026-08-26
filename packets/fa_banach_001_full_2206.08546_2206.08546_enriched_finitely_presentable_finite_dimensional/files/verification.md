# Verification record

## Target match

- Source: Jiří Rosický, arXiv:2206.08546v3, Remark 3.3, page 8.
- Published DOI: 10.1080/00927872.2023.2228412.
- Exact question: whether enriched finitely presentable Banach spaces must be
  finite-dimensional.
- Source positive direction: finite-dimensional Banach spaces are enriched
  finitely presentable (Theorem 3.1).
- Packet result: the converse, plus a single fixed shift diagram detecting
  every infinite-dimensional space.

The packet contains the 27-page source PDF and a 170-dpi render of page 8.

## Proof audit: the Banach colimit

Let S:c0->c0 be the left shift and consider the chain with every connecting
map equal to S.

1. The zero maps form a cocone.
2. Any cocone u_n:c0->E satisfies u_n=u_(n+m) S^m.
3. For each z in c0, norm(u_n z) <= norm(S^m z) -> 0.
4. Hence every u_n is zero and the zero cocone is universal.
5. Therefore the colimit in Ban is exactly the zero space.

This verifies the colimit by its universal property, independently of any
quoted colimit formula.

## Proof audit: the Josefson--Nissenzweig witness

For infinite-dimensional A, the classical theorem supplies phi_r in A* with
norm(phi_r)=1 and phi_r(x)->0 for every x.

1. Jx=(phi_r(x)) belongs to c0 for every x.
2. J:A->c0 is linear and norm(J)=sup_r norm(phi_r)=1, so it is a morphism of
   Ban.
3. S^m Jx is the tail (phi_(m+1)(x),...).
4. Interchanging the two suprema gives
   norm(S^m J)=sup_(r>m) norm(phi_r)=1.
5. This works over both real and complex scalars.

The supporting PDF includes a readable statement of the classical theorem.

## Proof audit: enriched comparison

1. In a directed colimit of metric spaces, the distance between two
   same-stage representatives is the infimum of their later-stage distances,
   followed by zero-distance quotient and completion.
2. The represented shift chain has stage-zero elements J and 0.
3. Their colimit distance is inf_m norm(S^m J)=1.
4. Thus they remain distinct through both the zero-distance quotient and
   completion.
5. But Ban(A,colim D)=Ban(A,0) is a singleton.
6. Therefore the comparison map is not an isomorphism in CMet, so an
   infinite-dimensional A is not enriched finitely presentable.
7. Combining this with source Theorem 3.1 gives the exact classification.

## Stronger fixed-diagram check

The diagram is independent of A. For finite-dimensional A, compactness of the
unit ball and Dini's theorem give norm(S^m T)->0 for every bounded T:A->c0.
For infinite-dimensional A, the JN operator has every tail norm equal to one.
This confirms that the shift chain is an exact finite-dimensionality detector
rather than an ad hoc counterdiagram.

## Route audit

Eight routes or failure modes were checked:

1. Josefson--Nissenzweig plus the c0 shift — full success.
2. Scalar contraction chains — fail because represented norms decay too.
3. Schauder-basis tail projections — work only for spaces with a basis.
4. Basic-sequence localization — extension control is noncanonical.
5. Increasing quotient chains — do not sequentially exhaust arbitrary
   nonseparable spaces.
6. Direct universal-property check of the zero colimit — succeeds.
7. Exact CMet pseudometric and completion audit — succeeds.
8. Real/complex scalar audit — succeeds.

## Novelty audit

- The four lightweight run indexes were searched for the arXiv id, exact
  title, Remark 3.3 wording, enriched finite presentability,
  Josefson--Nissenzweig, and the c0 shift. No duplicate was found.
- Crossref identifies the journal DOI and reports two citing works.
- OpenAlex likewise reports exactly two citing works as of 2026-08-11:
  Alexandru Chirvasitu, Semisimplicity manifesting as categorical smallness,
  and Rosický--Tendas, Notions of enriched purity.
- Both citing PDFs were downloaded and full-text searched. The former gives
  an alternative proof of the already-known finite-dimensional positive
  direction. The latter concerns enriched purity. Neither answers the
  converse, cites Josefson--Nissenzweig in this context, or uses a shift
  obstruction.
- Bounded arXiv/web queries for the exact question and for the combination of
  enriched finite presentability with Josefson--Nissenzweig found no direct
  answer.

The search is bounded, not exhaustive. Novelty confidence is moderate-high.

## Artifact audit

- Source PDF: 27 pages, metadata checked with pdfinfo.
- Supporting JN PDF: 14 pages, metadata checked with pdfinfo.
- Both embedded figures are genuine PDF renders and were visually inspected.
- Main LaTeX cites the source, the classical theorem, a modern theorem
  statement, and both later citing papers.
- Final packet is compiled repeatedly with temporary files confined to tmp/,
  all pages are rendered and visually inspected, and the log is checked for
  warnings and layout overflow.
- No computational verifier is appropriate; the result is exact and
  categorical/functional-analytic.

Recommendation: verify the three-line universal-property proof, the tail
norm identity, and the standard metric-colimit formula. If accepted, promote
as a full answer with the fixed-diagram strengthening.
