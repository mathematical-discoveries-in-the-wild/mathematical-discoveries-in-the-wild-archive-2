# Infinite-dimensional Gibbs-sampler direction addressed by arXiv:2604.01192

Status: `literature_implied_answer (broad direction; exact Metropolis formula scope retained)`.

The source paper, Chi-Fang Chen, Michael J. Kastoryano, and András Gilyén,
*An efficient and exact noncommutative quantum Gibbs sampler*,
arXiv:2311.09207, says after Proposition B.2 (PDF page 32) that its exact
formula appears to extend to infinite-dimensional systems and leaves a
verification for future work.

Simon Becker, Cambyse Rouzé, and Robert Salzmann,
*Quantum Gibbs Sampling in Infinite Dimensions: Generation, Mixing Times and
Circuit Implementation*, arXiv:2604.01192 (2026), explicitly cites the source
as the first exact finite-dimensional Lindbladian sampler and develops a
rigorous framework for KMS-symmetric quantum Markov semigroups with unbounded
Hamiltonians on separable Hilbert spaces.  Proposition 2.8 gives the
trace-class generator, and Section 4.1/Proposition 4.3 treats the
Gaussian-convoluted exact KMS construction and a spectral-agnostic coherent
term.  Later sections prove finite-dimensional approximation and circuit
implementation.

This is an agent-identified implication, not a claim that the supporting paper
repeats Proposition B.2's exact quasi-Metropolis time-domain formula verbatim.
That formula-specific identification remains a narrower question.  The broad
future-work direction—rigorous infinite-dimensional exact detailed balance and
implementable truncations—is already answered in the 2026 literature, so it is
not viable as a new-result target.

Files:

- `source_paper.pdf`: arXiv:2311.09207.
- `supporting_paper_2604.01192.pdf`: the decisive 2026 supporting paper.
- `solution_packet.pdf`: compact literature-status note.
