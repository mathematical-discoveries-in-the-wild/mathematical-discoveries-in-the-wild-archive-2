# A bi-Lipschitz class missed by every sublinear displacement class

Status: `full_solution_likely_valid`

Source: Michael Dymond and Vojtěch Kaluža, *Divergence of separated nets
with respect to displacement equivalence*, arXiv:2102.13046; Geometriae
Dedicata 218, article 15 (2024). The open question is on source PDF page 7.

## Result

For every dimension `d>=2`, there is one bi-Lipschitz equivalence class of
separated nets that contains no net admitting a sublinear-displacement
bijection to `Z^d`. Thus, for every increasing concave `phi=o(R)`, the
`phi`-displacement class of the lattice misses this bi-Lipschitz class.

Together with source Proposition 2.6, this fully classifies the paper's
intersection question:

```text
Every phi-displacement class meets every BL class
if and only if phi(R) is Omega(R).
```

The proof samples a Burago--Kleiner non-realizable density on rapidly growing
nested shells. A hypothetical bi-Lipschitz image with sublinear displacement
to the lattice yields, after blow-up, a bi-Lipschitz map transporting that
density to Lebesgue measure. This contradicts non-realizability.

## Files

- `solution_packet.pdf`: expert-facing theorem and proof.
- `source_paper.pdf`: source paper compiled locally from the complete arXiv
  TeX archive already present in the repository.
- `figures/open_problem_crop.png`: the exact source question from page 7.
- `code/crop_open_problem.py`: reproducible crop script.
- `verification.md`: proof, build, and visual-QA record.

## Novelty check

The published 2024 version still states the question as open. A bounded search
through 2026-08-11 covered the exact question, title, DOI, authors, and
displacement/BL-class terminology. The authors' later papers found in the
search concern bi-Lipschitz extension, not displacement-class intersections.
No later answer was located. Novelty confidence is moderate pending a full
citation review.

## Human-review recommendation

Check three points in order: the nested-shell adaptation of source Lemma 6.4,
passage of the lower bi-Lipschitz bound to the blow-up limit, and the
boundary-filling argument for the shifted lattice. If those pass, the result
is a full classification of the stated intersection question.

