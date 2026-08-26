# A two-channel instability region for the spinorial CKN inequality

Status: candidate partial result; verifier verdict `likely valid`.

Source: Jean Dolbeault, Maria J. Esteban, Rupert L. Frank, and Michael Loss,
*The CKN inequality for spinors: symmetry and symmetry breaking*,
arXiv:2504.16909v2 (13 July 2026).

Source location: Remark 26, PDF page 30. The paper proves instability using
single spinor-spherical-harmonic channels and leaves the optimal region under
mixing of channels open.

## Claimed contribution

For `-1/2 < alpha < 0`, set `d = 1/2-alpha`. The packet proves that the
symmetric optimizer is linearly unstable, and hence

`C_(alpha,p) < C*_(alpha,p)`, 

whenever

`p > p_mix(alpha) := 2 sqrt(1 + 2/d^2)`.

The interval `(p_mix(alpha),6)` is nonempty for every `alpha` in `(-1/2,0)`.
In particular, this gives symmetry breaking for every
`(1-sqrt(3))/4 < alpha < 0` and sufficiently large `p<6`, whereas the source's
single-channel theorem gives no instability anywhere in that alpha interval.
Thus mixing genuinely enlarges the published instability region.

By the reflection symmetry used in the source paper, the same argument gives
the reflected sufficient condition for `-1 < alpha < -1/2`:

`p > 2 sqrt(1 + 2/(alpha+3/2)^2)`.

## Proof mechanism

The two best low angular channels share the same scalar harmonic. Their
specific normalized combination is

`psi = sqrt(2/3) chi_1^(1/2) + sqrt(1/3) chi_-2^(1/2)
     = (sqrt(4 pi) Y_1^0, 0)^T`.

The lower spinor component cancels. Consequently the nonlinear real-part
factor in the Hessian is exactly `1`, compared with `2/3` and `1/3` in the
two pure channels. The angular energy is `d^2+2`. Optimizing the common radial
profile is the scalar Pöschl--Teller problem already used in the source paper.
Its exact ground energy reduces to

`E_mix = d^2 + 2
       - d^2/16 (sqrt(9p^2-12p+4) - (p-2))^2`.

Elementary algebra gives `E_mix<0` exactly when `p>p_mix(alpha)`.

## Scope and limitation

This is a substantial partial result, not the optimal mixed-channel region.
Allowing independent radial profiles in the two channels produces a genuine
`2 x 2` matrix Pöschl--Teller operator. Its constant angular mass matrix does
not commute with the rank-one potential matrix when `alpha != 0`, so the
scalar exact eigenvalue formula no longer diagonalizes the problem. Higher
angular blocks must also be excluded to solve the source problem in full.

## Novelty check

A bounded search on 9 August 2026 covered the run's lightweight indexes and
parsed arXiv corpus, plus arXiv searches for the paper title, the authors
Esteban and Frank, `mixing several channels`, and spinorial CKN instability.
No separate public paper containing this explicit two-channel threshold was
found. Novelty confidence is only moderate: arXiv:2504.16909v2 itself adds a
footnote saying that recent work of Esteban and Frank suggests channel mixing
does enlarge the region.

## Packet contents

- `main.tex`, `solution_packet.pdf`: formal proof packet.
- `source_paper.pdf`: arXiv:2504.16909v2.
- `figures/open_problem_crop.png`: full-width crop of Remark 26, PDF page 30.
- `verification.md`: adversarial verification report.
- `code/check_two_channel_instability.py`: coefficient, threshold, and radial
  quadrature sanity checks; the code is not part of the proof.

## Human review recommendation

Send to a human for mathematical review. The calculation is short and appears
complete. Before any external originality claim, ask the source authors about
the unpublished Esteban--Frank work mentioned in the added-in-proof footnote.
