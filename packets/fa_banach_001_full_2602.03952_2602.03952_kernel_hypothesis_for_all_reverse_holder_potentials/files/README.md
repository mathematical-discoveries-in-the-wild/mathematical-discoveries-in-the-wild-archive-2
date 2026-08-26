# The kernel hypothesis holds for every reverse-Holder potential

Status: `full_solution_likely_valid_with_strengthening`

Source: Pierre Portal, *Using wave packet decompositions to construct
function spaces: a user guide*, arXiv:2602.03952.

## Result

The future-work statement after Theorem 6.1 suggests that its kernel
hypothesis (6.3) should hold for every nonnegative potential `V in RH_q`,
`q>d/2`. This packet proves the suggestion under the conventions forced by
the source's examples and finite-speed formula: the standard critical radius
uses a supremum, `H=-Delta+V`, and the wave multiplier is
`psi(sigma sqrt(H))`.

In fact, for every `A>0` the multiplier kernel obeys

`|K_sigma(x,y)| <= C_A sigma^{-d} 1_{|x-y|<=R_psi sigma}`

times

`(1+sigma/rho(x))^{-A}(1+sigma/rho(y))^{-A}`.

Critical-radius comparability on `Q_j` then gives (6.3) with compactly
supported `g` and `h(s)=(1+s)^{-A}`, `A>1`. The stronger bound holds at every
scale and does not itself require `rho` to be globally bounded.

## Proof mechanism

The known critical-radius heat-kernel estimate gives weighted `L^2` column
bounds for a sufficiently high power of `(I+sigma^2 H)^{-1}`. Factor

`psi(sigma sqrt(H)) = A_sigma B_sigma A_sigma`,

where `A_sigma=(I+sigma^2 H)^{-m}` and the middle multiplier is bounded on
`L^2`. Cauchy--Schwarz pairs the two resolvent columns to give the pointwise
amplitude. Compact Fourier support of `psi` and finite wave propagation give
the exact spatial cutoff.

## Files and verification

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:2602.03952.
- `supporting_heat_kernel_original_2003.pdf`: the original heat-kernel result,
  especially Theorem 4.10.
- `supporting_heat_kernel_paper.pdf`: a 2021 restatement as Proposition 29.
- `figures/source_setup.png` and `figures/source_open_problem.png`: source
  setup and open statement on PDF pages 9--10.
- `figures/supporting_original_theorem_4_10.png`: original heat-kernel theorem.
- `figures/supporting_heat_kernel.png`: modern restatement of that estimate.

## Novelty check

Run attempts, ledgers, solutions, and indexes were searched for the arXiv id,
title, critical-radius kernel hypothesis, and wave-packet/reverse-Holder
phrases. A bounded web/arXiv search on 2026-08-13 included the source title,
id, the four named upcoming collaborators, and combinations of wave packets,
critical radii, spectral kernels, and reverse-Holder potentials. It found the
February 2026 source but no posted follow-up or prior statement of this
resolution.

## Human-review recommendation

Review as a likely valid full proof with strengthening. The key points are
the weighted resolvent-column lemma, the two-sided spectral factorization,
and the source-notation correction stated explicitly in the packet.
