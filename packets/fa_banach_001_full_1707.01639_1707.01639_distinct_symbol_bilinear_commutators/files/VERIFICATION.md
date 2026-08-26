# Verification

Status: candidate full split resolution in the standard real-symbol setting.

## Exact source match

- Problem A asks whether boundedness of
  `[b1,T]_1+[b2,T]_2` forces both distinct symbols into BMO.
- Problem B asks the analogous question for
  `[b2,[b1,T]_1]_2`.
- The packet uses the homogeneous, convolution, nonvanishing kernel setting
  used by the source's necessity proof. Its reciprocal-Fourier assumption
  implies nonvanishing away from the origin.

## Mathematical checks

- The separated-cube sector lemma follows from homogeneity, continuity, and
  `K(z,z) != 0`.
- The first median test has the correct scaling because
  `1/q=1/p1+1/p2` and both input median sets have at least half-cube measure.
- The source proves the `BMO_q=BMO` oscillation equivalence for every `q>0`,
  so the quasi-Banach range causes no gap.
- After `s=b1+b2` is known to be BMO, ordinary commutator sufficiency makes
  `[s,T]_2` bounded. The exact algebraic identity
  `S-[s,T]_2=[b1,T]_1-[b1,T]_2` has kernel factor `b1(y2)-b1(y1)`.
- The second median test controls the full mean oscillation of `b1`.
- For Problem B, a constant first symbol makes the inner commutator exactly
  zero, independently of `T`; `x_1` is locally integrable but not BMO.

## Scope

- Problem A is fully proved for real-valued symbols, the standard setting of
  the median argument. It also covers complex symbols for kernels real-valued
  up to a fixed global phase.
- The packet does not claim the variable-phase complex-kernel/complex-symbol
  corner. Problem B is refuted without any real/complex restriction.

## Artifact checks

- `main.tex` compiled without errors or layout warnings.
- `solution_packet.pdf` is a valid four-page PDF and was rendered at 144 dpi.
- All four rendered pages were visually inspected; equations, margins,
  headings, and references are legible with no clipping or overlap.
- `source_target_1707.01639.pdf` is a valid 18-page PDF.
- The result ledger parses as valid JSON and records model `GPT5.6`.
