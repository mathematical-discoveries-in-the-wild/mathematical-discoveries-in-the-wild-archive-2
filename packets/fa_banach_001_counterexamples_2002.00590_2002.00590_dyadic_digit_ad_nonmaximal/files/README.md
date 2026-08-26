# A dyadic-digit extension showing that `AD(0,1)` is not maximal

Status: candidate full negative answer to Problem 3.9, likely valid, requiring expert review.

Source: Aleksey Ber, Jinghao Huang, Karimbergen Kudaybergenov, and Fedor
Sukochev, *Non-existence of translation-invariant derivations on algebras of
measurable functions*, arXiv:2002.00590v1 (2020). The target is Problem 3.9 on
source PDF p. 13.

## Result

Identify `(0,1)` with the circle and let `b_n(t)` be the `n`th binary digit of
`t` (with either convention on the null set of dyadic rationals). Define

\[
 h(t)=\sum_{n\geq1}\left(\frac34\right)^n b_n(t).
\]

Then every dyadic-rational translate of `h` differs from `h` by a
finite-valued measurable function. Nevertheless, no nonzero localization
`chi_E h`, with `|E|>0`, belongs to `AD(0,1)`. Since `AD(0,1)` is integrally
closed, this makes `h` weakly transcendental over `AD(0,1)`.

Proposition 3.7 of Ber--Chilin--Sukochev therefore extends the approximate
derivative to the strictly larger algebra

\[
 \mathcal B=AD(0,1)[h]
\]

with `delta(h)=0`. The finite-valued translation increments have approximate
derivative zero, so `delta` commutes with every dyadic-rational translation.
Consequently `AD(0,1)` is **not** maximal in the sense asked by Problem 3.9.

The analytic obstruction is quantitative. Every approximately differentiable
function has its ordinary translation difference quotients converge in
measure. But on the half-set where `b_n(t)=0`,

\[
 \frac{h(t+2^{-n})-h(t)}{2^{-n}}=\left(\frac32\right)^n.
\]

The same half-density phenomenon persists inside every positive-measure set,
which rules out every localized `AD` part.

## Packet contents

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: the source-question paper.
- `supporting_paper_1906.00243.pdf`: source for the structure of `AD(0,1)`.
- `supporting_paper_BSCh06.pdf`: source for the weak-transcendental extension theorem.
- `figures/open_problem_crop.png`: source PDF p. 13, including Problem 3.9.
- `VERIFICATION.md`: structural proof and novelty audit.
- `code/verifier.py`: exact finite binary-arithmetic sanity checks.

## Scope and novelty

This is a full negative answer to the literal maximality question. It does not
produce an extension to all of `S(0,1)` and does not contradict the source
paper's nonexistence theorem for complete symmetric Delta-normed algebras with
dense simple functions.

Bounded searches on 11 August 2026 covered all four run indexes; the exact
problem sentence; the arXiv id and title; combinations of `AD(0,1)`, maximal,
translation-invariant derivation, dyadic translation, and approximately
differentiable; the 2023 journal version; and the 2023 paper on the isomorphism
between `S(0,1)` and `AD(0,1)`. No explicit resolution or matching digit-series
construction was found. Novelty is provisional.

## Human-review recommendation

Check the convergence-in-measure lemma for `AD`, the positive-measure
localization argument using the Rademacher digits, and the exact hypotheses of
Ber--Chilin--Sukochev Proposition 3.7. Then verify that a dyadic rotation
changes only the finite binary prefix and hence that the extended derivation
commutes with the whole dyadic translation group.

