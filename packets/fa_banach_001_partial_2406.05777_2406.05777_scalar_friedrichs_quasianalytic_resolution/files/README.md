# Scalar Friedrichs Quasi-Analytic Resolution

Source: N. A. Caruso and A. Michelangeli, *Open problems and perspectives on
solving Friedrichs systems by Krylov approximation*, arXiv:2406.05777v2,
Question 3 (Section 4, PDF page 11).

Status: likely valid coefficient-wide strong partial resolution, pending human
review. It can reasonably be viewed as a full resolution of the natural scalar
quasi-analytic-versus-smooth formulation, but the durable label remains
`partial` because the source question is open-ended rather than a precise
universal statement.

## Main result

Let `c in L^2_loc(R)` satisfy

```text
0 < delta <= Re c(x) <= M < infinity  a.e.
```

For the maximal closed realization `A_c=-d/dx+c(x)` on `L^2(R)`, every
nonzero quasi-analytic datum is Krylov-solvable:

```text
sum_{n>=1} ||A_c^n g||^(-1/n) = infinity
    implies
A_c^(-1)g in closure K(A_c,g).
```

The proof is coefficient-wide. The integrating factor is a unitary map from
the weighted space

```text
H_omega = L^2(R, exp(2 Re integral_0^x c) dx)
```

to ordinary `L^2`. It conjugates `A_c` to `-d/dx`, whose negative generates
right translation. Coercivity gives exponential stability for positive time.
A Denjoy-Carleman argument then places the whole group orbit of a
quasi-analytic datum in its closed Krylov space, and integrating the orbit
gives the inverse.

## Exact arbitrary-data criterion

For `g in C^infinity(A_c)`, put

```text
C(x) = integral_0^x c(s) ds,
q(x) = exp(-C(x)) g(x),
omega(x) = exp(2 Re C(x)).
```

The unique solution is

```text
f(x) = exp(C(x)) integral_x^infinity exp(-C(y)) g(y) dy.
```

It is Krylov if and only if `x -> integral_x^infinity q(y)dy` lies in the
`L^2(omega dx)` closure of `span{q,q',q'',...}`. This is an exact criterion
for every smooth datum, not only the quasi-analytic class.

Analytic vectors are dense for every admissible coefficient by Gaussian
group regularization, so the positive class is dense.

## Sharpness

For the constant coefficient `c=1`, Fourier transformation gives the exact
criterion

```text
(1-i xi)^(-1) in closure(polynomials) in L^2(|g-hat|^2 dxi).
```

Any two-sided exponential Fourier moment is sufficient. Conversely, an
affine-lognormal construction yields a nonzero Schwartz datum whose solution
is not Krylov. Its power norms grow at least like `const^n exp(n^2)`, so its
Carleman series converges: it is smooth but not quasi-analytic. Thus the
positive theorem and the obstruction fit without a gap.

## Files

- `main.tex`: self-contained theorem and proofs.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2406.05777v2.
- `figures/open_problem_crop.png`: source crop containing (4.4), (4.5), and
  Question 3.
- `verification.md`: adversarial verifier report.
- `code/lognormal_sanity.py`: high-precision regression checks, not used as
  proof.
- `tmp/`: LaTeX and rendering intermediates.

## Novelty check

A bounded run-index and arXiv/web search used the source title/authors and the
phrases `Krylov solvability Friedrichs`, `-d/dx+c(x) Krylov`, `analytic vector
Krylov-solvable`, stable semigroups, and quasi-analytic vectors. The closest
inspected works were arXiv:1811.08202, 2001.08127, 2102.13626, and 2210.04752.
No later explicit resolution of Question 3 or statement of the stable-group
theorem in this Krylov form was located. Novelty remains provisional; the
abstract lemma is a short classical Denjoy-Carleman application and may be
folklore.

## Human review recommendation

Preserve as a coefficient-wide strong partial result. Review especially:

1. the Denjoy-Carleman step for scalar group orbits;
2. the maximal-domain identification when the imaginary part of `c` is
   unbounded;
3. the Gaussian regularization proof of dense analytic vectors;
4. the affine-lognormal obstruction and its non-quasi-analytic growth bound.

