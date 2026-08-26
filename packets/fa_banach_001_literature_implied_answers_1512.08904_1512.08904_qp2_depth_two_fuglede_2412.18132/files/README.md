# Compact-open Fuglede in `Q_p^2`: depth two and all-depth subcases

Status: `literature_implied_answer (partial subcase)`

Source: Aihua Fan, Shilei Fan, Lingmin Liao, and Ruxi Shi, *Fuglede's
conjecture holds in `Q_p`*, arXiv:1512.08904v1 (2015), Section 6.4, printed
and PDF page 23.

Supporting paper: Weiqi Zhou, *On Tiling and Spectral Sets in
`Z_{p^2} x Z_{p^2}`*, arXiv:2412.18132v4 (22 March 2026), Theorem 1 on PDF
page 26 and Lemmas 11, 13, 14 on PDF pages 11–12.

## Result

For a normalized compact-open set

```text
Omega_A = A + p^m Z_p^2 subset Z_p^2,
A subset (Z/p^m Z)^2,
```

tiling and spectrality in `Q_p^2` are exactly equivalent to the corresponding
finite properties of `A`. Therefore Zhou's 2026 theorem settles the source
problem for every compact-open set of depth at most two.

At arbitrary depth, Zhou's general lemmas give:

- tile and `|A|=p` implies spectral;
- tile and `|A|=p^(2m-1)` implies spectral;
- at `|A|=p^(2m-1)`, spectral also implies tile.

An elementary subgroup argument additionally gives the full equivalence at
every depth whenever `A` has a subgroup tiling complement or subgroup
spectrum, including arbitrary graph residue sets.

## Why this is not full

The unrestricted compact-open question is equivalent to Fuglede's conjecture
for every subset of `(Z/p^m Z)^2` for all `m`. Zhou proves the complete theorem
only for `m=2`. A direct induction fails: a graph tile in `(Z/8Z)^2` can have
a five-point image modulo four, which cannot tile `(Z/4Z)^2`; nonconstant
fiber multiplicities are essential.

Three focused full-upgrade attempts are recorded in
`runs/fa_banach_001/attempts/1512.08904_qp2_fuglede_finite_quotient_reduction.md`.
No all-depth theorem or counterexample was found in the bounded current
literature search.

## Files

- `main.tex`, `solution_packet.pdf`: exact reduction, partial theorem, and scope.
- `source_paper.pdf`: original open-problem source.
- `supporting_paper_2412.18132.pdf`: decisive 2026 finite-group theorem.
- `verification_report.md`: proof-obligation and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/1512.08904_qp2_depth_two_fuglede_2412.18132.json`.
