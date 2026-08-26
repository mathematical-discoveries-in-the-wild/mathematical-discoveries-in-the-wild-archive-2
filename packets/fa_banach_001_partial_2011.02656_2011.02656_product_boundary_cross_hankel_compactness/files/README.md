# Continuous-symbol Hankel compactness on product domains

Status: candidate substantial partial theorem, likely valid, human review
required.

Source: Mehmet Celik, Sonmez Sahutoglu, and Emil J. Straube, “A Sufficient
condition for compactness of Hankel operators,” arXiv:2011.02656.

Remark 2 asks whether the paper's compactness theorem remains true for
symbols merely continuous on the closed convex domain.  This packet gives an
affirmative answer for every form level on a product of two bounded strictly
convex domains.  It also gives an affirmative `q=0` result on arbitrary
finite products of bounded convex domains.

The main new tool is a boundary-cross extension lemma.  A continuous
function on `cl D x cl G` that is holomorphic on both families of side faces
is the boundary trace of a function in `A(D x G)`.  On two strictly convex
factors, every positive-dimensional boundary variety is contained in a side
face, so the source hypothesis reduces to zero, one, or two constrained side
families according to their dimensions.  In each case the symbol is a
uniform limit of `C^1` symbols satisfying the source theorem.  The estimate

`||H_phi^q-H_psi^q|| <= ||phi-psi||_infinity`

then passes compactness to the continuous symbol.

Files:

- `solution_packet.pdf` — review-ready theorem and proof
- `main.tex` — packet source
- `source_paper.pdf` — source paper reconstructed from the run's ingested
  official arXiv TeX (external PDF retrieval was unavailable)
- `figures/open_problem_crop.png` — Theorem 1 and Remark 2 from source page 2
- `code/crop_open_problem.py` — reproducible crop script
- `verification_report.md` — proof and artifact checks

Human review should focus on the classification of boundary varieties in a
product of strictly convex factors and on the one-sided vector-valued
approximation lemma.  The packet does not claim to settle Remark 2 for an
arbitrary bounded convex domain.

