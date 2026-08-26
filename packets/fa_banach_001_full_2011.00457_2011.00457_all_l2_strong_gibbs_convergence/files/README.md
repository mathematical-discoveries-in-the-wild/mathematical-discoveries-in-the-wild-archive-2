# arXiv:2011.00457 — all-ℓ² strong Gibbs convergence

Status: candidate full answer.

The source asks whether its untruncated semigroup expansion converges to the Gibbs mode for every initial condition in `ell^2`, rather than only in `ell^1`. The answer is yes under the hypotheses of its Main Theorem.

The decisive observation is that the source's eigenvectors form a Schauder basis and the negative eigenvalues are ordered increasingly to zero. Relative to that basis, `exp(tA)-Pi` has diagonal coefficients

`0, exp(t nu_2), exp(t nu_3), ...`,

which increase to `1` in the basis index. Abel summation bounds all these basis multipliers uniformly in `t`. They converge to zero on every finite basis expansion, and density then gives strong convergence on all of `ell^2`.

The packet also proves the quantitative head–tail estimate

`||(exp(tA)-Pi)x|| <= 2K exp(t nu_N)||x|| + (1+K)||(I-P_N)x||`

and the sharp obstruction `||exp(tA)-Pi||>=1` for every `t`: convergence is strong but never in operator norm.

Files:

- `solution_packet.pdf`: full theorem, proof intuition, proof, quantitative estimate, and sharpness.
- `source_paper.pdf`: official arXiv PDF for 2011.00457.
- `main.tex`: packet source.
- `attempts.md`: proof-route audit.
- `verification.md`: mathematical, literature, and rendering checks.
