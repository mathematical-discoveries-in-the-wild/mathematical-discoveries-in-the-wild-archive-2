# Verification

## Mathematical scope

- Source: arXiv:2308.10455, Open Problem 6.1, PDF page 22.
- Later answer: arXiv:2407.15654, Theorem 5.12, PDF page 25.
- The source class is `A = sum q_alpha partial^alpha` with
  `deg(q_alpha) <= |alpha|`.
- The later class is `A = sum (a_alpha/alpha!) partial^alpha` with
  `deg(a_alpha) <= |alpha|`.
- Setting `a_alpha = alpha! q_alpha` identifies the classes exactly.
- Both properties are positivity preservation on all of `R^n` for every
  semigroup time `t >= 0`.
- Theorem 5.12 is an equivalence, not merely a necessary condition or a
  finite-order special case.

## Source evidence

- `evidence/source_p22-22.png` is a 160-dpi RGB render of source PDF page 22.
- `evidence/source_open_problem_crop.png` is an unaltered crop containing
  the degree-preserving setup and Open Problem 6.1.
- `evidence/support_p25-25.png` is a 160-dpi RGB render of supporting PDF
  page 25.
- `evidence/support_theorem_5_12_crop.png` is an unaltered crop containing
  the full statement of Theorem 5.12.

## Packet QA

- `latexmk -pdf` completed successfully.
- Every packet page was rendered to PNG in RGB mode and visually inspected.
- Page count, hashes, and final artifact checks are recorded below after
  sealing.

## Sealed artifacts

- `solution_packet.pdf`: 5 pages, Letter, unencrypted, 610652 bytes,
  SHA-256 `620e17161683ce947447e2f08b31de0e8bb196c40a75bc563fc690b9a7a5fdac`.
- `source_paper.pdf`: 270246 bytes,
  SHA-256 `90835409031cafacc7d933114abe4675474cc15f357662732b2228cd212f3718`.
- `supporting_paper_2407.15654.pdf`: 599871 bytes,
  SHA-256 `fad4d22d76406ba82fa56eba50f77af14a56fd973ed00a88a62409a9ac9c28fb`.
- `evidence/source_open_problem_crop.png`: RGB,
  SHA-256 `a4bfbc0c8d9fb1fe3eeda905c7f7e9b0eacafff468af2726158cfe5564e109f7`.
- `evidence/support_theorem_5_12_crop.png`: RGB,
  SHA-256 `0082c73272b171a83067156f714b9025c745f9ccb5e7f2b8a54156fad1fc25b7`.

Final visual inspection completed on 2026-08-11 for all five packet pages.
