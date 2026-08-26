# Full result: the Section 5.2 defining degree is exactly six

Status: `candidate_full_solution_likely_valid` (pending expert review)

Source: J. W. Helton, I. Klep, S. McCullough, and J. Volčič,
“Noncommutative polynomials describing convex sets,” arXiv:1808.06669,
Section 5.2, physical PDF page 24.

The source constructs an explicit degree-six scalar Hermitian polynomial
`f=f_1(1-(x+x*)^2)` defining a free spectrahedron and proves that the minimum
defining degree is at least five, but leaves open whether the displayed
polynomial is minimal. This packet proves that no degree-five scalar Hermitian
defining polynomial exists. Therefore the minimum is exactly six and the
source polynomial is minimal.

The key finite reduction classifies every possible degree-four atomic factor
with the required free singularity locus. Exact minimal-realization identities
reduce the classification to rank-one matrices `M` satisfying
`tr(M adj(L))=1`. The rank-one minors have exactly four solutions. For each of
the four resulting atoms, a six-by-six coefficient system proves that no
nonzero affine-linear factor can make the product Hermitian.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: exact arXiv source PDF.
- `supporting_paper_1708.05378.pdf`: factorization theorem used in the proof.
- `figures/open_problem_crop.png`: rendered source-page evidence.
- `code/verifier.py`: exact symbolic certificate over `Q(sqrt(2))`.
- `VERIFIER_REPORT.md`: command, checked claims, and recorded verdict.

Novelty check: on 2026-08-11 the four run indexes and bounded arXiv searches
using the exact source sentence, the source title/id, author combinations, and
“minimal degree defining polynomial”/“free spectrahedron” terms found no later
paper resolving this explicit degree-five-versus-six question. This does not
guarantee priority.

Human-review recommendation: inspect the factorization-to-realization
reduction and the four-point rank-one classification. The latter is printed as
an exact Gröbner-basis certificate and is rerunnable without numerical
approximation.
