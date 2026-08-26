# Sharp scaled limsup law for cosine families

Status: literature_implied_answer_full_scope_likely_valid

Source: Felix L. Schwenninger and Hans Zwart, *Less than one implies zero*,
arXiv:1310.6202, Remark 2.6 (PDF page 6).

## Answer

Every case in the source remark has a sharp affirmative answer:

- for `a > 0`,
  `limsup ||C(t)-cos(at)I|| < 8/(3 sqrt(3))` implies
  `C(t)=cos(at)I`; the constant is optimal, witnessed at equality by
  `cos(3at)I`;
- for `a = 0`, the optimal constant is `2`; and
- for semigroups, the optimal constant is `1`.

The unscaled cosine and semigroup cases are explicit in arXiv:1504.02355.
The remaining scaled case follows from arXiv:1502.00150: its Theorem 2.3
makes a bounded cosine sequence scalar when its first element has singleton
spectrum, and Lemma 3.5(ii) gives the sharp scalar frequency separation.
The tail hypothesis makes the whole strongly continuous cosine family
bounded; characterwise recurrence then forces all scalar frequencies to
equal `a`, so each sampled sequence has singleton spectrum.

## Provenance and scope

This is classified as a literature-implied full answer. The supporting
papers contain all decisive structural theorems, but they do not state the
scaled limsup implication; in fact arXiv:1504.02355 still records it as a
related open question. The packet supplies the short missing bridge and the
sharp constants.

A bounded search by exact formula, ids, titles, authors, and the core phrases
found no later paper explicitly stating the continuous scaled result.

## Packet contents

- `main.tex`, `solution_packet.pdf`: complete identification and proof.
- `source_paper.pdf`: arXiv:1310.6202v3.
- `supporting_paper_1502.00150.pdf`: singleton-spectrum and scalar-separation
  theorems.
- `supporting_paper_1504.02355.pdf`: unscaled cosine and semigroup results.
- `figures/`: source and supporting-theorem crops.
- `verification_report.md`: mathematical and artifact checks.

Human review should focus on the scalar discontinuity dichotomy and the
singleton-spectrum step in the generated commutative Banach algebra.
