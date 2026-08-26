# Counterexample packet: starred moments do not determine the pattern

Status: candidate full counterexample, likely valid, needs human review.

Source: Tapesh Yadav, *Wigner type laws for structured random matrices*,
arXiv:2201.00257.

Question: Section 5.3 asks whether two non-similar patterns must have
non-identical collections of limiting starred moments.

Result: no. The equal-half and unequal-half unions of two half-squares are
almost surely not similar at any matrix size from two onward, because their
traces differ. Nevertheless every limiting starred moment agrees.

Stronger theorem: every pattern whose horizontal and vertical sections have
the same constant measure `p` has, in a word of length `2n`, exactly `p^n`
times the corresponding full-square moment. Thus each `p` gives a large
moment-equivalence class.

Mechanism: every leading pairing quotient is a tree. Integrating a leaf uses
one of the two constant-section identities and contributes `p`. For the two
explicit block patterns, equality constraints and inequality constraints each
have exactly two block labelings on any tree.

Novelty check: exact-title, exact-question, variance-profile, and starred-
moment searches were run on 2026-08-12. They found relevant circular-law
literature but no later answer to this pattern-injectivity question. The local
arXiv corpus and the four cheap run indexes had no matching resolution.

Files:

- `main.tex`: full result and proof.
- `solution_packet.pdf`: compiled and visually checked proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_question_crop.png`: page-20 source crop.
- `verify_pairing_weights.py`: exhaustive low-order pairing verifier.
- `VERIFICATION.md`: analytic, computational, and visual QA report.

Review recommendation: check the leading-pairing tree reduction and the
finite-grid vertical-reversal trace witness. No numerical assumption is used
in the proof.

