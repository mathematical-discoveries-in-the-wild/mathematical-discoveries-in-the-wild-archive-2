# Quadratic sampling theorem for stable phase retrieval

Status: candidate_partial_result_likely_valid

This packet treats Problem 4.5 of Freeman--Ghoreishi,
arXiv:2109.14454. In the real case it proves that the desired sampling is
always possible with \(O_{C,\beta}(N^2)\) points, and with resulting
stability constant \(2C\). It also proves the desired \(O(N)\) conclusion
under a uniform joint small-ball hypothesis.

The main improvement over the immediate net argument is removal of an
extra \(\log N\): an empirical frame-operator upper bound makes the
phaseless difference class dimension-free Lipschitz before the net is
applied.

Novelty confidence is moderate. Exact-phrase searches and the later
arXiv:2210.05114 formulation still present the linear question as open; no
matching quadratic theorem was found. The literature check was targeted,
not exhaustive.

Human review should focus on:

1. the real scalar identity converting magnitude differences to
   \(q_{u,v}\);
2. the simultaneous matrix-Chernoff/Bernstein probability estimate;
3. the empirical Lipschitz extension from the constant-resolution net;
4. whether a similar complex-field statement is already standard.

Files:

- solution_packet.pdf: self-contained proof and source context;
- source_paper.pdf: locally rendered source paper;
- figures/source_problem_page.png: source page containing Problem 4.5;
- code/check_scalar_identity.py: numerical sanity check only;
- the run attempt log records eight focused upgrade attempts.

