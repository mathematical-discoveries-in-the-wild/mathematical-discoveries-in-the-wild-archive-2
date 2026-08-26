# Noncanonical invariant hyperplanes below exponential order

Status: `candidate_counterexample_likely_valid`

Source: José Bonet and Antonio Galbis, *Invariant subspaces of the integration
operators on Hörmander algebras and Korenblum type spaces*, arXiv:2003.13573,
Remark 5.4, page 10.

## Result

The hoped-for extension of Theorem 5.1 is false throughout the concrete family
highlighted in Remark 5.4.

Let `p_s(z)=|z|^s` and `Jf(z)=integral_0^z f(w)dw`. For every nonzero complex
number `mu`, set

`Lambda_mu(f)=sum_(n>=0) mu^n f^(n)(0)`.

- If `0<s<1`, `Lambda_mu` is continuous on both `A_p_s(C)` and
  `A_p_s^0(C)`.
- If `s=1`, it is continuous on the infraexponential algebra `A_|z|^0(C)`.

It satisfies `Lambda_mu(Jf)=mu Lambda_mu(f)`. Hence its kernel is a closed
codimension-one `J`-invariant subspace. This kernel is not one of the
vanishing-jet subspaces from Theorem 5.1, because it contains `z-mu`, whose
constant term is nonzero.

Thus the classification fails for every `0<s<1` in both algebras and for the
remaining `s=1` Fréchet algebra. The already-positive case
`A_|z|(C)=Exp(C)` from Theorem 5.3 is not contradicted.

## Mechanism

Cauchy's estimate gives

`|f^(n)(0)| <= n! ||f||_(a,s) (eas/n)^(n/s)`.

For `s<1`, the factor `n^(1-1/s)` decays polynomially inside the `n`th power,
so the derivative sequence decays faster than every geometric sequence. This
makes its generating function a continuous adjoint eigenfunctional. At
`s=1`, the same argument works on the zero-type algebra because one may choose
an arbitrarily small defining exponential seminorm.

## Novelty check

A bounded search on 2026-08-09 covered the exact title and arXiv id, the exact
phrases `integration operator invariant subspaces entire functions of order`,
`Hörmander algebras p(z)=|z|^s`, `infraexponential invariant subspaces`, and
`Borel transform integration operator invariant subspace`. It found the source
paper and related operator papers, but no later arXiv paper resolving Remark 5.4
or using these hyperplanes. Novelty confidence is moderate, not definitive.

## Files

- `main.tex`: complete counterexample theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Remark 5.4 on page 10.
- `VERIFICATION.md`: adversarial verifier report.

## Human review recommendation

Check the continuity argument on the (LB)-topology of `A_p_s`, then check that
the eigenfunctional identity uses the paper's normalization of `J`. If those
two points pass, accept this as a full negative answer for the entire family
explicitly singled out in Remark 5.4.

