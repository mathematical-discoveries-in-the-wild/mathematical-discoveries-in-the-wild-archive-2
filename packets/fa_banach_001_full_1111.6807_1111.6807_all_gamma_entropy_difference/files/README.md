# Entropic difference bodies: the fixed-additive-gamma question

Status: `candidate full solution, likely valid; needs human review`

Source: Sergey G. Bobkov and Mokshay M. Madiman, *On the Problem of
Reversibility of the Entropy Power Inequality*, arXiv:1111.6807. The displayed
question on source PDF page 5 asks for which `gamma>0` the dimension-free
bound `H(X-Y) <= C_gamma H(X)` holds when `f=V^{-beta}` and
`beta>=n+gamma`.

Answer: every `gamma>0`.

The proof bins the intrinsic information content `-log f(X)` in intervals of
width `n`. A bin lies in a convex density superlevel set `K`; conditioned on
two bins, `X-Y` lies in `K-K`, so Rogers--Shephard controls its entropy. The
sharp Fradelizi--Li--Madiman varentropy bound controls both the expected larger
bin and the entropy of the integer bin index uniformly in dimension. This
gives the explicit inequality `h(X-Y)<=h(X)+n c_gamma`, hence the requested
entropy-power bound with `C_gamma=exp(2c_gamma)`.

Primary output: `solution_packet.pdf`.

Proof attempt and route audit:
`runs/fa_banach_001/attempts/1111.6807_information_quantization_full_proof.md`.

Verification and novelty notes: `VERIFICATION.md`.

Ledger: `runs/fa_banach_001/ledger/results/1111.6807_all_gamma_entropy_difference.json`.

