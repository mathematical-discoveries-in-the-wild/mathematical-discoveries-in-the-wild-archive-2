# Cyclic-group BH subexponentiality answered by arXiv:2608.05366

Status: `literature_already_answered_full_subexponentiality_question`

## Source question

Becker--Klein--Slote--Volberg--Zhang, arXiv:2310.07926, Question 2
(source PDF page 9), ask whether the optimal cyclic-group
Bohnenblust--Hille constant `BH_{Omega_K}^{<=d}` is subexponential in `d`
for each fixed finite `K`.

## Later answer

Pellegrino--Raposo, arXiv:2608.05366v1, Corollary 1.1 (supporting PDF
page 5), explicitly answers the question. For each fixed `q>=2`,

```text
BH_deg(d,q) <= exp(c_q sqrt(d log d)
                    + O_q(sqrt(d/log d) log log d))
             = exp(o(d)).
```

The later paper first proves the same estimate for the larger
interaction-order class. Since the number of active coordinates of a Fourier
index is at most its total degree, the source's total-degree class is contained
in that larger class. The notation `BH_deg(d,q)` in the answer paper is
explicitly identified with `BH_{Omega_q}^{<=d}` in the source.

## Scope

This fully answers the source's subexponentiality starting question. It does
not determine the optimal growth of the BH constants, and it does not answer
the source's separate question about optimal `K`-dependence of the
uniform-norm discretization constant.

## Duplicate check

The four cheap indexes contained no packet for arXiv:2310.07926. A neighboring
triage record for arXiv:2406.08509 mentions that arXiv:2608.05366 answers this
narrower question, but does not package or ledger the exact source-to-answer
relation here.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: compiled status note.
- `source_paper.pdf`: official arXiv:2310.07926 PDF.
- `supporting_paper_2608.05366.pdf`: official answering paper.
- `verification_report.md`: source, theorem, build, and visual checks.
