# Verification report

Status: `candidate_full_likely_valid`

## Logical audit

The order-two tracial moment matrix has size `7x7`, hence rank at most seven.
For a representable noncommutative sequence, arXiv:1611.00494, Corollary 2.3,
forces rank at least four.  The proof packet checks the exhaustive cases:

| case | size-two input |
|---|---|
| commutative | commutator-square identity and simultaneous diagonalization |
| rank 7 | arXiv:1611.00494 page 3, citing BCKP13 Remark 3.9 |
| rank 4 | arXiv:1611.00494 Theorem 3.1 |
| rank 5 | arXiv:1611.00494 Theorems 6.5, 6.8, 6.11, 6.14 |
| rank 6, first three affine normal forms | arXiv:1611.00494 Proposition 4.1 and page-4 result summary |
| rank 6, `Y^2=1` | prior full packet for arXiv:2001.11614, Theorem 1 |

Invertible affine changes of the two variables send each matrix atom to an
atom of the same size, and the inverse change recovers the original moments.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1611.00494_all_quartic_atoms_size_two/code/verify_rank_exhaustion.py
```

The script checks, for 2,000 random real symmetric pairs of sizes 1 through
9, the exact numerical identity

```text
Tr(A^2 B^2) - Tr(ABAB) = (1/2) Tr([A,B]^T [A,B]),
```

and checks that the rank table `1,...,7` and all four rank-six normal forms
have no uncovered branch.  This is a regression check, not a substitute for
the cited source theorems or the supporting `Y^2=1` proof.

Observed output on 11 August 2026:

```text
PASS: 2000 commutator identities; maximum absolute error=1.421e-14
PASS: ranks 1..7 and all four rank-six normal forms are covered
```

## Evidence files

- `source_paper.pdf`: arXiv:1611.00494.
- `figures/source_rank_cases_part1.png` and
  `figures/source_rank_cases_part2.png`: the page-spanning “all but a single
  case” statement.
- `figures/source_rank6_normal_forms.png`: the four rank-six normal forms and
  the source's size-two conclusion for the first three.
- `figures/y2_conjecture_crop.png`: Conjecture 1 from arXiv:2001.11614.
- `supporting_packet_2001.11614.pdf`: full proof of that remaining case.
