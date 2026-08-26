# Conjecture 1 of arXiv:1904.09373 from Turán--Nazarov

Status: `literature_implied_answer (full answer to Conjecture 1 only)`

Wayne M. Lawton asks in Conjecture 1.1 of *Distribution of Small Values
of Bohr Almost Periodic Functions with Bounded Spectrum* (arXiv:1904.09373,
source PDF page 2) whether the constants in

\[
  J_f(u)\le C_n H_f^{-1/n}u^{1/n}
\]

for trigonometric polynomials with at most \(n+1\) frequencies can be chosen
uniformly bounded in \(n\).

The answer is yes.  The measurable Turán--Nazarov inequality, quoted as
Theorem 1.1 of Friedland--Yomdin, *An observation on the Turán--Nazarov
inequality* (arXiv:1107.0039, supporting PDF page 1), gives on every interval
\(I\)

\[
  \sup_I |f|\le \left(\frac{A|I|}{|E|}\right)^n\sup_E|f|
\]

for every measurable \(E\subset I\), with one absolute constant \(A\).
Taking \(E=\{x\in I:|f(x)|<u\}\), then letting centered intervals exhaust
\(\mathbb R\), proves

\[
  J_f(u)\le A\left(\frac{u}{H_f}\right)^{1/n}.
\]

The only limiting input is the defining Bohr coefficient identity:
the average of \(f(x)e^{-i\omega_jx}\) tends to \(a_j\), hence the interval
suprema have liminf at least \(H_f\).

This implication is agent-identified: Friedland--Yomdin and Nazarov predate
Lawton's conjecture and do not claim to answer it.  The result therefore belongs
in `literature_implied_answers`, not `literature_already_answered` or `full`.
Conjectures 2 and 3 of arXiv:1904.09373 are not addressed by this packet.

The source and supporting PDFs were compiled from the repository's local arXiv
source archives.  See `main.tex` and `solution_packet.pdf` for the complete
argument and `verification.md` for checks.

