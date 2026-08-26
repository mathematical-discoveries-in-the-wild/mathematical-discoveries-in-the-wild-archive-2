# Monomial linearizations satisfy the bulk stability assumptions

Status: `candidate_partial_likely_valid_all_monomial_degrees`.

Source: Laszlo Erdos, Torben Kruger, and Yuriy Nemish, *Local laws for
polynomials of Wigner matrices*, Journal of Functional Analysis 278 (2020),
108507, arXiv:1804.11340. After Theorem 2.14, the authors ask whether every
self-adjoint polynomial has a linearization satisfying their assumptions
(M1) boundedness and (M2) stability throughout every kappa-bulk.

## Result

For every integer `k>=2`, the standard symmetric `k x k` linearization from
Appendix A.1 of the source satisfies (M1)-(M2) for the self-adjoint polynomial

```text
p_k(x) = 1 + x^k
```

on every kappa-bulk. Consequently the source's conditional optimal bulk local
law applies to `1+(X^(N))^k` for every monomial degree.

Let `A_k` be the reversal permutation matrix, `J=e_1 e_1^T`, and let `D_k`
have a zero first row and column and the reversal matrix `A_(k-1)` in its
lower-right block. The standard linearization is

```text
L_k(x) = J - D_k + x A_k.
```

For `w=z-1`, put `C_z=((1-z)J-D_k)A_k`. Then

```text
(L_k(x)-zJ)A_k = xI + C_z,
det(xI+C_z) = x^k-w.
```

If `r_1,...,r_k` are the roots of `r^k=w`, the eigenvalues of `M(z)A_k`
are the semicircle Stieltjes values

```text
m_sc(r_j) = integral (x-r_j)^(-1) d mu_sc(x).
```

They satisfy `m^2+r m+1=0`. Vectorizing the stability operator gives
`I-(M A_k) tensor (M A_k)`. If it were singular, two roots would obey
`m_sc(r_i)m_sc(r_j)=1`. The quadratic identity would force `r_i=r_j`.
Away from `w=0` the roots are distinct, so `i=j`, then `m_sc(r_i)^2=1`
and `r_i=+/-2`. These are precisely spectral-edge values. The critical value
`w=0` has infinite limiting density. Neither case belongs to a kappa-bulk.
Compactness and the large-imaginary-part estimate then give the uniform bounds
required in (M1)-(M2).

## Scope and verification

This is a substantial infinite family but not a full solution for arbitrary
multivariable noncommutative polynomials. The monomial local law can also be
deduced more directly from the ordinary Wigner local law and spectral mapping;
the new point here is the exact verification of the source's linearization
conditions in every degree.

The included symbolic/numerical checker verifies the linearization determinant
and Schur complement for degrees 2 through 12, and tests the stability-spectrum
formula at representative complex spectral parameters. It is evidence only;
the all-degree proof is in the packet.

A bounded search through 2026-08-11 covered the run indexes, the exact open
sentence, the title/arXiv id with `general polynomial`, `monomial`, `minimal
linearization`, `stability operator`, and `bulk local law`, and later arXiv
work on polynomial Wigner matrices. It found later quadratic edge results but
no exact statement of this all-degree monomial verification. Novelty confidence
is moderate-to-low because the companion-matrix argument may be folklore.

Human-review recommendation: accept as a likely valid partial result after
checking the uniform compactness step and the source's sign convention for its
standard linearization.

Packet PDF: `solution_packet.pdf`.
