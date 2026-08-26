# Sharp swap-polynomial degrees on M2 and a general trace construction

**Status:** substantial partial result, likely valid; pending human review.

**Source:** Felix Huber, *Positive maps and trace polynomials from the
symmetric group*, arXiv:2002.12887, open question on PDF page 19.

## Result

The lowest swap-polynomial degrees on `M_2(C)` are determined exactly:

```text
ordinary tensor polynomials:  4
tensor trace polynomials:      3
```

An explicit minimal cubic trace formula is

```text
tau Gamma = tau/2 I tensor I
            + A0 tensor [B,C]
            + B0 tensor [C,A]
            + C0 tensor [A,B],

tau = tr(A[B,C]),   A0 = A - tr(A)I/2,
```

with analogous definitions of `B0,C0`.  The lower bound through degree two
is elementary.  Procesi's 2022 degree-four ordinary formula, together with a
short central-polynomial lower bound through degree three, gives the sharp
ordinary result.

For every `d>=2`, an invariant volume form on `sl_d` and its trace-dual
cofactors produce a multilinear tensor trace swap polynomial of degree
`d^2-1`.  Hence

```text
3 <= minimum trace swap degree <= d^2-1.
```

Exact Schur--Weyl Gram ranks additionally give `5 <= minimum <= 8` for
`d=3`.  Sharp minimality for `d>=3` remains open.

## Files and verification

- `main.tex` and `solution_packet.pdf`: complete proofs, literature boundary,
  and the exact `d=3` rank certificate.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: rendering of the source question on PDF
  page 19.
- `runs/fa_banach_001/attempts/2002.12887_swap_degree_search.py`: exact
  low-degree group-algebra search and exhaustive verification of the cubic
  identity on all matrix-unit triples.  Pass `--d3-exact` to reproduce the
  two larger exact Gram ranks.
- `runs/fa_banach_001/attempts/2002.12887_swap_degree_upgrade_attempts.md`:
  eight focused upgrade attempts and the remaining obstruction.

Recommended review focus: the use of the first fundamental theorem to realize
the exterior cofactors as trace polynomials, the source's degree convention,
and the optional `d=3` computer-assisted lower bound.

## Novelty check

Bounded searches on 17 August 2026 covered the run indexes, exact source
phrases, arXiv searches for swap and trace-swap polynomials, and Claudio
Procesi's later paper *A construction of swap or switch polynomials*
(arXiv:2102.10657; Adv. Math. 400 (2022)).  That paper supplies the ordinary
degree-four `M_2` construction, but no cubic trace formula or sharp trace
minimum was found.  Novelty confidence is moderate because the new formula is
an elementary dual-basis identity and may have an uncatalogued prior instance.
