# Full solution: no largest ideal with Hilbert space ideal

status: candidate_full_solution_likely_valid

source: Valentin Ferenczi, *There is no largest proper operator ideal*,
arXiv:2005.07672v2 (2021), published in *Mathematische Annalen* 387
(2023), 1043--1072.

target: Question 6.2 asks whether there is a largest operator ideal `U`
whose identity spaces are exactly the separable Hilbert spaces.

packet: `runs/fa_banach_001/solutions/full/2005.07672_no_largest_hilbert_space_ideal/`

ledger: `runs/fa_banach_001/ledger/results/2005.07672_no_largest_hilbert_space_ideal.json`

## Result

The answer is **no**, over both the real and complex scalars.

Let `H = ell_2`, let `X = X_S` be the Gowers--Maurey shift space, and
let `Y_t = Im(T_t)` be Ferenczi's infinite-codimensional range for
`T_t = I - tS + K_t`, with `t` equal to `1` or `-1`. Define

`J_t = Opp(H direct_sum X) intersection Opp(H direct_sum Y_t)`.

The proof establishes `Space(J_t) = H`, the space ideal of separable
Hilbert spaces. A largest ideal in this fiber would therefore contain both
`J_1` and `J_{-1}`, hence both `T_1` and `T_{-1}`. Their sum is Fredholm on
the non-Hilbert space `X`, forcing `I_X` into the alleged largest ideal and
contradicting its space ideal.

## Key new step

Gowers--Maurey prove that `X_S` has no unconditional basic sequence, so
`ell_2` and every finite power of `X_S` (or of a subspace `Y_t`) are
essentially incomparable. Gonzalez's direct-sum decomposition theorem then
splits a common complemented subspace into Hilbert and exotic pieces. The
exotic piece would, after discarding a finite-dimensional kernel, be a
complemented subspace of `X_S^m` embedded in `Y_t^n`, contradicting
Ferenczi's Proposition 4.4. Thus every common complemented subspace is
Hilbertian.

## Verification status

- The exact source question and Proposition 4.4 were checked in the source
  PDF and TeX.
- The no-unconditional-basic-sequence input was checked in the primary
  Gowers--Maurey source, arXiv:math/9407209, Section 5.2.
- The statement of Gonzalez's 1994 decomposition theorem was checked against
  the article abstract and bibliographic record.
- Exact and close-variant web searches performed on 2026-08-09 found the
  source question but no later answer.
- The packet is intended for expert human review; the most important point to
  audit is the use of upper semi-Fredholm stability under strictly singular
  perturbations in Lemma 3 of the packet.

## Files

- `main.tex`: complete proof and references.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of Question 6.2.
- `verification.md`: proof and novelty audit.
- `code/crop_source_page.py`: reproducible source-page crop.
