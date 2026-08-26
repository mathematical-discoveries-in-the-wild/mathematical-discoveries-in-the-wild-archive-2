# Literature-implied full answer: a weighted arc answers both questions

status: literature_implied_answer

source: Ruxi Shi, *On dimensions of frame spectral measures and their frame
spectra*, arXiv:2002.03855.

supporting literature: Longhui Li and Bochen Liu, *Fourier Frames on Salem
Measures*, arXiv:2506.01280.

## Result

Li--Liu's planar measure

`sigma = (x -> (x, sqrt(1-x^2)))_*(Lebesgue|[-1/2,1/2])`

is singular continuous, has orthonormal spectrum `Z x {0}`, and has Fourier
dimension one. This directly answers Shi's nonzero-Fourier-dimension question.

The packet adds the short upgrade that every positive normalized restriction
of this measure has entropy dimension exactly one. Every restriction has
Fourier dimension at most one, while the unrestricted measure has Fourier
dimension one. Therefore the supremal restricted Fourier dimension and the
infimal restricted upper entropy dimension are both one, answering Shi's
equality question as well.

Li--Liu do not explicitly identify these consequences for Shi's two
questions, so the provenance is literature-implied rather than literature
already answered.

## Files

- `main.tex`: complete identification and proof.
- `solution_packet.pdf`: rendered result note.
- `source_paper.pdf`: arXiv:2002.03855, compiled from cached official source.
- `supporting_paper_2506.01280.pdf`: Li--Liu, compiled from cached official
  source.
- `supporting_evidence.md`: exact source locations and provenance audit.
