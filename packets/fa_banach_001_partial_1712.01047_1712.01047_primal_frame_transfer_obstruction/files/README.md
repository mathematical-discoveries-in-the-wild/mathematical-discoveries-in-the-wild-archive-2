# Primal-frame transfer: exact criterion and near-Parseval obstruction

Status: `candidate_substantial_partial_likely_valid`

This packet addresses the primal-frame approximation-rate item in the Outlook
of arXiv:1712.01047.

It proves two self-contained abstract results:

1. Canonical-dual analysis equals the Moore--Penrose inverse Gramian applied
   to primal analysis. Weak-`ell^p` boundedness of that pseudoinverse transfers
   the source's coefficient sparsity to primal best `N`-term rates.
2. Frame bounds cannot provide this transfer. Even a Riesz basis with frame
   bounds arbitrarily close to one can have a vector with one nonzero primal
   analysis coefficient but primal best `N`-term error of order at least
   `(log N)^(-1/2)`.

The hybrid-specific pseudoinverse-Gramian localization estimate is not proved,
so the source's full primal-frame rate remains open in this packet. Eight
upgrade routes are recorded in the attempt file.

Files:

- `solution_packet.pdf` -- expert-facing proof packet
- `source_paper.pdf` -- arXiv:1712.01047
- `main.tex` -- packet source
- `verification.md` -- mathematical and artifact audit
- `tmp/` -- LaTeX and render QA artifacts

Attempt:
`runs/fa_banach_001/attempts/1712.01047_primal_dual_frame_transfer_attempt.md`

Ledger:
`runs/fa_banach_001/ledger/results/1712.01047_primal_frame_transfer_obstruction.json`
