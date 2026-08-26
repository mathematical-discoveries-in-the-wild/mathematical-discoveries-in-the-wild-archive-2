# Verification

## Claim audit

- Question 5.4 and its definition of independent equal-endpoint paths were
  checked in the parsed TeX and on source PDF page 11.
- The original Faudree--Simonovits paper was checked directly, not only
  through search snippets: its `C_{k,t}` definition is on supporting PDF page
  3 and Theorem 1 is on page 4.
- `C_{s,l}` consists of exactly `l` internally vertex-disjoint paths of
  exactly `s` edges with their two endpoints in common, matching the source.
- Theorem 1 gives `ex(v,C_{s,l}) <= c_{s,l} v^(1+1/s)` for every fixed
  `s,l`; its contrapositive proves Question 5.4 with `D=c_{s,l}`.
- Publication metadata was checked: Combinatorica 3 (1983), no. 1, pages
  83--93. The answer predates arXiv:0102211 (2001).
- Cheap run indexes contained no duplicate. A 2013 scholarly survey and
  modern theta-graph papers corroborate the classical attribution.

## Mathematical scope

This packet completely answers Question 5.4 affirmatively. It does not
address the paper's operator-space question about sigma(p) versus complete
sigma(p), its density conjecture for non-even p, or the separate circuit
exponent question.

## Artifact checks

- [x] Official source PDF and a full scan of the original answering paper are
  present and readable (14 and 12 pages).
- [x] Exact source-question, answer-definition, and answer-theorem crops were
  rendered from those PDFs and visually checked.
- [x] `main.tex` compiles without errors, undefined references, or box
  warnings.
- [x] Final PDF metadata and text extraction are healthy (3 letter-size
  pages, 3,864 extracted text characters).
- [x] Every final page was rendered at 150 dpi, confirmed RGB, and visually
  inspected for clipping, collisions, bad breaks, and legibility.
- [x] SHA-256 hashes are recorded below.

## SHA-256

```text
a162ba88166c0f14ba78c0354122fab2e302515f9cdb6a1830f62690c267480d  main.tex
a60f7a4cd9e86053db6620b07c801349731d43b0190d35943efb9bc2eff603b6  README.md
919005722279be9b33c797759453feec3592251d7ec65edc9bb07b4fba5a2403  solution_packet.pdf
358c12ffeea9f22b48983523c5c9132bb14f8575ae6c4457c1e44c5d00cc8757  source_paper.pdf
4067b31cf4b755bdd3af13f5b8eb93fd8400181345e2fa8a4938100be250c2dd  supporting_paper_faudree_simonovits_1983.pdf
0823cc45588afdb03859aa5e139c321e499ae7c8f56a10aebf46e2984948f96b  evidence/source_question_crop.png
07fc9e3c4166499e4de3139d945f8bf566f3a2a7e728d811df9f88026eaf0d88  evidence/answer_definition_crop.png
2e51c467a28e53cec5c7e039117ac1440264edd8caa80da8f15a1ee5041a1ee7  evidence/answer_theorem_crop.png
```

Verification completed at 2026-08-13T15:23:22Z.
