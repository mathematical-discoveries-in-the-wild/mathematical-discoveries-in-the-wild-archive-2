# Candidate full solution: arbitrary homogeneous matrix-pencil definability

Status: **candidate full solution, likely valid, needs expert review**

Source: Thomas Sinclair, *Model Theory of Operator Systems and
C\*-Algebras*, arXiv:2210.03862. In the source PDF this is Question 3.31,
immediately after Proposition 3.29.

## Result

The answer to Question 3.31 is **yes for the class of all operator systems**.
If `p` is any homogeneous linear matrix \*-polynomial and `k` is fixed, then

```text
S_p(E) = {X in E_k^n : 1 >= p(X)}
```

is a definable uniform assignment. Here the inequality means, as usual, that
`1-p(X)` belongs to the positive cone; in particular it forces `p(X)` to be
Hermitian.

Write

```text
q = (p+p*)/2,             r = (p-p*)/(2i).
```

Both `q` and `r` are Hermitian homogeneous pencils, and
`p(X)=q(X)+i r(X)`. The main point is quantitative: the real-linear map
`X -> r(X)` acts only on a fixed finite-dimensional scalar coefficient space.
Consequently it has, at every operator-system matrix level, a uniformly
bounded projection onto its kernel. If `1-p(X)` is within `delta` of the
positive cone, then `r(X)` is `O(delta)`. Projecting to `ker r` changes `X`
by `O(delta)`, and the Hermitian pencil `q` then satisfies

```text
q(Y) <= (1+O(delta)) 1.
```

The positive scalar rescaling used in Sinclair's Proposition 3.29 produces
an exact feasible tuple within `O(delta)` of `X`. Exercise 3.23 therefore
shows that the zero set is definable.

## Files

- `solution_packet.pdf`: source question, theorem, full proof, intuition,
  verification, and bounded novelty record.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_question_crop.png`: page-23 crop containing Proposition 3.29
  and Question 3.31.
- `code/verifier.py`: randomized finite-matrix checks of the decomposition,
  skew-kernel projection, and rescaling step.
- `VERIFICATION.md`: verification transcript and reviewer checklist.

## Human-review priority

Check the finite-coefficient amplification lemma: after identifying
`M_k(E)` over the reals with a fixed finite-dimensional coefficient space
tensored with `E^h`, a fixed scalar projection has a norm bound independent
of the operator system `E`. Everything after that is the source paper's
uniform zero-set criterion and homogeneity argument.

## Novelty status

A bounded search on 11 August 2026 covered all four run indexes, the exact
arXiv id, the exact question phrase, the current author-hosted PDF, and
decomposition/definability keywords. The current PDF still states the
question, and no direct answer was located. This is provisional novelty
evidence, not an exhaustive originality determination.
