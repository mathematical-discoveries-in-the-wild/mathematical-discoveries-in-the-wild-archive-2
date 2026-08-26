# Bounded novelty search

Search date: 2026-08-13.

The following local indexes and corpora were searched before promotion:

- `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and
  `proof_gaps/index.tsv` for arXiv:0806.3366, title fragments, `B(1,1)`,
  Lipschitz endpoint, finite piecewise-affine approximation, and oscillatory
  shear terms;
- the parsed local arXiv source corpus for the exact endpoint sentence and
  close terminology;
- existing result ledgers for the arXiv id and core approximation terms.

Bounded web/arXiv searches used the exact phrases `we do not know whether 1
belongs to B(1,1)` and `sup B(1,1)`, the paper title and authors, and
combinations of bi-Lipschitz homeomorphism, finite piecewise-affine density,
Lipschitz norm, endpoint, and oscillatory shear.  Searches also checked the
later planar Sobolev-approximation literature to distinguish that solved
first-order problem from this stronger exponent-one Holder-norm question.

The searches found the source paper and later Sobolev, diffeomorphic, and
bi-Lipschitz approximation results, but no paper explicitly resolving this
`B(1,1)` endpoint or presenting the boundary oscillatory-shear example.
This is a bounded search, not an exhaustive novelty or priority guarantee.
