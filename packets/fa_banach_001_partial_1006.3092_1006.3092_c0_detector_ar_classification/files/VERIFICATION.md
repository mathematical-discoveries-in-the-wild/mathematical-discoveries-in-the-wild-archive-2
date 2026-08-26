# Verification report

Verdict: `candidate_partial_result_likely_valid`

## Proof checks

1. A complete metric AR has a closed Kuratowski embedding in a Banach space;
   the AR property supplies a global retraction. A locally finite
   star-refinement and barycentric map produce a controlled homotopy and a map
   whose image is locally relatively compact.
2. A bounded non-totally-bounded subset of `c0` fails uniform tail decay. This
   gives markers `u_r` and increasing coordinates `q_r` with a large diagonal
   coordinate and small later-coordinate/earlier-marker interactions.
3. The increasing tail-control cover admits a shrinking and partition of unity
   with only two adjacent weights at any point.
4. The marker comparison was independently divided into five exhaustive cases
   after ordering the two upper ranks. Each lower bound is strictly greater
   than `delta^3/20` for `0 < delta <= 1`.
5. Continuity of `T` turns uniform `c0` separation into metric separation.
   Banakh–Cauty's SAP-to-LFAP lemma and their quoted Banakh–Zarichnyy criterion
   then imply Hilbert topology.
6. For the envelope corollary, Josefson–Nissenzweig provides the weak-star-null
   norm-one functionals. The supremum of a linear functional on the closed
   convex hull of `J(B_X)` equals its supremum on `J(B_X)`, proving the detector
   is noncompact.
7. A finite-dimensional envelope is the image of `X`, has a continuous linear
   section, and splits. Complementation lets every functional on the kernel
   extend to `X`, so that kernel has trivial dual/envelope.

## Upgrade attempts

Five distinct attempts are documented in `main.tex`: AR replacement of local
convexity; abstract detector lemma; infinite-dimensional envelope corollary;
finite-dimensional envelope splitting; and nonlinear/metric detector routes.
The last route meets a structural obstruction: all linear Banach-valued maps
factor through the Banach envelope, so no refinement of the linear marker
method can reach the trivial-envelope case.

## Novelty bounds

On 2026-08-17, exact source-question phrases and combinations of
`noncompact linear operator`, `c0`, `SAP`, `LFAP`, `linear metric AR`, `Banach
envelope`, `quasi-Banach`, and `Hilbert homeomorphic` were searched. The arXiv
record, official journal text, and small citation neighbourhood were checked.
No later full solution and no statement of the detector/envelope criterion was
found. This is a bounded search, not proof of novelty.

## Artifact checks

- Source crop rendered from page 8 of the official source PDF at 180 dpi.
- Packet compiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final PDF rendered at 144 dpi and every page visually inspected.
