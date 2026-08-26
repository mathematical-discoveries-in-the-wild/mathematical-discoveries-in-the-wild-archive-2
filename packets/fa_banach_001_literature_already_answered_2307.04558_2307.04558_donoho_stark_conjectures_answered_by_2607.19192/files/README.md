# Donoho--Stark interval conjectures answered by arXiv:2607.19192

Status: `literature_already_answered`

## Source questions

Oriol Baeza Guasch, *On an uncertainty result by Donoho and Stark*,
arXiv:2307.04558 (2023).

- Conjecture 1, arXiv PDF page 1, asks whether an interval time set maximizes
  the norm of the time--frequency concentration operator among all measurable
  sets of the same measure, when the frequency set is an interval.
- Conjecture 2, arXiv PDF page 10, asks the analogous question for analytic
  polynomials of degree at most `n` on the circle, without the paper's proved
  restriction `n delta <= pi`.

## Separate later answer

Luis Daniel Abreu and Michael Speckbacher, *Optimal concentration in the
Paley--Wiener space*, arXiv:2607.19192 (2026), answers both questions.

- Theorem 1.1, arXiv PDF page 1, proves optimal Paley--Wiener concentration
  on an interval for every finite-measure time set and every bounded interval
  frequency set, with no restriction on the product of the measures. Page 2
  explicitly says this confirms the Donoho--Stark conjecture and removes the
  restriction improved to `|Omega||E| <= 1` by Baeza--Guasch.
- Theorem 2.1, arXiv PDF page 3, proves that a circle interval maximizes the
  largest eigenvalue of the concentration operator on
  `span{1,e^{it},...,e^{iNt}}` among all measurable circle sets of the same
  measure. Its Rayleigh quotient (equation (5)) is exactly the concentration
  functional in source Conjecture 2.

Thus the later paper removes both small-product restrictions and fully answers
both conjectures. It does not claim uniqueness of the maximizing set, but
uniqueness was not part of either source conjecture.

The continuous identification is stated explicitly by the supporting authors.
The circle identification is an exact theorem-level match; the supporting
paper cites Baeza--Guasch but does not separately call its Theorem 2.1 an
answer to Baeza--Guasch's Conjecture 2.

## Search and verification

A bounded search through 13 August 2026 checked the run's registry, solution,
attempt, and proof-gap indexes; exact title and conjecture phrases; the official
arXiv records; and the full TeX/PDF of arXiv:2607.19192. The source and answer
statements were also checked page by page using PDF extraction. No new
mathematical result is claimed in this packet.

Files:

- `source_paper.pdf`: arXiv:2307.04558.
- `supporting_paper_2607.19192.pdf`: arXiv:2607.19192.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.
- Ledger: `runs/fa_banach_001/ledger/results/2307.04558_donoho_stark_conjectures_answered_by_2607.19192.json`.

