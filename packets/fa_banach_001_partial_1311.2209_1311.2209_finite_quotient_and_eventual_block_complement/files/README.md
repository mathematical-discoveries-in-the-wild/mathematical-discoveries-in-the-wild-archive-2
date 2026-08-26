# arXiv:1311.2209 — finite and eventual-block complementary spectra

- Status: `candidate_partial_result_pending_human_review`
- Model: `GPT5.6`
- Source: Jean-Pierre Gabardo and Chun-Kit Lai, *Spectral Measures Associated
  with the Factorization of the Lebesgue Measure on a Set via Convolution*,
  arXiv:1311.2209
- Target: Question (Q4), PDF page 22, for type-II natural complementary pairs

## Result

Write `P_n=N_1...N_n`.  At finite depth `2k`, every spectrum `L` of the odd
head convolution and every spectrum `C` of the even head convolution satisfy

`L direct-sum C = a complete residue system modulo P_(2k)`.

This is independent of the choice of the finite spectra.  The proof separates
their difference sets into disjoint odd and even Fourier-zero layers.

The packet then proves a tail-reduction theorem.  If the prescribed spectrum
has the block form

`Lambda = t + L direct-sum P_(2k) U`,

where `L` is normalized to contain zero, `U` is a spectrum of the renormalized odd tail, and `U` has a spectral
tiling complement `V` for the renormalized even tail, then

`Gamma = -t + C direct-sum P_(2k) V`

is a spectrum of the original even factor and `Lambda direct-sum Gamma=Z`.
Consequently Q4 holds for every spectrum with an arbitrary finite spectral
head and a canonical tail, and recursively for every eventual block-product
spectrum whose terminal tail already satisfies Q4.

The unrestricted arbitrary-tree case remains open.  Finite quotient tilings
only give a profinite complement; they do not ensure that the resulting paths
are ordinary integers or that a maximal orthogonal complement is complete.

## Contents

- `main.tex`, `solution_packet.pdf`: theorem statements, proofs, and scope.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: Question (Q4), source PDF page 22.
- `code/verify_finite_quotients.py`: exhaustive small-radix proof guard.
- `VERIFICATION.md`: commands, output, and reviewer checks.
- `NOVELTY.md`: bounded later-literature search.
- `runs/fa_banach_001/attempts/1311.2209_q4_typeII_complement_upgrade_log.md`:
  eight focused full-upgrade attempts.

## Human-review focus

Check the zero-layer convention, the modulo-`P_(2k)` injectivity argument,
and the tensor/product-spectrum lemma used in the head-tail reduction.  The
packet deliberately does not claim that every arbitrary spectral tree admits
a terminating spectral complement.
