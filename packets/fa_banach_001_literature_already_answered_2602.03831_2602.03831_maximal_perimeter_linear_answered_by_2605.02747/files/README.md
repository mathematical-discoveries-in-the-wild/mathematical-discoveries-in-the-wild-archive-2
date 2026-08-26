# Exact literature answer to the maximal-perimeter question

status: `literature_already_answered`

source: Silouanos Brazitikos, Apostolos Giannopoulos, Antonios Hmadi, and
Natalia Tziotziou, *On the maximal perimeter of isotropic log-concave
probability measures*, arXiv:2602.03831.

supporting answer: Alexandros Eskenazis, Apostolos Giannopoulos, and Natalia
Tziotziou, *Functional perimeter and the dimensional Brunn--Minkowski
inequality for log-concave measures*, arXiv:2605.02747v2.

## Identification

The source proves `c n <= Gamma_n <= C n^(3/2)` and asks on page 4 whether
`Gamma_n` has linear growth. The later paper cites the source for that
preceding bound and proves in Theorem 1.2 that

```text
Gamma_n ≍ n.
```

Its Section 4 proves the upper bound from the sharp level-set coarea estimate
`integral H^(n-1)(boundary {f >= t}) dt <= C n`; the lower bound comes from
the isotropic cube. This is a full affirmative answer to the exact question.

## Packet files

- `solution_packet.pdf`: checked literature-identification note.
- `source_paper.pdf`: source paper, compiled verbatim from the archived arXiv
  source.
- `supporting_paper_2605.02747.pdf`: answer paper, compiled verbatim from the
  archived arXiv source.
- `figures/source_question_crop.png`: exact source question on page 4.
- `figures/supporting_theorem_crop.png`: Theorem 1.2 on page 3.
- `figures/supporting_proof_crop.png`: proof on page 19.
- `verification.md`: provenance and QA record.

## Provenance

Direct PDF retrieval was unavailable, so the PDFs were compiled without
source edits from the exact local arXiv archives already recorded by the run:

- arXiv:2602.03831 source archive SHA-256:
  `1eb7475c06a981f4bc47ebc8861cdfdea5f2af86e9497c8e7046175de9d1339a`
- arXiv:2605.02747 source archive SHA-256:
  `628e6a58b7742031f1bf1f3b8dbd6c4bbbe34f8461261731f11fff5fe9ec5a90`
