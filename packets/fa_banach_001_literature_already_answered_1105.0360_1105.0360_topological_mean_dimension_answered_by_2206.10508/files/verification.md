# Verification record

## Exact source question

- Source: Benoit Kloeckner, arXiv:1105.0360.
- Location: PDF page 5, immediately after Corollary 1.3.
- Question: whether the topological mean dimension of the push-forward
  map is positive whenever the original map has positive entropy.

## Later answer

- Source: David Burguet and Ruxi Shi, arXiv:2206.10508.
- Location: PDF page 1, Main Theorem.
- Statement: for every compact topological system with positive
  topological entropy, the induced system on Borel probability measures
  has infinite topological mean dimension.

## Identification of the two formulations

On a compact metric space, a finite-order Wasserstein metric induces the
weak-* topology on the Borel probability measures. The source's
`(W_p(X), phi_#)` and the later paper's `(M(X), T_*)` therefore define the
same topological dynamical system after setting `T = phi`. The theorem
answers the exact question and strengthens positivity to infinity.

## Artifact QA

- Both PDFs were downloaded from arXiv and retained in this directory.
- The cited source and theorem pages were rendered before extraction.
- Both evidence crops were visually inspected for completeness and
  legibility.
- The final packet was compiled with `latexmk`, rendered page by page,
  and visually inspected.

## SHA-256

- `solution_packet.pdf`: `fb985f779ee6380c2872da6b262581f85b365b7fd8bdbabd969806b79f73715c`
- `source_paper.pdf`: `34dc64116ac9a51fcb433d53bc0a5e952327d1bdca9d21f3fbe41debe16bfc4c`
- `supporting_paper_2206.10508.pdf`: `1a41c5afb41bbd32e02cb8fea02680ac083a5ec2cd2d332208d96d3b279c03a4`
- `figures/source_question_crop.png`: `50a3c33cb2309068459b06c472abebe6051d407edfe9163909c7a63711d168fe`
- `figures/later_theorem_crop.png`: `cc16f7aa8a2be526b876f8705d5484a806225c1c7093508b96f75fce4dcdac2e`
