# Aligned Macaev operators lift through the canonical ELP twist

Status: `partial_result_likely_valid`

Source problem: F. Cabello Sanchez and R. Garcia, *The Twisted Hilbert
Space Ideals*, arXiv:2112.03852, page 5:

> Is every operator in the Macaev ideal liftable?

## Result

Let `Omega_ELP` be the canonical block quasilinear map defining the
Enflo-Lindenstrauss-Pisier twisted Hilbert sequence, with its `n`-th domain
block equal to `ell_2^(3^n)`. For a bounded scalar sequence `(a_n)`, let

`D_a = direct_sum_n a_n I_(ell_2^(3^n))`.

If `delta_n` is the distance of the `n`-th ELP block map from the linear maps,
then

`D_a` lifts through `Omega_ELP` if and only if
`sup_n |a_n| delta_n < infinity`.

The explicit ELP recursion gives `delta_n` of order `sqrt(n)`. Consequently,

`D_a` lifts through `Omega_ELP` if and only if
`sup_n sqrt(n) |a_n| < infinity`.

In particular, every such block-scalar `D_a` in the Macaev ideal lifts through
the ELP sequence. The same conclusion holds under the weaker endpoint bound
`s_j(D_a) = O(1/log(j+1))`.

This is significant because the canonical ELP quasilinear map is known not to
be equivalent to a centralizer. The source paper already handles multiplication
operators through centralizers; this packet supplies an endpoint-positive
subcase for a canonical non-centralizer twist.

## Scope

This does **not** resolve either universal question in arXiv:2112.03852. The
operator must be scalar on the canonical ELP blocks, and the conclusion concerns
lifting through that particular twisted Hilbert sequence. Arbitrary Macaev
operators and arbitrary twisted Hilbert sequences remain open.

## Evidence and files

- `main.tex`: complete theorem and proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv:2112.03852.
- `supporting_paper_2603.22484.pdf`: the 2026 source used for the explicit ELP
  recursion, its finite-block complementability bound, and the fact that
  `Omega_ELP` is not equivalent to a centralizer.
- `figures/open_problem_crop.png`: source question on page 5.
- `VERIFICATION.md`: independent proof audit and limitations.

## Novelty check

Bounded searches used the exact source title and question, `Macaev liftable`,
`twisted Hilbert local splitting`, and the 2026 ELP/non-centralizer paper
arXiv:2603.22484. No later paper claiming the universal endpoint result or this
aligned-block characterization was found. Novelty confidence is moderate, and
human literature review is recommended.

Ledger: `runs/fa_banach_001/ledger/results/2112.03852_elp_block_scalar_macaev_liftability.json`.

