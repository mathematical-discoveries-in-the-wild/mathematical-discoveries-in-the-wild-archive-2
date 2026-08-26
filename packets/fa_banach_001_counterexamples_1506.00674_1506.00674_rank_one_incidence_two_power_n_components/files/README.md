# Rank-one incidence variety has exactly `2^N` components

Status: `candidate_counterexample_likely_valid`

Source: Dan Edidin, *Projections and phase retrieval*, arXiv:1506.00674,
Remark 4.4 on PDF page 7.

## Result

The source says that irreducibility of its complex incidence variety
`I_{k_1,...,k_N,M}` is not known.  Irreducibility is false in the allowed
rank-one case.  If every `k_i=1`, then the incidence variety has exactly
`2^N` irreducible components.  The components are indexed by choosing, for
each projected line, whether that line is orthogonal to `x` or to `y`.

More generally, if `r` of the projection ranks equal one, the incidence
variety has at least `2^r` irreducible components.  In particular, it is
reducible whenever one rank is one.

Each component in the all-rank-one case has dimension

```text
N(M-2) + 2M - 2,
```

which is exactly the dimension computed in Proposition 4.3 after setting
all `k_i=1`.  Thus the result explains why the source's dimension argument
correctly controls the real locus without needing the full incidence variety
to be irreducible.

## Key identity

A complex symmetric rank-one idempotent is

```text
P_u = u u^T / (u^T u),       u^T u != 0.
```

Consequently,

```text
y^T P_u x = (u^T y)(u^T x)/(u^T u),
```

so the incidence equation is the union of the two closed alternatives
`P_u x=0` and `P_u y=0`.

## Packet contents

- `main.tex` and `solution_packet.pdf`: formal theorem, proof, limitations,
  novelty check, and review guidance.
- `source_paper.pdf`: local copy of arXiv:1506.00674.
- `figures/open_problem_crop.png`: full-width crop of Proposition 4.3 and
  Remark 4.4 from source PDF page 7.
- `verification.md`: independent step audit.
- `code/check_rank_one_factorization.py`: exact-rational sanity checks of the
  factorization and component-separating witnesses.

Ledger record:
`runs/fa_banach_001/ledger/results/1506.00674_rank_one_incidence_two_power_n_components.json`.

## Scope

This packet resolves the source's irreducibility uncertainty negatively and
classifies the all-rank-one case.  It does not classify the incidence variety
when every rank lies between `2` and `M-1`, and it does not challenge the
source's generic phase-retrieval theorem.
