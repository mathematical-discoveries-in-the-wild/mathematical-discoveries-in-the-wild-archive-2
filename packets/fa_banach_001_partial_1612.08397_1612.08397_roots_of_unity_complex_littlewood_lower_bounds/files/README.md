# Roots-of-unity lower bounds for complex Littlewood constants

Status: **candidate partial result; likely valid; human review requested**

Source: W. Cavalcante, D. Pellegrino, and E. Teixeira, *On the geometry of
multilinear forms*, arXiv:1612.08397, Section 5.2, page 17.

## Result

For every integer `n >= 2`, the finite-dimensional complex Orlicz and mixed
Littlewood constants from the source satisfy

```text
kappa_O^C(n), kappa_L^C(n)
    >= (n/sqrt(2)) sin(pi/(2n)).
```

The bound is attained by an explicit two-column roots-of-unity matrix for the
mixed Littlewood functional and by its transpose for the Orlicz functional.
It equals `1` at `n=2`, agreeing with source Theorem 25, and is strictly
greater than `1` for every `n >= 3`. In particular,

```text
kappa_O^C(3), kappa_L^C(3) >= 3 sqrt(2)/4.
```

Thus the exceptional value `1` proved in the source cannot persist in any
higher dimension. The lower bound increases to `pi/(2 sqrt(2))`.

## Proof mechanism

Let `zeta=exp(2 pi i/n)` and take the matrix with rows
`(1,zeta^k,0,...,0)`, `k=0,...,n-1`. Its mixed numerator is `n sqrt(2)`.
Its bilinear norm reduces exactly to

```text
2 max_u sum_{k=0}^{n-1} |cos(u + pi k/n)|.
```

A parity split of the signed geometric sum proves that this maximum is
`2 csc(pi/(2n))`. Transposition preserves the bilinear norm and turns the
same construction into one whose Orlicz numerator is also `n sqrt(2)`.

## Boundary and novelty status

This is not a full answer to the source problem: it supplies explicit lower
bounds, not the exact finite-dimensional constants. A bounded full-upgrade
attempt isolated the still-missing `n=3` upper bound and is recorded in
`../../../attempts/1612.08397_exact_n3_upper_bound_frontier.md`.

A bounded search on 9 August 2026 covered the source's arXiv full text and
citation neighborhood, exact searches for the displayed formula and
roots-of-unity construction, and the later arXiv:1912.10313. The later paper
establishes the dimension-free complex mixed constant `2/sqrt(pi)` but does
not provide the finite-`n` formula sought here. No match for this explicit
finite-dimensional bound was located, so originality is provisional.

## Verification report

Verdict: **likely valid**. The proof is elementary and exact. The included
script numerically checks the trigonometric maximum and matrix ratio for a
range of dimensions; it is corroboration only, not proof.

Human review should focus on the signed geometric-sum identities in the odd
and even cases and on the endpoint reduction of the bilinear norm to the
two-dimensional torus.

## Files

- `solution_packet.pdf`: complete review packet
- `main.tex`: proof source
- `source_paper.pdf`: original source paper
- `figures/open_problem_crop.png`: source page 17
- `code/verify_roots_of_unity_bound.py`: numerical corroboration
