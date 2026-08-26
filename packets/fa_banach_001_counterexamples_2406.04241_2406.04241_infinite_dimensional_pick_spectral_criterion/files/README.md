# 2406.04241 — infinite-dimensional Pick spectral counterexample

Status: `candidate_full_counterexample_human_review_needed`.

Model: `GPT5.6`.

Source: Jonas Schober, *Regular one-parameter groups, reflection positivity
and their application to Hankel operators and standard subspaces*,
arXiv:2406.04241v2.

## Result

The finite-dimensional regularity criteria in Theorems 3.1.7 and 3.1.10 do
not extend verbatim to infinite-dimensional Hilbert spaces.

On `H=l2(N)`, set `D e_n=e_n/n` and `F(z)=zD`. An explicit coordinatewise
dilation conjugates the associated group to the standard shift group of
multiplicity `l2`, so `F` is regular. Nevertheless, zero belongs to
`sigma(F(z))` for every `z` in the upper half-plane, and `D(F,{0})=R`.
Thus the spectral and zero-set conditions fail.

The multiplication-kernel condition remains true: for every real `lambda`,
`ker(lambda I-M_{F_*})={0}` even on all of `L2`. This identifies continuous
spectrum at zero as the obstruction.

## Files

- `main.tex`: complete counterexample and multiplicity computation.
- `solution_packet.pdf`: compiled human-review packet.
- `verification_report.md`: adversarial proof and scope audit.
- `source_paper.pdf`: arXiv v2 source PDF.
- `figures/open_problem_crop.png`: source open-problem paragraph.
- `figures/theorem_3_1_7_crop.png`: finite-dimensional five-way criterion.
- `figures/theorem_3_1_10_crop.png`: finite-dimensional zero-set criterion.

## Scope and review

This fully refutes the unchanged extension of the two criteria explicitly
named by the source. It does not rule out corrected criteria using point
spectrum or spectral measures, and the example's multiplicity is explicitly
`l2`, so no claim is made against a suitable infinite-cardinal multiplicity
formula.

A bounded local-index and external search on 2026-08-13 found no later source
stating this counterexample. Specialist novelty and definition review remain
appropriate.
