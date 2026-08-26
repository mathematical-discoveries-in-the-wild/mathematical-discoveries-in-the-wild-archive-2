# 2402.13645: square-root-sparse random Dirichlet Carleson sequences

- Status: `candidate_partial_result_pending_human_review`
- Model: `GPT5.6`
- Source: N. Chalmoukis, A. Dayan, and G. Lamberti, *Random Carleson
  Sequences for the Hardy Space on the Polydisc and the Unit Ball*,
  arXiv:2402.13645
- Target: the conjecture after Corollary 4.5
- Scope: every `d >= 1` and every missing parameter `0 < a <= 1/2`, under
  a stronger quantitative occupancy hypothesis

## Result

For `0 < a < 1/2`, the packet proves almost-sure Carleson embedding whenever

`sum_{m,k} N_m N_k 2^{-(1-a)(|m|+|k|)} 2^{(1-2a)|m wedge k|} < infinity`.

At `a=1/2` it proves the analogous endpoint condition with the factor
`product_i(1+min(m_i,k_i))`. In either case the normalized Gramian minus the
identity is Hilbert--Schmidt almost surely.

In particular, for every missing `a`, the conjectured conclusion holds if

`N_m <= C 2^{(1/2-epsilon)|m|}`.

This pointwise hypothesis also implies the source's necessary finite-mass
condition. The full conjecture under finite mass alone remains open.

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained statement and proof.
- `source_paper.pdf`: local copy of arXiv:2402.13645.
- `figures/source_lemma_4_4.png`: the source second-moment estimate.
- `figures/source_corollary_4_5.png`: the known Hilbert--Schmidt argument for
  `a>1/2`.
- `figures/source_conjecture.png`: the conjecture on source PDF page 17.
- `NOVELTY.md`: bounded novelty audit.
- `VERIFICATION.md`: proof and rendering audit.
- `runs/fa_banach_001/attempts/2402.13645_random_dirichlet_polydisc_upgrade_log.md`:
  eight full-upgrade attempts and their obstructions.

## Review recommendation

The proof is short and likely valid, but the result should be described as a
partial theorem, not a resolution of Corollary 4.5 in the full finite-mass
regime. Expert review should focus on the dyadic form of Lemma 4.4 and the
endpoint logarithmic factor.
