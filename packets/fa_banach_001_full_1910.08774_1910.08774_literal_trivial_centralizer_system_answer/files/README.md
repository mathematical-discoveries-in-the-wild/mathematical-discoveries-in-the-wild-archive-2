# 1910.08774 — literal trivial-centralizer-system answer

## Outcome

Candidate full positive answer to the displayed question exactly as written,
with a decisive formulation caveat.

The question asks only for the existence of *some* system of trivial
centralizers whose distances have the same supremum as the distance of a
given centralizer.  It imposes no requirement that the system be obtained
from the given map by restriction, compression, approximation, or any other
localization.  Under those quantifiers the answer is always yes, for arbitrary
quasinormed modules and independently of the exponents.

## Main result

Let \(X=L^p_0\), \(Y=L^q\), and
\(\mathscr N=\mathscr M_{\mathcal M}(X,Y)\).  For an
\(\mathcal M\)-centralizer \(\Omega:X\to Y\), write
\[
 D=\operatorname{dist}(\Omega,\mathscr N)\in[0,\infty].
\]

- If \(D<\infty\), then \(\Omega\) is itself a trivial centralizer, so the
  one-element system \(\{\Omega\}\) has supremal distance \(D\).
- If \(D=\infty\), construct a bounded nonlinear homogeneous map
  \(B:X\to Y\).  It is a trivial centralizer and has a finite positive
  distance \(d\) from \(\mathscr N\).  Then
  \(\Omega_n=nB/d\) is trivial and
  \(\operatorname{dist}(\Omega_n,\mathscr N)=n\), so the supremum is
  infinite.

The only real lemma is \(d>0\): if \(d=0\), module morphisms would approach
\(B\) uniformly on the unit ball, and additivity would pass to the limit,
contradicting the construction of \(B\).

## Files

- `main.tex` — exact source transcription, theorem, proof, audit, and caveat.
- `solution_packet.pdf` — compiled packet for specialist review.
- `source_paper.pdf` — arXiv source paper.
- `figures/open_problem_crop.png` — exact source question on page 29.
- `tmp/` — build and rendered-page artifacts.

## Interpretation warning

This result does **not** supply the intended substitute for the paper's
Lemma 3.  The Schatten proof uses trivial centralizers obtained by specified
finite-rank compressions of the original map.  To express that problem, the
question must require a concrete relation and compatibility condition between
\(\Omega\) and every \(\Omega_i\).  Once such a condition is added, the
argument here no longer applies and the substantive arbitrary-von-Neumann
algebra problem remains open.

## Human review

A specialist should verify that no convention elsewhere in the paper silently
builds localization into the word “system.”  If it does not, the author should
be informed that the displayed question is formally vacuous and invited to
state the intended compression/localization axioms.
