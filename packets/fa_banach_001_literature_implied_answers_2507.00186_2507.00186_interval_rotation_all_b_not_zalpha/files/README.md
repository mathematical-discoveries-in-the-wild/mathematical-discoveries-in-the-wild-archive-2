# Interval rotations: Question 5.7 has a complete positive answer

Status: `literature_implied_answer (complete; stronger all-irrational-rotation form)`.

Source: Valentin Gillet, *Linear dynamics of random products of operators*,
arXiv:2507.00186v3, Question 5.7 on printed/PDF page 45. The paper asks
whether Corollaries 3.22 and 3.23 remain valid for
`A_1=[0,b)`, `A_2=[b,1)` whenever `b` is not in `Z alpha`.

## Answer

Yes. In fact the continued-fraction hypotheses in those two corollaries are
unnecessary for this conclusion.

For every irrational `alpha` and every `b in (0,1)` with
`b notin Z alpha (mod 1)`, put

`d_b = 1_[0,b) - b`.

Then, for Lebesgue-almost every `x`,

`limsup_n S_n d_b(x)=+infinity` and
`liminf_n S_n d_b(x)=-infinity`.

The function used in the source paper is `f=d_b/(1-b)`, so it has the same
two-sided divergence. The hypotheses of the paper's Theorems 3.19 and 3.20
are therefore satisfied, and their conclusions give the weak mixing asserted
in Corollaries 3.22 and 3.23 for every irrational rotation.

## Why this is literature-implied

Halász's 1976 one-sided bounded-remainder theorem says that if the discrepancy
of a measurable set is bounded on even one side on a positive-measure set of
starting points, then `exp(2 pi i m(A))` is an eigenvalue of the underlying
ergodic transformation. V. T. Sós states this result explicitly in
*Irregularities of Partitions*, printed page 234. For rotation by `alpha`, the
eigenvalues are exactly `exp(2 pi i k alpha)`, so one-sided boundedness for
`[0,b)` would force `b in Z alpha (mod 1)`.

The packet also gives a short self-contained measurable-coboundary proof of
this implication. Neither Halász nor Sós discusses the operator-theoretic
Question 5.7; the identification with that question is made here. Because the
decisive theorem predates the source question, this is not claimed as a new
run theorem.

## Scope warning

The conclusion is almost-everywhere, exactly as required by the source's
definition of a random weakly mixing sequence. It is not a pointwise theorem
for every starting point. Ying and Zheng, arXiv:2210.08441, characterize many
rational interval lengths for which a particular orbit has one-sided bounded
discrepancy even though the interval is not a bounded-remainder interval. This
does not contradict the result above because the exceptional invariant set
has measure zero.

## Files

- `main.tex`: complete identification, self-contained proof, operator lift,
  and literature/scope audit.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: locally rendered arXiv:2507.00186v3 source.
- `supporting_sos_irregularities_partitions.pdf`: supporting survey containing
  the explicit one-sided Halász theorem.
- `supporting_halasz_1976_metadata.md`: metadata/access note for the original
  1976 theorem.
- `figures/open_question_page_45.png`: source Question 5.7.
- `figures/halasz_one_sided_theorem_page_234.png`: supporting theorem statement.

Human review recommendation: verify the one-sided coboundary lemma and the
one-line eigenvalue reduction, then retain as a complete literature-implied
answer and duplicate/status memory rather than count it as an original proof.

