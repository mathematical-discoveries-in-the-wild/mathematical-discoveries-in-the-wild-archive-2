# Counterexample to the probabilistic continuous Hilbert norm conjecture

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source: Bañuelos--Kim--Kwaśnicki, arXiv:2209.09737, Conjecture 9.6.

## Result

The source conjectures that its probabilistic continuous Hilbert transform
`T` has

```text
||T||_(L^p -> L^p) = cot(pi/(2p*)).
```

This is false already at `p=2`.

Corollary 9.3 decomposes the kernel as

```text
K_T(x) = 1/(pi x) + J(x),
```

where `J` is odd, integrable, and strictly positive for `x>1`. Moreover
`M=integral_1^infinity x J(x) dx` is finite and positive. Therefore, with the
Fourier convention `exp(-ix xi)`,

```text
hat J(xi) = -2 i M xi + o(xi)       as xi -> 0+.
```

The Hilbert kernel has multiplier `-i` at positive frequencies, so

```text
m_T(xi) = -i(1 + 2M xi + o(xi)),
```

whose modulus is strictly larger than one for all sufficiently small positive
`xi`. Plancherel gives `||T||_(2->2)>1`, whereas the conjectured value is
`cot(pi/4)=1`.

## Scope

This fully disproves the claim about the one-dimensional continuous operator
`T`, and hence Conjecture 9.6 as stated. It does not give the exact `L^2` norm
or settle the higher-dimensional `T^(k)` and classical discrete Riesz-transform
questions.

## Duplicate and novelty checks

The four cheap indexes have no exact hit for arXiv:2209.09737 or Conjecture
9.6. Bounded arXiv-facing searches for the paper title, probabilistic
continuous Hilbert transform, the conjectured norm, and the source's numerical
constant found no matching resolution. Human review should check for an
erratum or later discussion not indexed under the exact terminology.

## Files

- `main.tex`: full multiplier proof.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/open_question_crop.png`: actual crop of Conjecture 9.6.
- `code/crop_open_question.py`: crop script.
- `verification_report.md`: source, analysis, build, and visual checks.
