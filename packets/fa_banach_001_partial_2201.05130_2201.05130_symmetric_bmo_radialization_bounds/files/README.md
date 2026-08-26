# Symmetric BMO rearrangement: radialization and dimension bounds

- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_08`
- **Model:** `GPT5.6`
- **Source:** Almut Burchard, Galia Dafni, Ryan Gibara, *Vanishing Mean
  Oscillation and Continuity of Rearrangements*, arXiv:2201.05130.
- **Status:** substantial partial result, likely valid.

The source asks for the dimension dependence of the optimal decreasing- and
symmetric-rearrangement constants on cube-BMO.  This packet proves that the
intermediate radialization operator

`g(s) -> g(omega_n |x|^n)`

has norm of exact order `sqrt(n)` on nonnegative decreasing BMO functions.  It
then constructs the explicit logarithmic cusp

`f_n(x)=(-log|x_1|-||x'||_infinity)_+`,

whose BMO norm is at most `4` in every dimension but whose symmetric
rearrangement has BMO norm asymptotic to
`kappa sqrt(n)`, with `kappa=(1/7)sqrt(17/(5 pi))`.  Thus the optimal symmetric
constant is not dimension-free and is at least of order `sqrt(n)`.  Combining
the radialization theorem with arXiv:2011.09111, Theorem 1.1, improves the
published exponential upper estimate to order `n`.

The decreasing-rearrangement constant itself remains open.  If that constant
is dimension-free, the packet's two bounds imply the sharp classification
`D_n = Theta(sqrt(n))` for symmetric rearrangement.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: arXiv:2201.05130.
- `supporting_paper_2011.09111.pdf`: the published `O(sqrt(n))` decreasing
  rearrangement estimate used in the upper bound.
- `figures/open_problem_crop.png`: source-question crop spanning PDF pages 1-2.
- `code/verify_asymptotics.py`: seeded Monte Carlo sanity check for the CLT
  constant (not part of the proof).
- `code/crop_source.py`: reproducible source-crop builder.

## Verification focus

Reviewers should check the cube Poincare/small-ball estimate for
`Var(log|X|)`, the uniform cube-BMO estimate for the logarithmic cusp, and the
delta-method passage from `sum X_i^2` to the explicit asymptotic mean
oscillation.  All three arguments are self-contained in the packet.

