# Spectral-radius criterion for every quadratic holomorphic polynomial

**Status:** complete theorem for the finite-dimensional question in Remark
1.5 / Remark 4.7, likely valid and pending human review; substantial partial
result relative to the paper's broader Brown-support question.

**Source:** Akihiro Miyagawa, *The spectra of polynomials in free
(semi)circular operators*, arXiv:2603.19528v2 (2026), Theorem 1.4 / Theorem 4.6
and Remark 1.5 / Remark 4.7.

## Result

For every `A in M_2(C)`, `b in C^2`, and nonzero `lambda`, let `Q_lambda` be
the structured `6 x 6` recursion matrix in the source.  Then

```text
Q_lambda^n e_1 does not tend to 0  iff  r(Q_lambda) >= 1.
```

Consequently, for every quadratic holomorphic polynomial

```text
P(c_1,c_2) = sum_{i,j} a_ij c_i c_j + sum_i b_i c_i,
```

one has

```text
spec(P(c_1,c_2)) = {0} union {lambda != 0 : r(Q_lambda) >= 1}.
```

This removes the source's restrictions `b=0`, `conjugate(A)A` having no
distinct real eigenvalues, or `A` being symmetric.

## Mechanism

If a spectral-radius eigenvalue were invisible from `e_1`, it would lie in the
lower block `[[0,conjugate(A_lambda)],[A_lambda,0]]`.  The source's determinant
reduction leaves only a positive simple con-eigenvalue.  Its con-eigenvector
reduces the problem to a scalar quadratic whose root lies in the closed unit
ball.  The free Szego kernel then places `lambda` in the spectrum, contradicting
the source theorem's characterization by the orbit of `e_1`.

## Scope and files

The result settles the sharper all-coefficient question about `Q_lambda`, but
does **not** prove that the Brown-measure support equals the spectrum.  Weak
eigenvalue-measure convergence does not by itself rule out spectral regions of
zero Brown mass.

- `main.tex` and `solution_packet.pdf`: theorem, proof, verification, and
  limitations.
- `source_paper.pdf`: locally compiled PDF of the cached arXiv v2 source.
- `figures/open_problem_crop.png`: Remark 1.5 on source PDF page 3.
- `runs/fa_banach_001/attempts/2603.19528_quadratic_spectral_radius_upgrade_attempts.md`:
  five focused routes, including the Brown-support upgrade obstruction.

The proof has no computational dependency.  Recommended human-review focus:
the determinant comparison that isolates the positive simple eigenvalue, the
transpose/conjugation conventions in the con-eigenvector step, and the
closed-ball extension of the free Szego-kernel lemma.

