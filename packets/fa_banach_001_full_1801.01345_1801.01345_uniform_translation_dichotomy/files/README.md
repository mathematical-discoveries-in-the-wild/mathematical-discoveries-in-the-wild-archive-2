# Uniformly bounded translations: complete dichotomy

**Status:** candidate full result, likely valid  
**Source:** Anton Baranov and Hélène Bommier-Hato, *De Branges spaces and Fock spaces*, arXiv:1801.01345, question following Theorem 2.4 on page 5  
**Agent:** `agent_lane_04` (`GPT5.6`)  
**Date:** 2026-08-13

The packet proves that every nonzero de Branges space whose full real-translation group is uniformly bounded is, as a set, either `PW_a` for some `a>0` or the one-dimensional constant space. Therefore the source's intended infinite-dimensional converse is true. If its wording is read literally without a dimension hypothesis, constants are the unique trivial exception.

The proof first averages the norm to make translations unitary without losing the de Branges axioms. Translation invariance of the new kernel then puts the Hermite--Biehler row `(A,B)` on a one-parameter `SL(2,R)` orbit. Elliptic, parabolic, and hyperbolic generators give respectively the Paley--Wiener kernel, the constant kernel, and an impossible non-positive two-point Gram matrix.

Contents:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:1801.01345.
- `figures/open_problem_crop.png`: full-width source crop containing Theorem 2.4 and the question.
- `proof_audit.md`: explicit verifier report.
- `code/sl2_kernel_audit.py`: symbolic audit of the three kernel forms.

Ledger: `runs/fa_banach_001/ledger/results/1801.01345_uniform_translation_dichotomy.json`.
