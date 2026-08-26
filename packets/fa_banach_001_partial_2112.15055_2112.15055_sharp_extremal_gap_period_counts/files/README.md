# Sharp extremal gap counts at fixed essential period

**Status:** candidate partial result, likely valid, pending human review.

**Source target:** Krishna Kumar G. and V. B. Kiran Kumar, *Stability in
Non-Normal Periodic Jacobi Operators: Advancing Börg's Theorem*,
arXiv:2112.15055, Section 5.1, PDF page 21.

The source asks for a relationship between the number of spectral gaps and the
essential period of a self-adjoint periodic Jacobi operator, and suggests that
the number of gaps should be “on the order of” the period.

## Result

For every integer `p >= 2`, among all self-adjoint periodic Jacobi operators
whose least (essential) period is `p`,

```text
minimum number of open gaps = 1,
maximum number of open gaps = p - 1.
```

In particular, there is a period-`p` operator with exactly one open gap for
every arbitrarily large `p`. Hence no lower bound growing with `p`—linear or
otherwise—can hold from the essential period alone. The source's `p-1`
example is the opposite sharp extreme.

## Construction mechanism

For `p>2`, vary the two-band compact set

```text
E_s = [-1,0] union [s,1],  0<s<1.
```

The equilibrium mass of the right band varies continuously from `1/2` to
`0`, so choose `s` for which it is `1/p`. For `p=2`, use any symmetric
two-band set. Corollaries 4.5 and 6.4 of Christiansen–Simon–Zinchenko,
arXiv:0810.3273, realize the set as the spectrum of an isospectral-torus
Jacobi matrix and identify its period with the denominator of its band
harmonic measures. Since `1/p` has least denominator `p`, the resulting
Jacobi matrix has least period exactly `p` and exactly one open gap.

Börg's theorem gives the lower bound of one for nonconstant/minimal-period
`p>1` coefficients. Floquet theory gives at most `p-1` gaps, and the source's
explicit example attains that number.

## Scope and novelty

This sharply resolves the extremal minimum and maximum gap counts, but it does
not classify which intermediate counts or gap geometries occur, nor address
the paper's non-normal pseudospectral optimization questions.

A bounded search on 2026-08-17 used arXiv/the web and the run indexes with the
phrases `one gap p-periodic Jacobi`, `exactly one gap periodic Jacobi`,
`minimal period one gap Jacobi matrix`, and `arbitrary period finite gap
Jacobi`. No exact statement of the extremal theorem was found. The proof is a
direct agent-identified consequence of established finite-gap Jacobi theory,
so novelty confidence is moderate rather than high.

## Verification and reviewer focus

- The source statement is preserved in `figures/open_problem_crop.png`.
- `source_paper.pdf` is arXiv:2112.15055.
- `supporting_paper_0810.3273.pdf` contains the finite-gap realization and
  period criterion (Corollaries 4.5 and 6.4, PDF pages 23 and 42).
- No numerical computation is used.
- The key reviewer checks are the continuity/end-point limits of the band
  equilibrium mass and the deduction of *least* period from the reduced
  denominator `1/p`.

Ledger:
`runs/fa_banach_001/ledger/results/2112.15055_sharp_extremal_gap_period_counts.json`.
