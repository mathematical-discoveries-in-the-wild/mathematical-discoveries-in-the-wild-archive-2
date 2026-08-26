# Direct proof for the Fitzpatrick extension of a subdifferential

Result type: `full`

Status: candidate full solution, likely valid, pending expert review.

## Source problem

Stephen Simons, *Quasidensity: a survey and some examples*,
arXiv:1711.06165. Problem 4.10 asks for a simple direct proof of Theorem 4.8:

```text
(partial f)^F = partial(f*)
```

for every proper convex lower-semicontinuous function on a real Banach
space.

## Contribution

The packet gives a four-line structural proof, relative to Theorems 4.3 and
4.6 already stated immediately before the problem in the source survey.
Writing `H(x,x*) = f(x) + f*(x*)`, Fenchel--Young equality on the graph of
`partial f` gives `phi_{partial f} <= H`. Conjugation reverses this inequality,
so every point of the Fitzpatrick extension satisfies equality in the
Fenchel--Young inequality for `f*`; hence

```text
(partial f)^F is contained in partial(f*).
```

The left side is maximally monotone by the survey's Theorems 4.3 and 4.6,
while the right side is monotone. The inclusion is therefore equality.

This answers a proof-method question about an already-known theorem; it does
not claim a new theorem statement.

## Files

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: source evidence containing Theorem 4.8 and
  Problem 4.10.
- `verification.md`: independent proof audit and novelty notes.
- `tmp/`: build products and rendered pages used for visual QA.

## Literature and dependency check

A bounded exact-phrase and theorem-formula search found the source survey,
Simons's earlier arXiv:1407.1100 paper, and the later stand-alone analysis
arXiv:1907.07278, but no occurrence of this sandwich-plus-maximality proof.
The maximality theorem used in the last step has an independent proof in
Section 11 of arXiv:1407.1100 and does not depend on the subdifferential
identity, so the argument is noncircular. Novelty confidence is moderate,
not exhaustive.

## Human review focus

Please check that the intended meaning of “direct” permits use of Theorems
4.3 and 4.6 from the same survey. Mathematically, the key checks are the
order reversal under conjugation and the final use of maximal monotonicity.
