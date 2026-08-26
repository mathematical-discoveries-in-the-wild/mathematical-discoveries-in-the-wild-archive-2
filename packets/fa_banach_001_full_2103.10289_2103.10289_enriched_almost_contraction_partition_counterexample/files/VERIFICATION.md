# Verification

Status: candidate full negative answer.

## Exact source match

- The source asks whether every enriched almost contraction has a partition
  into restrictions that are enriched contractions (or nonexpansive).
- Its motivating examples and weakly-Picard comparison require restriction
  self-maps, hence invariant cells. Without invariance, singleton cells make
  the question vacuous.

## Algebraic checks

- Same-side pairs for `S` have zero output difference.
- In either cross-half-line ordering, the `L=2` term alone is at least `2`,
  which proves the `(delta,L)=(1/2,2)` inequality.
- For `T=3S-2I`, both enriched expressions are exactly three times the
  corresponding expressions for `S`, giving `(b,theta,L)=(2,3/2,2)` with
  `theta<b+1`.
- `T(8/5)=-1/5` and `T(-1/5)=-13/5`.
- The forced pair has input distance `9/5` and output distance `12/5`.
- An enriched restriction would require
  `9k+12 <= 9 eta`, hence `eta >= k+4/3`, contradicting `eta<k+1`.

## Artifact checks

- `main.tex` compiled without errors or layout warnings.
- `solution_packet.pdf` is a valid three-page PDF and was rendered at 144 dpi.
- All three rendered pages were visually inspected; formulas, margins,
  headings, and bibliography are legible with no clipping or overlap.
- `source_target_2103.10289.pdf` is a valid 17-page PDF.
- The result ledger parses as valid JSON and records model `GPT5.6`.
