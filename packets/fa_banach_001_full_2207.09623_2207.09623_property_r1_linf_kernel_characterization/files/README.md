# Candidate Full Solution: Property-\((R_1)\) Kernels in \(\ell_\infty^n\)

Source: Syamantak Das and Tanmoy Paul, *On property-\((R_1)\) and relative Chebyshev centers in Banach spaces-II*, arXiv:2207.09623.

Result type: `full`

Status: candidate full solution, likely valid, pending expert review.

## Result

For linearly independent rows \(\alpha_1,\ldots,\alpha_m\in\ell_1^n\), set
\[
V=\bigcap_i\ker\alpha_i\subset\ell_\infty^n.
\]
Then \(V\) has property \((R_1)\) for all finite subsets if and only if the row space \(\operatorname{span}\{\alpha_i\}\) admits a basis whose vectors, up to nonzero scalar rescaling, are \(e_j\) or \(e_j\pm e_k\).

Equivalently, after coordinate permutation and sign changes, \(V\) is a direct product of zero coordinates, free singleton coordinates, and one-dimensional diagonal blocks.

## Proof mechanism

1. In finite dimension, ordinary and strong property \((R_1)\) coincide.
2. Intersections of common-radius \(\ell_\infty\)-balls are exactly bounded coordinate boxes.
3. The resulting box-intersection property is equivalent to invariance under coordinatewise clipping \(T_r\).
4. A minimal-support argument classifies clipping-invariant linear subspaces as signed diagonal block products.
5. Taking annihilators yields the row-space criterion.

## Files

- `solution_packet.pdf`: expert-facing proof packet.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: source arXiv paper.
- `supporting_paper_1507.07795.pdf`: closest related primary paper, used as a structural literature cross-check.
- `figures/open_problem_crop.png`: source page 17 crop containing Remark 5.2(a).
- `VERIFICATION.md`: independent proof audit and review risks.
- `tmp/`: build and page-render intermediates.

## Novelty status

The cheap run indexes and bounded exact/close web searches found no answer to the source question. Miesch--Pav\'on, arXiv:1507.07795, Theorem 4.7, earlier classified weakly externally hyperconvex subspaces of \(\ell_\infty^n\) by the same signed-coordinate structure, but did not discuss property \((R_1)\). The packet's box/clipping equivalence and proof are self-contained. Novelty confidence is moderate pending an expert search of older \(1\frac12\)-ball terminology.

## Human review

Recommended focus: the ordinary-to-strong reduction and the minimal-support clipping lemma. A secondary reviewer should assess whether an older ball-intersection theorem already states the property-\((R_1)\)/clipping equivalence.
