# Vertical Lq monotonicity for general de Branges–Rovnyak kernels

Status: `candidate full result, likely valid, pending human review`

This packet gives an affirmative answer to Question 6.6 of Baranov–Fricain–
Mashreghi, arXiv:0802.0789.  For every Schur function `b` on the upper
half-plane, every `1<q<infinity`, every real `x`, and
`0<=y2<=y1`,

```text
||k^b_{x+i y1}||_q <= C(q) ||k^b_{x+i y2}||_q,
```

with the usual finite-boundary-kernel interpretation when `y2=0`.  One may
take

```text
C(q) = 1 + A_q A_q' / pi,
A_s = (integral_R (1+u^2)^(-s/2) du)^(1/s).
```

The proof uses only an exact two-kernel identity, the elementary disk
inequality `|a-w|<=|1-conj(a)w|`, and the Hardy-space Cauchy point-evaluation
bound.  It works for all `1<q<infinity`, improving the range needed in the
source.

Files:

- `source_paper.pdf`: arXiv:0802.0789.
- `figures/equation_6_9_context_crop.png`: source PDF page 27, including the
  inequality labeled (6.9).
- `figures/open_problem_crop.png`: complete Question 6.6 on source PDF page
  28.
- `main.tex`, `solution_packet.pdf`: formal theorem and proof.
- `verification.md`: mathematical and artifact checks.

Question 6.6 is fully answered.  The packet does not claim answers to the
paper's distinct Question 3.3.  Question 6.4 was subsequently answered in the
literature by Aleman–Malman (2017).
