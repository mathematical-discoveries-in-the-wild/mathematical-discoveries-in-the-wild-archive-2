# Literature-implied answer: DLSI is invariant under bounded ground-state perturbations

status: `literature_implied_answer (full bounded-perturbation case)`

source: Leonard Gross, *Invariance of intrinsic hypercontractivity under
perturbation of Schrodinger operators*, arXiv:2412.20282v2.

supporting result: Laurent Miclo, *On hyperboundedness and spectrum of Markov
operators*, Invent. Math. 200 (2015), 311--343.

packet:
`runs/fa_banach_001/solutions/literature_implied_answers/2412.20282_dlsi_perturbation_via_miclo_tightening/`

ledger:
`runs/fa_banach_001/ledger/results/2412.20282_dlsi_perturbation_via_miclo_tightening.json`

## Identification

Gross asks in Remark 6.19 (source PDF pages 69--70) whether the ground-state
measure after a bounded potential perturbation satisfies a defective
logarithmic Sobolev inequality (DLSI) whenever the original ground-state
measure does. The answer is affirmative whenever the original ground-state
Markov semigroup is ergodic, as it is when the original ground state is
unique.

A DLSI is equivalent to hyperboundedness. Miclo's Theorem 1 says that an
ergodic, self-adjoint, hyperbounded Markov operator has a spectral gap. Thus
the original form also satisfies a Poincare inequality. Gross's own
Proposition 7.16 (Rothaus tightening) combines that Poincare inequality with
the DLSI to produce a zero-defect LSI. Gross's Theorem 2.2 can then be applied
to the perturbing potential. Every bounded potential meets its exponential
integrability hypotheses, and the perturbed ground-state measure satisfies a
zero-defect LSI, hence in particular a DLSI.

The same implication works for unbounded perturbations satisfying Gross's
two exponential-integrability conditions after the nonquantitative tightening
constant is fixed.

## Provenance and scope

This is a full answer to the bounded-potential question in the standard
unique-ground-state/ergodic setting, but it is classified as a literature
implication rather than a new run proof: every decisive ingredient was
already published. Miclo predates the source question and does not identify
his theorem as answering it; the connection is agent-identified.

The argument does not cover nonergodic forms. It also gives no spectral-gap or
LSI constant from the DLSI constants alone: Miclo proves qualitative existence
and shows that no such general quantitative conversion is possible. If a
Poincare constant `C_P` is known separately, Gross's Proposition 7.16 gives
the explicit tightened constant

```text
c_0 = C + C_P (D/2 + 1)
```

from `Ent(f^2) <= 2 C E(f,f) + D ||f||_2^2`.

## Search bounds

The run indexes were searched for arXiv:2412.20282, the exact title, DLSI,
intrinsic hyperboundedness, and Miclo tightening. Web/arXiv searches through
2026-08-09 used the exact open-question sentence and close combinations of
`DLSI`, `bounded perturbation`, `ground state`, and `Miclo`. They found the
source article and the older hyperboundedness/spectral-gap literature, but no
paper explicitly identifying this implication with Gross's Remark 6.19.

## Files

- `main.tex`: compact derivation and source locations.
- `solution_packet.pdf`: rendered status packet.
- `source_paper.pdf`: arXiv:2412.20282v2.
- `supporting_paper_miclo_2015.pdf`: Miclo's decisive theorem.
- `verification.md`: hypothesis audit and PDF QA.
