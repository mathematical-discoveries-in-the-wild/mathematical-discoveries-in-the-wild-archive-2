# Periodically forced OU counterexample to weak convergence

**Status:** full counterexample, likely valid; pending human review.

**Source:** Patrick Cattiaux and Arnaud Guillin, *Semi Log-Concave Markov
Diffusions*, arXiv:1303.6884, Remark 4.5 on PDF page 29.

## Result

The source's time-dependent curvature assumptions do not force the tight
transition laws `P(t,x,.)` to converge weakly.  The one-dimensional SDE

```text
dX_t = dB_t - X_t dt/2 + sin(t) dt,   X_0=x,
```

satisfies `(H.C.K(t))` with equality for `K(t)=t`, and
`integral_0^infinity exp(-K(s)) ds=1`.  Its law is Gaussian with

```text
mean = (2/5)sin(t) - (4/5)cos(t) + (x+4/5)e^(-t/2),
variance = 1-e^(-t).
```

The family is tight, but the times `2 pi n` and `(2n+1) pi` converge to the
distinct limits `N(-4/5,1)` and `N(4/5,1)`.  This fully answers the universal
convergence question in the negative.

## Files and verification

- `main.tex` and `solution_packet.pdf`: statement, source capture, and full
  calculation.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop.png`: actual rendering of Remark 4.5 on source
  PDF page 29.
- `runs/fa_banach_001/attempts/1303.6884_time_inhomogeneous_convergence_attempt.md`:
  concise discovery record.

The proof is exact and has no computational dependency.  Recommended review
focus: confirm that the source intends no extra centering or convergence
assumption beyond its displayed `(H.C.K(t))` hypothesis; the example satisfies
the stated smoothness, ellipticity, curvature, integrability, and tightness
requirements verbatim.
