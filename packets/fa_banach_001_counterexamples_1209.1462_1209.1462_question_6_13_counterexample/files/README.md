# Counterexample to Question 6.13 of arXiv:1209.1462

Source: Stanislav Shkarin, *Non-sequential weak supercyclicity and
hypercyclicity*, arXiv:1209.1462 (2012).

Status: candidate full counterexample, likely valid.

## Result

Question 6.13 is false at `p=1`, `q=infinity`, hence `r=2`.

The first six unit vectors of `ell_1` are the two coordinate vectors and
the four vectors

```text
(e_1-conj(omega)e_2)/2,  omega in {1,-1,i,-i}.
```

Giving each threshold `2/5` already makes the six inequalities impossible
for every point of the closed unit ball of `ell_infinity`; their squared
budget is only `24/25`.  A strictly positive geometric tail with squared
mass `1/25` makes the total budget exactly one, as required by the question.

## Files

- `main.tex`: complete counterexample and proof.
- `solution_packet.pdf`: rendered solution packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/question_6_13_crop.png`: source question on PDF page 33.
- `figures/source_page_33.png`: full rendered source page.
- `code/verify_counterexample.py`: exact and numerical diagnostic checks.
- `verification.md`: verification record and scope notes.

## Scope

This fully answers the universal statement in Question 6.13 negatively.  It
does not settle the separate weak-closedness conjecture that an affirmative
answer would have implied.

## Human review recommendation

Accept as a candidate full counterexample.  Check the projective reduction,
the strict fourth-root covering estimate, and the geometric-tail identity.
