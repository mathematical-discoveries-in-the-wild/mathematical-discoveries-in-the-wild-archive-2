# Partial Result: The SD-Nonfriendly Converse for (c_0)-Sums

Status: `candidate_partial_likely_valid_needs_human_review`

Run: `fa_banach_001`  
Agent: `agent_lane_07`  
Source: D. Bilik, V. Kadets, R. Shvidkoy, G. Sirotkin, and D. Werner,
*Narrow operators on vector-valued sup-normed spaces*, arXiv:math/0106227.

## Target

Proposition 4.3(c) of the source proves that, if every strong Daugavet
operator on (C(K,E)) is (C)-narrow, then (E) is SD-nonfriendly.  The
paper asks whether the converse holds.  The same question is still listed as
Question 8.2 in the authors' May 2025 monograph.

## Result

Write (mathsf P_K(E)) for the property that every strong Daugavet operator
(C(K,E)\to W), with arbitrary range (W), is (C)-narrow.  This packet
proves two permanence principles:

1. (mathsf P_K) passes from a norm-dense family of (M)-summands to the
   ambient space.
2. Both (mathsf P_K) and SD-nonfriendliness pass to arbitrary
   (c_0)-sums, provided the summands have the corresponding property.

Consequently, if

\[
  E=\Bigl(\bigoplus_{\gamma\in\Gamma}E_\gamma\Bigr)_{c_0}
\]

and every (E_\gamma) is separable and USD-nonfriendly, then (E) is
SD-nonfriendly and every strong Daugavet operator on (C(K,E)) is
(C)-narrow for every compact Hausdorff (K).  The index set (Gamma) may
be uncountable.  In particular, the converse holds for every
(c_0)-sum of finite-dimensional spaces, extending the source's single
(c_0) example to a broad nonseparable class.

## Scope

This is a substantial positive class, not a solution of the unrestricted
equivalence.  The proof depends on norm-dense approximation by
(ell_\infty)-summands.  An arbitrary SD-nonfriendly space need not have
such an (M)-summand skeleton.

## Files

- `main.tex`: theorem, proof, literature status, and obstruction analysis.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: source paper.
- `supporting_monograph_2025.pdf`: authors' 2025 monograph retaining the
  question as open.
- `VERIFICATION.md`: proof and artifact checks.

## Novelty check

The cheap run indexes were searched for the exact arXiv id, title,
SD-nonfriendly, USD-nonfriendly, (C)-narrow, strong Daugavet, direct-sum,
and (c_0)-sum phrases.  A bounded primary-source web search found the source
and the 2025 monograph, but no later answer or explicit statement of this
(c_0)-sum permanence theorem.

