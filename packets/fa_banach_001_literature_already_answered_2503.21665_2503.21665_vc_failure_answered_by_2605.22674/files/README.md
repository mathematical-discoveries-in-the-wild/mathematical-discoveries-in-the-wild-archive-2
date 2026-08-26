# Vitali--Caratheodory does not force Newtonian quasicontinuity

status: `literature_already_answered`

source: Anders Bjorn, Jana Bjorn, and Lukas Maly, *Non-quasicontinuous
Newtonian functions and outer capacities based on Banach function spaces*,
arXiv:2503.21665.

supporting answer: Anders Bjorn and Jana Bjorn, *Quasicontinuity of
N^{1,infinity} functions and the Vitali--Caratheodory property on general
metric spaces*, arXiv:2605.22674.

## Identification

The source asks whether the properties not supplied by its
Vitali--Caratheodory theorem can fail when the underlying function space has
the Vitali--Caratheodory property.  In the locally compact setting these are
the quasicontinuity properties (A), (F), and (G).

The later paper answers yes, already for the Banach function space
`X=L^infinity`.  On

```text
P = {0, 2^{-n} : n >= 1},
mu = delta_0 + sum_{n>=1} 2^{-n} delta_{2^{-n}},
```

every singleton has positive measure, so `L^infinity(P)` has the
Vitali--Caratheodory property and `C_infinity` is outer.  Nevertheless,
`chi_{ {0} }` is not weakly quasicontinuous and has no quasicontinuous
representative.  Thus (A), (F), and (G) all fail.

## Packet files

- `solution_packet.pdf`: checked literature-identification note.
- `source_paper.pdf`: official arXiv PDF of arXiv:2503.21665.
- `source_question_crop.pdf`: source PDF page 4 containing the exact question.
- `supporting_paper_2605.22674.pdf`: official arXiv PDF of the answer paper.
- `supporting_answer_crop.pdf`: supporting PDF pages 2 and 4, containing
  Theorem 1.2 and Example 3.3.
- `verification.md`: mathematical match, provenance, and QA record.

The packet does not claim a new theorem and does not resolve the source's
separate questions about `(F) => (E)`, arbitrary Banach function spaces, or
removing properness from the general outer-capacity theorem.
