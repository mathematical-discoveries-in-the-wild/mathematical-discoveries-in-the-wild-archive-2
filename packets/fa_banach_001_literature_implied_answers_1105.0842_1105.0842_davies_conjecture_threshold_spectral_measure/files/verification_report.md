# Verification report

## Claim checked

For every source-Theorem-3.19 operator and for the locally twisted shifted
Dirichlet Laplacian, the heat kernel has a strictly positive fixed-point
`t^(-3/2)` limit coefficient, hence satisfies Davies' ratio limit.

## Source-location check

- `source_paper.pdf` has 24 pages.
- The exact open statement is Appendix C, Remark C.2, PDF page 22.
- The current PDF numbers the general elliptic result Theorem 3.19 (PDF page
  16); older source text may number it Theorem 3.18.
- The fixed-point diagonal estimate appears as (1.6) for the twisted tube and
  (3.66) in Theorem 3.19 for the general class.

## Supporting-source check

- `supporting_paper_1705.08972.pdf` has 51 pages.
- The black-box framework allows multiple cylindrical ends and Dirichlet
  waveguides by taking the end cross-section to be a disjoint union.
- Shifting by `E_1` replaces the transverse Dirichlet operator by
  `H_Y=-Delta^D_omega-E_1 >= 0`, which satisfies the abstract hypotheses.
- Lemma 2.4 makes each zero-channel generalized eigenfunction smooth in the
  zero threshold coordinate after ruling out a pole.
- Lemma 2.5, equation (2.24), gives the continuous spectral-measure jump.
- Lemma 2.6 identifies the `1/lambda` cutoff-resolvent singularity with the
  values `Phi_j(0)` and states the threshold-resonance criterion.

## Stone-factor audit

With `R(lambda)=(H-lambda^2)^(-1)`, Stone's formula is

```text
dE(lambda^2)
 = (1/(2 pi i)) [R(lambda)-R(-lambda)] 2 lambda d lambda.
```

Below the first positive transverse threshold, Lemma 2.5 is

```text
(1/i)[R(lambda)-R(-lambda)]
 = (1/(2 lambda)) sum_j Phi_j(lambda) tensor Phi_j(lambda).
```

Multiplying gives

```text
dE(lambda^2)
 = (1/(2 pi)) sum_j Phi_j(lambda) tensor Phi_j(lambda) d lambda.
```

If `Phi_j(lambda)=lambda Psi_j+O(lambda^2)`, then

```text
(1/(2 pi)) integral_0^infinity exp(-t lambda^2) lambda^2 d lambda
 = 1/(8 sqrt(pi) t^(3/2)).
```

This confirms the coefficient in the packet.

## Obstruction audit

1. A zero eigenfunction gives a nondecaying nonnegative diagonal term and is
   incompatible with the source upper bound.
2. A nonzero `Phi_j(0,x)` gives a nonnegative continuous spectral density
   bounded below at `x`, hence a `t^(-1/2)` diagonal lower bound.  There is no
   cancellation because the density is a sum of squared moduli.
3. Once the zero eigenprojection and resonance vanish, meromorphic regularity
   gives a pole-free neighborhood of zero, so positive embedded point spectrum
   cannot accumulate into the low-energy integral.
4. The high spectral part is exponentially small pointwise after placing the
   time-one heat kernel on both sides; this avoids treating point evaluation
   as an `L^2` vector.
5. The diagonal lower estimate forces `B(x,x)>0`.  The source explicitly cites
   fixed-point heat-kernel equivalence; standard parabolic Harnack chaining
   gives the same comparison for the general uniformly elliptic class and
   makes every `B(x,y)` strictly positive.

## Computational status

No numerical computation is used.  The Gaussian integral and all constants
are evaluated exactly.  The evidence is the two local PDFs plus the displayed
operator and spectral-measure identities.

## Render verification

- `solution_packet.pdf` has 3 letter-sized pages.
- `latexmk` completed successfully after two cross-reference passes.
- The final log has no unresolved references, warnings, overfull boxes,
  underfull boxes, or errors.
- All three pages were rendered to PNG at 144 dpi and visually inspected.
  Equations, citations, margins, page numbers, and both bibliography entries
  are readable and unclipped.
- Final packet SHA-256:
  `17b320162dab0ff6c2bd5cc52983736d9d691af85b31e9d9cddae9d3d37fdbfb`.
