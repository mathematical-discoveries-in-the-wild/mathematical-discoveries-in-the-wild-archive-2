# Weak-star and UEB topologies agree on Haar-density probabilities

Status: `full_solution_likely_valid`

Source: Vadim Alekseev, Hiroshi Ando, Friedrich Martin Schneider, and
Andreas Thom, *Amenability and skew-amenability of actions of topological
groups*, arXiv:2412.00438v2 (2025-10-24).

## Result

The unnumbered question after Remark 3.12 on page 9 has an affirmative
answer. For every locally compact group `G` with left Haar measure `nu`, the
topology `sigma(C_0(G)^*, C_0(G))` on `P(G,nu)` agrees with each topology
pulled back from the UEB topology by the right- and left-uniform embeddings
`Xi_nu`. In particular, both maps `Xi_nu` are weak-star-to-UEB continuous.

The key missing step beyond Appendix Lemma A.2 of the source is tightness.
A weak-star neighborhood of any probability measure forces all nearby
probabilities to put almost all mass in one compact set. A bounded uniformly
equicontinuous test family is totally bounded in sup norm on that compact set
by Arzela-Ascoli. A compactly supported cutoff and a finite net then upgrade
pointwise weak-star control to uniform control over the whole UEB family.

## Files

- `main.tex`: complete proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv:2412.00438v2.
- `figures/open_problem_crop.png`: the question on source page 9.
- `tmp/`: build and rendering intermediates.

## Verification and novelty

The proof is non-computational. The main points for human review are that
weak-star convergence inside the probability subspace gives eventual
uniform tightness even for nets, and that the compact-space Arzela-Ascoli
theorem requires neither metrizability nor second countability.

On 2026-08-09 the run indexes were searched for the arXiv id, title, and the
terms `weak-star UEB probability topology`, with no duplicate result. A
bounded arXiv/web search used the exact quoted sentence, the displayed
duality notation, and close variants. It found the current source and general
UEB/weak-convergence background, but no later paper explicitly resolving this
question. The current arXiv v2 still contains the question.

Human-review recommendation: verify and promote after checking the cutoff
estimate and the standard inclusion
`C_0(G) subset RUCB(G) intersection LUCB(G)` for the source conventions.
