# Irregular STFT sampling: exact later-literature answer

status: `literature_already_answered`

source: Philipp Grohs and Lukas Liehr, *Non-uniqueness theory in sampled
STFT phase retrieval*, arXiv:2207.05628v2.

supporting answer: Philipp Grohs and Lukas Liehr, *Phaseless sampling on
square-root lattices*, arXiv:2209.11127v2; published in *Foundations of
Computational Mathematics* 25 (2025), 351--374.

## Identification

The source proves that ordinary lattice samples never identify every signal
in `L^2(R^d)` up to global phase, regardless of the window and lattice
density. Its Conclusion (PDF page 32) then asks whether irregular sampling or
greater sampling redundancy can be beneficial.

The later paper gives a direct affirmative answer to the irregular-sampling
branch. Its Theorem 1.1 proves injectivity for a broad analytic window class
on sufficiently dense rectangular square-root lattices

```text
A (sqrt(Z))^(2d),   sqrt(Z) = {+/-sqrt(n) : n >= 0}.
```

Corollaries 1.2 and 1.3 give explicit Gaussian, polynomial-times-Gaussian,
and Hermite windows. The later paper explicitly cites the source as the
ordinary-lattice obstruction it overcomes.

## Packet files

- `solution_packet.pdf`: checked literature-identification note.
- `source_paper.pdf`: official arXiv PDF of arXiv:2207.05628v2.
- `supporting_paper_2209.11127.pdf`: official arXiv PDF of the answer paper.
- `verification.md`: mathematical match, provenance, and QA record.

This is an existence answer, not a classification of all irregular sampling
sets or all windows.
