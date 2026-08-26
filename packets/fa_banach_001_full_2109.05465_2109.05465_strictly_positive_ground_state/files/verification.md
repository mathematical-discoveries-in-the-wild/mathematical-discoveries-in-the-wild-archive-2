# Verification report

Verdict: `candidate_full_affirmative_answer_likely_valid`

## Target audit

The exact open problem is on source PDF page 9. It assumes
`sigma_d(W_V(b)) subset [-2,2)` for `0 <= V in L^1(R)` and asks whether a
lowest eigenfunction can be chosen strictly positive. The packet covers this
full setting. For nonzero `V`, source Theorem 1.3 supplies a discrete
eigenvalue; for `V=0`, the question has no lowest discrete eigenfunction and
is vacuous.

## Kernel audit

- For `lambda=-2 cos(omega)` with `0<omega<pi`, numerator and denominator in
  the source Green kernel have the same sign away from zero, and their ratio
  has a positive diagonal limit.
- At `lambda=-2`, the exact limit is
  `G(t)=t/[2 b^2 sinh(pi t/b)]`, with `G(0)=1/(2 pi b)`.
- Both kernels are bounded, continuous, decay exponentially, belong to
  `L^2(R)`, and are strictly positive everywhere.

## Compactness and Perron audit

- `K_lambda=sqrt(V) G_lambda sqrt(V)` is Hilbert--Schmidt because
  `||K||_HS^2 <= ||G||_infty^2 ||V||_1^2`.
- On `S={V>0}`, its kernel is strictly positive almost everywhere, so it is
  positivity improving.
- The packet proves the needed compact Perron statement directly. In
  particular, any second top eigenvector would change sign, and
  `<|w|,K|w|>-<w,Kw>=4<w_+,K w_->>0` contradicts maximality of the Rayleigh
  quotient.

## Birman--Schwinger audit

- Eigenvalue correspondence puts `1` in `sigma(K_lambda0)`.
- The counting principle says eigenvalues of `K_lambda0` above one count
  eigenvalues of `W_V(b)` strictly below the ground eigenvalue; there are
  none.
- Since `K_lambda0` is nonnegative, its spectral radius is therefore exactly
  one. The simple Perron eigenspace corresponds to a simple ground-state
  eigenspace.

## Reconstruction and domain audit

For the positive Perron vector `phi`, let `h=sqrt(V)phi`. Then `h in L^1` by
Cauchy--Schwarz and `psi=G*h in L^2` because `G in L^2`. The identity
`K phi=phi` gives `sqrt(V)psi=phi` and hence `V psi=h`. The Fourier integral

```text
integral 2 cosh(2 pi b k) |hhat(k)|^2
         / (2 cosh(2 pi b k)-lambda0)^2 dk
```

is finite, so `psi` lies in the free form domain. The form identity therefore
places it in the Friedrichs operator domain with eigenvalue `lambda0`.
Finally, convolution of the continuous positive kernel with nonzero
`h>=0` is continuous and strictly positive at every point.

## Novelty audit

Searched on 11 August 2026:

- the run registry and lightweight solution/attempt/proof-gap indexes;
- the local parsed arXiv corpus for the arXiv id, exact question, operator
  notation, and positivity keywords;
- external exact-phrase, title/author, DOI/citation-oriented, author-page, and
  functional-difference ground-state searches;
- adjacent 2025 work by Ilyin--Laptev--Schimmer--Zernova on nonselfadjoint
  functional-difference operators.

No later explicit answer was found. Novelty confidence is moderate, and this
is not a priority claim.

## Human verifier focus

1. Confirm the quadratic-form Birman--Schwinger counting statement for the
   source's `L^1` potentials.
2. Recheck the endpoint `lambda0=-2` limit and its strict positivity.
3. Check that the form-domain estimate completes the resolvent
   reconstruction without assuming `sqrt(V)phi in L^2`.

## Artifact audit

The final packet compiled without unresolved references, overfull boxes, or
layout warnings. All four pages were rendered at 150 dpi and inspected
individually on 11 August 2026; the source crop, formulas, margins, page
breaks, and reference are clear and unclipped.

```text
solution_packet.pdf  7eea84bdf5ba4f6d72d5517f57b55046ab7424b3808a1d483cecdd2805378e4f
source_paper.pdf      22353b679cde2d019099e63cbe658f52a4a105b7fb3101b06a88993277c319e8
open_problem_crop     2849d3a8d3640b55ca7a32307d5cb7f5f95134101d429a3b19726fae935dcb20
```
