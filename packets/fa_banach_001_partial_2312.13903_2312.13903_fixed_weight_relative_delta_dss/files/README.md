# A fixed-weight DSS criterion for Orlicz--Lorentz inclusions

**Status:** candidate partial result, likely valid; full characterization not
claimed.

**Source:** Luis Bernal-González, Daniel L. Rodríguez-Vidanes, Juan B.
Seoane-Sepúlveda, and Hyung-Joon Tag, *New Results in Analysis of
Orlicz-Lorentz spaces*, arXiv:2312.13903, Section 5, item 4 (source page 34;
published in *Advances in Mathematics* 489 (2026), 110808).

## Result

For any fixed weight `w` on `[0,1]`, consider the continuous inclusion

`J : Lambda_{phi_2,w} -> Lambda_{phi_1,w}`.

The following are equivalent:

1. `phi_2` satisfies the relative `Delta_{phi_1}(infinity)` condition;
2. the norm ratio `||f||_{phi_1,w}/||f||_{phi_2,w}` tends uniformly to zero
   over all nonzero functions supported on sets whose measure tends to zero.

Consequently, the relative-Delta condition makes `J` disjointly strictly
singular.  The proof is a direct high/low-amplitude modular split and works
for every fixed weight without an ordinary `Delta_2` assumption.  Conversely,
mutual domination of the two Orlicz functions at infinity makes the two norms
equivalent, so `J` is not DSS.

This answers a substantial sufficient regime of the source question and
exactly characterizes the stronger uniform small-support property.  It does
not characterize all DSS inclusions: failure of uniform small-support decay
only yields disjoint blocks with individual norm ratios bounded below, not an
isomorphism on their entire closed span.

## Files and verification

- `solution_packet.pdf`: reviewer-facing theorem, proof, limitations, and
  bounded novelty check.
- `VERIFIER_REPORT.md`: independent proof-structure and render checklist.
- `source_paper.pdf`: the original arXiv source.
- `figures/open_problem_crop.png`: real source-page crop of Section 5, item 4.
- `code/render_open_problem.py`: reproducibly renders that crop.
- Attempt record:
  `runs/fa_banach_001/attempts/2312.13903_fixed_weight_dss_upgrade_attempts.md`.
- Ledger:
  `runs/fa_banach_001/ledger/results/2312.13903_fixed_weight_relative_delta_dss.json`.

The main reviewer checks are the Luxemburg normalization in the modular split,
the inverse-function equivalence, and whether the criterion is already
implicit in a broader almost-compact embedding theorem.
