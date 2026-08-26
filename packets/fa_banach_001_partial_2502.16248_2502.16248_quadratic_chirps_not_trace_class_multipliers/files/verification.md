# Verification report

Status: `candidate_substantial_partial_result_likely_valid_needs_human_review`

## Mathematical audit

1. **Gaussian normalization.** For
   `g_r(t)=(2r)^(d/4) exp(-pi*r*|t|^2)`, direct Gaussian integration gives
   `||g_r||_2=1`; hence `G_r=g_r tensor g_r` has trace and Hilbert--Schmidt
   norms one.
2. **Ambiguity formula.** Substituting the source's symmetric
   time--frequency shift gives
   `FW(G_r)(x,xi)=exp[-pi/2*(r|x|^2+r^(-1)|xi|^2)]`.  Its squared `L2` norm
   is one.
3. **Centered kernel convention.** With `u=(t+s)/2` and `x=t-s`, the kernel
   is the inverse Fourier transform in `xi` of `FW(A)(x,xi)`.  The symmetric
   phase in `rho(x,xi)` cancels exactly; no residual `x*xi` phase remains.
4. **Complex Gaussian.** Multiplication by `exp(pi*i*c*(|x|^2+|xi|^2))`
   changes the `xi` Gaussian coefficient to
   `D_(r,c)=1/(2r)-i*c`.  Since `Re D_(r,c)>0`, the standard complex Gaussian
   integral and the principal square-root branch are valid.
5. **Schur estimate.** Taking absolute values retains a nonnegative Gaussian
   in `u` and a factor `exp(-pi*r*|t-s|^2/2)`.  Dropping the former and using
   `|D_(r,c)|>=|c|` makes both Schur integrals at most
   `(2/(|c|r))^(d/2)`.
6. **Trace lower bound.** For trace-class `A`, singular values give
   `||A||_2^2 <= ||A||_infinity ||A||_1`.  The chirp output has
   `||A||_2=1`, so its trace norm is at least `(|c|r/2)^(d/2)`.
7. **Sine cancellation check.** The sine output is the difference of the
   `c=1` and `c=-1` chirp outputs divided by `2i`; its operator norm still has
   the bound `(2/r)^(d/2)`.  Its squared Hilbert--Schmidt norm is an exact
   `sin^2` Gaussian integral.
8. **Oscillatory term.** The complex term in that integral has modulus
   `((r^2+4)(r^(-2)+4))^(-d/4)`.  Since
   `(r^2+4)(r^(-2)+4)=17+4(r^2+r^(-2))>=25`, the squared Hilbert--Schmidt
   norm is at least `(1-5^(-d/2))/2` for every `r>0`.
9. **Conclusion.** The input trace norms stay one and the output trace-norm
   lower bounds diverge, so the relevant multiplier maps cannot be bounded on
   `S^1`.

## Upgrade-attempt audit

- The proof was extended from the source's sine to every nonzero radial
  quadratic chirp and finite nonconstant chirp sums.
- The completely-bounded reduction was checked as the natural full-problem
  route.  No proof that bounded continuous Weyl multipliers are automatically
  completely bounded was found.
- Compact-support exhaustion and Lagrangian restriction were tested.  Both
  encounter a genuine concentration/uniformity obstruction measured by the
  same squeezed Gaussian family.

## Computational audit

Running

```text
conda run --no-capture-output -n sandbox python \
  code/verify_gaussian_bounds.py
```

reproduces the exact lower-bound constants for several dimensions and
squeezing parameters, verifies the Gaussian-product inequality symbolically
at high precision, and checks the predicted divergence.  The script is a
sanity check only; every global estimate in the packet is analytic.

## Literature audit

- Cheap registry, solution, attempt, and proof-gap indexes contained no exact
  row for arXiv:2502.16248 or Question 1.
- Exact-question and exact-candidate searches found only the source paper.
- Searches for quadratic chirps, Fourier--Wigner trace-class multipliers,
  bounded Weyl-covariant maps, twisted Fourier multipliers, and citing works
  through 2026-08-11 found no later answer or the packet theorem.
- Werner's 1984 paper treats positive covariant correspondence rules and does
  not settle arbitrary bounded trace-class multipliers.

## Rendering audit

The final packet is a four-page US-Letter PDF.  The final `latexmk` log has no
warnings, undefined references, overfull boxes, or underfull boxes.  All four
pages were rasterized at 150 dpi with Poppler and inspected individually; the
displayed equations, citations, proof-ending symbols, margins, and page breaks
are clean, and the source-paper crop on page 1 is legible.  The final packet and
the compiled `tmp/main.pdf` are byte-identical, with SHA-256
`dd07e69acef61e01aa3776900dc65665913cb89b13d403869621bab3527b8690`.
