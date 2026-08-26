# Verification record

## Mathematical match

- Source PDF page 32 asks whether irregular sampling or greater sampling-set
  redundancy is beneficial after proving universal non-uniqueness for
  ordinary lattices.
- Supporting PDF page 3, Theorem 1.1, gives a positive irregular scheme:
  sufficiently dense rectangular square-root lattices phase retrieve every
  signal in `L^2(R^d)` for a broad analytic window class.
- Supporting Corollaries 1.2 and 1.3 specialize the theorem to
  polynomial-times-Gaussian and Hermite windows.
- The supporting paper explicitly cites *Non-uniqueness theory in sampled
  STFT phase retrieval* as the ordinary-lattice obstruction.
- Scope is recorded as an affirmative existence answer, not a classification
  of all irregular sampling sets or windows.

## Source provenance

- `source_paper.pdf` is the official arXiv PDF for arXiv:2207.05628v2,
  SHA-256 `574fc1fbe36f21c6ebff62a9c3f093a243fb838e469509cc93647f0594b986f9`.
- `supporting_paper_2209.11127.pdf` is the official arXiv PDF for
  arXiv:2209.11127v2, SHA-256
  `69d314bf8c5af48be1f24b58c1f0a76a7c69e13e85ded974468b3d59bec7f84b`.

## Final packet QA

- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed after two
  passes; the final log has no warnings, overfull/underfull boxes, or
  unresolved references.
- `solution_packet.pdf` has two letter-size pages.
- Ghostscript `nullpage` validation succeeded, and text extraction contains
  the status, exact source question, later theorem, proof mechanism, scope,
  and references.
- Both final pages were rendered at 160 dpi and visually inspected. There are
  no clipped elements, collisions, illegible formulas, or blank pages.
- Final `solution_packet.pdf` SHA-256:
  `aecf1c5b76a5978d0f531ea6f4941ca3656d3892b89bda9327634f46a182d01f`.
