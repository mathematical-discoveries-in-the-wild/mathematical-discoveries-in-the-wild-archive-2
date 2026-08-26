# Counterexample packet: strong Birkhoff--James bases at every point

## Source

- Debmalya Sain, Kallol Paul, and Lokenath Debnath,
  *Characterization of inner product spaces*, arXiv:1407.5016.
- Target: Conjecture 2.11 on page 6 of the arXiv PDF.
- Model: GPT5.6.

## Classification

- Status: `counterexample_likely_valid`.
- Scope: full disproof in every finite dimension at least three.

## Result

Fix conjugate exponents `p,q in (1,infinity)` with `p != 2`. On `R^2`, use
the `ell_p` norm in the two quadrants where the coordinate product is
nonnegative and the `ell_q` norm in the other two quadrants. This is a smooth,
strictly convex, non-Euclidean Radon norm: Birkhoff--James orthogonality is
symmetric.

For every `n >= 3`, take the Euclidean sum

```text
X_n = E_p direct_sum_2 ell_2^(n-2).
```

It remains smooth, strictly convex, and non-Euclidean. Nevertheless every unit
vector of `X_n` belongs to a strongly orthonormal Hamel basis in the sense of
Birkhoff--James. An explicit basis and all its norming functionals are given in
the packet. Thus Conjecture 2.11 is false, even under the extra hypothesis of
strict convexity.

## Idea of Proof

For a unit vector `(r a, s c)` in the Euclidean sum, choose a unit Radon partner
`b` with `a perpendicular_B b` and `b perpendicular_B a`. The first three
basis vectors are

```text
(r a, s c),  (-s a, r c),  (b,0).
```

Complete `c` orthonormally in the Hilbert summand. The unique norming
functionals have the same two-by-two rotation pattern and vanish on every
other basis vector. Strict convexity turns these supporting equalities into
the strict inequalities required by strong orthonormality.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled and visually inspected proof.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: exact source excerpt.
- `code/verify_counterexample.py`: deterministic numerical checks.
- `code/crop_source.py`: exact source-crop helper.
- `verification_report.md`: mechanical and visual checks.
- `novelty.md`: bounded novelty-search record.

