# Fractional heat generator domains on the circle are algebras

Status: **candidate partial result; likely valid; human review requested**

Source: Adam Skalski and Ami Viselter, *Generating functionals for locally
compact quantum groups*, arXiv:1901.07477, Remark 2.9 on page 9.

## Result

The source asks whether its natural twisted-Fourier core

```text
span(D_+) intersect D(L)
```

is always an algebra for the generator of a symmetric quantum convolution
semigroup.

For the classical compact group `T` and every wrapped fractional heat
semigroup

```text
mu_t_hat(n) = exp(-t |n|^alpha),   0 < alpha <= 2,
```

the packet proves more: the entire generator domain on `C(T)` is closed under
pointwise multiplication. Therefore the source core is an algebra throughout
this family.

## Proof mechanism

If `A_alpha f` is continuous, periodic Riesz-potential estimates give

```text
omega_f(r) <= C ||A_alpha f||_infinity *
  r^alpha                 for 0 < alpha < 1,
  r log(e/r)              for alpha = 1,
  r                       for 1 < alpha < 2.
```

The fractional product rule has a carré-du-champ kernel comparable to
`|y|^(-1-alpha)`. The product of the two displayed moduli makes that integral
uniformly absolutely convergent in all three ranges, so the carré du champ is
continuous. Fractional-heat smoothing plus closedness of the generator then
proves product closure on the full domain. The endpoint `alpha=2` is the
classical `C^2(T)` heat-generator domain.

## Boundary and novelty

The general quantum-group question remains open. The packet does not cover
arbitrary convolution exponents even on the circle.

A bounded current-literature search found standard fractional Schauder and
Sobolev algebra machinery but no source explicitly stating either this
`C(T)` domain-algebra theorem or its identification as a partial answer to
Remark 2.9. The ingredients are standard, so novelty is **provisional**.

## Verification

Verdict: **likely valid**. No numerical experiment is used as proof evidence.
Human review should focus on the periodic Riesz-kernel translation estimate,
uniform graph-norm control of the carré-du-champ integral, and the source
identification `span(D_+) = A(T)`.

## Files

- `solution_packet.pdf`: review packet
- `main.tex`: complete proof source
- `source_paper.pdf`: original source paper
- `supporting_paper_stinga_2018.pdf`: fractional-Laplacian formula and
  Schauder comparison source
- `../../../attempts/1901.07477_generator_core_algebra_attempt.md`: failed
  general routes and the classical reduction that led to the theorem
