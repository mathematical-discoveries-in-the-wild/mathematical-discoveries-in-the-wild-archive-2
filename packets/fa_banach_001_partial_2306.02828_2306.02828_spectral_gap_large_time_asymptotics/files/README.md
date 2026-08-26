# arXiv:2306.02828 — spectral-gap large-time asymptotics

This packet gives a substantial partial answer to the source paper's
question about the optimal range of Lebesgue exponents in its decay theorem.

For the small-data global solution built in the paper, the existing decay at
one admissible exponent first forces entry into a small `L^infinity` ball.
The harmonic-oscillator spectral gap then yields exponential decay in every
`L^a`, `p <= a <= infinity`, at every rate below `d^beta`. A second spectral
argument proves the `L^2` expansion

`u(t) = c exp(-d^beta t) phi_0 + O(exp(-mu t))`

for every `mu < min((d+2)^beta, m d^beta)`.

- `source_paper.pdf`: arXiv:2306.02828v3
- `assets/source_question_crop.png`: direct crop of PDF page 4
- `solution_packet.pdf`: compiled proof packet
- `verification.md`: integrity, mathematical, and visual checks

The result resolves the large-time decay mechanism, but does not settle the
short-time endpoint range in the source's exact all-time estimate. Human
review remains pending.
