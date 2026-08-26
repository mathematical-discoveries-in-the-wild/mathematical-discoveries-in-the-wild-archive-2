# The general-matrix quantum Boolean radius

Status: `candidate_full_class_by_class_answer_likely_valid`.

This packet answers the problem left in Remark 5.4 of Volberg--Zhang,
*Noncommutative Bohnenblust--Hille inequalities* (arXiv:2210.14468v4): what
happens when the self-adjointness restriction in their quantum Boolean-radius
theory is removed?

## Result

For the literal extension of their four matrix classes:

- the all-matrix radius is exactly zero;
- the degree-at-most-`d` radius is exactly zero for every `d>=1`;
- in exact positive degree `d`, the arbitrary-matrix radius lies between
  `(2/pi)^(1/d)` times the self-adjoint radius and the self-adjoint radius;
- for the union of positive homogeneous degrees, the comparison factor is
  `2/pi`.
- the identical collapse/comparison holds for complex-valued Boolean
  functions relative to real-valued functions;
- with that complex Boolean radius, the source's two-sided comparison extends
  verbatim to arbitrary matrices:

  ```text
  qBr_n^C(F_n^q) <= Br_n^C(F_n),
  Br_3n^C(F_3n) <= 3 qBr_n^C(F_n^q).
  ```

Consequently, the nonhomogeneous theory collapses because complex phases can
hide coefficient mass from the operator norm, while the homogeneous theory
retains all asymptotic orders proved in the source paper.

## Main mechanisms

The exact counterexample family is

```text
A_a = a I + i sqrt(1-a^2) P,
```

where `P` is any nonidentity self-adjoint Pauli string.  Each `A_a` is unitary,
but its quantum Boolean radius tends to zero as `a` tends to one.

For a positive homogeneous degree, phase averaging gives

```text
K_d^sa <= K_d^C <= (pi/2) K_d^sa
```

for the `ell_1` Pauli coefficient-to-operator-norm constants.  Taking
reciprocal `d`th roots gives the radius comparison.

The source's matrix-to-Boolean reduction is already valid for arbitrary
matrices and produces complex-valued functions.  Its coefficient identity
therefore proves the full factor-three comparison once the complex Boolean
radius is used.

## Files

- `main.tex` and `solution_packet.pdf`: expert-facing proof packet.
- `source_paper.pdf`: arXiv:2210.14468v4.
- `figures/open_problem_crop.png`: Definition 5.3 and Remark 5.4, page 16.
- `code/verify_general_matrix_radius.py`: numerical sanity checker.
- `verification.md`: proof checks, literature bounds, and PDF QA.

## Boundary

The packet treats the literal extension of the source definition.  It does
not compute the best possible homogeneous complexification constant, and it
does not study modified phase-invariant or traceless definitions.  The
novelty check is bounded through 2026-08-09, not exhaustive.
