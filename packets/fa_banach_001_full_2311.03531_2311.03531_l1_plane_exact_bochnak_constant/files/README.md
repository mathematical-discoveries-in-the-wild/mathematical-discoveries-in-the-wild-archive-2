# Exact Bochnak constant of the real l1 plane

Status: `candidate full solution`

Source: Jorge Tomás Rodríguez, *A 2-dimensional real Banach space with
constant of analyticity less than one*, arXiv:2311.03531v2, PDF page 3.

## Result

The packet proves

`c_b(l_1^2(R)) = exp(2 Catalan/pi)/sqrt(2) = 1.2668686397429209...`.

The upper bound is valid in every degree and follows from Poisson--Jensen
plus a sharp two-parameter logarithmic-integral maximization. The matching
lower bound reduces the problem to a compact weighted polynomial extremal on
the unit circle and applies the weighted Siciak--Zakharyuta theorem after an
explicit positive boundary-jump calculation.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained source.
- `source_paper.pdf`: arXiv:2311.03531v2.
- `source_question.png`: source definition and exact-value question, PDF page 3.
- `supporting_paper_siciak_zakharyuta.pdf`: arXiv:2305.08260v3.
- `verification_report.md`: proof and rendering audit.

## Review recommendation

Recommended for expert review as a new full result. The most important point
to check is the distributional subharmonic gluing in the weighted polynomial
lemma; the packet includes its explicit nonnegative jump density.
