# Bounded novelty search

Search cutoff: 2026-08-13

## Scope

The search covered:

- the run's `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`,
  and `proof_gaps/index.tsv`;
- exact arXiv id and title searches;
- exact and close-variant searches for the Section 8.3 strict-inclusion
  question;
- queries combining `weighted Sobolev`, `complex interpolation`,
  `Stein-Weiss`, `strict inclusion`, and `counterexample`;
- local full-source searches among later papers citing or discussing
  arXiv:1807.10790;
- bounded web/arXiv and citation-trace searches through the cutoff date.

## Later related papers inspected

- arXiv:2204.11583, *Density results and trace operator in weighted Sobolev
  Spaces defined on the half line equipped with power weights*. Its complex
  interpolation application treats density and particular half-line power
  weights. It does not give the strict-inclusion construction here.
- arXiv:2503.14636, *Complex interpolation of power-weighted Sobolev spaces
  with boundary conditions*. It treats power weights, traces, boundary
  conditions, and density on half-spaces and smooth bounded domains. It does
  not state the source question's requested counterexample or the block
  projection mechanism here.

## Outcome

No prior full answer to the exact strict-inclusion question, no unrestricted
Stein--Weiss counterexample matching this construction, and no duplicate of
the two-witness block-projection argument was found. This is a bounded search,
not an exhaustive novelty guarantee; the packet remains marked for human
review.

