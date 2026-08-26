# Infinite annuli refute the universal erfc plunge profile

**Status:** candidate full counterexample, likely valid, pending expert review.

**Source:** Simon Halvdansson, *Empirical plunge profiles of time-frequency
localization operators*, arXiv:2502.11805, Conjecture 2.6 on printed page 13.

## Result

There is a compact, regular-closed, rotationally invariant set
`Omega subset R^2` whose boundary has finite one-dimensional Hausdorff measure
for which the uniform `O(1/R)` erfc eigenvalue profile in Conjecture 2.6 fails.
In fact,

```text
limsup_R R sup_k |lambda_k^(R Omega) - predicted_erfc_profile(k,R)| = infinity.
```

The set is a countable union of concentric, ultrathin annuli accumulating at
the origin. In the radial coordinate `t = pi |z|^2`, the annuli are intervals
`[a_m,a_m+ell_m]` with `a_m=4^(-m)` and inductively tiny `ell_m`.

Radial localization operators have the Hermite basis as a common eigenbasis,
and their unordered eigenvalues are exact Gamma-density integrals. At a scale
`R_m`, the `m`-th annulus has large scaled boundary length but its whole
spectral bump is bounded by `C R_m ell_m/sqrt(a_m)`, chosen to tend to zero.
All later annuli are spectrally negligible at that scale. The finite earlier
annuli obey the source paper's proved erfc law. Consequently the actual
fixed-level eigenvalue count misses an unbounded boundary contribution, while
the conjectured uniform profile would force only `O(1)` counting error.

## Scope

The counterexample targets the stated finite-boundary-length hypothesis. Its
boundary has infinitely many components and is not uniformly Ahlfors regular.
It therefore does not refute a possible corrected theorem for finitely many
boundary components, uniformly Ahlfors-regular boundaries, or sufficiently
smooth domains. The source explicitly distinguishes its finite-component
Proposition 2.5 from the full-generality Conjecture 2.6.

## Packet contents

- `solution_packet.pdf` / `main.tex`: construction and proof.
- `source_paper.pdf`: arXiv:2502.11805.
- `figures/open_problem_crop.png`: source crop of Conjecture 2.6 and its
  counting-function interpretation.

## Verification and novelty

The proof is symbolic and has no computational dependency. Review should
focus on the inductive choice of annulus widths, the Poisson maximal-atom
bound, and the passage from a uniform eigenvalue profile to an `O(1)`
fixed-level counting law.

A bounded search on 2026-08-09 covered the run indexes, the arXiv id and exact
title, the conjecture's erfc formula, boundary-universality terminology, and
the author's 2025 thesis. The thesis still presents the statement as a
conjecture, and no later resolution or infinite-annulus counterexample was
found. This is not an exhaustive MathSciNet or zbMATH priority search.

