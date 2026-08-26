# Group Spencer conjecture for finite groups: literature answer

Status: `literature_already_answered`.

The source paper is Afonso S. Bandeira, Dmitriy Kunisky, Dustin G. Mixon, and
Xinmeng Zeng, *On the concentration of Gaussian Cayley matrices*,
arXiv:2212.00066 (published in ACHA 73 (2024), 101694).  Its Theorem 12 proves
the `O(sqrt(|G|))` signing bound for abelian and simple finite groups, and its
Discussion (PDF page 9) asks for the theorem for more general groups.

Afonso S. Bandeira and Helmut Boelcskei, *Matrix Discrepancy for
Representations of Finite Groups*, arXiv:2606.12181v2, explicitly cite the
source, identify the general finite-group case as the conjecture left there,
and prove it as Theorem 2 (PDF page 2): for every finite group `G`,

`min_epsilon || sum_{g in G} epsilon_g rho(g) || <= C sqrt(|G|)`.

Thus the source's group extension is fully answered in later literature.  The
general Matrix Spencer conjecture for arbitrary contraction families remains
open; this packet claims only the finite-group representation case.

Files:

- `solution_packet.pdf`: compact identification note.
- `source_paper.pdf`: arXiv:2212.00066.
- `supporting_paper_2606.12181.pdf`: the answering paper.
- Ledger: `ledger/results/2212.00066_group_spencer_answered_2606.12181.json`.

