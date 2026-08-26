# Core-dimension recurrence question: negative literature answer

Status: `literature_already_answered`.

Question 5.15.5 on source-PDF page 111 of David Benson's *Modular
Representation Theory and Commutative Banach Algebras* asks whether the core
dimensions `c_n^G(M)` eventually satisfy a constant-coefficient linear
recurrence, equivalently whether their generating function is rational.

Cheng Meng's arXiv:2603.11592 explicitly answers the underlying
Benson-Symonds question negatively. Theorem 4.21 and the following example
give the concrete choice

```text
G = V_4,   M = Omega(k) direct-sum Omega^{-1}(k),
```

whose core-dimension sequence is not eventually recursive. The paper also
displays its algebraic but nonrational core series. The noninteger `n^(1/2)`
factor in the coefficient asymptotics is incompatible with any eventual
constant-coefficient recurrence.

Files:

- `solution_packet.pdf`: compact status and identification note.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: Benson's question source, arXiv:2008.13155.
- `supporting_paper_2603.11592.pdf`: Meng's negative answer.

Scope: this answers Question 5.15.5 only. It does not settle the adjacent
questions concerning `gamma_G`, symmetry of the completed representation
ring, algebraic integrality, or tensor-square growth.
