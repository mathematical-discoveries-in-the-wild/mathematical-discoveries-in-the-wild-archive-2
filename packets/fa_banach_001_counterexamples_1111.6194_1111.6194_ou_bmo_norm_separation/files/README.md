# Ornstein-Uhlenbeck separation of semigroup BMO norms

**Status:** candidate counterexample, likely valid, pending expert review.

**Source:** Marius Junge and Tao Mei, *BMO spaces associated with semigroups
of operators*, arXiv:1111.6194, open problem (ii)(a),(c),(c') on printed
page 33.

## Result

The requested comparisons in (c) and (c') fail for the classical
one-dimensional Ornstein-Uhlenbeck semigroup on Gaussian space, despite its
being symmetric, ergodic, analytic, hypercontractive, and satisfying the
strict Bakry-Emery curvature inequality `Gamma_2 >= Gamma`.

For the bounded truncations

```text
f_R(x) = max(-R,min(x,R)),
```

one has

```text
||f_R||_bmo(T) <= 1,
||(T_t-T_2t)f_R||_infinity -> infinity  (every fixed t>0),
||f_R||_BMO(T) -> infinity.
```

Thus no constant can make (c') hold, and the two seminorms in (c) are not
equivalent even on bounded functions in one fixed classical semigroup. On the
natural `L_2` completion the separation is strict: the coordinate `h(x)=x`
has `||h||_bmo(T)=1` but `||h||_BMO(T)=infinity`.

The same coordinate also shows that the strong hypotheses above do not force
the triple comparison in (a). For the subordinated Poisson semigroup `P`,

```text
||h||_BMO(Gamma) = 1/2,
||h||_BMO(P) = ||h||_BMO(partial) = infinity.
```

Moreover, the bounded truncations have uniformly bounded `BMO(Gamma)` norm
while their `BMO(P)` norms diverge.

## Proof mechanism

Mehler's formula makes the little-`bmo` expression a conditional variance.
A 1-Lipschitz truncation cannot have larger variance than its Gaussian input,
so the little-`bmo` norms stay bounded. In contrast, the OU drift moves the
coordinate mean from `e^(-t)x` to `e^(-2t)x`. Truncation only hides this drift
at finite radius; `L_2` convergence to the unbounded coordinate forces the
`L_infinity` norm of the drift difference to diverge. Kadison's inequality
puts that difference below the big-`BMO` norm.

For part (a), the carré du champ sees only the bounded derivative of the
coordinate, whereas the Poisson oscillation norms also see its unbounded
mean drift.

## Scope

This is a full negative answer to the universal estimates (c) and (c') and a
counterexample to (a) under a particularly strong natural hypothesis package.
It is not a complete characterization of all semigroups for which the norms
are equivalent. It does not contradict the source's positive theorem for the
Poisson comparison in (b), nor later sufficient-condition theorems for (c).

## Packet contents

- `solution_packet.pdf` / `main.tex`: theorem, proof, scope, and literature
  bounds.
- `source_paper.pdf`: arXiv:1111.6194.
- `figures/open_problem_crop.png`: printed page 33, open problem (ii).
- `code/verify_ou_truncations.py`: non-proof numerical check of Mehler
  formulas for several truncation radii.

## Verification and novelty

The proof is exact and has no computational dependency. The included script
checks the conditional-variance formula and the linear growth of the drift
term on a finite grid.

A bounded search on 2026-08-09 covered the run indexes; exact and close-variant
arXiv searches for the displayed norm comparison, the `T_t-T_2t` term, and
Ornstein-Uhlenbeck counterexamples; arXiv:1204.5082, 1701.06623, and
1907.07375; and the locally available arXiv source corpus. The 2012 follow-up
states that the two norms may differ, gives sufficient conditions for
equality, and notes that OU fails one of those conditions, but the searched
sources did not give this explicit coordinate/truncation separation or the
part-(a) separation. Novelty is therefore provisional; this was not an
exhaustive MathSciNet or zbMATH priority search.

**Human-review recommendation:** high priority. Check the source's intended
domain (`L_infinity` versus its `L_2` completion), the one-line Lipschitz
variance bound, and the subordination gradient estimate. The bounded
truncations make the negative answer to (c),(c') independent of the domain
convention.
