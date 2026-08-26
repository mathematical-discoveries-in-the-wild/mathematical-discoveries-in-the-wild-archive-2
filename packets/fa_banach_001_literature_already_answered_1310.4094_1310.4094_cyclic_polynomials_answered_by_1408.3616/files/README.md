# Cyclic polynomials on the bidisk answered by arXiv:1408.3616

Status: literature_already_answered.

Source/open-problem paper: Catherine Beneteau, Alberto A. Condori, Constanze
Liaw, Daniel Seco, and Alan A. Sola, *Cyclicity in Dirichlet-type spaces and
extremal polynomials II: functions on the bidisk*, arXiv:1310.4094.

Source question: Problem 5.2 asks for a characterization of the cyclic
polynomials in the product-weight spaces `D_alpha` on the bidisk for every
`alpha <= 1`.

Supporting answer paper: Catherine Beneteau, Greg Knese, Lukasz Kosinski,
Constanze Liaw, Daniel Seco, and Alan Sola, *Cyclic polynomials in two
variables*, arXiv:1408.3616.

Answer: complete. The later paper explicitly identifies the source question
as Problem 5.2 and says that it solves it. Its Main Theorem classifies each
irreducible polynomial `f` with no zero in the open bidisk:

- for `alpha <= 1/2`, every such `f` is cyclic;
- for `1/2 < alpha <= 1`, cyclicity holds exactly when the torus zero set is
  empty or finite, or `f` is a constant multiple of `zeta-z_1` or
  `zeta-z_2` with `zeta` on the unit circle;
- for `alpha > 1`, cyclicity holds exactly when the torus zero set is empty.

General polynomials are classified factor by factor because a polynomial is
cyclic exactly when all of its irreducible factors are cyclic. A polynomial
with a zero in the open bidisk is never cyclic.

Packet contents:

- `source_paper.pdf`: original arXiv:1310.4094 PDF.
- `supporting_paper_1408.3616.pdf`: answering arXiv:1408.3616 PDF.
- `main.tex`: compact archival LaTeX note.
- `solution_packet.pdf`: rendered and visually checked status note.
- `code/build_packet.py`: ReportLab builder for the status note.
- `tmp/rendered/`: rendered page images used for visual QA.

Scope: this is a later-literature resolution, not new run mathematics. It
settles the source's polynomial-classification Problem 5.2. It does not settle
the preceding Brown-Shields question for arbitrary outer functions.
