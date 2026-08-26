# Noncommuting Exponential Spectra in an Operator Algebra

Status: `candidate full result - likely valid pending human review`

Source: Hubert Klaja and Thomas Ransford, *Non-commutativity of the
exponential spectrum*, arXiv:1510.08109, Question 4.2 on PDF page 7.

## Result

There exists a separable complex Banach space `E` and operators `S,T` in
`B(E)` such that

```text
epsilon(ST) \ {0} != epsilon(TS) \ {0}.
```

In fact, `1/2` belongs to `epsilon(ST)` and does not belong to
`epsilon(TS)`.

## Construction

Use Motakis's space `X` for `K=S^4` from arXiv:2110.10868. For every scalar
Lipschitz function `f` on `S^4`, the diagonal operator `D_f` on `X` is
bounded, the assignment `f -> D_f` is multiplicative, and the Calkin class
`[D_f]` corresponds to `f` under an isomorphism

```text
Cal(X) ~= C(S^4).
```

Put `E=X direct-sum X` and amplify the lift entrywise to smooth
`2 x 2` matrix functions. Lift the explicit Klaja-Ransford functions `a,b`
to operators `S,T`. Their hard product satisfies

```text
I - 2ST = lift(I - 2ab),
```

whose Calkin image is the non-null-homotopic Klaja-Ransford map. Hence it
cannot be a product of exponentials. The reversed product has the explicit
form

```text
I - 2TS = exp(diag(D_g,0)),
g(z) = i * (pi - 4 arctan(z_2)).
```

Scaling by `1/2` does not change membership in the identity component of
the invertible group, which gives the asserted exponential-spectrum
separation.

## Literature and novelty bounds

- The run indexes and local arXiv corpus were searched for the exact arXiv
  id, title, Question 4.2, operator exponential spectrum, and the
  Klaja-Ransford/Motakis combination. No duplicate packet or matching result
  was found.
- Exact web searches and a citation-list check through 2026-08-17 found the
  2025 Daniel-Ghosh paper on `B(ell^p direct-sum ell^q)`. It proves
  commutativity for that special space and a one-way result from Calkin
  commutativity to operator-algebra commutativity. It does not state the
  existence result proved here.
- Motakis's paper contains no occurrence of Klaja, Ransford, or exponential
  spectrum, and exact web searches combining the two papers returned no
  connection.

The proof is a new synthesis of two published constructions, so novelty
confidence is moderate rather than definitive.

## Files

- `solution_packet.pdf`: formal proof packet.
- `main.tex`: LaTeX source.
- `problem.md`: exact question and scope.
- `solution.md`: plain-text proof companion.
- `verification.md`: adversarial proof and artifact audit.
- `references.md`: literature and novelty record.
- `source_paper.pdf`: arXiv:1510.08109.
- `supporting_paper_2110.10868.pdf`: Motakis's Calkin realization.
- `figures/open_problem_crop.png`: source Question 4.2 crop.

Human review should focus on the matrix amplification of Motakis's quotient
map and the exact explicit logarithm for the reversed product.
