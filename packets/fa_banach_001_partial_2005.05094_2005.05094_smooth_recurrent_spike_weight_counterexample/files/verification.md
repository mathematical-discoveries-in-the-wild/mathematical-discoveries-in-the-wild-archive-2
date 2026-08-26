# Verification record

## Source and novelty check

- Exact source problem: arXiv:2005.05094, published PDF page 31, immediately
  after Lemma 7.2.
- The source states that `L^1 cap L^infinity` is necessary and proves a
  positive result for even radially decreasing weights.
- Bounded searches covered the exact open-problem phrase, critical-line
  Carleson weights for Hardy spaces of Dirichlet series, the source title and
  authors, and later related papers through 2026. No prior occurrence of the
  recurrent-spike counterexample or a full weight characterization was found.
- arXiv:2405.03522 answers a different problem from the source (interchanging
  the limits in the mean counting function); it does not address this weight
  problem.

## Mathematical checks

- The unit-norm identity for the truncated zeta kernels is exact.
- The peak estimate follows from a `1/16 + 1/16` phase-error split and the
  triangle inequality, yielding the stated `7/8` amplitude lower bound.
- Rational independence of prime logarithms follows from unique
  factorization; Kronecker recurrence supplies arbitrarily many separated
  peak centers.
- With `h_k=1/k`, `K_k=k^2`, and `log N_k >= 2^k k^2`, every `L^q` budget is
  summable while the tested embedding values grow at least linearly in `k`.
- The symmetric decreasing rearrangement is in `L^1 cap L^infinity` and falls
  exactly under source Lemma 7.2.
- `code/verify_peak_bounds.py` passed its finite peak and parameter-scaling
  checks.

## Artifact QA

- The source PDF was downloaded from arXiv and retained in this directory.
- The final packet compiled without overfull/underfull boxes, unresolved
  references, or substantive warnings.
- All three final pages were rendered at 150 dpi and visually inspected.

## SHA-256

- `solution_packet.pdf`: `81f982631160f6797ce7f26ca6e76c0ea4932718150ea1852977733e3272d6b0`
- `source_paper.pdf`: `9371ee5da9d87bbd1eb51ff68a5ef4cce88c86ca2dfa4f425559735758129015`
- `code/verify_peak_bounds.py`: `9c0fca3e7a08be2bf6656ee0c30d7ff1802f6886eda58842819158b8df99c395`
