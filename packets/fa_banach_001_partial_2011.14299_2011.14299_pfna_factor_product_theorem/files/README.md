# Products with a point-finite-assignment factor

Status: `candidate_partial_result_likely_valid`

This packet gives a new positive subprogram for the compact-product problem
in Kąkol--Leiderman, arXiv:2011.14299. The main theorem is purely topological:
if `X` is a Delta-space and `Y` admits a point-finite neighborhood assignment,
then `X x Y` is a Delta-space.

Consequences include:

- `X x K` is Delta for every Delta-space `X` and every scattered Eberlein
  compactum `K`;
- it is enough that one factor be a countable union of closed subspaces with
  point-finite neighborhood assignments;
- for compact factors, it is enough that one factor be a countable union of
  scattered Eberlein compacta;
- the result covers all compact scattered factors of height at most two;
- it also covers the non-Eberlein one-point compactifications of classical
  Isbell--Mrówka spaces.

The proof expands a disjoint family one vertical fiber at a time. A
point-finite assignment on the second factor ensures that only finitely many
fiberwise expansions can affect any point of the product.

The packet is partial: the product of two arbitrary compact Delta-spaces
remains open. The 2023 follow-up arXiv:2307.16047 explicitly reiterates that
status, while the possible upgrade through countable Eberlein decompositions
is itself a named open problem.

Artifacts:

- `solution_packet.pdf`: formatted proof packet.
- `source_paper.pdf`: arXiv:2011.14299; the source problem is on PDF page 12.
- `supporting_paper_2104.10506.pdf`: countable closed-union theorem.
- `supporting_paper_2307.16047.pdf`: current problem status and surrounding
  structure.
- `figures/open_problem_crop.png`: source-page evidence.
- Attempt audit:
  `runs/fa_banach_001/attempts/2011.14299_compact_delta_product_pfna_route.md`.
- Ledger:
  `runs/fa_banach_001/ledger/results/2011.14299_pfna_factor_product_theorem.json`.

Final packet verification: 4 letter-size pages, 293761 bytes; all four pages
were rendered at 144 dpi and visually inspected with no clipping, overlap, or
illegible text. SHA-256:
`140dcfa71990703b5831b522c7b947d959bf3dc0450890fdee8ae574b7070ae3`.
