# Exact Gaussian-operator norm for arXiv:1409.1262

Status: `literature_implied_answer (full exact characterization)`.

## Result

Remark 4.6 of Aleman–Viola asks for the exact norm of `exp(-tP)` on a
quadratically weighted Fock space when the pluriharmonic part of the weight
does not vanish.

Conjugation by the source paper's unitary sends the evolution operator to

`f(w) -> exp(w^T C_t w/2) f(B_t w)`.

This is exactly a Gaussian integral operator `B[S_t]` in Neretin's notation,
with

`S_t=[[C_t,B_t^T],[B_t,0]]`.

Neretin's 2011 canonical-invariant and exact-norm theorems therefore give a
finite-dimensional answer at every bounded time. The invariants are obtained
from a generalized eigenvalue pencil of size `2n`, and the norm is a
determinant times a product over those invariants.

In the stable case `Spec M subset {Re lambda>0}`, the identification also
gives the explicit previously unstated limit

`lim ||exp(-tP)|| = det(I-K^*K)^(-1/4)`,

where `K=G^{-T}HG^{-1}` represents the pluriharmonic part. Together with the
source paper's return-to-equilibrium estimate, this gives the same sharp
exponential-polynomial error term for the norm.

## Classification

The decisive Gaussian-operator norm theorem predates the source paper. The
matrix identification appears not to have been made in either source, so the
packet is classified as literature-implied rather than as a new solution.

## Files

- `main.tex` — detailed identification, exact formulas, and large-time limit.
- `solution_packet.pdf` — compiled note.
- `source_paper.pdf` — full source paper.
- `source_open_question_crop.pdf` — source Remark 4.6, printed pp. 58–59.
- `supporting_neretin_gaussian_operators.pdf` — full supporting monograph.
- `supporting_gaussian_definition_crop.pdf` — Gaussian operator definition
  and boundedness theorem.
- `supporting_canonical_invariants_crop.pdf` — canonical invariants and the
  generalized eigenvalue pencil.
- `supporting_exact_norm_crop.pdf` — exact norm theorem, including the
  arbitrary bounded case.
- `verification.md` — convention, formula, compilation, and visual checks.

## Search evidence

The cheap run indexes were searched for `1409.1262`, the paper title, and
exact norm / quadratic Fock / Gaussian operator keywords; no previous result
was found. A current web search on 2026-08-12 checked the exact source phrase,
the title, citation-style queries, and recent weighted-composition literature.
No explicit later answer to the remark was located. The source bibliography
does not cite Neretin, Olshanski, Howe, or the Gaussian-operator literature.

