# Verification report

Date: 2026-08-11  
Model: GPT5.6

## Mathematical checks

- Checked the Jung upper bound for arbitrary, including uncountable, index
  sets.  The coordinate centers form an element of the bounded product because
  their norms are uniformly bounded relative to one fixed point of the set.
- Checked the factor-witness normalization.  Translating the nearisometry and
  postcomposing by a surjective linear isometry both biject the family of
  affine isometries, so the infimal approximation distance is unchanged.
- Checked the lifted max-product map directly using
  `|max(a',b)-max(a,b)| <= |a'-a|`; surjectivity and bounded distance from the
  identity are inherited coordinatewise.
- Checked the possible coordinate-mixing obstruction.  If an affine isometry
  `Tz=Lz+w` is a bounded distance from the identity, then
  `t(L-I)z+w` is bounded for every fixed `z` as `t` tends to infinity, forcing
  `L=I`.  Restriction to the bad coordinate then recovers the original factor
  lower bound.
- Checked the constants in the examples against the decisive supporting
  paper: Hilbert spaces have `H=J`, `H(c0)=J(c0)=2`, and a real
  `n`-dimensional Hilbert factor has `J=sqrt(2n/(n+1))`.
- Stress-tested three upgrade routes beyond max products: finite `p` sums,
  general norm-one complemented subspaces, and support-functional analogues of
  the Hilbert sharpness construction.  Each has a stated structural
  obstruction; none is used in the theorem.

## Source and novelty checks

- The exact sharpness question was located on printed page 4 of
  arXiv:math/0201098 and cropped from the locally stored source PDF at full page
  width.
- The Huuskonen--Vaisala supporting PDF was checked for its Theorems 1.11 and
  3.2 and its Section 3 summary.
- The bounded novelty check covered the run's exact-id and keyword indexes,
  exact web phrase searches, nine OpenAlex-indexed citations of the survey, and
  seven OpenAlex-indexed citations of the supporting paper.  No formula for
  affine Hyers--Ulam constants of direct sums or max products was found.
  Novelty confidence remains moderate because older nearisometry literature is
  sparse and incompletely indexed.

## PDF verification

- `main.tex` compiled successfully with `latexmk` to a four-page PDF.
- The final LaTeX log contains no warning, overfull, underfull, or undefined
  reference lines.
- All four rendered pages were visually inspected.  The source crop, theorem,
  formulas, proof ending, examples, limitations, and bibliography are legible,
  with no clipping or overlap.
- SHA-256 of `solution_packet.pdf`:
  `3fd4b2b67724b1d1dc613a4fb8bb61e40135dbeb7949dabee160047ba815c1bf`.

