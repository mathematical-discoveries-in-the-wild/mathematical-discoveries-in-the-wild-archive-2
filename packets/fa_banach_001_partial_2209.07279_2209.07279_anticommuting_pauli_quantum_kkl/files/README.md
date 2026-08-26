# Quantum KKL for anticommuting-Pauli observables

Status: `candidate_partial_likely_valid`

Source: Cambyse Rouzé, Melchior Wirth, and Haonan Zhang, *Quantum
Talagrand, KKL and Friedgut's theorems and the learnability of quantum
Boolean functions*, arXiv:2209.07279, Remark 3.10 on page 13.

## Result

The source recalls the open Montanaro--Osborne conjecture that every balanced
quantum Boolean function on (n) qubits has an (L^2)-influence of order at
least (log n/n). This packet proves a stronger bound for the natural class

\[
 A=\sum_{s=1}^m c_s\Gamma_s,
 \qquad \sum_s c_s^2=1,
\]

where the \(\Gamma_s\) are distinct, nonidentity, pairwise anticommuting
Hermitian Pauli strings and the \(c_s\) are real. Such an \(A\) is
automatically a balanced quantum Boolean function. If

\[
 Q=\max_j \operatorname{Inf}_j^2(A),
\]

then

\[
 Q\ge \rho_n:=\frac{\sqrt{24n+9}-3}{4n}
 =\frac{6}{\sqrt{24n+9}+3}
 \ge \frac{6}{\sqrt{33}+3}\frac1{\sqrt n}.
\]

In particular this class satisfies the conjectured KKL conclusion, with room
to spare.

## Proof mechanism

Put \(w_s=c_s^2\), and let \(q_j\) be the total coefficient-square mass of
strings that are nonidentity on qubit \(j\). Then
\(q_j=\operatorname{Inf}_j^2(A)\). Every pair of globally anticommuting Pauli
strings must locally anticommute on at least one qubit. On qubit \(j\), if the
weights carrying labels \(X,Y,Z\) are \(x_j,y_j,z_j\), the weight of locally
anticommuting pairs is

\[
 x_jy_j+x_jz_j+y_jz_j\le q_j^2/3.
\]

Thus all unordered pairs are covered by the qubits, giving

\[
 \frac{1-\sum_s w_s^2}{2}
 \le \frac13\sum_jq_j^2\le \frac n3Q^2.
\]

If \(a=\max_s w_s\), then \(Q\ge a\) and
\(\sum_s w_s^2\le a\). Optimizing
\(Q\ge\max\{a,\sqrt{3(1-a)/(2n)}\}\) gives the displayed bound.

## Verification and scope

- `main.tex` contains the source statement, definitions, formal theorem,
  proof, literature check, and limitations.
- `solution_packet.pdf` is the rendered review packet.
- `source_paper.pdf` is the original arXiv paper.
- `figures/open_problem_crop.png` is a full-width crop of Remark 3.10.
- `code/verify_small_cases.py` exhausts every pairwise-anticommuting subset of
  the two-qubit Pauli strings and tests deterministic random weights; it also
  tests random three-qubit families. This is only a consistency check.

The full quantum \(L^2\)-KKL conjecture remains open. General quantum Boolean
functions can have commuting Pauli pairs whose off-identity products cancel
in \(A^2=I\); the proof here deliberately assumes away that cancellation
geometry. Exact and close-variant searches through 2026-08-09 did not locate
this influence bound, but novelty confidence is moderate rather than
definitive.

Human review recommendation: **review as a likely-valid substantial partial
result**. The key checks are the weighted pair-cover inequality and the passage
from global anticommutation to local anticommutation coverage.
