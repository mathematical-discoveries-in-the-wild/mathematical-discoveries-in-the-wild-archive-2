# MONK minimax outlier rate

Status: `literature_implied_answer (full minimax-rate resolution)`.

The page-4 open question in arXiv:1802.04784 asks whether MONK's robustness to outliers is optimal. The source supplement's arbitrary-block bound, retuned with `Q` of order `N_c + log(1/eta)`, gives the RKHS error term

`sqrt(||Sigma|| (N_c + log(1/eta))/N)`.

Theorem 3.2 and the minimax discussion in arXiv:2510.07867 establish that the corresponding finite-variance scalar median-of-means rate is optimal under adversarial contamination. The linear kernel `K(x,y)=xy` embeds scalar mean estimation into the MONK setting and gives a matching `sqrt(N_c/N)` lower bound for both kernel mean embedding and MMD. The supporting authors do not explicitly state this MONK/RKHS implication, so the provenance is `literature_implied_answers`, not `literature_already_answered` and not a new full solution.

Scope limitation: this resolves minimax rate optimality, not exact leading constants or the exact breakdown behavior as the number of corrupted blocks approaches one half.

Files:

- `solution_packet.pdf`: compact mathematical identification and proof of the implication.
- `source_paper.pdf`: locally compiled copy of arXiv:1802.04784 from the cached arXiv source.
- `supporting_paper_2510.07867_metadata.md`: supporting-paper metadata and exact theorem location. The PDF could not be downloaded because network resolution was unavailable during packaging.
- Ledger: `runs/fa_banach_001/ledger/results/1802.04784_monk_minimax_outlier_rate.json`.
