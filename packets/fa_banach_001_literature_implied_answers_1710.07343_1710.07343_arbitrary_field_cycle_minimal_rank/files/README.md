# Arbitrary-field block-cycle minimal rank

## Classification

- Status: `literature_implied_answer_with_independent_constructive_proof`.
- Source: Ben W. Grossmann and Hugo J. Woerdeman, *Fractional minimal rank*,
  arXiv:1710.07343, Theorem 3.2 and Section 5.2, Problem 1.
- Model: GPT5.6.

## Identification

The source asks whether its rank-`n` completion theorem for an `n`-cycle of
invertible `(n-1) x (n-1)` blocks remains true over an arbitrary field when
the holonomy has no fixed vector. Grossmann's 2019 thesis explicitly states
that Cohen--Pereira's 2018 regular-block cycle theorem gives a completion of
rank at most `(nk-d)/(n-1)`. In the question's regime `k=n-1,d=0`, this is
exactly `n`, matching the source lower bound. The relation is recorded as an
implication because Cohen--Pereira do not appear to name the later numbered
question.

## Independent proof

The packet also gives a field-uniform construction based on a path of
`(k+1) x k` frames joined by transverse rank-one updates. It proves the
stronger formula

```text
mr(A_H) = n-1  if H = I,
mr(A_H) = n    if H != I,
```

for every field. The key lemma is that every invertible matrix is similar,
over its base field, to one with all leading principal minors nonzero. A
one-row lift followed by backward-chosen column replacements then constructs
the required path.

## Files

- `main.tex`, `solution_packet.pdf`: identification and constructive proof.
- `source_paper.pdf`: arXiv source paper.
- `supporting_thesis_2019.pdf`: author thesis giving the decisive attribution.
- `figures/open_problem_crop.png`: exact source question.
- `figures/supporting_bound_crop.png`: thesis bridge to Cohen--Pereira.
- `code/verify_frame_path.py`: exhaustive graph search and constructive checks.
- `novelty.md`, `verification_report.md`: search and audit notes.

## Review focus

Verify the frame-path indexing in the final cycle edge and compare the exact
Cohen--Pereira theorem statement with the thesis attribution. The independent
proof does not rely on the closed-access paper, but it does use the lower bound
from Theorem 3.2 of the source.
