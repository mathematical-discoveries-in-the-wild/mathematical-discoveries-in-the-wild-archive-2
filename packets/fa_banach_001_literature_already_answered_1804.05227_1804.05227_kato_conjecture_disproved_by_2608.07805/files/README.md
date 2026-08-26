# Kato's positive-commutator conjecture was disproved by arXiv:2608.07805

Status: `literature_already_answered` (negative answer).

Herbst and Kriete's Conjecture 1.4 in *The Howland--Kato Commutator
Problem*, arXiv:1804.05227, asks whether every nonzero positive commutator
`i[f(P),g(Q)]` for increasing bounded real `f,g` must satisfy
`f in K_a`, `g in K_b` for strip widths with `ab=pi/2`.

Rupert L. Frank and Paata Ivanisvili, *A counterexample to the Kato
conjecture for positive commutators*, arXiv:2608.07805 (7 August 2026),
explicitly identifies this conjecture and disproves it.  Their Theorem 1 proves

```text
i[arctan(P), arctan(Q)] >= 0,     Tr C = pi/2,
```

so the commutator is nonzero.  Both functions are increasing.  Their
Proposition 15 says `arctan` belongs to `K_1` but to no `K_a` with `a>1`,
whereas `-arctan` belongs to no positive-width Kato class.  Therefore no
simultaneous sign choice can produce widths `a,b` with `ab=pi/2>1`, and their
Corollary 3 explicitly states that the Kato conjecture fails.

This is an exact, author-aware literature answer: the supporting authors cite
Herbst--Kriete and label the same formulation.  It is therefore not counted as
a new pipeline counterexample.

