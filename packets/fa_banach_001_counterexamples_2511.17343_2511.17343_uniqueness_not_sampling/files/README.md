# A uniqueness set which is not sampling

Status: `candidate counterexample likely valid`.

This packet answers two explicit unknowns in Filippo Giannoni, *Sampling on
Paley--Wiener spaces on graphs, with particular focus on the infinite-dimensional
case* (arXiv:2511.17343v6).

Under exactly the paper's stated graph assumptions, it constructs a positive-band
infinite-dimensional Paley--Wiener space with a set `W` such that:

- `W` is a uniqueness set;
- `W` is not a sampling set;
- the uniqueness norm `||.||_W` is incomplete;
- `V\W` is not a lambda-set.

The graph is the disjoint union of `C_8` and an infinite family of finite
10-regular bipartite Ramanujan graphs of unbounded order.  The source does not
assume connectedness; no connected version is claimed.

Files:

- `main.tex` and `solution_packet.pdf`: full counterexample proof.
- `source_paper.pdf` and `source_paper.tex`: official arXiv source copies.
- `figures/source_page_8.png`: source completeness question.
- `figures/source_page_10.png`: source existence question.
- `code/verify_counterexample.py`: exact symbolic checks.
- `verification.md`: mathematical, scope, novelty, and packet QA record.

