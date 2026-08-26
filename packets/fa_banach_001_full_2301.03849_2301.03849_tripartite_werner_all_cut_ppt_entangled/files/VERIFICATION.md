# Verification record

## Exact audit

For the proposed point,

```text
r_plus=3/4, r_minus=1/32, r_0=7/32,
r_1=r_2=0, r_3=3/16.
```

- State positivity: `r_3^2=36/1024 < r_0^2=49/1024`.
- The four linear one-cut PPT margins are `1/32`, `7/32`, `3/32`,
  and `89/32` (including the nonnegative `r_minus` condition).
- The transverse square is `36/1024`; its two PPT upper bounds are
  `89/1024` and `49/1024`.
- The biseparability branch parameter is `u=-17/29`, so the negative branch
  applies.  Its left side is `189/1024` and its right side is `144/1024`.
  The strict violation is `45/1024`.
- Because `r_1=r_2=0`, conjugation by the three-cycle fixes the state and
  cyclically permutes the three cuts.

## Executable checks

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2301.03849_tripartite_werner_all_cut_ppt_entangled/code/verify_candidate.py
```

The script performs all rational inequalities with `fractions.Fraction`.
It also constructs the permutation operators, the density matrix, and all
three partial transposes directly for `d=3,4,5`; it checks trace one,
positive semidefiniteness, the target coordinates, cyclic invariance, and
positive partial transposes.  The matrix computation is a consistency check,
not a substitute for the dimension-independent proof.

Observed direct-matrix minimum partial-transpose eigenvalues were approximately
`0.00452401` for `d=3`, `0.00227280` for `d=4`, and `0.00136691` for
`d=5`, identical across the three cuts up to floating-point error.

## Document QA

`main.tex` was compiled with `latexmk`/pdfLaTeX.  The final log contains no
warnings, undefined references, underfull boxes, or overfull boxes.  Text was
extracted from the four-page `solution_packet.pdf` and checked for unresolved
placeholders and stray LaTeX command text.  After correcting two spacing
commands caught during the first visual pass, all four final pages were
re-rendered at 170 dpi and visually inspected.  The source crop, formulas,
margins, references, and page transitions are legible and unclipped.

## Human review request

Please prioritize:

1. the transcription of Lemma 10 and Theorem 5 from Eggeling--Werner;
2. the convention-independent claim that the three-cycle carries the
   `A|BC` criteria to the other two cuts; and
3. the coefficient normalization in the displayed density operator.
