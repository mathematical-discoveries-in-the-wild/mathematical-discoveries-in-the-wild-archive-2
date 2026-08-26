# Infinite-dimensional complex `L_p` spaces in the Bernstein problem

Status: `literature_implied_answer (complete for the infinite-dimensional
complex L_p subfamily)`.

Problem 17 of arXiv:2003.11002 asks for the complex Banach spaces `X` on
which Bernstein's inequality holds for every continuous homogeneous
polynomial, equivalently `c(m,X)=1` in every degree.

Theorem 3.1 of arXiv:1908.08107 says that an infinite-dimensional complex
space with the degree-two symmetric operator norm property must have optimal
type and cotype exponents both equal to two.  Since an infinite-dimensional
complex `L_p(mu)` has exponents `min(p,2)` and `max(p,2)`, the all-degree
property forces `p=2`.  Conversely, `L_2(mu)` is Hilbert and Banach's
polarization theorem gives the property in every degree.

Thus, within infinite-dimensional complex `L_p(mu)` spaces, the answer is
exactly `p=2`.  The supporting paper predates the source problem and does not
identify itself as answering Problem 17, so this is an agent-identified
literature implication, not an explicit later solution and not a new proof.

Files:

- `solution_packet.pdf`: compact source-to-theorem identification and scope.
- `source_paper.pdf`: arXiv:2003.11002.
- `supporting_paper_1908.08107.pdf`: the type/cotype obstruction.
- `main.tex`: rebuilt packet source.
- `VERIFICATION.md`: independent source, implication, and render audit.

The arbitrary-space characterization, all finite-dimensional cases, and the
two-Hilbert-block candidate remain open in this recovery.
