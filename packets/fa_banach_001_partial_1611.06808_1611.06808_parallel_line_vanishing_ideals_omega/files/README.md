# Parallel-line vanishing ideals have property `(Omega)`

Status: `candidate_partial_result_likely_valid`  
Source: arXiv:1611.06808, Conjecture 2.3, printed p. 6  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Claim

Let `K` be an arbitrary compact subset of finitely many parallel affine lines
in `R^d`.  Then the value-vanishing ideal

`I_K={f in C-infinity(R^d): f|K=0}`

has property `(Omega)`.  No regularity, density, or extension hypothesis is
placed on the compact slices.

The proof builds an explicit simultaneous restriction section by transverse
interpolation.  It gives a topological direct-sum decomposition of the
ambient ideal into the complemented ideal vanishing on all carrier lines and
the lifted one-dimensional slice ideals.  The source proves `(Omega)` for
every closed ideal of `C-infinity(R)`.  The packet proves directly that
`C-infinity(R^d)` has `(Omega)` and that the property is stable under
complemented subspaces and finite direct sums.

This is a higher-dimensional partial result.  It does not prove Conjecture
2.3 for arbitrary compacta, and it does not settle the source's separate
union-stability question.

## Contents

- `solution_packet.pdf` — human-review packet (after compilation)
- `main.tex` — packet source
- `source_paper.pdf` — arXiv:1611.06808
- `question_crop.png` — exact source conjecture
- `references/vogt_omega_smooth_spaces.pdf` — primary background reference
- `code/make_question_crop.py` — reproducible crop
- `code/verify_parallel_line_splitting.py` — deterministic splitting check
- `verification.md` — proof, build, visual, and literature audit

## Reproduce the structural check

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1611.06808_parallel_line_vanishing_ideals_omega/code/verify_parallel_line_splitting.py
```

Expected final line:
`simultaneous restriction/right-inverse checks passed on 303 samples`.

## Literature-search boundary

The run indexes, exact source wording, exact conjecture phrase, property
`(Omega)`, vanishing ideals, union stability, and later citations of DOI
`10.1007/s00209-019-02388-5` were checked through 2026-08-11.  No later
settlement was found.  This is a bounded novelty check, not an exhaustive
priority claim.
