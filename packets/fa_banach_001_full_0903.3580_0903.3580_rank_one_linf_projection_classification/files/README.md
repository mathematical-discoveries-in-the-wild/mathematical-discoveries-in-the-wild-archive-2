# arXiv:0903.3580 — exact rank-one L-infinity contractivity classification

Status: candidate full solution, likely valid, pending human review.

The source asks whether parameter pairs beyond its plotted and directly checked families make the rank-one projection `P_{Y_{xi,phi}}` L-infinity contractive. The packet proves there are none.

For every unit vector `v` in `C^N`, the orthogonal projection `vv*` has induced infinity norm

`||vv*||_(infinity -> infinity) = ||v||_infinity ||v||_1`.

It is contractive exactly when all nonzero coordinates of `v` have the same modulus. This gives the complete source parameter list and a dimension-free strengthening.

Files:

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: official arXiv PDF.
- `figures/`: source-page evidence and rendered packet QA pages.
- `code/verify_classification.py`: independent numerical sanity checks.
- `VERIFICATION.md`: verification and novelty notes.
