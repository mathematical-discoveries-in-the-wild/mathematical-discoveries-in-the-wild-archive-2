# Multivariable rank-one Toeplitz semicommutators vanish

Status: `candidate_substantial_partial_likely_valid`

This packet addresses Remark 4.3 of arXiv:2101.03937. The source asks for a
several-variable extension of Ding--Qin--Zheng's possible-rank theorem for a
single product `T_phi T_psi-T_h`.

The packet proves the full rank-one half in the source setting: for complex
dimension `N>=2`, every nonnegative integer Bergman weight `gamma`, bounded
pluriharmonic `phi,psi`, and bounded `C^(2N+2+2gamma)` symbol `h`, rank at
most one forces `T_phi T_psi=T_h`.

The proof double-centers the complexified Brown--Halmos identity. A kernel
that would have separation rank at most one is shown to have rank at least

`binomial(2N+1+gamma,N)-2 >= 8`.

The classification or construction of all nonzero ranks at least two is not
settled. Eight materially distinct upgrade routes are recorded in the
attempt file.

Files:

- `solution_packet.pdf` -- expert-facing proof packet
- `source_paper.pdf` -- arXiv:2101.03937
- `main.tex` -- packet source
- `verification.md` -- mathematical and artifact audit
- `tmp/` -- LaTeX and render QA artifacts

Attempt:
`runs/fa_banach_001/attempts/2101.03937_multivariable_rank_one_semicommutator_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/2101.03937_multivariable_rank_one_semicommutator_vanishing.json`
