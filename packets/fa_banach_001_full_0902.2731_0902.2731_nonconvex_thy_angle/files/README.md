# A nonconvex gauge with a global Thy angle

This packet gives candidate full affirmative answers to Problems 1 and 2 of
Thurey, arXiv:0902.2731.

The example is the gauge on `R^2`

\[
q(r\cos\theta,r\sin\theta)=r\left(1+\frac1{10}\cos4\theta\right).
\]

Its unit ball is nonconvex, so the triangle inequality fails. Nevertheless,
the normalized polarization cosine is strictly decreasing as the oriented
separation of two rays runs from `0` to `pi`. It therefore stays in `[-1,1]`,
which proves CSB, and the same strict monotonicity yields axiom (An 11).

The expensive step is reproducible: `verify_certificate.py` derives the
rational derivative directly from the displayed gauge and proves positivity
of its reduced numerator and denominator by checking all 28,122 tensor
Bernstein coefficients over exact rational arithmetic.

Artifacts:

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: editable proof source.
- `verify_certificate.py`: exact symbolic and Bernstein verifier.
- `verification_report.md`: recorded mathematical and rendering checks.
- `novelty_search.md`: bounded literature search.
- `source_paper.pdf`: source paper.
- `figures/problem_crop.png`: exact source excerpt containing both problems.

Status: candidate full affirmative answers, likely valid; priority is not
asserted.
