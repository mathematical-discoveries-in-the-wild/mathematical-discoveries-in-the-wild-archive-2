# Full candidate: two-scale Beckner inequalities via score transport

Status: `candidate_full_solution_likely_valid` (awaiting human review).

Source target: Vishwak Srinivasan, *Understanding two-scale criteria for
Poincare and log-Sobolev inequalities in the Euclidean case through
Phi-entropies*, arXiv:2509.15410, Discussion and Section 6.1, source PDF
pages 21--22.

For every `1 < p <= 2`, this packet proves joint and mixture
`Phi_p`-Sobolev inequalities under an exact power-divergence score-transport
condition.  It then verifies that condition in two regimes already central to
the source paper:

- if the conditional scores are pointwise bounded by `B`, the joint and
  mixture have exactly the same constant formulas `zeta(B)` and `xi(B)`
  conjectured in the source;
- under the source MGF condition with proxy `barL^2`, the full Beckner scale
  holds with `barL^2` replaced by `p barL^2`.

The proof bypasses the failed Legendre-duality route.  For a test function
`psi`, normalize by its conditional mean `M(y)` and use

```text
Ent_{Phi_p,P_y}(psi) = M(y)^p D_p(psi/M(y) || P_y).
```

This exact homogeneity turns the conditional-score covariance directly into
the conditional Beckner entropy.  A sharp power-Pinsker inequality gives the
bounded-score corollary with no loss.

Files:

- `solution_packet.pdf`: review-ready theorem and proof.
- `main.tex`: packet source.
- `source_paper.pdf`: locally compiled arXiv source paper.
- `figures/open_problem_crop_1.png` and `open_problem_crop_2.png`: the complete
  two-page source question and stated obstruction.
- `code/verify_beckner_score_transport.py`: finite numerical sanity checks.
- `code/crop_source_pages.py`: reproducible source-evidence crops.
- `verification_report.md`: adversarial proof and rendering checks.
- `novelty_search.md`: bounded literature-search record.

Important limitations: the factor `p` in the MGF corollary is not claimed
optimal; a variance bound alone does not imply the score-transport condition
for `p<2`; and the packet does not address the source's separate broad HMC
regularity program.

Primary verifier focus: check the normalization and all factors of `p` in the
score term, then the second-derivative proof of the sharp power-Pinsker lemma.

