# Generalised Schwartz Extension Counterexamples

Source: Karsten Kruse, *Extension of vector-valued functions and sequence
space representation*, arXiv:1808.05182; Bull. Belg. Math. Soc. Simon
Stevin 29 (2022), 307–331.

Status: candidate full negative answer, likely valid.

## Result

Both extension questions posed after Corollaries 4.8 and 4.9 fail for the
same target space: `E = c_00` with the topology inherited from the product
`C^N`. This space is generalised Schwartz but not semi-Montel.

- On `Omega = {0} union {1/n}`, the data `f(1/n) = (1,...,1,0,...)`
  have bounded uniformly continuous scalar extensions for every continuous
  functional, but the forced value at zero is the all-ones sequence, outside
  `c_00`.
- For the disc algebra, enumerate a dense boundary set `(zeta_j)` and use
  `a_n(z) = product_{k<=n}(z-zeta_k)`. At each sampled boundary point the
  coordinate vector has finite support, while every coordinate at the forced
  center value is nonzero.

## Files

- `main.tex`: theorem and exact proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original source PDF.
- `figures/open_question_crop.png`: source page 21 with both corollaries and
  the open sentence.
- `code/verify_coordinate_patterns.py`: finite consistency checks.
- `verification.md`: reproducibility, checksum, and visual-QA record.

## Human Review Recommendation

Check that `c_00` in the product topology is generalised Schwartz but not
semi-Montel, then verify the two coordinatewise uniqueness arguments. The
disc construction satisfies the topology-fixing hypothesis because its
sample set is dense in the unit circle.
