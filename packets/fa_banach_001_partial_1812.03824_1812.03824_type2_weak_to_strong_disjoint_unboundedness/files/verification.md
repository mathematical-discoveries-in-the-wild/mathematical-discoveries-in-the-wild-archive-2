# Verification

Status: passed.

## Mathematical checks

- A union of `N` component-large sets with cardinality at least `eta k` has
  one component of cardinality at least `(eta/N) k`.
- Passing to a subsequence fixes that component while preserving increasing
  horizons and the null witness sequence.
- Proposition 8 of Bernardes--Bonilla--Müller--Peris applies exactly to this
  single-component weak block condition.
- An upper-density-one unbounded orbit for one component is automatically a
  type-2 orbit because the tuple sum/max dominates that component.
- The weak type-1 condition rules out power-boundedness of every component.
- In finite dimension, the vectors without full-orbit divergence for a
  non-power-bounded matrix lie in a proper Jordan spectral subspace.
- For a normal operator, non-power-boundedness is equivalent to norm greater
  than one, and every vector outside the spectral subspace for `|z|<=1` has
  norm-divergent full orbit.
- A finite union of proper closed subspaces cannot cover the ambient space.

## Build and visual QA

- `pdflatex` completed repeated final passes with no warnings, overfull boxes,
  underfull boxes, undefined references, or errors in the final log.
- Final packet: 4 US-letter pages, 320673 bytes.
- All four pages were rendered at 120 dpi and visually inspected. The source
  crop, theorem statements, equations, proof endings, references, and margins
  are clean; nothing is clipped or overlapped.

## Artifact hashes

```text
source_paper.pdf              f1f7c94a11ba36275cd2139aa7599adc713abb0085260e34dac892c8e4e6b091
supporting_paper_2013JFA.pdf b398b667661fea0b8d078f1cba87cbab86cc5ef6bc731aee2f7f9ad9a5d593c4
open_problem_crop.png        cb70ac59626141b5a8134d2f5885007531843a3c79c5ea7aa7ef556e401c654a
solution_packet.pdf           ab11e0d39e00bd0b85ef40556fc8dafff079f4e07e72aa8ec8b9c78ec9fce861
```
