# Counterexample Packet: Discrete Steklov Spectrum Without Weyl's Law

Run: `fa_banach_001`

Result type: `candidate_counterexample_likely_valid`

## Source Question

- Mikhail Karpukhin, Jean Lagacé, and Iosif Polterovich, *Weyl's law for
  the Steklov problem on surfaces with rough boundary*, arXiv:2204.05294.
- Source location: page 13, Remark 4.3.
- Local PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Remark 4.3 asks whether there are domains whose Steklov spectrum is discrete
but for which the Weyl law fails.

## Counterexample

The answer is yes. Start with the unit square. At the top points
`x_j=2^{-j}`, attach a square room of side

`r_j = exp(-j^2)`

through a rectangular passage of length `r_j` and width

`w_j = r_j^2 log(j+1)`.

The resulting bounded simply connected domain has a rectifiable Jordan
boundary. Its natural boundary Sobolev space has compact embedding into
`L^2(boundary)`, so its Steklov spectrum is discrete. The proof combines a
uniform neck trace estimate with the critical one-dimensional estimate

`int_I |v|^2 <= C |I| log(e/|I|) ||v||_{H^{1/2}}^2`.

On the other hand, a function that rises linearly through passage `j` and is
constant on room `j` has Dirichlet energy `r_j log(j+1)` and boundary mass at
least a fixed multiple of `r_j`. The disjoint test functions therefore give

`sigma_{N-1} <= log(N+3)`.

Thus the counting function is at least `N` at spectral parameter
`2 log(N+3)`. This is incompatible with the planar Weyl law
`N(sigma) = |boundary| sigma / pi + o(sigma)`.

## Verification Status

The packet contains full proofs of:

- the uniform appendage trace inequality;
- compactness of the global boundary trace by a finite-core/uniform-tail
  argument;
- discreteness of the variational Steklov spectrum;
- the logarithmic eigenvalue upper bound and consequent failure of Weyl's
  law.

No computational assertion is used. The verdict is
`candidate_counterexample_likely_valid`, pending expert review of the compact
trace argument in the source paper's natural boundary Sobolev-space
formulation.

## Novelty Check

Before promotion, the run indexes were searched for arXiv:2204.05294, the
source title, `Steklov`, `discrete spectrum`, `Weyl law`, and
`rooms and passages`; no duplicate packet or attempt was found.

Bounded web searches on 2026-08-09 used the exact Remark 4.3 sentence and
variants of `Steklov spectrum discrete Weyl law counterexample` and
`rooms and passages Steklov`. They surfaced the source paper and classical
rooms-and-passages constructions for other boundary-value problems, but no
later answer to Remark 4.3 and no Steklov construction matching this packet.
This is a bounded search, not a claim of exhaustive novelty.

## Files

- `README.md`: this summary.
- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source evidence from page 13.
- `verification.md`: independent proof-check checklist and review focus.
- `tmp/`: LaTeX build intermediates and rendered QA pages.

## Human Review Recommendation

Prioritize review of Lemma 2 (the appendage trace estimate) and the passage
from its uniform tail bound to compactness on the completed boundary Sobolev
space. Once those are accepted, the min--max contradiction to Weyl's law is
immediate.
