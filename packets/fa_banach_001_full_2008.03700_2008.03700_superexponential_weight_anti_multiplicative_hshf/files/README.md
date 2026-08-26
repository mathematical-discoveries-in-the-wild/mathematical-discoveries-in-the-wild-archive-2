# Candidate Full Solution: An Anti-multiplicative HSHF on the Disk

Source paper: Eugene Bilokopytov, *Multiplier algebras of normed spaces of
continuous functions*, arXiv:2008.03700 (Question 4.9, page 13).

Result type: `full`

Status: candidate full solution, likely valid, pending human review.

## Open Question

Question 4.9 asks:

> Does there exist an anti-multiplicative HSHF over the unit disk?

Here an HSHF is a Hilbert space of holomorphic functions whose norm topology
is stronger than the compact-open topology, and anti-multiplicative means that
its bounded multiplier algebra consists only of constants.

## Candidate Contribution

Yes. Define

```text
H = {f(z)=sum_(n>=0) a_n z^n : sum_(n>=0) |a_n|^2 exp(2n^2) < infinity}.
```

This is a Hilbert space of entire functions and therefore an HSHF over the
disk. If `phi(z)=sum b_j z^j` is a multiplier and `b_j != 0` for some `j>=1`,
apply its multiplication operator to the unit vectors
`u_n(z)=exp(-n^2)z^n`. The coefficient of degree `n+j` gives

```text
||M_phi u_n|| >= |b_j| exp((n+j)^2-n^2)
                = |b_j| exp(2jn+j^2),
```

which diverges. Hence no nonconstant multiplier exists, while every constant
is a multiplier. Thus `Mult(H)=C`.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: source PDF crop containing Question 4.9.
- `main.tex`: complete candidate proof and review notes.
- `solution_packet.pdf`: rendered packet.
- `verification.md`: independent proof-obligation checklist.
- `tmp/`: source-page render and LaTeX/rendering intermediates.

## Novelty Check

Before promotion, the run registry and solution/attempt/proof-gap indexes were
searched for arXiv:2008.03700 and the core phrases `anti-multiplicative HSHF`,
`Hilbert space of holomorphic functions`, and `only constant multipliers`.
No duplicate packet or prior run answer was found.

A bounded web search on 2026-08-09 used the exact question, the exact phrase
`anti-multiplicative HSHF`, and close variants about reproducing-kernel Hilbert
spaces with only constant multipliers. It found the source paper and general
multiplier-space literature, but no later source explicitly answering Question
4.9. This is a bounded check, not a claim of exhaustive bibliographic novelty.

## Human Review

Recommended for expert review as a candidate full affirmative answer. The key
check is that the one-coefficient lower bound is legitimate for an arbitrary
multiplier; it is, because multiplication by a monomial shifts Taylor
coefficients without mixing them. A reviewer should also confirm that the
source's convention for HSHF imposes no extra normalization beyond Hilbert
NSHF; the constructed space contains the constant function `1` and has bounded
point evaluations.
