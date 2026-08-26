# 2110.06346 — the exceptional C3 base pair is singular

Status: candidate full negative answer to the exact undecided base case.

Model: GPT5.6.

For the compact type-C3 group Sp(3), let x have type C2 x C1 and y have
type C1 x C1. The packet proves that the orbital convolution mu_x * mu_y is
purely singular. It also proves the sharp strengthening that the product of
the two conjugacy classes has exact real dimension 20 in the
21-dimensional group.

The mechanism is a universal quaternionic centralizer intersection. For
every relative conjugation g, the Lie centralizers z_x and Ad(g)z_y share a
nonzero skew-Hermitian operator, so their orthogonal tangent spaces never
span sp(3). An explicit rational orthogonal change of basis makes the
intersection exactly one-dimensional.

Verification:

- code/verify_c3_pair.py passed 20,000 randomized quaternion identities.
- The same script verified the explicit sharpness example exactly over the
  rationals: constraint rank 6, kernel dimension 1, product-map rank 20.
- source_paper.pdf is a locally compiled copy of arXiv:2110.06346.
- figures/open_problem_crop.png records the exact source passage on PDF
  page 18.

Scope: this resolves the C3 base question only. It does not settle the
source's nonexceptional Cn/Dn conjecture or the higher exceptional families.

Novelty: bounded searches of the run indexes, exact pair notation, arXiv,
and the source author's later orbital-measure work found no later resolution.
Confidence is moderate pending expert literature review.

Ledger:
runs/fa_banach_001/ledger/results/2110.06346_C3_exceptional_pair_is_singular.json
