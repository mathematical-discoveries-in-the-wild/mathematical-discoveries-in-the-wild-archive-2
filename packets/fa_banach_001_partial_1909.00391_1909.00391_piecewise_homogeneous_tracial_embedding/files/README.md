# Piecewise-homogeneous tracial embedding theorem

Status: `candidate_partial_likely_valid`.

The source target is Conjecture 6.1 of Cédric Arhancet,
*Positive contractive projections on noncommutative Lp-spaces and
nonassociative Lp-spaces*, arXiv:1909.00391.  It asks for a full isometric
characterization of positively contractively complemented subspaces of
Haagerup noncommutative `L^p`-spaces.

Arhancet's companion paper arXiv:2307.04452 defines the relevant
nonassociative spaces and proves the tracial embedding implication for a
single `JW*`-factor with separable predual.  The present packet glues that
factor theorem over a countable piecewise-homogeneous center.  Concretely, it
covers

```text
J = direct_sum_j L^infinity(Omega_j; F_j),
```

where the index set is countable, each measure is finite, and each `F_j` is a
tracial `JW*`-factor with separable predual.  It includes countable atomic
centers and homogeneous diffuse centers.  The construction uses exact
vector-valued complex interpolation, tensoring the factor projections with
the identity, and a weighted `ell^p` direct sum.

This is a partial result.  The arbitrary measurable-field case, the
nontracial state case, and the unresolved direction identifying every
positive projection range remain open.

Files:

- `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1909.00391.
- `supporting_paper_2307.04452.pdf`: factor theorem and later status.
- `figures/open_conjecture_crop.png`: exact source conjecture.
- `code/make_crop.py`: reproducible crop script.
- `verification.md`: proof and artifact audit.

Ledger:
`runs/fa_banach_001/ledger/results/1909.00391_piecewise_homogeneous_tracial_embedding.json`.
