# Verification report

Status: `candidate full counterexample; likely valid`

## Mathematical audit

1. `x=(2^{-2^j})` belongs to `l_1`, has infinite support, and therefore lies
   in `P\c_00`.
2. The range proof for `U_N` explicitly recovers `x` and every coordinate
   vector from two successive tails; no infinite linear combination is used.
3. The exact column error is `2R_j/(a_j+R_j)`, and the displayed geometric
   bound proves its tail supremum tends to zero.
4. `||U_N-I||<1` gives injectivity and the two-sided norm estimate; explicit
   range recovery gives surjectivity onto `P`.
5. The distance-one transfer lemma separately handles the zero operator and
   allocates half the requested lifting error to distortion and half to the
   `c_00` lift.
6. An isometry `c_00 -> P` extends onto the completions because its range is
   both dense and closed. The extreme-point argument then forces preservation
   of `c_00`, contradicting `x in P\c_00`.

No unproved lemma remains.

## Computational audit

Command:

```text
conda run --no-capture-output -n sandbox python code/check_superlacunary_tails.py
```

The script uses exact rational arithmetic through coordinate 12. It checks the
successive-tail identity, positivity of every diagonal in the finite tail
basis, the exact column-distance formula, and strict decay of the tested
errors. This is a sanity check only; the infinite estimate is proved in
`main.tex`.

Final output: `PASS: exact tail identities, triangularity, and
superlacunary error decay verified`.  The tested column errors decrease from
`0.118079492009` at `j=2` to `1.72723371102e-77` at `j=8`.

## Source and visual audit

- `source_paper.pdf` was compiled locally from the cached original arXiv TeX;
  it has 27 pages.
- `figures/open_problem_crop.png` is a readable full-width crop from source
  PDF page 10 and contains the complete conjecture paragraph.
- The final packet has 4 letter-sized pages. Its final LaTeX log contains no
  warnings or overfull boxes.
- The final packet is built with intermediates under `tmp/`; all four pages
  were rendered at 140 dpi and individually inspected, together with the
  final source crop, for clipping, overlap, missing glyphs, and legibility.

## Checksums

- `solution_packet.pdf`:
  `54ab01f275e8eb1faec2e8ae6ac94e29f1fa7052921ff4b65f365e413ebd6ffa`
- `source_paper.pdf`:
  `425cecc5cf85f6a0d0c9d4af827e338eb392bc8afcf5f6f9f3b8d3a857e0a2ff`
- `figures/open_problem_crop.png`:
  `7e504779563d677c9fca4fd6dffbcfad5f293562cc6b1a3ab105c48c095243ce`

## Literature/novelty audit

The bounded search and its limitation are recorded in the README and packet.
The local run indexes, exact local-corpus searches, and the available later
citation produced no prior answer. External search returned no usable records,
so novelty confidence is moderate.

## Reviewer focus

The key points are the finite (Hamel, not Schauder) range computation for the
tail basis and the quantitative transfer of extreme projectivity through
distortions tending to one.
