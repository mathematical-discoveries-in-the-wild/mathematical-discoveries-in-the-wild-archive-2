# Endpoint L1 multilinear Fourier–Schur transference

Status: **candidate full affirmative answer, likely valid, pending specialist review**.

This packet answers Remark 3.3 of Caspers–Krishnaswamy-Usha–Vos,
*Multilinear transference of Fourier and Schur multipliers acting on
non-commutative Lp-spaces* (arXiv:2206.00549). The Fourier-to-Schur
multiplicatively bounded transference theorem remains true when one input
exponent and the output exponent equal 1 and every other input exponent is
infinity.

The new ingredient is a direct trace-class coefficient-freezing lemma for
`lambda_a h_U^2 lambda_b`. It factors this element into two normalized L2
columns and uses strong continuity of a coefficient representation. This
replaces all three unavailable endpoint uses named by the source authors.

Files:

- `solution_packet.pdf` — expert-review packet.
- `main.tex` — self-contained packet source.
- `source_paper.pdf` — locally compiled exact arXiv source release for 2206.00549.
- `supporting_paper_2201.10400.pdf` — locally compiled exact arXiv source release for the CJKM proof being patched.
- `figures/open_problem_crop.png` — real rendered crop of source PDF page 11.
- `VERIFICATION.md` — audit checklist and review priorities.

Scope: the theorem is for locally compact, second-countable, unimodular
groups. It does not claim the later non-unimodular endpoint variant.
