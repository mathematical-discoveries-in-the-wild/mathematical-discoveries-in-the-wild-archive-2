# Direct-product stability of the M_d-AP: answered in later literature

Status: `literature_already_answered`

Source/open-problem paper: Ignacio Vergara, *The M_d-Approximation
Property and Unitarisability*, arXiv:2202.12198; *Proceedings of the American
Mathematical Society* 151 (2023), 1209–1220, DOI
`10.1090/proc/16204`.

Supporting answer paper: Ignacio Vergara, *Some remarks on M_d-multipliers
and approximation properties*, arXiv:2509.07861 (2025).

Packet: `runs/fa_banach_001/solutions/literature_already_answered/2202.12198_md_ap_direct_products_answered_2025/`

Ledger: `runs/fa_banach_001/ledger/results/2202.12198_md_ap_direct_products_answered_2025.json`

## Identification

Remark 4.2 on PDF page 7 of arXiv:2202.12198 states:

> We do not know if M_d-AP is stable under direct products.

The later paper arXiv:2509.07861 explicitly cites the source as `[Ver]` and
strengthens its amenable-kernel extension theorem. Theorem 1.3 proves that if
`Gamma` and `G/Gamma` both have M_d-AP, then `G` has M_d-AP. Corollary 1.4 on
PDF page 3 then states explicitly that, for every `d >= 2`, M_d-AP for
discrete groups is stable under direct products, semidirect products, and
free products. Its proof on PDF page 10 obtains direct products as the
trivial-action case of semidirect products.

This is an exact, author-aware later answer to the source remark, so the
result is classified as literature already answered rather than as a new
run discovery.

## Independent verification

The direct-product subcase also has a short check from the definitions. If
`u_i -> 1` weak-star in `M_d(G)` and `v_j -> 1` weak-star in `M_d(H)`, with
both nets finitely supported, then

`w_(i,j)(g,h) = u_i(g) v_j(h)`

is finitely supported. Tensoring the defining Hilbert-space factorizations
gives

`||w_(i,j)||_{M_d(G x H)} <= ||u_i||_{M_d(G)} ||v_j||_{M_d(H)}`.

Weak-star convergent nets are norm bounded. The product net converges to one
on every point of `G x H`, hence on every finitely supported element of the
predual; uniform boundedness and density of `C[G x H]` in `X_d(G x H)` then
give weak-star convergence. This confirms the statement but is not claimed
as a novel result.

## Search evidence

The four lightweight run indexes were searched for arXiv:2202.12198, the
paper title, `M_d-AP`, `unitarisability`, and direct-product stability. A
bounded web/arXiv search used the exact phrases `M_d-AP direct products` and
`M_d approximation property direct product group`. It found arXiv:2509.07861,
whose source was locally available and was checked at Theorem 1.3, Corollary
1.4, and the proof of that corollary.

## Scope

This packet resolves only Remark 4.2 of the source. The broader question
whether M_d-AP is equivalent to ordinary AP for every `d >= 2` remains open;
the 2025 supporting paper restates it as the question whether M_2-AP and
M_d-AP are equivalent for all `d >= 3`.

## Files

- `source_paper.pdf`: arXiv:2202.12198.
- `supporting_paper_2509.07861.pdf`: exact later answer.
- `main.tex` and `solution_packet.pdf`: compact status note.

