# Verification record

## Mathematical match

- Source page 4 asks whether the same supremal maximal-perimeter constant
  `Gamma_n` grows linearly in `n`.
- Supporting paper page 3, Theorem 1.2, states `Gamma_n ≍ n`.
- The supporting introduction cites arXiv:2602.03831 for the prior
  `Gamma_n <= C n^(3/2)` estimate, eliminating a notation or scope mismatch.
- Supporting page 19 proves `Gamma(mu) <= C n` for every isotropic
  log-concave probability measure and invokes the isotropic cube for the
  matching lower bound.
- No additional symmetry, smoothness, or product assumption is imposed.

## Source provenance

Both PDFs were compiled verbatim from exact archived arXiv source downloads:

- `data/raw/arxiv/2602.03831/source_download`
  SHA-256 `1eb7475c06a981f4bc47ebc8861cdfdea5f2af86e9497c8e7046175de9d1339a`.
- `data/raw/arxiv/2605.02747/source_download`
  SHA-256 `628e6a58b7742031f1bf1f3b8dbd6c4bbbe34f8461261731f11fff5fe9ec5a90`.

Compiled PDFs before packet finalization:

- `source_paper.pdf` SHA-256
  `ff7a02c06377c80410255441a4c979796ce7d54626079de3df222e11c2cb8f73`.
- `supporting_paper_2605.02747.pdf` SHA-256
  `a540ea9193d7071888f46cfdb9188f69fe822805fcb9ad8bb4cda103b5af8d42`.

The original papers' internal cross-references resolve after two LaTeX
passes. Their displayed bibliographies are embedded directly in the source.

## Evidence crops

- `source_question_crop.png` SHA-256
  `d7ab0bff7994db2d84444ea5a8aa42b9feb4fd5ad06bfe3c36f1a5ea9cb51762`.
- `supporting_theorem_crop.png` SHA-256
  `25c6f1565f2bd005df6a44714daacbcdcab5f34007a92d61ed1ed8e37120fe3c`.
- `supporting_proof_crop.png` SHA-256
  `5d10d9a4ae29857dade4a09752a6fff3562ef3f4f2457ecb49593e2ea604d4f7`.

All three crops were rendered at 180 dpi and inspected visually before being
placed in the packet.

## Final packet QA

- `solution_packet.pdf` has 3 letter-size pages.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error` completed after two
  passes with no warnings, overfull boxes, underfull boxes, or unresolved
  references in `tmp/main.log`.
- Ghostscript `nullpage` validation succeeded.
- Ghostscript text extraction contains the status, source question, exact
  supporting theorem, proof mechanism, Proof Intuition, provenance, and both
  references.
- Every final page was rendered at 180 dpi and visually inspected. There are
  no clipped elements, collisions, illegible evidence crops, or stray blank
  pages.
- Final `solution_packet.pdf` SHA-256:
  `7689d34a7633b32e7a9205c46a459f49424b084332014522cb6ac2ead2d4a1bf`.
