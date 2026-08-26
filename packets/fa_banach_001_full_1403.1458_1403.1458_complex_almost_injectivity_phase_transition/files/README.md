# Complex almost-injectivity phase transition at `N=2d`

Status: `candidate_full_solution_likely_valid`  
Source: arXiv:1403.1458, Conjecture 2, printed pp. 22--23  
Agent: `agent_lane_03`  
Model: `GPT5.6`

## Claim

For every standard complex rank-one measurement system with `N <= 2d-1`,
the ambiguous signals contain an open dense conull set.  Hence no such system
is almost injective, in either the source's open-dense sense or the later
almost-everywhere sense.  Together with the known generic sufficiency for
`N >= 2d`, this proves the source conjecture that the phase transition is
exactly `N=2d`.

The new ingredient is a degree-zero obstruction.  At the critical count, a
regular signal gives a square phase-membership map
`T^(2d-2) -> C^(d-1)`.  Its identity zero cannot be the unique nondegenerate
zero.  If the normalized intensity map has deficient maximal rank instead,
the constant-rank theorem gives positive-dimensional fibers.

## Contents

- `solution_packet.pdf` — human-review packet (generated after compilation)
- `main.tex` — packet source
- `source_paper.pdf` — arXiv:1403.1458
- `question_crop.png` — exact two-page source excerpt
- `references/balan_casazza_edidin_math0412411.pdf` — known generic
  sufficiency used for phase-transition part (b)
- `references/huang_rong_wang_xu_1909.08874.pdf` — decisive 2021 status and
  generic-critical comparison
- `code/make_question_crop.py` — reproducible source crop
- `code/verify_torus_obstruction.py` — deterministic numerical stress test
- `verification.md` — proof, build, rendering, and literature audit
- `tmp/` — LaTeX build and rendered-page QA artifacts

## Verification

From the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1403.1458_complex_almost_injectivity_phase_transition/code/verify_torus_obstruction.py
```

Expected final line: `all deterministic stress tests passed`.

Compile into the packet-local temporary directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=runs/fa_banach_001/solutions/full/1403.1458_complex_almost_injectivity_phase_transition/tmp \
  runs/fa_banach_001/solutions/full/1403.1458_complex_almost_injectivity_phase_transition/main.tex
```

## Literature-search boundary

The exact source and the cheap run indexes were checked first.  Later search
used the phrases `2d-1 PR-ae`, `standard phase retrieval`, and
`almost injective complex phase retrieval`, plus the citing works for DOI
`10.1016/j.acha.2020.08.002`, through 2026-08-11.  No later solution of the
exceptional standard rank-one case was found.  This is a bounded novelty
check, not an exhaustive priority claim.
