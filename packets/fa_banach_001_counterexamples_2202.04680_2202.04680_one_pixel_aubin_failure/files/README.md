# One-pixel failure of automatic Aubin regularity

This packet gives a candidate full negative answer to the convergence-condition
question on source PDF page 17 of arXiv:2202.04680v3.

The source asks whether the Aubin property and a dual-variable smallness
condition required by the cited nonlinear PDHG analysis hold for its discrete
segmentation functional. They do not hold automatically over the proposed
model class.

Choose one pixel, two classes, and zero feature maps. Then both the discrete
gradient and the nonlinear data operator vanish. At the barycentric
segmentation and zero dual variable, the smallness condition is as favorable
as possible, but the inverse linearized saddle operator is not Aubin: an
arbitrarily small normal perturbation selects a simplex vertex at fixed
distance from the barycenter.

The result does not assert that the numerical algorithm diverges, nor that the
Aubin property fails for every nondegenerate image. It disproves an
unqualified automatic-validity claim and shows that additional hypotheses on
the data and saddle point are indispensable.

Files:

- main.tex: proof packet source.
- solution_packet.pdf: compiled packet.
- verification_report.md: independent checks and scope.
- attempt_log.md: investigation history.
- source_paper.pdf: arXiv:2202.04680v3.
- figures/open_problem_crop.png: exact source question.
- code/make_source_crop.py: reproducible crop script.
