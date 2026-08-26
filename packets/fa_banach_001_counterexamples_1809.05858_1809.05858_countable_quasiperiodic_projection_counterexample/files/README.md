# Counterexample packet: countably many quasiperiodic projections

Status: `candidate_counterexample_likely_valid`

Source: Omer Ginat, *The Method of Alternating Projections*,
arXiv:1809.05858, the question on printed page 16 asking whether Sakai's
finite-family norm-convergence theorem remains true for `J = infinity` and a
quasiperiodic index sequence.

## Result

The answer is negative.  The packet constructs explicitly:

- a countable family of closed hyperplanes in `ell_2`, together with the
  whole space as one harmless member;
- a sequence `sigma: N -> N` in which every index has bounded gaps; and
- a unit initial vector whose successive orthogonal projections do not
  converge in norm.

The orbit is exactly `a_k v_k` at times `2k-1` and `2k`, where `(v_k)` is a
slowly rotating weakly-null unit sequence and `a_k` tends to a positive
constant.  Thus the orbit converges weakly to zero while its norm stays away
from zero.  The common intersection of the subspaces is `{0}`.

## Files

- `main.tex`: self-contained counterexample and bounded literature audit.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `code/check_schedule.py`: finite-dimensional verification of the exact
  shadowing identity; it is not used as proof.
- `verification.md`: proof and render checks.

## Novelty status

The run indexes and exact arXiv searches were checked on 2026-08-11.  The
later arXiv:2405.04848 treats a different pseudo-periodic regime with a finite
recurrent core and additional monotonicity assumptions; it does not cover the
present schedule, in which every one of countably many indices is recurrent.
No exact later answer was found within the bounded search.  Novelty is
plausible, not certified.
