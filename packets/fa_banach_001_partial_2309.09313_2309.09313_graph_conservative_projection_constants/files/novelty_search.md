# Bounded novelty search

Search cutoff: 2026-08-11.

## Searches

The search used the exact source title/id and question phrase, together
with combinations of:

- conservative vector fields / `CVF(G)` / integral extension;
- cut space / gradient space / cycle space / projection constant;
- weighted cycle / hyperplane / `ell_infinity` projection;
- complete graph / complete bipartite graph / invariant projection;
- cactus / block graph / cut-vertex decomposition.

The repository's cheap indexes and locally parsed arXiv sources were also
searched. In particular, arXiv:2305.12582 was inspected directly for graph
families and projection statements.

## Closest literature located

- Thomas Schlumprecht, arXiv:2309.09313, states the target extension and
  complementation question.
- Stephen J. Dilworth, Denka Kutzarova, and Mikhail I. Ostrovskii,
  arXiv:2305.12582, develops invariant/minimal projections on graph cycle
  spaces and their transportation-cost applications. It emphasizes that
  invariant projections may be nonunique for some graph families.
- Dilworth--Kutzarova--Ostrovskii, arXiv:1807.03814, uses symmetry averaging
  and projection estimates for recursive graph families including Laakso
  and diamond graphs.
- Tomasz Kobos, arXiv:1411.6214, records Bohnenblust's codimension-one bound
  and studies equality cases. The weighted-cycle result should therefore be
  viewed as an explicit hyperplane calculation.
- Marc A. Rieffel, arXiv:math/0508097, proves a broad equality between
  finite-dimensional Lipschitz extension constants and projection
  constants.
- Network-systems literature records that the standard uniform cutset
  projection on rings and complete graphs has infinity norm
  `2(n-1)/n`. This supports but reduces novelty confidence in those two
  specializations.

## Assessment

No located source stated the full collection of exact weighted-cycle,
weighted-cactus, complete-bipartite, and cut-vertex block formulas in the
form proved in this packet. However, the ingredients are close to classical
hyperplane projection and invariant-projection methods, and the complete
graph/ring norm is known for the canonical projection. The packet therefore
makes **no priority claim**. It is labeled a candidate partial result,
likely valid, with moderate novelty confidence for the biclique and block
synthesis and low-to-moderate confidence for the individual classical
special cases.
