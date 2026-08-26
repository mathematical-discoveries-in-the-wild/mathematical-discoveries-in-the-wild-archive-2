# Verification report — 1210.1287 nilpotent-shift OU spectrum

Verdict: `likely valid full literal counterexample; human review needed`.

## Exact scope

The packet disproves the hypothesis-free extension of source Theorem 1.1 to
all cases with empty `sigma_p(A*)`. The example also has empty `sigma(A)` and
does not decide the sharpened nonempty-spectrum/no-adjoint-eigenvalue case.

## Adversarial checks

1. **C0 drift semigroup.** The left shift on `L2(0,1)` is a strongly
   continuous contraction and is zero at every time `t>=1`.

2. **Adjoint point spectrum.** The generator is `f'` with boundary `f(1)=0`;
   its adjoint is `-g'` with boundary `g(0)=0`. Every exponential solution of
   `A*g=lambda g` is killed by the boundary condition.

3. **Admissible noise.** `B e_n=2^-n e_n` is bounded, nonzero, injective, and
   Hilbert-Schmidt. Hence each integrated covariance is positive trace class
   and defines a Gaussian Radon measure.

4. **Nondegeneracy.** For nonzero `x`, the integrand
   `||B S*(s)x||^2` is continuous and positive at zero, so its integral is
   positive. Thus `Q_infty` is injective and, being self-adjoint, has dense
   range. The invariant Gaussian is nondegenerate.

5. **Invariant covariance.** Splitting the covariance integral proves
   `Q_infty=Q_t+S(t)Q_infty S*(t)`. This is the standard Gaussian invariance
   identity.

6. **Eventual projection.** At `t>=1`, both `S(t)=0` and `Q_t=Q_infty`, so the
   Mehler formula gives `P(t)=Pi`, the expectation projection, on bounded
   functions and therefore on its `L1` contraction extension.

7. **Invariant decomposition.** Constants and the mean-zero kernel of `Pi`
   form a bounded invariant direct sum of `L1`.

8. **Entire mean-zero resolvent.** On the mean-zero subspace `P_0(t)=0` for
   `t>=1`. The finite Laplace transform from zero to one is a two-sided inverse
   to `lambda-L_0` for every complex `lambda`; the time-one boundary term is
   zero.

9. **Full spectrum.** Every nonzero complex number is in the resolvent of the
   direct-sum generator, while zero is an eigenvalue with eigenvector `1`.
   Hence `sigma(L)={0}`.

10. **Prior attribution.** Van Neerven–Priola Example 2.9 is included and
    credited for the nilpotent-shift identity. It does not supply the present
    `L1` spectrum statement. Novelty is intentionally described as limited.

## Residual review risk

The main risk is interpretive: the 2012 author may have intended to retain a
nonempty drift spectrum although the displayed open question does not say so.
The packet therefore labels the result as a full answer to the literal wording
and states the surviving sharpened problem prominently.

## Artifact verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed cleanly.
- The final log contains no warnings, undefined references, overfull boxes, or
  underfull boxes.
- All five pages of `solution_packet.pdf` were rendered at 144 dpi and visually
  inspected. The source theorem/question, supporting prior example, equations,
  proofs, and bibliography are legible and unclipped.
- `solution_packet.pdf` SHA-256:
  `c86a6a53696b6a28d11c9683d7bedcbfe95b7547791f30bfe392d0336d3b8825`.
- `source_paper.pdf` SHA-256:
  `0fa0bd9728cf8f13ef6d70573e0d72214fac7b6a1c079e0ee2cb67fc7ed376bd`.
- `supporting_prior.pdf` SHA-256:
  `748308b168334ec6299a19184ece3f5115748b96bd977c7651b8f7ab08b31c47`.
