# arXiv:1611.02540 — cardinality-only Gabor NERF conjecture fails

Status: `literature_implied_answer` (full counterexample to Conjecture 5.1 as
written).

For the allowed Gabor frame with index set
`Lambda_M = {0} x Z_M`, the least squared singular value is exactly
`M min_j |g(j)|^2`. If `g` is uniform on the complex unit sphere, then

`P(M min_j |g(j)|^2 >= c) = (1-c)^(M-1)`

for `0 < c < 1`. Thus the lower frame bound converges to zero in probability,
while the conjectured scale `|Lambda_M|/M` equals one. The packet also proves
the same collapse for every fixed number of consecutive translations.

The decisive frame-bound identity is Proposition 4.1 of Salanevich--Strachan,
arXiv:2509.01325. The relationship to the 2019 conjecture is not made explicit
there, so this is recorded in the literature-implied provenance bucket.

Files:

- `solution_packet.pdf`: compact counterexample-status note and proof.
- `main.tex`: note source.
- `source_paper.pdf`: official arXiv:1611.02540 PDF.
- `supporting_paper_2509.01325.pdf`: official arXiv PDF containing the exact frame-bound formula.
