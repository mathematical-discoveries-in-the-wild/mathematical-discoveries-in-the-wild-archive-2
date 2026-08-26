# 2304.06423: sharp mixed-norm threshold for the PGA

- Status: `candidate_full_likely_valid`
- Model: `GPT5.6`
- Source: V. N. Temlyakov, *On the rate of convergence of greedy
  algorithms*, arXiv:2304.06423v1
- Target: whether `gamma_m(alpha,H)=O(m^{-alpha/2})` extends past
  `alpha=1/3`
- Answer: yes, exactly through `alpha_*=0.365551412606085...`; no above it

## Result

Let `Gamma=1.152343688265233...` be the root in `[1,1.5]` of

`(1+x)^(1/(2+x))(1+1/(1+x))-1-1/x=0`,

and put `alpha_*=Gamma/(2+Gamma)`.

The packet proves that the uniform mixed PGA rate

`gamma_m(alpha,H)=O(m^{-alpha/2})`

holds for every `0<alpha<=alpha_*` and fails for every `alpha>alpha_*`.
Together with the signed-orthonormal lower example, the order is exactly
`m^{-alpha/2}` throughout the valid range.

The new upper step is a two-scale rescaling of Sil'nichenko's scalar-envelope
proof. It yields

`a_m b_m^Gamma <= C ||f||^2 ||f||_{A_1}^Gamma`.

Combining this with `a_m b_m^{-2}<=1/(m+1)` gives the endpoint mixed rate.
Klusowski--Siegel's sharp lower construction proves failure above the same
threshold.

## Packet contents

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: official arXiv source PDF.
- `figures/source_question.png`: exact source question crop.
- `supporting/silnichenko_2004.pdf`: primary supporting upper-proof paper.
- `supporting/klusowski_siegel_2307.07679.pdf`: official arXiv supporting
  sharp-lower paper.
- `verification.md`: proof, source, novelty, and rendering audit.
- `attempts/2304.06423_pga_mixed_rate_threshold/attempts.md`: attack and
  upgrade log.

## Review recommendation

Recommended for expert review as a full rate-order answer. Focus on the
independent horizontal/vertical rescaling in the scalar envelope lemma and
on the fixed-target quantifiers in the sharp lower theorem.
