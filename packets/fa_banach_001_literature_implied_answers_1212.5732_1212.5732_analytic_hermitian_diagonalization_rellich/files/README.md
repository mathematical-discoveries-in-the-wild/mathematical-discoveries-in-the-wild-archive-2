# Literature-Implied Answer: Analytic Hermitian Families Are Diagonalizable

Status: `literature_implied_answer (full answer to Question 2.9)`

Source paper: Justin Cyr, Jason Ekstrand, Nathan Meyers, Crystal Peoples, and Justin Peters, *Diagonalizing Hermitian Matrices of Continuous Functions*, arXiv:1212.5732v1.

Source question: Question 2.9 on page 8 asks whether a Hermitian matrix family on an interval is continuously diagonalizable when its entries extend analytically to a complex domain containing the interval. The question writes `A in M_n(C[a,b])` but refers to the three-entry notation for a `2 x 2` matrix introduced in equation (1). The answer below covers both the literal `2 x 2` reading and the intended arbitrary finite-dimensional reading.

Answer recorded here: Yes. In fact, the diagonalizing unitary can be chosen real analytic on the interval. Rainer's arXiv:1111.4475v2, Theorem 1.1(A) on page 1, gives global analytic parameterizations of eigenvalues and eigenvectors for a one-real-parameter analytic normal family; the discussion on page 18 shows that for normal matrices the eigenvectors can be chosen orthonormal. A finite-dimensional Hermitian family is normal and has compact resolvent, so the theorem applies. Putting the analytic orthonormal eigenvectors into the columns of `U(t)` gives an analytic unitary with `U(t)^* A(t) U(t)` diagonal.

Endpoint detail: the source assumes holomorphic extensions to a domain containing the compact interval. Hermiticity identities, initially valid on `[a,b]`, are real-analytic identities and therefore extend to a slightly larger real interval inside that domain. Thus the one-parameter theorem applies on an open interval containing `[a,b]`.

Provenance: this is an agent-identified implication, not an explicit claim by Rainer to answer Cyr--Ekstrand--Meyers--Peoples--Peters. Rainer's preprint was submitted in November 2011 and revised in April 2012, before arXiv:1212.5732 was submitted. Rainer also identifies the self-adjoint real-analytic case as the classical theorem of Rellich.

Scope limitation: this fully answers only Question 2.9. It does not settle the separate question in the introduction asking for an arbitrary-`n` analogue of the source paper's `C^1` Theorem 2.6 under its finite-collision/simple-derivative hypothesis.

Bounded literature check: the run indexes were searched for `1212.5732`, the exact title, `analytic Hermitian`, and `Rellich`; no prior run packet was found. Web/arXiv searches used the exact source title with `Rellich`, `Question 2.9`, and one-parameter analytic Hermitian eigenvector terms. The decisive supporting source is arXiv:1111.4475, Theorem 1.1(A) and the orthonormality conclusion on page 18.

Files:

- `source_paper.pdf`: the open-question source.
- `supporting_paper_1111.4475.pdf`: Rainer's perturbation theorem.
- `main.tex`, `solution_packet.pdf`: compact status and proof-of-implication note.

Ledger: `ledger/results/1212.5732_analytic_hermitian_diagonalization_rellich.json`.
