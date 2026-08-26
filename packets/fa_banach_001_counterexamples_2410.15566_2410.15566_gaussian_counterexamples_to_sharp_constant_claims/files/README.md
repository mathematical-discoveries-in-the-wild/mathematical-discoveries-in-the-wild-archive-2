# Gaussian counterexamples to two sharp-constant claims

- status: `candidate_counterexamples_likely_valid`
- run: `fa_banach_001`
- agent: `agent_lane_02`
- model: `GPT5.6`
- source arXiv id: `2410.15566`
- source target: the printed constant in Remark 2.2 and its use in Corollary 2.3; context is Question 2.4 of Antonelli--Calzi--Gordina

## Full results

This packet gives two explicit, normalized Gaussian counterexamples.

1. In the source convention on `H^2`, the Gaussian

   ```text
   f(x,y,z) = pi^(-1) (8/(5*pi))^(1/4)
              exp(-(|x|^2+|y|^2)/2 - 4*z^2/5)
   ```

   has entropy--energy quotient

   ```text
   J(f) = (5/12)(8/5)^(1/6)(pi*e)^(-5/6)
        = 0.0754405987422...
   ```

   This is strictly larger than the constant printed in Remark 2.2,

   ```text
   C_print(2,1) = 2^(-5/2) pi^(-11/12)
                = 0.0619019448788... .
   ```

   Therefore the printed specialization of Corollary 2.3 is false.  The
   source transcribed the gamma-ratio exponent as `1/Q`; Yang's cited theorem
   has `2/Q`.

2. In Suguro's standard convention on `H^1`, the Gaussian

   ```text
   g(x,y,s) = pi^(-1/2) (1/(6*pi))^(1/4)
              exp(-(x^2+y^2)/2 - s^2/12)
   ```

   forces a logarithmic Sobolev constant at least

   ```text
   J(g) = (3/4)(6*pi^3*e^3)^(-1/4)
        = 0.0959268502867...,
   ```

   whereas `2/(Q*pi*e) = 1/(2*pi*e) = 0.0585498315243...`.  Thus the exact-
   equality branch of Suguro's proposal is false already on `H^1`.

Both comparisons have short exact proofs; they do not rely on floating-point
rounding.

## Scope

These are full counterexamples to two explicit numerical claims, not a full
solution of Question 2.4.  The optimal constant `alpha_n` remains open.  The
second counterexample does not refute Suguro's separate asymptotic suggestion
that `2/(Q*pi*e)` may approximate the best constant as dimension grows.

## Novelty check

The run indexes were searched by arXiv id, title, and the core constant
phrases.  A bounded primary-source web search through 2026-08-09 checked the
current arXiv record, Yang's cited theorem, Suguro's journal paper, and queries
for an erratum, correction, or Gaussian counterexample.  No prior correction
or counterexample was found.  This is bounded evidence, not a claim of
exhaustive literature novelty.

## Files

- `main.tex`: expert-facing theorem and proofs, with source evidence crops.
- `solution_packet.pdf`: rendered packet.
- `verification.md`: independent algebra, source, and scope checks.
- `code/verify_constants.py`: exact-form and numerical checks.
- `code/make_evidence_crops.py`: reproducible crop definitions.
- `figures/`: source-claim screenshots used in the packet.
- `source_paper.pdf`: arXiv:2410.15566v1.
- `supporting_paper_yang_2024.pdf`: arXiv:2301.03332v4.
- `supporting_paper_suguro_2024.pdf`: the open-access 2024 proposal.
