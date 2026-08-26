# Eventual ultraboundedness: a sharp nonlocal threshold

Status: `candidate_sharp_partial_obstruction_likely_valid`.

Source: P. Cattiaux, M. Fathi, and A. Guillin, *Self-improvement of the
Bakry--Emery criterion for Poincaré inequalities and Wasserstein contraction
using variable curvature bounds*, arXiv:2002.09221, page 26.

## Result

The source asks for an example in which `sup_x r(2 eta,x,x)` is finite at one
time although the semigroup is not ultrabounded at every positive time.  The
packet first observes that, for a symmetric Markov kernel, the diagonal
hypothesis is exactly eventual ultraboundedness.

It then gives a sharp counterexample once the local Langevin-diffusion
restriction is removed.  On the normalized torus, let

```text
P_t = (I-Delta)^(-t).
```

This is the conservative reversible Markov semigroup obtained by Gamma
subordination of Brownian motion.  Its kernel is bounded exactly when
`t>d/2`.  Hence `r(2 eta,x,x)` is bounded for every `eta>d/4`, while the
semigroup is not ultrabounded in the source's all-times sense.

The proof is self-contained: absolute convergence of the Fourier series gives
the upper half of the threshold, and the periodized Gaussian heat kernel in
the Gamma integral gives a power or logarithmic singularity at the origin for
`t<=d/2`.

## Scope

This is a sharp partial obstruction, not a full answer to the source's
finite-dimensional Langevin question.  The generator `log(I-Delta)` is
nonlocal, whereas the source works with `Delta-grad(V).grad` on Euclidean
space.  Thus the result proves that symmetry, reversibility, compact state
space, and the Markov property do not force one-time smoothing to propagate
backwards; any positive theorem must use locality or an equivalent diffusion
structure.

The packet also records eight focused upgrade attempts, including an exact
star-chain model, a one-dimensional hitting-time route invalidated by a
published correction, standard smooth-potential tests, and a plateau-potential
construction whose missing global upper estimate remains the decisive gap.

See `solution_packet.pdf` for the complete theorem, proof, literature scope,
and human-review checklist.
