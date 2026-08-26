# Two Survey Conjectures Refuted in Later 2026 Papers

Status: `literature_already_answered`

## Source

- A. Aldroubi, C. Cabrelli, I. Krishtal, and U. Molter, *Dynamical Sampling: A Survey*, arXiv:2511.10769v3.
- Conjecture 1 (typeset page 9): a Bessel suborbit sampled at Müntz–Szász times should remain a frame for every positive-spectrum Carleson frame.
- Conjecture 3 (typeset page 19): normalized orbits of bounded normal operators should never form frames in infinite dimension.

## Resolution

- Conjecture 1 is false. Gallardo-Gutiérrez and Partington, arXiv:2605.29671v1, explicitly give counterexamples to this conjecture. Their Example 3.4 includes prime sampling. The packet specializes it to the concrete diagonal data `r_j = 1 - 2^{-j}`, `b_j = sqrt(1-r_j^2)` and gives a complete short proof. The later density theorem in Krishtal–Miller, arXiv:2607.18491v1, also subsumes this example because the primes have natural density zero.
- Conjecture 3 is false. Krishtal and Pfander, arXiv:2606.20848v1, explicitly identify the survey conjecture and construct a bounded invertible normal operator on `l2(N)` whose normalized single-vector orbit is a frame.

No novelty is claimed. The prime proof is included to make the first negative answer immediately checkable without reconstructing the functional model in the supporting paper.

## Files

- `main.tex`, `solution_packet.pdf`: literature-status note and proof.
- `source_paper.pdf`: arXiv:2511.10769v3.
- `supporting_paper_2605.29671.pdf`: direct counterexample to Conjecture 1.
- `supporting_paper_2606.20848.pdf`: direct counterexample to Conjecture 3.
- `supporting_paper_2607.18491.pdf`: later density characterization subsuming the prime example.
- `references.md`: exact evidence map.
- `verification_report.md`: build and mathematical verification record.

## Human review

- [ ] A human expert has independently checked the packet.
