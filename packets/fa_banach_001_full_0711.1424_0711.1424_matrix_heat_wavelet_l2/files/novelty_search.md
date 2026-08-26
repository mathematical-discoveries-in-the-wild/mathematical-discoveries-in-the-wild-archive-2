# Bounded novelty and literature search

Date: 2026-08-13  
Agent/model: `agent_lane_10` / `GPT5.6`

## Searches performed

- Cheap run indexes: exact arXiv id `0711.1424`, exact title, `composite
  wavelet`, `matrix heat`, `positive definite cone`, and `Gårding--Gindikin`.
- Exact web/arXiv searches for the title and Problems A--C.
- Keyword searches combining matrix spaces, cone-valued scaling, heat
  semigroups, Calderón reproduction, admissible wavelets, and Cayley
  derivatives of matrix-gamma densities.
- Full-source inspection of the closest cited predecessor:
  G. Ólafsson, E. Ournycheva, and B. Rubin, arXiv:math/0409100.

## Findings

The closest predecessor proves `L2` reproduction and Riesz inversion for a
direct multiscaled convolution wavelet on `M_{n,m}`.  Its Riesz-inversion
theorem assumes a direct Fourier profile vanishing in a neighborhood of the
rank-deficient boundary.  The 2007 source cites this work and still poses the
heat-composite problem.  A nonzero cone Laplace transform is analytic on the
open cone and cannot meet that support-away-from-boundary condition.

Later search hits either cite the 2008 proceedings paper in unrelated
one-parameter/Bessel settings or concern other matrix/conformal wavelet
transforms.  No later paper explicitly answering Problems A--C, and no exact
formula with the cone profile

`det(s)^N det(I+s)^(-beta)`

and the weighted matrix-beta constant was located through the search date.

## Assessment

Novelty is **plausible but cautious**.  The Fourier multiplier philosophy is
close to the 2006 predecessor.  The material step is the realization of a
boundary-vanishing cone Laplace profile by an actual `L1` cone wavelet,
together with the exact weighted criterion and the Fubini-free convergence
argument.  Different terminology in the symmetric-cone/Laguerre literature
could conceal an equivalent construction.

