# 1305.2325: product-density escape and tail-rich inverse criterion

- Status: `candidate_partial_result_pending_human_review`
- Model: `GPT5.6`
- Source: Frédéric Bayart and Imre Z. Ruzsa, *Difference sets and frequently
  hypercyclic weighted shifts*, arXiv:1305.2325
- Surviving target: whether the inverse of an invertible frequently
  hypercyclic bilateral weighted shift on `c_0(Z)` is frequently hypercyclic

## Results

For cumulative products

`W_r=product_{1<=nu<=r} w_nu` and
`L_r=product_{-r+1<=nu<=0} w_nu`,

the packet proves that every invertible frequently hypercyclic bilateral
shift has a constant `delta>0` such that

`lower_density({r: W_r>R and L_r<1/R}) >= delta`

for every `R`. A density-diagonal lemma then gives one set `A` of lower
density at least `delta` along which `W_r -> infinity` and `L_r -> 0`.

The packet also proves a full conditional upgrade. If a standard
Bayart--Ruzsa/Grosse-Erdmann witness family has a positive-lower-density set
whose witness labels tend to infinity, then the inverse is frequently
hypercyclic. A sufficient check is that the lower densities of all tail
unions of the witness family are bounded below by one positive constant.
Eventual monotonicity of `L_r` is another concrete full-positive case.

The unrestricted bilateral-shift inverse question remains open. Quentin
Menet's arXiv:1910.04452 settles the general operator question negatively but
does not produce a bilateral weighted shift.

## Contents

- `main.tex` and `solution_packet.pdf`: theorem statements and proofs.
- `source_paper.pdf`: arXiv:1305.2325.
- `later_characterization.pdf`: arXiv:1707.03994.
- `general_counterexample_reference.pdf`: arXiv:1910.04452.
- `figures/source_question.png`: source PDF page 16.
- `figures/later_open_status.png`: later persistence statement, PDF page 13.
- `NOVELTY.md` and `VERIFICATION.md`: bounded audits.
- `runs/fa_banach_001/attempts/1305.2325_bilateral_c0_inverse_upgrade_log.md`:
  eight focused upgrade attempts.

## Review focus

Expert review should check the symmetric reformulation of the pairwise
product condition, the lower-density diagonal lemma, and the translation and
partition argument in the tail-rich inversion theorem.
