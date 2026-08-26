# The proposed enlargement is not 3-c-monotone

Status: `candidate counterexample; likely valid; human review requested`.

This packet answers the explicit open question in Remark 4.2 of Tongseok
Lim, *Maximal Monotonicity and Cyclic Involutivity of Multiconjugate Convex
Functions* (arXiv:2207.04830; SIAM J. Optim. 33 (2023), 2489–2511).

For the contact set `Gamma` in Example 4.1, the paper proves that
`Gamma union {(0,0,0)}` is `c`-monotone and conjectures that it is
`c`-cyclically monotone. The packet gives two explicit points of `Gamma`
which, together with the origin, violate the order-three cyclic inequality by
exactly `lambda^2/8`. Thus the proposed enlargement is not even
3-`c`-monotone.

This does **not** decide whether the original `Gamma` has some other proper
`c`-cyclically monotone extension, so it does not settle maximal
`c`-cyclical monotonicity of `Gamma` itself.

Contents:

- `solution_packet.pdf`: proof and review notes;
- `source_paper.pdf`: the source paper;
- `figures/open_problem_crop.png`: Remark 4.2 from PDF page 26;
- `code/verify_certificate.py`: exact rational-arithmetic check;
- `code/random_cycle_search.py`: the falsification search which found the
  pattern.

Ledger record:
`runs/fa_banach_001/ledger/results/2207.04830_tilde_gamma_not_3_c_monotone.json`.
