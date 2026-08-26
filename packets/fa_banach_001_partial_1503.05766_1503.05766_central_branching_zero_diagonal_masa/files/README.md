# Partial result: central branching is the only maximality obstruction

Status: candidate partial result, likely valid, subject to human review.

Source: arXiv:1503.05766, Ken Dykema and Paul Skoufranis,
*Numerical Ranges in II_1 Factors*.

The sentence immediately before Lemma 6.1 asks whether every trace-zero
operator in a type `II_1` factor has zero conditional expectation onto some
MASA. The exact source page is included as
`figures/open_problem_crop.png`, and the compiled arXiv source is preserved as
`source_paper.pdf`.

## Result

Let `M` be a type `II_1` factor with separable predual and let `tau(T)=0`.
Choose, by Zorn's lemma, an abelian von Neumann algebra `A` maximal among those
satisfying `E_A(T)=0`, and put

```text
N = A' intersect M,    Z = Z(N),    g = E_Z(T).
```

The packet proves:

- `A` is diffuse.
- If `g=0`, then `A` is a MASA.
- In particular, if `Z=A`, then `A` is a MASA.
- If the central inclusion `A` contained in `Z` is relatively atomless, then
  `A` is a MASA.

Thus a non-MASA maximal zero-diagonal algebra would have to exhibit all three
features simultaneously: a strictly larger relative-commutant center, a
nonzero central expectation of `T`, and conditionally atomic central
branching.

The key lemma is a measurable fiberwise zero-diagonal construction: in a
finite von Neumann algebra with separable predual, a center-valued trace-zero
element has zero expectation onto an abelian algebra containing the center.
Matrix fibers use the elementary zero-diagonal induction and `II_1` fibers use
Lemma 6.1 of the source.

## Scope

This does not solve the full source question: the central obstruction need not
vanish abstractly. The finite algebra `M_2(C) direct_sum C`, with central
trace-zero element `I_2 direct_sum (-1)` under equal summand weights, shows
that only the trivial projections may have zero pairing. Eight materially
different upgrade attempts are recorded in
`../../../attempts/1503.05766_zero_diagonal_masa_upgrade_attempts.md` and
summarized in the packet.

Bounded searches through arXiv, exact-title/phrase queries, the author pair,
and MASA/zero-diagonal terminology found no later resolution. Marcoux's 2022
Problem 3.3 retains the broader C-star-algebra question. Novelty confidence is
moderate; the direct-integral lemma is standard in ingredients, while this
specific obstruction reduction was not found.

## Files

- `main.tex`: source transcription, theorem, proofs, attempts, and limitations.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: exact source paper compiled from the stored arXiv source.
- `figures/open_problem_crop.png`: rendered source evidence.
- `code/verify_finite_central_obstruction.py`: exhaustive rank check for the
  finite central obstruction.
- `VERIFIER_REPORT.md`: adversarial proof audit.

## Human review

Focus on the Effros-Borel measurable-selection step in the center-valued
zero-diagonal lemma and the use of conditional Lyapunov convexity for the
relatively atomless corollary. The rest is elementary conditional-expectation
and relative-commutant bookkeeping.
