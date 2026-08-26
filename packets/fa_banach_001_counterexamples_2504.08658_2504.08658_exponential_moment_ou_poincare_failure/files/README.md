# Exponential moment does not force finite-time OU Poincare regularization

Candidate full counterexample to the open question in Section 3.2.2, PDF
page 17, of arXiv:2504.08658v2.

The construction is a symmetric, exponentially weighted mixture of unit
Gaussians at centers `+/-2^k`.  Its square-root density belongs to
`H^1(gamma)` and has a finite exponential moment.  At every finite OU time,
the centers remain increasingly separated, producing compactly supported
test functions whose Poincare Rayleigh quotients tend to zero.

Files:

- `solution_packet.pdf`: proof packet;
- `main.tex`: packet source;
- `source_paper.pdf`: current official arXiv PDF;
- `figures/open_question_crop.png`: source question on PDF page 17;
- `verification.md`: mathematical and novelty audit;
- `code/check_log_rayleigh.py`: numerical check of the explicit log bound.

