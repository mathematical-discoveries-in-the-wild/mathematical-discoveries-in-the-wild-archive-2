# Asymmetric-weight conjugation counterexample

This packet gives a counterexample to Theorem 1.5 of arXiv:2507.16516 as
printed, for every fixed `1 <= q < infinity`.  The source defines a weight
only by measurability, the lower bound `omega >= 1`, and
submultiplicativity; it does not require `omega(x)` and `omega(-x)` to be
comparable.  An asymmetric polynomial weight meeting all the stated
hypotheses makes complex conjugation fail on the weighted Fourier algebra.

The packet also proves the exact repair for this obstruction:
`A^q_omega` is closed under complex conjugation if and only if
`omega(x) ~ omega(-x)` almost everywhere.

Files:

- `solution_packet.pdf`: human-readable source-backed proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv v2 source PDF checked on 9 August 2026.
- `figures/`: reproducible crops from source pages 3, 6, 7, and 26.
- `code/crop_source_pages.py`: crop provenance.
- `code/verify_asymmetric_weight.py`: independent symbolic/numerical sanity checks.
- `verifier_notes.md`: proof audit and reproducibility record.
- `novelty_search.md`: bounded literature-search record and claim limits.

This is a candidate mathematical result subject to human verification.  It
does not claim that reflection comparability alone repairs every other step
of the paper's functional-calculus proof.
