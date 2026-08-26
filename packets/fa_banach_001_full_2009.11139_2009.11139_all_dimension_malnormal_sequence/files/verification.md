# Verification

## Padding lemma

- Direct block multiplication of `T=[[A,v],[0,L]]` against a self-adjoint
  `B=[[C,x],[x*,b]]` gives the four displayed commutator blocks.
- The lower-left estimate uses
  `||x*(LI-A)|| >= (L-||A||)||x||=||x||`.
- `||v x*||_2=||v|| ||x||=||x||` for a unit padding vector.
- Malnormality of `A` applies because `C` is self-adjoint.
- The operator norm of `(C-cI)v` is bounded by its Hilbert--Schmidt norm.
- The squared Hilbert--Schmidt distance to `cI` contains exactly two copies of
  `||x||^2`.
- Orthogonal projection onto scalar matrices justifies replacing `c` by the
  normalized trace of the full block matrix.
- Rescaling multiplies the malnormality constant linearly.

## All dimensions

- The source's Proposition 3.3 provides contractions in `M_(3m)` uniformly for
  every sufficiently large `m`, not merely a sparse subsequence of `m`.
- Residues one and two modulo three require at most two padding operations.
- A single nilpotent Jordan block has upper triangular Toeplitz commutant; its
  self-adjoint commutant is scalar.
- Compactness turns this qualitative commutant fact into positive
  malnormality in each fixed small dimension.
- Only finitely many small constants are minimized, so the final common
  constant remains positive.

## Source and novelty

- Problem 5.1 appears on PDF page 12.
- Exact-title, exact-problem, padding, and citation searches found no later
  solution or matching lemma.

## Build and visual checks

- `latexmk -pdf` completed successfully with no warnings, overfull boxes, or
  unresolved references in the final log.
- The resulting packet has three pages.
- All three pages were rendered to PNG at 130 dpi and inspected individually;
  the source-problem crop, displayed block calculations, theorem, corollaries,
  and references are legible, with no clipping or layout defects.
