# Verification

Verified on 2026-08-13 by `agent_lane_15`.

## Artifact and source integrity

- `solution_packet.pdf`: 2 pages; SHA-256 `c479f0f8c4bacc6b5feda831ec2518f99d3f321096f61f2535cdef1f14881ee6`.
- `source/1710.00285.pdf`: official arXiv source PDF, 21 pages; SHA-256 `a9ece1b86ef6c28ec15bcc621b32d8facbef302d10d7a5053fbd23c04e23d4a0`.
- `source/1904.05612.pdf`: official arXiv source PDF, 15 pages; SHA-256 `49de771ab5b79489a1ad2a6dec647bf257c3305864c7c6c9457a467b85ce0103`.
- `source/2102.01462.pdf`: official arXiv source PDF, 16 pages; SHA-256 `acf2e24a8fa6b12c602fa74eaf85ed09f50de54a4c2d38f07898be313cdd467a`.
- `source/source_question_page8.png`: real crop from PDF page 8 of arXiv:1710.00285; SHA-256 `c8566a5aa25828e15eb69ccf89fea1b2249b82c382e2459afb543cf11469f1f2`.
- `main.tex`: SHA-256 `e17fef922b993684620646c25679170471009f87a2d2bf16cec15ee303eaca0c`.

## Rendering audit

The final PDF was rendered at 170 dpi with Poppler to RGB PNG files `tmp/render-1.png` and `tmp/render-2.png`. Every rendered page was visually inspected. Both pages are complete and legible, with no clipping, overlap, missing glyphs, blank pages, or malformed mathematics. The embedded source crop is sharp enough to verify the wording of Remark 3.14 directly.

## Mathematical and provenance audit

- The source question is quoted only through a genuine crop and a faithful paraphrase of Remark 3.14.
- The regular-subfactor statement is scoped to Theorem 3.10 of arXiv:1904.05612.
- The depth-two statement is scoped to Theorem 3.14 and Corollary 3.15 of arXiv:2102.01462.
- The packet labels the outcome as partial: neither cited theorem settles every finite-index irreducible subfactor.
- The proof-intuition discussion tracks the cited proof mechanisms and is separated from the theorem statements.
- Three upgrade attempts were audited: extension up the Jones tower, simultaneous left/right frame scaling, and the group-subfactor polynomial-counting special case. Each obstruction is recorded in the associated attempt note.
- Exact arXiv-id, title, author, and core-keyword searches through 2026-08-13 found no later arXiv theorem settling the unrestricted two-sided-basis question.
