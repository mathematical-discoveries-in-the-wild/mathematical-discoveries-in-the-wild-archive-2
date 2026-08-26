# Real interpolation without the finite-`p^+` hypothesis

Status: `full_solution_likely_valid`

Source target: Henning Kempka and Jan Vybíral, *Lorentz spaces with variable
exponents*, arXiv:1210.1738, Theorem 8 and Remark 4(i), PDF page 14.

The source proves

```text
(L_{p(.),q_0(.)}(R^n), L_infinity(R^n))_{theta,q}
    = L_{p(.)/(1-theta),q}(R^n)
```

under `p^+<infinity`, then explicitly asks whether that hypothesis can be
removed. This packet gives an affirmative answer in the full stated range:
measurable exponents `p,q_0:(R^n)->(0,infinity]` bounded away from zero,
`0<theta<1`, and `0<q<=infinity`. In particular, `p` may be unbounded, may
equal infinity on a set of positive measure, and may have `p^-<1`.

The proof avoids the generalized inverse responsible for the source
restriction. It discretizes the distribution function

```text
h_k = ||1_{|f|>2^k}||_{L_{p(.)}}
```

and proves two endpoint `K`-functional estimates. A level-grouping argument
identifies the weak Lorentz endpoint. Dyadic truncation identifies every
constant Lorentz endpoint `L_{p(.),r}` through a forward discrete Hardy
operator with a geometric kernel. Taking `r=q_0^-` and using the source's
monotone Lorentz embeddings sandwiches the variable-`q_0` interpolation
space between the two identified endpoints.

The endpoint cases `q=infinity`, `q_0^-=infinity`, positive-measure
`{p=infinity}`, and the quasi-Banach ranges `p^-<1` and `q_0^-<1` are
included explicitly. The proof uses level-set inclusions, dyadic distribution
estimates, and elementary sequence inequalities; it does not use local
convexity.

A bounded official-arXiv title/formula/keyword search through 11 August 2026
found no later removal of `p^+<infinity` from this theorem. The packet is an
agent-produced full result, subject to expert verification and novelty review.

Files:

- `solution_packet.pdf`: complete statement, intuition, proof, and checks.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:1210.1738.
- `figures/open_problem_crop.png`: source Remark 4(i), PDF page 14.
- `code/check_discrete_hardy.py`: randomized finite tests of the two discrete
  Hardy estimates (supporting sanity check only, not part of the proof).
