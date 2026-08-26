# All-temperature entropy decay by bounded Gibbs reweighting

Status: `candidate_full_solution_likely_valid_human_review_needed`

Source: Pietro Caputo and Mario Morellini, *Kac's Program and Relative
Entropy Decay for Nonlinear Spin-Exchange Dynamics*, arXiv:2511.05223v1,
Section 4.5 (PDF page 34).

## Result

For every real symmetric interaction matrix `J`, every partition of `[n]`,
and the associated multi-component mean-field spin-exchange kernel, the
nonlinear evolution has uniform exponential relative-entropy decay to the
matching Ising equilibrium.  An explicit valid rate is

`alpha_J = (1/(4n)) exp(-3 osc_sigma (sigma^T J sigma / 2))`.

This removes the source's high-temperature, positive-definiteness, and
spectral-radius restrictions and affirmatively answers its exponential
ergodicity question.  The rate may be exponentially small in `n`, as the
source explicitly permits.

## Mechanism

The bounded likelihood transform with weight
`w(sigma)=exp(sigma^T J sigma/2)` maps the `J=0` equilibrium family to the
interacting family.  It costs at most `max(w)/min(w)` in KL divergence.  Exact
Barker-collision algebra costs at most the square of the same ratio in entropy
production.  The source's already-proved `J=0` nonlinear MLSI then transfers
with total cubic loss.

The proof bypasses, and does not prove, the paper's separate uniform-in-tilt
canonical covariance conjecture.

## Files

- `solution_packet.pdf`: theorem, proof, source evidence, verification, and
  novelty audit.
- `source_paper.pdf`: arXiv:2511.05223v1.
- `figures/open_problem_crop.png`: full Section 4.5 question from PDF page 34.
- `code/verify_reweighting.py`: exhaustive small-cube identity and inequality
  checker.
- `verification.md`: commands, results, and reviewer focus.
- Attempt note:
  `runs/fa_banach_001/attempts/2511.05223_all_temperature_bounded_reweighting.md`.

Human review should focus on the entropy-production normalization, the exact
pairwise reweighting identity, and the information-projection inequality.
