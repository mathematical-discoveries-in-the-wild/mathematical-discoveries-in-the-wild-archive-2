# Density-one Sidon subsystems: an explicit necessary dependence on the deficit

Status: `candidate_partial_result_likely_valid`

Source: Jean Bourgain and Mark Lewko, *Sidonicity and variants of
Kaczmarz's problem*, arXiv:1504.05290, Problem 26 (PDF page 20).

## Result

Let `sid(A)` denote the best Sidon lower constant of a subsystem.  The
Bourgain--Lewko construction itself gives universally bounded
orthonormal `psi_2` systems `Phi^(n)` of size `n+1` such that, for every
fixed `0 < epsilon < 1` and every

```text
A subset Phi^(n),   |A| >= (1-epsilon)(n+1),
```

one has

```text
limsup sid(A) <= epsilon/(1-epsilon).
```

More explicitly, if `B` is the set of ordinary (nonzero-indexed)
functions retained in `A`, `m=|B|`, and `k=n-m`, then

```text
sid(A) <= [k + n/sqrt(log n) + 6 sqrt(log n)
           + k sqrt(log n/n)] / m.
```

Consequently, any affirmative answer to Problem 26 must have
`gamma(7,C0,epsilon) <= epsilon/(1-epsilon)` for the universal subgaussian
constant `C0` of the construction.  In particular, deleting only `o(n)`
functions can never produce a uniformly Sidon subsystem.

## Mechanism

The construction has a common damping factor

```text
D(r) = [1 + (log n/n^2)(sum_i r_i)^2]^(-1/2).
```

For equal coefficients on any retained set `B`, the omitted `k` Rademacher
coordinates can cancel at most `k` units of the retained Rademacher sum.
After that threshold, `D` compresses the remaining sum to at most
`n/sqrt(log n)`.  The Walsh--Rudin--Shapiro term costs only
`6 sqrt(log n) + k sqrt(log n/n)`.  Dividing by the `l_1` norm `m` gives
the displayed estimate.

## Scope

This is a quantitative obstruction, not a full answer to Problem 26.  For a
fixed positive `epsilon`, the upper bound still permits a positive Sidon
constant depending on `epsilon`, exactly as the problem allows.  The
existence question for fixed `epsilon` remains open here.

A bounded arXiv/local-source search used arXiv:1504.05290, its citations,
the exact phrase of Problem 26, and the terms `density-one Sidon subsystem`,
`Sidon lower constant`, and `uniformly bounded psi_2 orthonormal system`.
Pisier's later arXiv:1602.02430 resolves the two-fold tensor question, not
Problem 26.  No source stating the quantitative obstruction above was found;
novelty confidence is therefore bounded rather than definitive.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem and proof.
- `source_paper.pdf`: arXiv:1504.05290.
- `figures/open_problem_crop.png`: Problem 26 on source PDF page 20.
- `VERIFICATION.md`: independent algebra and scope checks.

Human review should focus on the exact rewriting of the common density factor
and the passage from a subsystem of the full `n+1` family to its retained
ordinary indices.
