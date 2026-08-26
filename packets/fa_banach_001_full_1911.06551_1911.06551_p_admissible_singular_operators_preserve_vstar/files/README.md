# P-admissible singular-type operators preserve the Morrey property (V*)

This packet gives a candidate full positive answer to the open question in
Section 3, immediately before Theorem 3.11, of arXiv:1911.06551.

## Result

Let `1<p<infinity` and `0<=lambda<n`. Every p-admissible sublinear
singular-type operator from Definition 2.1 of the source maps
`V^(*) L^{p,lambda}(R^n)` into itself. In particular, every singular integral
operator `S` considered by the source preserves `(V*)`.

The result is stronger than the question because it applies to the entire
p-admissible sublinear class, not only linear singular integrals.

## Proof idea

The `(V*)` tail gives small `L^p` mass on every far unit ball, while the
Morrey norm gives a decaying large-scale average. On each dyadic annulus the
size-condition potential is therefore bounded by

```text
min(eta_N, M 2^{-k(n-lambda)/p}).
```

Summing yields the vanishing modulus
`eta_N(1+log(M/eta_N))`. Local input is controlled by global `L^p`
boundedness, and bounded-origin input decays like `|x|^{-n}` on far output
balls.

## Files

- `main.tex`: source question, theorem, proof, scope, and novelty check.
- `solution_packet.pdf`: compiled review packet.
- `verification.md`: mathematical, computational, and render checks.
- `source_paper.pdf`: arXiv source PDF.
- `figures/open_problem_crop.png`: the source question on PDF page 9.
- `code/verify_dyadic_modulus.py`: numerical stress test of the dyadic bound.

Status: candidate full proof, likely valid. Independent human review is
requested, especially of the noncompact-tail use of the source size condition.
