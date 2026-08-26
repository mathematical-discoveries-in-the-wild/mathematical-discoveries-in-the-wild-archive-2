# Verification

## Mathematical scope

- Source: arXiv:math/0311324, PDF page 4.
- Exact question: for arbitrary Banach `X`, are PP-narrow maps
  `L_1[0,1] -> X` stable under two-term sums?
- Later answer: V. V. Mykhaylyuk and M. M. Popov, *On sums of narrow
  operators on Köthe function spaces*, JMAA 404 (2013), 554--561,
  DOI `10.1016/j.jmaa.2013.03.008`.
- The publisher abstract states that for every Köthe Banach `E` there are a
  Banach space `Y` and two narrow maps `E -> Y` with non-narrow sum, and
  explicitly identifies `E=L_1` as a negative answer to the question.
- The authors' 2012 conference abstract writes the exact arbitrary-range
  question and announces a negative answer.
- The official 2025 Kadets--Martin--Rueda Zoca--Werner monograph states the
  finished counterexample and cites the 2013 paper as reference [236].
- “Narrow” in the later Köthe-space paper is the Plichko--Popov condition
  called “PP-narrow” by the source.  The sign and quantifier definitions match.
- This does not conflict with the positive result for self-maps in `L(L_1)`;
  the counterexample uses a different Banach range `Y`.

## Source evidence

- `evidence/source_question_page-04.png`: 180-dpi RGB render of source PDF
  page 4.
- `evidence/source_question_crop.png`: unaltered crop containing the source
  open-problem sentence.
- `evidence/conference_answer_page-027.png`: 180-dpi RGB render of the
  conference PDF page 27.
- `evidence/conference_answer_crop.png`: unaltered crop containing exact
  Problem 1 and the negative-answer announcement.
- `evidence/monograph_counterexample_page-158.png`: 180-dpi RGB render of
  monograph PDF page 158 (book page 140).
- `evidence/monograph_counterexample_crop.png`: unaltered crop containing
  Definition 5.4.2, the positive self-map result, and the counterexample.

## Packet QA

- Build in `tmp/` with `latexmk -pdf`.
- Render every final page to RGB PNG and visually inspect it.
- Record final page count, file sizes, and SHA-256 hashes below after sealing.

## Sealed artifacts

- Final packet: 4 Letter pages, unencrypted PDF 1.7.
- Every final page was rendered at 150 dpi in RGB mode and visually inspected.
- Sealed at: `2026-08-11T22:23:48Z`.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `solution_packet.pdf` | 715619 | `2f069df5606781f4e45a1e0f466bf3734efbb81bb56c1ad248a3a34acc506209` |
| `source_paper.pdf` | 159792 | `9f44c06b4acab8dd774cda45552b2eb78110a9649b317210529102965fcd166d` |
| `supporting_conference_2012.pdf` | 2547229 | `7d6e4754e559a6329a1a323a4de6ab8eb2272de00fc3dbf4d5adc06af96a2f80` |
| `supporting_monograph_2025.pdf` | 4605119 | `7632410ca60e80dc74f5db1bf4eda2ca41836304f19b41d2802d5171eb4217c6` |
| `evidence/source_question_crop.png` | 138196 | `3622bcbdb6ac8dfc2fdadd12549d4f4c9fb5c7b60a06b083bbe2c3e76080278f` |
| `evidence/conference_answer_crop.png` | 138883 | `a4aa6807196d2f84d246afe012990ebf189561e51a79594f39bd59b6a776435c` |
| `evidence/monograph_counterexample_crop.png` | 257491 | `7270db09356ada8146ba1a8d0c907e2aadbab4874aa3ce573aeedb4e848da5e8` |
