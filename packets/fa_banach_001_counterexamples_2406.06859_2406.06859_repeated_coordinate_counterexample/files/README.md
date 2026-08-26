# A reflexive counterexample to the outside-c0 spaceability question

This packet gives a full negative answer to the final open question on source
PDF page 20 of arXiv:2406.06859v2, *On Sequences with at Most a Finite Number
of Zero Coordinates*, by Diego Alves and Geivison Ribeiro.

## Files

- `solution_packet.pdf`: review-ready counterexample and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv v2 source PDF.
- `figures/open_problem_crop.png`: rendered source excerpt containing the
  concluding theorem summary and open question.
- `VERIFICATION.md`: proof, terminology, literature, build, and visual-QA
  record.
- `code/crop_source.py`: reproducible source-crop helper.

## Result

There is a closed subspace `F` of `ell_infinity`, linearly isometric to
`ell_2`, such that

```text
F intersection c0 = {0},       Z(F) = empty.
```

Consequently `F \ Z(F)=F` is `(alpha,c)`-spaceable for every cardinal
`alpha<=c`, including all relevant infinite `alpha`.  This disproves the
proposed extension of the paper's finite-alpha characterization.

The example is robust under every natural repair of the source's phrase
"a subspace of `ell_infinity \ c0`": it is disjoint from the canonical `c0`
apart from zero, does not contain canonical `c0`, and, being reflexive, does
not even contain an isomorphic copy of `c0`.

## Construction in one line

Take a countable norming family for `ell_2`, repeat its `k`-th functional on
an infinite coordinate block `A_k`, and set all coordinates in another
infinite block `B` to zero.  Repetition prevents a nonzero image from lying in
`c0`; the block `B` guarantees infinitely many zero coordinates.

## Review focus

Check the norming-family isometry, the repeated-block argument for
`F intersection c0={0}`, and the direct verification of
`(alpha,c)`-spaceability once `F\Z(F)=F`.
