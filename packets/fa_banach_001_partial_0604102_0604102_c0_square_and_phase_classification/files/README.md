# Square and phase norm equalities on `C_0(L)`

Status: `candidate_strong_partial_likely_valid`

Source: V. Kadets, M. Martin, and J. Meri, *Norm equalities for
operators*, arXiv:math/0604102, source PDF pages 16--18.

## Result

For every locally compact Hausdorff `L` with at least two points, the
following are equivalent on the real space `C_0(L)`:

```text
||I+T^2||=1+||T^2|| for every rank-one T;
||I-T^2||=1+||T^2|| for every rank-one T;
L has no isolated points;
C_0(L) has the Daugavet property.
```

For complex `C_0(L)` and every fixed unit scalar `omega!=1`, the identity

```text
||I+omega T||=||I+T|| for every rank-one T
```

is equivalent to the same no-isolated-points/Daugavet condition. Thus all
finite-root and full-circle properties from the source collapse on complex
`C_0(L)` spaces.

The necessity proof gives an explicit exact witness at every isolated point:
`||I+T^2||=17/16` while `1+||T^2||=18/16`.

## Scope

This is a complete classification for the classical `C_0(L)` family, hence a
strong partial answer. The arbitrary real Banach-space square implication and
arbitrary complex subgroup-equivalence question remain open.

## Files

- `main.tex`: self-contained theorem, local-bump proof, exact counterexamples,
  scope, and novelty audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: official 21-page arXiv source PDF.
- `figures/`: real and complex source-question crops.
- `verification.md`: proof, literature, and render audit.
- `code/check_obstruction.py`: exact rational arithmetic guard.
- `code/crop_source.py`: reproducible source-crop script.

Human review should focus on the slice argument, the total-variation row-norm
calculation, and the one-dimensional real exception.
