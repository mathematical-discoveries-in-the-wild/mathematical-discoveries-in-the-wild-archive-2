# Verification Report

## Claim checked

For `d >= 3` and `1/d <= mu < 1/2`, the Werner state `sigma_mu` is
entangled but is not detected by any pair of entanglement testers from
`S_1^d` to Hilbert spaces.  More strongly, its exact all-tester envelope is
`1 + 2 max(0,1/d-mu)`.

## Analytic audit

1. Output projective-norm duality was checked directly: composing a dual
   contraction on the two Hilbert outputs with the local testers produces a
   witness whose associated map has Hilbert-factorization norm at most one.
2. Haar averaging is legitimate because the factorization-norm unit ball is
   convex and invariant under local unitary conjugation.  Werner invariance
   reduces every optimizing witness to `a I+b F`.
3. For `A=a+b/d` and `c=1-1/d`, the explicit scalar/traceless factorization
   gives `gamma_2(T_{a,b}) <= max(|b|,|A|+c|b|)`.
4. The reverse inequality was checked in two independent directions:
   an off-diagonal matrix unit gives `gamma_2 >= |b|`; restricting to diagonal
   matrices gives `a J+b I`, whose nuclear norm divided by `d` is
   `|A|+c|b|` and lower-bounds `gamma_2`.
5. Optimizing `A+b(2mu-1-1/d)` under `|b|<=1` and
   `|A|+c|b|<=1` gives exactly `1+2(1/d-mu)_+`.
6. Entanglement is direct, without using the full Werner classification:
   every separable state has nonnegative flip expectation, whereas
   `Tr(F sigma_mu)=2mu-1<0` for `mu<1/2`.

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/\
2010.06365_werner_states_undetected_by_all_testers/code/\
verify_werner_counterexample.py
```

The script checks:

- positivity, trace one, and flip expectation `-1/3` for
  `(5I-3F)/36`;
- exact rational multiplicity/eigenvalue identities;
- the two-dimensional support optimization for `d=2,...,10` and 101 values
  of `mu` in each dimension;
- the factorization parameter choice in 7000 random `(a,b,d)` cases.

These computations are consistency checks, not ingredients of the proof.

## Novelty audit

On August 11, 2026 the cheap run indexes were searched for arXiv:2010.06365,
`entanglement testers`, `Werner`, and `factorization through ell_2`; no prior
packet or attempt was present.  Exact-title and keyword searches on arXiv and
the web found the source, its journal version, a 2021 workshop report that
still repeats the question, and later papers using the SIC/realignment
comparison, but no answer to completeness.

OpenAlex listed six citing works through 2025.  Their titles/abstracts or
full-text citation contexts were checked: *A tensor norm approach to quantum
compatibility*; *Magic squares: Latin, semiclassical, and quantum*; *A family
of separability criteria and lower bounds of concurrence*; *The entanglement
criteria based on equiangular tight frames*; *Enhanced Schmidt-number criteria
based on correlation trace norms*; and *Symmetric measurement-induced lower
bounds of concurrence*.  The accessible arXiv sources 2202.13993,
2402.09972, and 2503.21177 cite the source only for background or the
SIC/realignment comparison.  No all-tester Werner optimality theorem or
counterexample was found.  Novelty remains plausible rather than certified.

## Human-review focus

The two points worth checking first are the passage from output projective
duality to the `gamma_2` witness ball and the normalization in the diagonal
nuclear-norm lower bound.  Both are written out in the packet.  If they pass,
the counterexample and the full Werner-envelope formula are complete.
