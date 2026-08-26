# Fractional ranges for cyclic projections

Status: `literature_implied_answer (full)`.

Source target: Catalin Badea and David Seifert, *Ritt operators and
convergence in the method of alternating projections*, arXiv:1510.04560,
Remark 4.4(b) on PDF page 14.

## Result

For any finite family of closed subspaces `M_i`, with
`T = P_{M_N} ... P_{M_1}`, and every `0 < alpha < 1/2`,

```text
M_1^perp + ... + M_N^perp  subset  Ran(I-T)^alpha.
```

This fully answers the source's stronger fractional-range question and does
not require its aligned-case hypothesis.

The input is Reich--Zalas, arXiv:2205.13843, Lemma 4.1(iii), which proves
`||T^n P_{M_i^perp}|| = O(n^-1/2)` in operator norm.  If `c_n` are the
coefficients of `(1-z)^(-alpha)`, then

```text
B_i = sum_{n >= 0} c_n T^n P_{M_i^perp}
```

converges in operator norm for `alpha < 1/2`, and the absolutely convergent
binomial Cauchy product gives `(I-T)^alpha B_i = P_{M_i^perp}`.

## Files

- `main.tex` and `solution_packet.pdf`: statement, proof, scope, and provenance.
- `source_paper.pdf`: source paper.
- `supporting_sources/reich_zalas_2205.13843.pdf`: later supporting paper.
- `figures/`: exact source-question and supporting-lemma pages.
- `VERIFICATION.md`: proof and PDF audit.

This is an agent-identified implication of known literature, not a claim that
the supporting authors explicitly answered the source question.
