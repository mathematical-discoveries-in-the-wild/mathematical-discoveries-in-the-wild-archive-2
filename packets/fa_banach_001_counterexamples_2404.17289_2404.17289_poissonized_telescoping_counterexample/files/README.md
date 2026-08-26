# A convergent (o(1/k)) series whose Poisson transform is not (L^1)

**Status:** candidate full counterexample, likely valid; human review
recommended.

This packet answers Remark 3.4(c) of A. K. J. Pritchard and D. Seifert,
*The asymptotic behaviour of the Cesàro operator* (arXiv:2404.17289),
negatively.

Let
\[
s(x)=\frac{\sin(\log(x+e^2))}{\log(x+e^2)},\qquad
a_k=s(k)-s(k+1).
\]
Then \(\sum a_k\) converges telescopically and \(a_k=o(k^{-1})\), but
\[
F(t)=e^{-t}\sum_{k=0}^\infty a_k\frac{t^k}{k!}
\]
is not absolutely integrable.  Indeed, Poisson concentration gives
\[
F(t)=-\frac{\cos(\log(t+e^2))}{(t+e^2)\log(t+e^2)}
+O\!\left(\frac1{t(\log t)^2}+\frac1{t^2\log t}\right).
\]

Defining \(x_0=0\) and \(x_{k+1}=(k+1)a_k\) also proves that the paper's
series condition (3.2) is strictly weaker than its integral condition (3.1).

Files:

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real crop of printed page 6.
- `code/verify_poisson_counterexample.py`: numerical regression.
- `verification.md`: proof and render verification.
- `novelty_search.md`: bounded novelty search.

Ledger:
`runs/fa_banach_001/ledger/results/2404.17289_poissonized_telescoping_counterexample.json`.

